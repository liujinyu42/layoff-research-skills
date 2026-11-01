#!/usr/bin/env python3
"""Install v1.4.0 research skills and an isolated Python runtime."""
from pathlib import Path,PurePosixPath
import argparse,hashlib,json,os,shutil,subprocess,sys,tempfile,urllib.request,venv,zipfile
VERSION='1.4.0'
ARCHIVE_SHA256='5ab8c9ed3a1233774366ec5fb48db4c3213d69197cc318640ce0ffe706eb30d2'
ARCHIVE_URL='https://raw.githubusercontent.com/liujinyu42/layoff-research-skills/main/layoff-research-skills-v1.4.0-github.zip'
SKILLS=('layoff-announcement-tracker','listed-filing-extractor')

def unpack(archive,dest):
 raw=Path(archive).read_bytes()
 if hashlib.sha256(raw).hexdigest()!=ARCHIVE_SHA256:raise ValueError('Source ZIP checksum mismatch; nothing installed')
 with zipfile.ZipFile(archive)as z:
  for i in z.infolist():
   path=PurePosixPath(i.filename)
   if path.is_absolute()or '..'in path.parts or '\\'in i.filename or (i.external_attr>>16)&0o170000==0o120000:raise ValueError('Unsafe ZIP path')
  z.extractall(dest)
 root=Path(dest)/'layoff-research-skills'
 if not(root/'install.py').is_file():raise ValueError('Installer missing from verified source')
 return root

def add_runtime(skill,python):
 script=skill/'scripts/research.py';original=skill/'scripts/research_impl.py'
 if not original.exists():script.rename(original)
 (skill/'scripts/runtime.json').write_text(json.dumps({'python':str(python.absolute()),'version':VERSION},indent=2)+'\n')
 script.write_text('''#!/usr/bin/env python3
from pathlib import Path
import json,os,runpy,sys
HERE=Path(__file__).resolve().parent
python=Path(json.loads((HERE/'runtime.json').read_text())['python'])
if not python.is_file():raise SystemExit('Research runtime missing. Run quick_install.py again with --force.')
if Path(sys.executable).absolute()!=python.absolute():os.execv(str(python),[str(python),str(HERE/'research_impl.py'),*sys.argv[1:]])
runpy.run_path(str(HERE/'research_impl.py'),run_name='__main__')
''')

def main(argv=None):
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--target',choices=['workbuddy','workbuddy-ai','codex'],default='workbuddy');p.add_argument('--dest');p.add_argument('--home',help='Persistent runtime directory');p.add_argument('--force',action='store_true');p.add_argument('--archive',help='Use the same verified source ZIP offline');p.add_argument('--skip-dependencies',action='store_true',help='Advanced: use current interpreter, which must already have requirements');p.add_argument('--dry-run',action='store_true');a=p.parse_args(argv)
 if sys.version_info<(3,10):raise ValueError('Python 3.10 or newer is required')
 dest=Path(a.dest).expanduser().resolve()if a.dest else Path.home()/('.'+a.target)/'skills'
 home=Path(a.home).expanduser().resolve()if a.home else Path.home()/'.local/share/layoff-research-skills'/VERSION
 plan={'version':VERSION,'target':a.target,'destination':str(dest),'runtime':str(home),'skills':SKILLS,'archive_sha256':ARCHIVE_SHA256,'downloads_source':not bool(a.archive),'installs_dependencies':not a.skip_dependencies,'starts_collection':False}
 print(json.dumps(plan,ensure_ascii=False,indent=2),flush=True)
 if a.dry_run:return 0
 existing=[n for n in SKILLS if(dest/n).exists()]
 if existing and not a.force:raise ValueError('Skills already exist; stop active tasks, then use --force to back up and replace them')
 # Do not start downloads/dependency installation before destination checks.
 for n in SKILLS:
  if(dest/n).is_symlink():raise ValueError('Symlink destination requires manual installation')
 with tempfile.TemporaryDirectory(prefix='layoff-research-download-')as scratch:
  folder=Path(scratch);archive=folder/'source.zip'
  if a.archive:shutil.copyfile(Path(a.archive).expanduser(),archive)
  else:
   request=urllib.request.Request(ARCHIVE_URL,headers={'User-Agent':'LayoffResearchInstaller/1.4.0'})
   with urllib.request.urlopen(request,timeout=60)as response,archive.open('wb')as f:shutil.copyfileobj(response,f)
  root=unpack(archive,folder/'source')
  if a.skip_dependencies:python=Path(sys.executable)
  else:
   env=home/'venv';home.mkdir(parents=True,exist_ok=True)
   if not(env/'pyvenv.cfg').is_file():venv.EnvBuilder(with_pip=True).create(env)
   python=env/('Scripts/python.exe'if os.name=='nt'else'bin/python')
   print('Installing Python dependencies in the isolated runtime...',flush=True)
   subprocess.run([str(python),'-m','pip','install','-r',str(root/'requirements.txt')],check=True)
  command=[str(python),str(root/'install.py'),'--dest',str(dest)]+(['--force']if a.force else[])
  subprocess.run(command,check=True)
  for n in SKILLS:
   add_runtime(dest/n,python)
   subprocess.run([str(python),str(dest/n/'scripts/research.py'),'--help'],stdout=subprocess.DEVNULL,check=True)
  # Copy the long first-use prompt out of the temporary source extraction.
  home.mkdir(parents=True,exist_ok=True);shutil.copyfile(root/'prompts/first-run.en.md',home/'first-run.en.md')
  (home/'installation.json').write_text(json.dumps({**plan,'python':str(python),'status':'installed'},ensure_ascii=False,indent=2)+'\n')
 print('Installed both skills. Refresh skills/reopen your host, then use the README first-run prompt. No collection has started.',flush=True)
 print('Full prompt: '+str(home/'first-run.en.md'))
 return 0
if __name__=='__main__':
 try:raise SystemExit(main())
 except (ValueError,OSError,subprocess.CalledProcessError,zipfile.BadZipFile)as e:print('Installation stopped: '+str(e),file=sys.stderr);raise SystemExit(2)
