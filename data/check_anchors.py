# -*- coding: utf-8 -*-
"""Comprueba, contra el HTML en vivo, si cada ancla del plan de enlazado
interno existe realmente en la pagina de origen."""
import io, re, sys, json, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
UA = {'User-Agent': 'Mozilla/5.0'}

PLAN = {
 'EN': {
  'https://openeb5.com/': [
    'The EB-5 Immigrant Investor Program',
    'Every Open EB5 project is selected for compliance',
    'We work with investors across Latin America, Asia, Europe, the Middle East, and Oceania,',
    'Real names, verifiable track records.',
    'I-526E adjudication ranges from 12-24 months depending on category.',
  ],
  'https://openeb5.com/about-us/': ['the federal EB-5 program', 'the EB-5 Reform and Integrity Act of 2022.'],
  'https://openeb5.com/the-team/': ['EB-5 applicants'],
  'https://openeb5.com/eb-5/': ['Open EB5, a USCIS-approved Regional Center,', 'Open EB5 projects', 'review your eligibility', 'I-526E filing, consular processing, and the I-829 milestone.'],
  'https://openeb5.com/the-complete-guide-to-eb-5-investment/': ['USCIS-approved Regional Center', 'The EB-5 Program', 'job-creating projects.', 'I-526E petition filing'],
  'https://openeb5.com/countries/': ['the EB-5 program', 'Open EB5'],
  'https://openeb5.com/america/': ['Open EB5 for proximity', 'U.S. immigration counsel'],
  'https://openeb5.com/asia/': ["Open EB5's", 'the EB-5 program', 'the EB-5 Reform Act of 2022'],
  'https://openeb5.com/europe/': ["Open EB5's", 'the EB-5 Reform Act of 2022'],
  'https://openeb5.com/oceania/': ['the EB-5 program', 'the EB-5 Reform Act of 2022'],
  'https://openeb5.com/business/5-factors-to-consider-before-choosing-an-eb-5-project-in-2026/': ['Midtown Pharr project', 'The EB-5 Immigrant Investor Program', 'EB-5 project', 'I-956F approval from USCIS'],
  'https://openeb5.com/business/eb-5-project-strength-explained-why-midtown-brownsville-ii-is-a-strategic-opportunity-in-the-rio-grande-valley/': ['U.S. Department of Commerce economic reports', 'EB-5 program overview guide'],
  'https://openeb5.com/business/open-eb5-secures-i-956f-approval-for-midtown-pharr-a-milestone-in-the-rio-grande-valley/': ['Emilio Guzman, CEO of Open EB5', 'Open EB5 is a U.S.-based EB-5 Regional Center', 'I-956F approval'],
  'https://openeb5.com/business/what-happens-after-obtaining-the-green-card-through-eb-5-stages-rights-and-next-steps/': ['EB-5 program requirements', 'Form I-829,', 'At Open EB-5, we closely monitor each case'],
  'https://openeb5.com/business/eb-5-grandfathering-deadline-september-30-2026/': ['The EB-5 Reform and Integrity Act of 2022', 'Open EB-5', 'investment in qualified projects.'],
  'https://openeb5.com/business/midtown-brownsville-positioned-at-the-center-of-a-new-u-s-energy-industrial-expansion/': ['EB-5 project currently available in Brownsville', 'U.S. energy and industrial landscape.'],
  'https://openeb5.com/business/eb-5-program-how-a-financial-contribution-allows-you-to-legally-immigrate-to-the-u-s/': ['The EB5 program', 'TEA zones (Targeted Employment Area),', 'Open EB-5 is the ideal team'],
  'https://openeb5.com/business/families-in-latin-america-and-europe-are-choosing-the-eb-5-program-why/': ['USCIS (U.S. Citizenship and Immigration Services)', 'Midtown Pharr,', 'At Open EB-5,', 'What would you do if you had the chance to open the doors of the United States to your children today?'],
 },
 'ES': {
  'https://openeb5.com/ES/': ['Cada proyecto de Open EB5', 'El Programa de Inmigrante Inversionista EB-5', 'Latinoamérica, Asia, Europa, Medio Oriente y Oceanía,', 'La adjudicación del I-526E'],
  'https://openeb5.com/ES/nosotros/': ['el programa federal EB-5,', 'EB-5 Reform Act de 2022.', 'Open EB5'],
  'https://openeb5.com/ES/el-equipo/': ['el programa federal EB-5'],
  'https://openeb5.com/ES/eb-5/': ['Open EB5, Centro Regional aprobado por USCIS', 'Los proyectos de Open EB5', 'el hito I-829.'],
  'https://openeb5.com/ES/guia-integral-para-inversiones-eb5/': ['Centro Regional aprobado por USCIS con sede en McAllen, Texas.', 'El Programa EB-5', 'proyectos que crean empleo.', 'Presentación de petición I-526E'],
  'https://openeb5.com/ES/paises/': ['los proyectos de Texas de Open EB5', 'Open EB5'],
  'https://openeb5.com/ES/proyectos-actuales/': ['Open EB5', 'Ley de Reforma EB-5 de 2022.'],
  'https://openeb5.com/ES/america/': ['Open EB5'],
  'https://openeb5.com/ES/asia/': ['los proyectos de Texas de Open EB5'],
  'https://openeb5.com/ES/europa/': ['Open EB5.'],
  'https://openeb5.com/ES/blog/guia-de-la-visa-de-inversionista-eb-5-requisitos-costos-y-el-camino-hacia-la-green-card/': ['el Programa de Inversión EB-5', 'agenda una consulta personalizada para iniciar tu proceso hoy mismo.', 'openeb5', 'I-485'],
  'https://openeb5.com/ES/blog/que-pasa-despues-de-obtener-la-green-card-por-eb-5-etapas-y-proximos-pasos/': ['una solicitud EB-5', 'programa EB-5', 'Formulario I-829,'],
  'https://openeb5.com/ES/blog/green-card-como-obtenerla-por-inversion-empleo-o-familia/': ['EB-2 NIW'],
  'https://openeb5.com/ES/blog/que-es-la-green-card-y-que-beneficios-ofrece-en-estados-unidos/': ['Open EB-5', 'ventajas del programa EB-5', 'Aprobación del I-829'],
  'https://openeb5.com/ES/blog/requisitos-actualizados-para-la-visa-eb-5-en-2025/': ['Todavía tienes dudas sobre el programa EB-5'],
  'https://openeb5.com/ES/blog/por-que-texas-es-el-lugar-ideal-para-invertir-y-obtener-tu-visa-eb5-con-open-eb5/': ['Midtown Pharr,', 'nuestro equipo te guía', 'Agenda una consulta', 'Valle del Río Grande'],
 },
}


