import pgf

TREE_FILE = 'all_trees.txt'
#TREE_FILE = 'new_trees.txt'  # to extract all functions in the remaining trees, with no ignore
STOP_FILE = 'ignored_funs.txt'

# to include all functions
def no_ignore_fun(f):
    return False

# to exclude suffixes, e.g. _PN
def ignore_by_suffix(fs):
    return lambda f: any([f.endswith(s) for s in fs])

# to exclude an item in a set
def ignore_by_list(fs):
    return lambda f: any([f==s for s in fs])


def funs_in_tree(tree, ignore=no_ignore_fun):
    funs = set()
    f, ts = tree.unpack()
    if not ignore(f):
        funs.add(f)
    for t in ts:
        for f in funs_in_tree(t, ignore):
            funs.add(f)
    return funs
    

def select_trees(trees, ignore=no_ignore_fun):
    selected = []
    covered = set()
    for tree in trees:
        new = False
        for f in funs_in_tree(tree, ignore):
            if f not in covered:
                covered.add(f)
                new = True
        if new:
            selected.append(tree)
    return selected, covered

import sys
def select_from_file(file=TREE_FILE):
    msg = 'usage: select_trees trees|funs (STOPFILE|ignoredsuffixlist)?'
    if not sys.argv[1:]:
        print(msg)
        return
    else:
        mode = sys.argv[1]
        ignore = no_ignore_fun
        if sys.argv[2:]:
            if sys.argv[2]=='STOPFILE':
                with open(STOP_FILE) as file:
                    ignores = {line.strip() for line in file}
                    ignore = ignore_by_list(ignores)
            else:
                ignores = sys.argv[2].split(',')
                ignore = ignore_by_suffix(ignores)
    trees = []
    with open(TREE_FILE) as file:
        for line in file:
            try:
                trees.append(pgf.readExpr(line))
            except:
                pass
    selected, covered = select_trees(trees, ignore)
    if mode=='trees':
        for tree in selected:
            print(tree)
    elif mode=='funs':
        for fun in covered:
            print(fun)
    else:
        print(msg)
        
if __name__ == '__main__':
    select_from_file()

