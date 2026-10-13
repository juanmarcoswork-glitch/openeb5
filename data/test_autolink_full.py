# -*- coding: utf-8 -*-
"""Verificacion completa del plan de enlazado interno.

Lee las reglas directamente de los dos inc/internal-links.php, las aplica
con un puerto fiel del algoritmo PHP sobre el HTML en vivo, y comprueba:

  1. Cuantas anclas se aplican de verdad (a nivel de nodo de texto, no de
     texto plano: una frase partida por <b> no se puede envolver).
  2. Que la transformacion NO aumente la profundidad de anidamiento de
     <a> respecto del HTML original.
  3. Que el numero de <a> crezca exactamente en el numero de anclas
     aplicadas.
"""
import io, os, re, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
UA = {'User-Agent': 'Mozilla/5.0'}
ROOT = r'c:/Users/juanm/OneDrive/Desktop/Proyectos/clientes/openeb5'

TAG_RE = re.compile(r'(<[^>]+>)')
NAME_RE = re.compile(r'^</?\s*([a-z0-9]+)', re.I)
H_RE = re.compile(r'^h[1-6]$')


# ── Extraer las reglas del PHP ────────────────────────────────────────
def parse_rules(php_path):
    src = io.open(php_path, encoding='utf-8').read()
    body = src[src.index('function openeb5_autolink_rules() {'):src.index('/**\n * Reglas que aplican a la request actual.')]

    # Resolver las variables de URL declaradas al inicio de la funcion.
    vars_ = {}
    for m in re.finditer(r"\$(\w+)\s*=\s*'([^']*)'\s*;", body):
        vars_[m.group(1)] = m.group(2)
    for m in re.finditer(r"\$(\w+)\s*=\s*\$(\w+)\s*\.\s*'([^']*)'\s*;", body):
        if m.group(2) in vars_:
            vars_[m.group(1)] = vars_[m.group(2)] + m.group(3)

    body = re.sub(r'/\*.*?\*/', '', body, flags=re.S)
    body = re.sub(r'//[^\n]*', '', body)

    rules, current = {}, None
    for line in body.splitlines():
        line = line.strip()
        mkey = re.match(r"^'([^']+)'\s*=>\s*array\($", line)
        if mkey:
            current = mkey.group(1)
            rules[current] = []
            continue
        mr = re.match(r"^array\(\s*'anchor'\s*=>\s*(.+?),\s*'url'\s*=>\s*(.+?)\s*(?:,\s*'ext'\s*=>\s*(true))?\s*\),?$", line)
        if mr and current:
            def lit(tok):
                tok = tok.strip()
                if tok.startswith("'") and tok.endswith("'"):
                    return tok[1:-1].replace("\\'", "'")
                if tok.startswith('"') and tok.endswith('"'):
                    return tok[1:-1]
                mcat = re.match(r"^\$(\w+)\s*\.\s*'([^']*)'$", tok)
                if mcat:
                    return vars_.get(mcat.group(1), '?') + mcat.group(2)
                mvar = re.match(r'^\$(\w+)$', tok)
                if mvar:
                    return vars_.get(mvar.group(1), '?')
                return tok
            rules[current].append({'anchor': lit(mr.group(1)), 'url': lit(mr.group(2)), 'ext': bool(mr.group(3))})
    return rules


# ── Puerto del algoritmo ──────────────────────────────────────────────
def autolink(html, rules):
    rules = sorted(rules, key=lambda r: -len(r['anchor']))
    parts = TAG_RE.split(html)
    depth = {'a': 0, 'script': 0, 'style': 0, 'heading': 0, 'button': 0}
    done, applied = set(), []

    for i, part in enumerate(parts):
        if part and part[0] == '<':
            m = NAME_RE.match(part)
            if m:
                tag = m.group(1).lower()
                closing = part[1] == '/'
                selfclose = part.rstrip().endswith('/>')
                key = tag if tag in depth else ('heading' if H_RE.match(tag) else None)
                if key and not selfclose:
                    depth[key] += -1 if closing else 1
                    if depth[key] < 0:
                        depth[key] = 0
            continue
        if not part.strip() or sum(depth.values()) > 0:
            continue
        for r in rules:
            anchor = r['anchor']
            if anchor in done:
                continue
            bases = [anchor]
            if "'" in anchor:
                bases.append(anchor.replace("'", '&#039;'))
                bases.append(anchor.replace("'", '&#8217;'))
                bases.append(anchor.replace("'", '’'))
            candidates = []
            for base in bases:
                candidates.append(base)
                t = base.rstrip(' ,.;: ')
                if t and t != base:
                    candidates.append(t)
            pos, needle, low = -1, anchor, part.lower()
            for c in candidates:
                p = low.find(c.lower())
                if p != -1:
                    pos, needle = p, c
                    break
            if pos == -1:
                continue
            found = part[pos:pos + len(needle)]
            attrs = ' target="_blank" rel="noopener nofollow"' if r.get('ext') else ''
            part = part[:pos] + f'<a href="{r["url"]}"{attrs}>{found}</a>' + part[pos + len(needle):]
            done.add(anchor)
            applied.append(anchor)
        parts[i] = part
    return ''.join(parts), applied


