#!/usr/bin/env python3
"""Render one translated lesson from immutable PT text units, without network calls."""
import argparse, html, json
from pathlib import Path
from html.parser import HTMLParser
from bs4 import BeautifulSoup, NavigableString, Comment
ROOT=Path(__file__).resolve().parents[2]

def lesson_span(text, lesson):
    offsets=[0]
    for line in text.splitlines(keepends=True): offsets.append(offsets[-1]+len(line))
    class Sections(HTMLParser):
        def __init__(self): super().__init__(convert_charrefs=False);self.depth=0;self.start=None;self.end=None;self.target=None
        def position(self):
            line,col=self.getpos();return offsets[line-1]+col
        def handle_starttag(self,tag,attrs):
            if tag=='section':
                self.depth+=1
                if dict(attrs).get('id')==f'v-aula-{lesson}':self.start=self.position();self.target=self.depth
        def handle_endtag(self,tag):
            if tag=='section':
                if self.start is not None and self.end is None and self.depth==self.target:self.end=text.index('>',self.position())+1
                self.depth-=1
    parser=Sections();parser.feed(text)
    if parser.start is None or parser.end is None:raise ValueError(f'Lesson {lesson} section not found')
    return parser.start,parser.end

def normalize(value):return ' '.join(html.unescape(value).split())

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--track',type=int,required=True);parser.add_argument('--lesson',type=int,required=True);parser.add_argument('--lang',choices=['en','es'],required=True);args=parser.parse_args()
    units=json.loads((ROOT/f'i18n/translations/track-{args.track}-lesson-{args.lesson}.json').read_text())
    index=0 if args.lang=='en' else 1
    mapping={normalize(k):v[index] for k,v in units.items()}
    def translate(value):
        key=normalize(value)
        if key not in mapping:return value
        leading=value[:len(value)-len(value.lstrip())];trailing=value[len(value.rstrip()):]
        return leading+mapping[key]+trailing
    source=(ROOT/f'curso/trilha-{args.track}/curso.html').read_text();start,end=lesson_span(source,args.lesson)
    soup=BeautifulSoup(source[start:end],'html.parser')
    # Complete text units only: never translate part of an identifier or already-translated output.
    for node in list(soup.find_all(string=True)):
        if isinstance(node,Comment) or node.parent.name in ('script','style'):continue
        value=translate(str(node))
        if value!=str(node):node.replace_with(NavigableString(value))
    for element in soup.find_all():
        for attr in ('data-def','data-fb','data-cap','data-rotulo','data-exlbl','title','alt','aria-label','placeholder'):
            if isinstance(element.get(attr),str):element[attr]=translate(element[attr])
    # JSON remains data: escaping is handled by the JSON encoder, never by HTML substitution.
    for script in soup.select('script[type="application/json"]'):
        cards=json.loads(script.string or script.get_text())
        if not isinstance(cards,list):continue
        for card in cards:
            if isinstance(card,dict):
                for field in ('front','back'):
                    if isinstance(card.get(field),str):card[field]=translate(card[field])
        script.string='\n'+json.dumps(cards,ensure_ascii=False,indent=2).replace('</','<\\/')+'\n'
    page=ROOT/f'curso/{args.lang}/trilha-{args.track}/curso.html';text=page.read_text();a,b=lesson_span(text,args.lesson)
    page.write_text(text[:a]+str(soup)+text[b:])
    print(f'updated {page.relative_to(ROOT)} from PT using {len(mapping)} complete units')
if __name__=='__main__':main()
