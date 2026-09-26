"""Check completed lesson catalogs against generated HTML without external services."""
from pathlib import Path
from bs4 import BeautifulSoup, Comment
from collections import Counter
import argparse,json,re
ROOT=Path(__file__).resolve().parents[2]
LOCALIZED={'data-def','data-fb','data-cap','data-rotulo','data-exlbl','title','alt','aria-label','placeholder'}
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--track',type=int);args=parser.parse_args()
 catalogs=sorted((ROOT/'i18n/translations').glob(f'track-{args.track or "*"}-lesson-*.json'))
 results=[]
 for catalog in catalogs:
  match=re.fullmatch(r'track-(\d+)-lesson-(\d+)\.json',catalog.name)
  track,lesson=map(int,match.groups());units=json.loads(catalog.read_text())
  assert all(isinstance(v,list) and len(v)==2 and all(isinstance(s,str) and s.strip() for s in v) for v in units.values()),catalog
  source=BeautifulSoup((ROOT/f'curso/trilha-{track}/curso.html').read_text(),'html.parser').select_one(f'#v-aula-{lesson}')
  for lang in ['en','es']:
   target=BeautifulSoup((ROOT/f'curso/{lang}/trilha-{track}/curso.html').read_text(),'html.parser').select_one(f'#v-aula-{lesson}')
   assert target is not None,(catalog.name,lang,'missing view')
   assert Counter(x.name for x in source.find_all())==Counter(x.name for x in target.find_all()),(catalog.name,lang,'structure')
   for a,b in zip(source.find_all(),target.find_all()):
    assert a.name==b.name,(catalog.name,lang,'tag order')
    for key,value in a.attrs.items():
     if key not in LOCALIZED:assert b.get(key)==value,(catalog.name,lang,key)
   candidates=[]
   for x,y in zip(source.find_all(),target.find_all()):
    for attr in LOCALIZED:
     v=x.get(attr,'')
     if len(v)>35 and v==y.get(attr):candidates.append(f'unchanged {attr}: {v[:140]}')
   a=source.select_one(f'#cards-{lesson}');b=target.select_one(f'#cards-{lesson}')
   if a:
    aa=json.loads(a.string);bb=json.loads(b.string);assert len(aa)==len(bb),(catalog.name,lang,'card count')
    for x,y in zip(aa,bb):
     assert x.keys()==y.keys(),(catalog.name,lang,'card keys')
     for key in ('front','back'):
      v=y.get(key,'')
      if (len(v)>35 and v==x.get(key)) or re.search(r'ção|ções|\bvocê\b|\bnão\b',v,re.I):candidates.append(f'card {key}: {v[:140]}')
   for n in target.find_all(string=True):
    if isinstance(n,Comment) or n.parent.name in ['script','style']:continue
    if re.search(r'ção|ções|\bvocê\b|\bnão\b|\baprendizado\b',str(n),re.I):candidates.append(str(n).strip()[:160])
   for e in target.find_all():
    for attr in LOCALIZED:
     value=e.get(attr,'')
     if re.search(r'ção|ções|\bvocê\b|\bnão\b',value,re.I):candidates.append(f'{attr}: {value[:140]}')
   results.append({'track':track,'lesson':lesson,'lang':lang,'units':len(units),'pt_candidates':candidates})
 print(json.dumps(results,ensure_ascii=False,indent=2))
 if any(r['pt_candidates'] for r in results):raise SystemExit(1)
if __name__=='__main__':main()
