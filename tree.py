def tree(label,branches=[]):
    for branch in branches :
        assert is_tree(branch)
    return [label]+list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1 :
        return False
    for branch in branches(tree) :
        if not is_tree(branch) :
            return False
    return True

def is_leaf(tree):
    return not branches(tree)


def fib_tree(n):
    if n <= 1 :
        return tree(n)
    else :
        left , right = fib_tree(n-2),fib_tree(n-1)
    return tree(label(left)+label(right),[left,right])

#counting leaves in a tree 

def count_leaves(t):
    if is_leaf(t):
        return 1 
    else : 
        branch_counts = [count_leaves(b) for b in branches(t)]
        return sum(branch_counts)

#list all of leaves in a tree
def leaves(tree):
    if is_leaf(tree) :
        return label(tree)
    else :
        return sum([leaves(b) for b in branches(tree)],[])

def increment_leaves(t):
    if is_leaf(t):
         return tree(label(t)+1)
    else :
        bs = [increment(b) for b in branches(t)]
        return tree(label(t),bs)

def increment(t):
    return tree(label(t)+1,[increment(b) for b in branches(t)])

# reach base case when is leaves, the brances will be [], increment(b) can not be conducted 

def print_tree(t,indent=0):
    print(' '*indent + str(label(t)))

    for b in branches(t) :
        print_tree(b,indent+1)


#count
def count_paths(t,total):
    """ Return the number of paths from the root to any node in tree for 
    which the labels along the path sum to total ."""
    if label(t) == total :
        found = 1 
    else :
        found = 0 
    return found + sum ([count_paths(b, total-label(t)) for b in branches(t)])