def body_text(html):
    h = re.sub(r'(?is)<(script|style|noscript|svg)\b.*?</\1>', ' ', html)
    h = re.sub(r'(?s)<!--.*?-->', ' ', h)
    h = re.sub(r'(?s)<[^>]+>', ' ', h)
    h = (h.replace('&amp;', '&').replace('&#039;', "'").replace('&rsquo;', "'")
           .replace('&nbsp;', ' ').replace('&quot;', '"').replace('&#8217;', "'")
           .replace('&ndash;', '-').replace('&mdash;', ','))
    return re.sub(r'\s+', ' ', h)


def fetch(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r:
            return url, r.read().decode('utf-8', 'replace')
    except Exception as e:
        return url, ''


urls = [u for lang in PLAN for u in PLAN[lang]]
pages = {}
with ThreadPoolExecutor(max_workers=5) as ex:
    for u, h in ex.map(fetch, urls):
        pages[u] = body_text(h) if h else None

hit = miss = 0
for lang in PLAN:
    print('=' * 70)
    print(lang)
    print('=' * 70)
    for url, anchors in PLAN[lang].items():
        txt = pages.get(url)
        short = url.replace('https://openeb5.com', '')
        if txt is None:
            print(f'  [sin respuesta] {short}')
            continue
        low = txt.lower()
        results = []
        for a in anchors:
            ok = a.lower() in low
            results.append((ok, a))
            if ok:
                hit += 1
            else:
                miss += 1
        n_ok = sum(1 for ok, _ in results if ok)
        print(f'  {short}   {n_ok}/{len(anchors)}')
        for ok, a in results:
            if not ok:
                print(f'       NO ENCONTRADA: "{a[:80]}"')

print()
print(f'TOTAL anclas: {hit + miss}  ·  encontradas {hit}  ·  no encontradas {miss}')
