"""Build the technical notebook; keeps historical routes and assets in place."""
from pathlib import Path
import re
from html import escape
ROOT=Path(__file__).resolve().parents[1]
ACADEMIC='https://sophiaqian02.github.io/Sophia_Qian.github.io/'
RUBRIC='/2026/10/09/rubrics-and-rl/'
TITLE='Do Rubrics Expand What RL Can Learn?'
DESC='Experiments on rubric-guided post-training: judge choice, reward design, distillation, and the difference between sampling efficiency and reasoning coverage.'
def write(path,s):
 p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s)
def shell(title,body,path='/',description=DESC,lang='en',article=False):
 return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)} · Sophia Qian</title><meta name="description" content="{escape(description)}"><meta name="theme-color" content="#ffffff"><link rel="canonical" href="https://sophiaqian02.github.io{path}"><meta property="og:title" content="{escape(title)}"><meta property="og:description" content="{escape(description)}"><meta property="og:type" content="{'article' if article else 'website'}"><meta property="og:url" content="https://sophiaqian02.github.io{path}"><link rel="icon" href="/assets/notebook-icon.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/notebook.css?v=20261009-serif"><script src="/assets/notebook.js?v=20261009-serif" defer></script></head><body><a class="skip" href="#main">Skip to content</a><header class="site-header"><div class="wrap"><a class="brand" href="/">Sophia Qian<b> / notes</b></a><nav aria-label="Main navigation"><a href="/">Technical Blog</a><a href="{ACADEMIC}">Academic Homepage ↗</a></nav></div></header>{body}<footer class="site-footer"><div class="wrap"><span>© 2026 Feifei (Sophia) Qian · Research in progress</span><a href="{ACADEMIC}">Academic Homepage ↗</a><a href="mailto:Sophia0830BNU@gmail.com">Get in touch ↗</a></div></footer></body></html>'''
def fig(m):
 name,w,h,caption,source=m.groups()
 return f'''<figure class="experiment"><div class="figure-head"><a href="/assets/rubric-rl/{name}" target="_blank" rel="noopener">Open full-size ↗</a></div><a href="/assets/rubric-rl/{name}" target="_blank" rel="noopener" aria-label="Open experiment figure full-size"><img src="/assets/rubric-rl/{name}" width="{w}" height="{h}" loading="lazy" decoding="async" alt="{escape(caption)}"></a><figcaption>{caption}</figcaption></figure>'''
def article(title,hero,content,path,lang='en',extras='',css=''):
 content=re.sub(r'(<h2 id="[^"]+">)\d+ / ',r'\1',content)
 headings=re.findall(r'<h2 id="([^"]+)">(.*?)</h2>',content)
 toc=''.join(f'<li><a href="#{i}">{re.sub("<[^>]+>","",t)}</a></li>' for i,t in headings)
 body=f'''<div class="progress" aria-hidden="true"></div><main id="main" class="{css}"><header class="hero"><div class="wrap">{hero}</div></header>{extras}<div class="wrap reading-layout"><aside class="toc" aria-label="On this page"><details class="toc-disclosure" open><summary>Contents</summary><ol>{toc}</ol></details><a class="back" href="/">← All notes</a></aside><article class="prose">{content}<p><a href="/">← Back to all notes</a></p></article></div></main>'''
 write(path.strip('/')+'/index.html',shell(title,body,path,description=DESC,lang=lang,article=True))
content=(ROOT/'notebook/content/rubrics-and-rl.html').read_text()
content=re.sub(r'\{\{FIG:([^|]+)\|(\d+)\|(\d+)\|([^|]+)\|(\d+)\}\}',fig,content)
hero=f'''<span class="kicker">Field notes / 002 · Post-training</span><h1>Do Rubrics Expand <em>What RL Can Learn?</em></h1><p class="deck">Reading the evidence behind rubric-guided rewards, teacher feedback, and the limits of reasoning coverage.</p><div class="meta"><span>Feifei (Sophia) Qian</span><time datetime="2026-10-09">October 9, 2026</time><span>Preliminary experimental analysis</span></div><div class="tags"><span>Reinforcement learning</span><span>Rubrics</span><span>On-policy distillation</span></div>'''
extras='''<div class="wrap summary-strip"><div><span class="kicker">One distinction</span><strong>Efficiency ≠ coverage</strong><p>Read the whole pass@k curve.</p></div><div><span class="kicker">Four benchmarks</span><strong>No universal winner</strong><p>The effect changes with the task.</p></div><div><span class="kicker">Seven experimental figures</span><strong>Evidence before claims</strong><p>Original plots, explicit limitations.</p></div></div>'''
article(TITLE,hero,content,RUBRIC,extras=extras)
art='''<div class="orb-art" aria-hidden="true"><svg viewBox="0 0 320 320" fill="none"><circle cx="160" cy="160" r="125" stroke="#52678b"/><circle cx="160" cy="160" r="85" stroke="#52678b"/><path d="M35 210L95 155L160 182L222 87L285 111M35 242L95 222L160 153L222 157L285 55" stroke="#a698ea" stroke-width="3"/><path d="M35 263L95 235L160 202L222 148L285 119" stroke="#63d3c5" stroke-width="3"/><g fill="#63d3c5"><circle cx="95" cy="235" r="6"/><circle cx="222" cy="148" r="6"/></g><g fill="#a698ea"><circle cx="95" cy="155" r="6"/><circle cx="222" cy="87" r="6"/></g><text x="25" y="25" fill="#c1cbdf" font-size="10" letter-spacing="3">IDEAS / EVIDENCE / ITERATION</text></svg></div>'''
body=f'''<main id="main" class="wrap"><section class="index-hero"><div><span class="kicker">Sophia's technical notebook</span><h1>Technical notes</h1><p>Notes on graph learning, language models, and how we teach machines to reason. Experiments, explanations, and the questions worth keeping.</p></div>{art}</section><section class="index-tools" aria-label="Filter notes"><div class="filters"><button data-filter="all" aria-pressed="true">All notes</button><button data-filter="RL" aria-pressed="false">Post-training</button></div><label class="search"><input id="search" type="search" placeholder="Search the notebook…" aria-label="Search notes"></label></section><p class="status" id="status" role="status" aria-live="polite">1 note</p><p id="empty" hidden>No matching notes. Try a different keyword or choose All notes.</p><div class="cards"><article class="card" data-note data-tags="RL"><a class="card-art" href="{RUBRIC}" aria-label="Read Do Rubrics Expand What RL Can Learn?"><span class="art-small">POST-TRAINING / EXPERIMENT LOG</span><strong>Rubrics × RL</strong></a><div class="card-body"><span class="kicker">October 9, 2026 · English</span><h2><a href="{RUBRIC}">{TITLE}</a></h2><p>Seven experimental figures on judge choice, reward design, and whether better sampling means broader reasoning coverage.</p><div class="tags"><span>Rubrics</span><span>RL</span><span>Distillation</span></div><a class="read-link" href="{RUBRIC}">Read the experiment log ↗</a></div></article></div></main>'''
write('index.html',shell('Technical Blog',body,description='Sophia Qian’s technical notebook on graph learning, LLMs, rubrics, and reinforcement learning.'))
write('blog/index.html',shell('Technical Blog',body,description='Sophia Qian’s technical notebook.'))
write('.nojekyll','')
write('assets/notebook-icon.svg','<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#17243c"/><text x="10" y="43" font-family="Georgia,serif" font-size="36" fill="#b9adf6">sq</text></svg>')
print('Built notebook index, Rubric-RL post, only.')

# Remove only links to the deleted article from historical theme pages.
for folder in ['archives','tags','categories','about']:
 for old in (ROOT/folder).rglob('index.html'):
  old.write_text(re.sub(r'<a\b[^>]*href=[\"\']/2026/04/08/graph-rag/[\"\'][^>]*>.*?</a>', '', old.read_text(), flags=re.S))
old=ROOT/'404.html'
old.write_text(re.sub(r'<a\b[^>]*href=[\"\']/2026/04/08/graph-rag/[\"\'][^>]*>.*?</a>', '', old.read_text(), flags=re.S))
import json
write('search.json',json.dumps([{'title':TITLE,'path':RUBRIC,'content':DESC}],ensure_ascii=False))

# Canonical blog pages; the academic site's sitemap is also listed in robots.txt.
write('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://sophiaqian02.github.io/</loc></url><url><loc>https://sophiaqian02.github.io' + RUBRIC + '</loc></url></urlset>\n')
