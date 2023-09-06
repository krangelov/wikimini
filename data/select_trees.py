import sys
import pgf

"""
To populate Wiki.gf:

  $ python3 select_trees.py funs -_LN,_GN,_SN,_PN,_N,_A,_V2,_V3 | sort

To populate Words.gf:

  $ python3 select_trees.py funs +_LN,_GN,_SN,_PN,_N,_A,_V2,_V3 | sort
"""

TREE_FILE = 'all_trees.txt'
#TREE_FILE = 'new_trees.txt'  # to extract all functions in the remaining trees, with no ignore
STOP_FILE = 'ignored_funs.txt'

# to include all functions
def select_all(f):
    return True


# to exclude suffixes, e.g. _PN
def select_by_suffix(fs, sign):
    if sign:
        return lambda f: any([f.endswith(s) for s in fs])
    else:
        return lambda f: not any([f.endswith(s) for s in fs])
        
# to exclude an item in a set
def select_by_list(fs, sign):
    if sign:
        return lambda f: any([f==s for s in fs])
    else:
        return lambda f: not any([f==s for s in fs])


def funs_in_tree(tree, select=select_all):
    funs = set()
    f, ts = tree.unpack()
    if select(f):
        funs.add(f)
    for t in ts:
        for f in funs_in_tree(t, select):
            funs.add(f)
    return funs
    

def select_trees(trees, select=select_all):
    selected = []
    covered = set()
    for tree in trees:
        new = False
        for f in funs_in_tree(tree, select):
            if f not in covered:
                covered.add(f)
                new = True
        if new:
            selected.append(tree)
    return selected, covered


def select_from_file(file=TREE_FILE):
    msg = 'usage: select_trees trees|funs (+STOPFILE|-STOPFILE|+suffixlist|-suffixlist)?'
    if not sys.argv[1:]:
        print(msg)
        return
    else:
        mode = sys.argv[1]
        select = select_all
        if sys.argv[2:]:
            sign = sys.argv[2][0] == '+'
            funs = sys.argv[2][1:]
            if funs=='STOPFILE':
                with open(STOP_FILE) as file:
                    funlist = {line.strip() for line in file}
                    select = select_by_list(funlist, sign)
            else:
                funlist = funs.split(',')
                select = select_by_suffix(funlist, sign)
    trees = []
    with open(TREE_FILE) as file:
        for line in file:
            try:
                trees.append(pgf.readExpr(line))
            except:
                pass
    selected, covered = select_trees(trees, select)
    if mode=='trees':
        for tree in selected:
            print(tree)
    elif mode=='funs':
        for fun in covered:
            print(' ', fun + ',')
    else:
        print(msg)
        
if __name__ == '__main__':
    select_from_file()

