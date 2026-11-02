from pathlib import Path
import re,sys
p=Path(__file__).resolve().parent
required=['index.html','style.css','app.js','firebase-config.js','firestore.rules','storage.rules','firebase.json','.nojekyll']
issues=[]
for x in required:
 if not (p/x).is_file(): issues.append('Missing: '+x)
if (p/'index.html').exists():
 html=(p/'index.html').read_text(encoding='utf-8')
 for name in ['style.css','app.js']:
  if name not in html: issues.append('HTML does not reference '+name)
if (p/'app.js').exists() and 'firebase-config.js' not in (p/'app.js').read_text(encoding='utf-8'): issues.append('Missing Firebase config import')
print('STRUCTURE: '+('PASS' if not issues else 'FAIL'))
for x in issues: print(' -',x)
if (p/'firebase-config.js').exists() and 'PASTE_' in (p/'firebase-config.js').read_text(encoding='utf-8'):
 print('CONFIG: Not configured yet (expected; fill Firebase details before deploying)')
sys.exit(bool(issues))
