WIKI_ABSTRACT_FILE = '../Wiki.gf'

RGL_MISSING_FILE = 'missing-in-rgl-Grammar.tsv' # a local copy...

files = """MiniChi.gf	MiniFin.gf	MiniKor.gf	MiniRon.gf	MiniSpa.gf	MiniTur.gf
    MiniAfr.gf	MiniDut.gf	MiniFre.gf	MiniMlt.gf	MiniRus.gf	MiniSwa.gf
    MiniBul.gf	MiniEng.gf	MiniGer.gf	MiniPol.gf	MiniSlv.gf	MiniSwe.gf
    MiniCat.gf	MiniEst.gf	MiniIta.gf	MiniPor.gf	MiniSom.gf	MiniTha.gf
    """.split()

langs = [file[-6:-3] for file in files]

funs = []
with open(WIKI_ABSTRACT_FILE) as file:
    funs = {f[:-1] if f[-1] == ',' else f for f in file.read().split()}

# print(funs)

def massage(row):
    def color(s):
        if s.strip() == '-':
            return "red"
        elif s.strip() == '+':
            return "cyan"
        else:
            return "white"  
    return ['<td bgcolor="'+color(cell) +'">'+cell+'</td>' for cell in row[0:1]+row[2:]]
            
    
with open(RGL_MISSING_FILE) as file:
    header = file.__next__().split('\t')
    rows = [['<th>'+title+'</th>' for title in header[0:1]+header[2:]]]
    for row in file:
        row = row.split('\t')
        if row[0] in funs:
            rows.append(massage(row))

print('<table border="1">')
for row in rows:
    print('<tr>'+''.join(row)+'</tr>')
print('</table>')

