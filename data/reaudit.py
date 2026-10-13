# -*- coding: utf-8 -*-
import json, re, sys, time, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor

UA = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36'}

def fetch(url, method='GET'):
    req = urllib.request.Request(url, headers=UA, method=method)
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            body = r.read().decode('utf-8','replace') if method=='GET' else ''
            return {'url':url,'code':r.status,'final':r.url,'headers':dict(r.headers),'body':body}
    except urllib.error.HTTPError as e:
        return {'url':url,'code':e.code,'final':url,'headers':dict(e.headers),'body':''}
    except Exception as e:
        return {'url':url,'code':0,'final':url,'headers':{},'body':'','err':str(e)}

def txt(html):
    h = re.sub(r'(?is)<(script|style|noscript|svg)\b.*?</\1>',' ',html)
    h = re.sub(r'(?is)<header\b.*?</header>',' ',h)
    h = re.sub(r'(?is)<footer\b.*?</footer>',' ',h)
    h = re.sub(r'(?s)<!--.*?-->',' ',h)
    h = re.sub(r'(?s)<[^>]+>',' ',h)
    h = re.sub(r'&[a-z]+;|&#\d+;',' ',h)
    return re.sub(r'\s+',' ',h).strip()

def analyze(r):
    b = r['body']; out = {'url':r['url'],'code':r['code'],'final':r['final']}
    if not b: return out
    m = re.search(r'(?i)<html[^>]*\blang=["\']([^"\']+)', b); out['lang']=m.group(1) if m else None
    m = re.search(r'(?is)<title[^>]*>(.*?)</title>', b); out['title']=re.sub(r'\s+',' ',m.group(1)).strip() if m else None
    m = re.search(r'(?is)<meta[^>]+name=["\']description["\'][^>]*content=["\']([^"\']*)', b)
    if not m: m = re.search(r'(?is)<meta[^>]+content=["\']([^"\']*)["\'][^>]*name=["\']description["\']', b)
    out['metadesc']=m.group(1).strip() if m else None
    m = re.search(r'(?is)<link[^>]+rel=["\']canonical["\'][^>]*href=["\']([^"\']+)', b); out['canonical']=m.group(1) if m else None
    out['hreflang']=re.findall(r'(?is)<link[^>]+hreflang=["\']([^"\']+)["\'][^>]*href=["\']([^"\']+)', b) + \
                    re.findall(r'(?is)<link[^>]+href=["\']([^"\']+)["\'][^>]*hreflang=["\']([^"\']+)', b)
    out['h1']=[re.sub(r'\s+',' ',txt(x)).strip() for x in re.findall(r'(?is)<h1[^>]*>(.*?)</h1>', b)]
    out['words']=len(txt(b).split())
    out['plugins']=sorted(set(re.findall(r'wp-content/plugins/([a-z0-9\-]+)', b)))
    out['scripts']=len(re.findall(r'(?i)<script[^>]+src=', b))
    out['styles']=len(re.findall(r'(?i)<link[^>]+rel=["\']stylesheet', b))
    out['cache']=r['headers'].get('Cache-Control')
    out['nitro']=r['headers'].get('X-Nitro-Cache')
    out['schema_types']=sorted(set(re.findall(r'"@type"\s*:\s*"([A-Za-z]+)"', b)))
    out['imgs_noalt']=len([x for x in re.findall(r'(?is)<img\b[^>]*>', b) if not re.search(r'(?i)\balt\s*=', x)])
    # internal links
    out['links']=sorted(set(re.findall(r'(?is)<a[^>]+href=["\'](https?://(?:www\.)?openeb5\.com[^"\'#?]*)', b)))
    return out

urls = json.load(open(sys.argv[1], encoding='utf-8'))
res=[]
with ThreadPoolExecutor(max_workers=6) as ex:
    for r in ex.map(fetch, urls):
        res.append(analyze(r))
json.dump(res, open(sys.argv[2],'w',encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'{len(res)} urls analizadas -> {sys.argv[2]}')
