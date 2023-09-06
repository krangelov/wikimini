import urllib.request
from bs4 import BeautifulSoup



def gfpedia_url(qid):
    return 'https://cloud.grammaticalframework.org/wikidata/index.wsgi?id=' + qid + '&lang=en&edit=1'

with open('Qs.tmp') as qidfile:
    for line in qidfile:
        qid = line.split()[1]
        print('--', qid)
        try:
            with urllib.request.urlopen(gfpedia_url(qid)) as response:
                html = response.read()

                ix = str(html).find('"gp-dump">')
                html = str(html)[ix+10:]
                bs = BeautifulSoup(html, 'html.parser')
                for p in bs.find_all('p'):
                    print(p.get_text())
        except:
            print('--', qid, 'FAILED')

