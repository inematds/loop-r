"""Add reciprocal language navigation after local translation builds; no network."""
from pathlib import Path
import os,re
ROOT=Path(__file__).resolve().parents[2]
CSS='''<style id="language-navigation-style">
.language-links,.languages{display:inline-flex;align-items:center;gap:.5rem;font:12px system-ui;white-space:nowrap}.language-links a,.languages a{color:inherit;text-decoration:none}.language-links [aria-current=page],.languages [aria-current=page]{font-weight:700;text-decoration:underline}.language-links{padding:.5rem 1rem}.links>a[lang]{font:12px system-ui}.bar-inner{flex-wrap:wrap}.bar .languages{pointer-events:auto}header.top .wrap{flex-wrap:wrap}
@media(max-width:760px){nav>.wrap{height:auto;min-height:60px;flex-wrap:wrap;gap:12px;padding-block:10px}nav .links{gap:10px;flex-wrap:wrap}}
</style>'''
JS='''<script id="language-navigation-script">(()=>{const update=()=>{document.querySelectorAll('a').forEach(a=>{if(!['PT','EN','ES'].includes(a.textContent.trim()))return;if(!a.dataset.languageBase)a.dataset.languageBase=a.getAttribute('href');const u=new URL(a.dataset.languageBase,location.href);u.search=location.search;u.hash=location.hash;a.href=u.href;const current=(document.documentElement.lang||'pt').slice(0,2).toUpperCase();if(a.textContent.trim()===current)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current');});};update();addEventListener('hashchange',update);})();</script>'''
sources=[ROOT/'guia/index.html',ROOT/'curso/index.html']+[ROOT/f'curso/trilha-{n}/curso.html' for n in range(1,6)]
for source in sources:
 rel=source.relative_to(ROOT)
 if rel.parts[0]=='guia':dest={l:ROOT/'guia'/l/'index.html' for l in ['en','es']}
 elif len(rel.parts)==2:dest={l:ROOT/'curso'/l/'index.html' for l in ['en','es']}
 else:dest={l:ROOT/'curso'/l/Path(*rel.parts[1:]) for l in ['en','es']}
 dest={'pt':source,**dest}
 for lang,p in dest.items():
  text=p.read_text()
  if lang!='pt' and rel.as_posix()=='curso/trilha-4/curso.html':text=re.sub(r'href=([\"\'])aula.css\1', 'href="../../trilha-4/aula.css"',text)
  paths={l:os.path.relpath(d,p.parent) for l,d in dest.items()}
  # Normalize selectors so rebuilding from a PT page cannot duplicate them.
  text=re.sub(r'<span\b[^>]*class="languages"[^>]*>.*?</span>','',text,flags=re.S)
  text=re.sub(r'<nav\b[^>]*class="language-links"[^>]*>.*?</nav>','',text,flags=re.S)
  text=re.sub(r'<div class="wrap language-links">\s*</div>','',text)
  text=re.sub(r'<a\b[^>]*>\s*(?:PT|EN|ES)\s*</a>','',text)
  text=text.replace('<!-- source-language-links -->','')
  links='<span class="languages">'+' · '.join(f'<a lang="{"pt-BR" if l=="pt" else l}" href="{paths[l]}">{l.upper()}</a>' for l in dest)+'</span>'
  if rel.parts[0]=='guia':text=text.replace('<button class="tgl"',links+'<button class="tgl"',1)
  elif len(rel.parts)==2:text=text.replace('</header>','</header><div class="wrap language-links">'+links+'</div>',1)
  else:text=text.replace('</div></div>',links+'</div></div>',1)
  text=re.sub(r'<link\b(?=[^>]*\brel=["\'](?:alternate|canonical)["\'])[^>]*>\s*','',text)
  head=''.join(f'<link rel="alternate" hreflang="{"pt-BR" if l=="pt" else l}" href="{paths[l]}">' for l in dest)
  head+=f'<link rel="alternate" hreflang="x-default" href="{paths["pt"]}"><link rel="canonical" href="https://inematds.github.io/loop-r/{p.relative_to(ROOT).as_posix()}">'
  text=re.sub(r'<style id="language-navigation-style">.*?</style>','',text,flags=re.S)
  text=re.sub(r'<script id="language-navigation-script">.*?</script>','',text,flags=re.S)
  text=text.replace('</head>',head+CSS+'</head>',1).replace('</body>',JS+'</body>',1)
  p.write_text(text)
print('PT/EN/ES reciprocal links, alternates, canonical, and hash/query navigation updated for 21 pages.')
