import pgf

# prerequisite:
# gf -make WikiEng.gf WikiSwe.gf WikiFin.gf

PGF_FILE = 'Wiki.pgf'
TREE_FILE = 'data/some_trees.txt'
# TREE_FILE = 'data/all_trees.txt'


gr = pgf.readPGF(PGF_FILE)

def funs_in_tree(tree):
    funs = []
    f, xs = tree.unpack()
    funs.append(f)
    for x in xs:
        for f in funs_in_tree(x):
            funs.append(f)
    return funs


with open(TREE_FILE) as trees:
    missing = {lang: {} for lang in gr.languages}
    for tree in trees:
        try:
            tree = pgf.readExpr(tree)
            print(tree)
            for name, lang in gr.languages.items():
                print(lang.linearize(tree))
                for f in funs_in_tree(tree):
                    if not lang.hasLinearization(f):
                        missing[name][f] = missing[name].get(f, 0) + 1
        except:
            print(tree)
    print(missing)
    for name, funs in missing.items():
        print(name, len(funs))

