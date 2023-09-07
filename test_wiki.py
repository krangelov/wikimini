import pgf

# prerequisite:
# gf -make WikiEng.gf WikiSwe.gf WikiFin.gf

PGF_FILE = 'Wiki.pgf'
TREE_FILE = 'data/all_trees.txt'


gr = pgf.readPGF(PGF_FILE)

with open(TREE_FILE) as trees:
    for tree in trees:
        try:
            tree = pgf.readExpr(tree)
            print(tree)
            for lang in gr.languages.values():
                print(lang.linearize(tree))
        except:
            print(tree)
        