def max_anchor_depth(html):
    depth = maxd = 0
    for m in re.finditer(r'</?a\b[^>]*>', html, re.I):
        if m.group(0).startswith('</'):
            depth -= 1
        else:
            depth += 1
        maxd = max(maxd, depth)
        if depth < 0:
            depth = 0
    return maxd


# ── Slug -> URL en vivo ───────────────────────────────────────────────
EN_URL = {
    '__front__': 'https://openeb5.com/',
    'about-us': 'https://openeb5.com/about-us/',
    'the-team': 'https://openeb5.com/the-team/',
    'eb-5': 'https://openeb5.com/eb-5/',
    'the-complete-guide-to-eb-5-investment': 'https://openeb5.com/the-complete-guide-to-eb-5-investment/',
    'countries': 'https://openeb5.com/countries/',
    'america': 'https://openeb5.com/america/',
    'asia': 'https://openeb5.com/asia/',
    'europe': 'https://openeb5.com/europe/',
    'oceania': 'https://openeb5.com/oceania/',
}
ES_URL = {
    '__front__': 'https://openeb5.com/ES/',
    'nosotros': 'https://openeb5.com/ES/nosotros/',
    'el-equipo': 'https://openeb5.com/ES/el-equipo/',
    'eb-5': 'https://openeb5.com/ES/eb-5/',
    'guia-integral-para-inversiones-eb5': 'https://openeb5.com/ES/guia-integral-para-inversiones-eb5/',
    'paises': 'https://openeb5.com/ES/paises/',
    'proyectos-actuales': 'https://openeb5.com/ES/proyectos-actuales/',
    'america': 'https://openeb5.com/ES/america/',
    'asia': 'https://openeb5.com/ES/asia/',
    'europa': 'https://openeb5.com/ES/europa/',
}


def url_for(lang, slug):
    table = EN_URL if lang == 'EN' else ES_URL
    if slug in table:
        return table[slug]
    return (f'https://openeb5.com/business/{slug}/' if lang == 'EN'
            else f'https://openeb5.com/ES/blog/{slug}/')


def fetch(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=45) as r:
            return url, r.read().decode('utf-8', 'replace')
    except Exception as e:
        return url, ''


plans = {
    'EN': parse_rules(os.path.join(ROOT, 'wp-content/themes/openeb5/inc/internal-links.php')),
    'ES': parse_rules(os.path.join(ROOT, 'ES/wp-content/themes/openeb5/inc/internal-links.php')),
}

jobs = [(lang, slug, url_for(lang, slug)) for lang in plans for slug in plans[lang]]
pages = {}
with ThreadPoolExecutor(max_workers=5) as ex:
    for u, h in ex.map(fetch, [j[2] for j in jobs]):
        pages[u] = h

tot_applied = tot_rules = structural_fails = 0
unapplied = []

for lang, slug, url in jobs:
    rules = plans[lang][slug]
    tot_rules += len(rules)
    html = pages.get(url) or ''
    if not html:
        print(f'  [sin respuesta] {lang} {url}')
        continue
    m = re.search(r'(?is)<body\b', html)
    body = html[m.start():] if m else html

    d_before = max_anchor_depth(body)
    a_before = len(re.findall(r'<a\b', body, re.I))
    out, applied = autolink(body, rules)
    d_after = max_anchor_depth(out)
    a_after = len(re.findall(r'<a\b', out, re.I))

    tot_applied += len(applied)
    ok_depth = d_after <= d_before
    ok_delta = (a_after - a_before) == len(applied)
    if not (ok_depth and ok_delta):
        structural_fails += 1

    flag = 'OK ' if (ok_depth and ok_delta) else 'FAIL'
    print(f'[{flag}] {lang} {url.replace("https://openeb5.com", "")}  {len(applied)}/{len(rules)}  '
          f'<a> {a_before}->{a_after}  anidamiento {d_before}->{d_after}')
    for r in rules:
        if r['anchor'] not in applied:
            unapplied.append((lang, slug, r['anchor']))

print()
print(f'ANCLAS APLICADAS: {tot_applied}/{tot_rules}')
print(f'FALLOS ESTRUCTURALES (anidamiento o delta): {structural_fails}')
if unapplied:
    print('\nSin aplicar:')
    for lang, slug, a in unapplied:
        print(f'  {lang} · {slug}\n      "{a[:90]}"')
