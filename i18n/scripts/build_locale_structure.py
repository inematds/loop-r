from pathlib import Path
root=Path('/home/nmaldaner/projetos/loop-r')
for lang in ('en','es'):
    p=root/'guia'/lang/'index.html'; s=p.read_text()
    alternates=f'<link rel="alternate" hreflang="pt-BR" href="../"><link rel="alternate" hreflang="en" href="{("./" if lang=="en" else "../en/")}"><link rel="alternate" hreflang="es" href="{("../es/" if lang=="en" else "./")}"><link rel="alternate" hreflang="x-default" href="../">'
    s=s.replace('<link rel="alternate" hreflang="pt-BR" href="../"><link rel="alternate" hreflang="en" href="../en/"><link rel="alternate" hreflang="es" href="../es/"><link rel="alternate" hreflang="x-default" href="../">',alternates)
    s=s.replace('  .pill{display:inline-block;', '  .links .langs{display:inline-flex;gap:7px}\n  .links .langs a{color:var(--mut);font-size:.85rem}\n  .links .langs a.on{color:var(--amb);font-weight:700}\n  .pill{display:inline-block;')
    p.write_text(s)
    # Course tracks
    for n in range(1,6):
        p=root/'curso'/lang/f'trilha-{n}'/'curso.html'; s=p.read_text()
        s=s.replace('lang="pt-BR"',f'lang="{lang}"',1)
        # Update document title by preserving title suffix and translating the exact track name/title separately later.
        enhref='../../es/trilha-'+str(n)+'/curso.html' if lang=='en' else '../../en/trilha-'+str(n)+'/curso.html'
        pthref='../../trilha-'+str(n)+'/curso.html'
        selector=f'<span class="languages"><a href="{pthref}" lang="pt-BR">PT</a> · <a href="./curso.html" lang="{lang}">{lang.upper()}</a> · <a href="{enhref}" lang="{"es" if lang=="en" else "en"}">{"ES" if lang=="en" else "EN"}</a></span>'
        s=s.replace('</div></div>\n\n<!-- ===== TRILHA ===== -->',selector+'\n</div></div>\n\n<!-- ===== TRILHA ===== -->',1)
        s=s.replace('</head>','<link rel="alternate" hreflang="pt-BR" href="'+pthref+'"><link rel="alternate" hreflang="en" href="'+("./curso.html" if lang=="en" else enhref)+'"><link rel="alternate" hreflang="es" href="'+(enhref if lang=="en" else "./curso.html")+'"><link rel="alternate" hreflang="x-default" href="'+pthref+'">\n</head>')
        s=s.replace('.view{display:none}.view.active{display:block}', '.view{display:none}.view.active{display:block}\n  .languages{font:11px var(--mono);white-space:nowrap}.languages a{color:var(--muted);text-decoration:none}.languages a[lang="'+lang+'"]{color:var(--accent);font-weight:700}')
        p.write_text(s)
    # course overview alternates
    p=root/'curso'/lang/'index.html'; s=p.read_text()
    alternates=f'<link rel="alternate" hreflang="pt-BR" href="../"><link rel="alternate" hreflang="en" href="{("./" if lang=="en" else "../en/")}"><link rel="alternate" hreflang="es" href="{("../es/" if lang=="en" else "./")}"><link rel="alternate" hreflang="x-default" href="../">'
    s=s.replace('</head>',alternates+'\n</head>')
    p.write_text(s)
