



def partition(T):
    pivot = T[0]
    gauche = [elt for elt in T[1:] if elt < pivot]
    droite = [elt for elt in T[1:] if elt > pivot]
    return pivot, gauche, droite


def build_quicksort_tree(T, parent=None, relation="racine"):

    if len(T) == 0:
        return None
    pivot, sous_T = T[0], T[1:]
    if parent is None:
        print(f"{pivot} est la racine")
    else:
        print(f"{pivot} est le fils {relation} de {parent}")
    if len(sous_T) >= 1:
        _, gauche, droite = partition(T)
        build_quicksort_tree(gauche, pivot, "gauche")
        build_quicksort_tree(droite, pivot, "droit")
    return pivot


def print_tree(T, indent=0):

    if not isinstance(T, tuple) and not isinstance(T, list):
        return

# Exemple d’utilisation
if __name__ == '__main__':
    tableau = [ 491, 325, 861, 729, 378, 627, 811, 271, 690, 443, 910, 171, 143, 539 ]
    print("Placement à faire :")
    build_quicksort_tree(tableau)