def stable_quickselect(arr, k):
    """
    Implémentation de la sélection rapide stable avec mémoire auxiliaire
    pour trouver l'élément de rang k (basé sur 1)
    """
    # Copie du tableau original pour garder l'ordre stable
    indexed_arr = [(arr[i], i) for i in range(len(arr))]
    
    # Séquence des couples (pivot, rang du pivot)
    pivot_sequence = []
    
    def select(arr, k, left=0, right=None):
        if right is None:
            right = len(arr) - 1
        
        if left == right:
            # Important: On doit également enregistrer le pivot lorsqu'on atteint une feuille
            pivot_val = arr[left][0]
            pivot_sequence.append((pivot_val, 1))  # C'est toujours un tableau de taille 1, donc rang 1
            return arr[left][0]
        
        # Choisir le premier élément comme pivot
        pivot_val = arr[left][0]
        pivot_idx = left
        
        # Partition stable (en utilisant mémoire auxiliaire)
        less = []
        greater = []
        
        for i in range(left + 1, right + 1):
            if arr[i][0] < pivot_val or (arr[i][0] == pivot_val and arr[i][1] < arr[pivot_idx][1]):
                less.append(arr[i])
            else:
                greater.append(arr[i])
        
        # Reconstruire le tableau
        for i, val in enumerate(less):
            arr[left + i] = val
        
        # Position du pivot après partition
        new_pivot_idx = left + len(less)
        arr[new_pivot_idx] = arr[pivot_idx]
        
        for i, val in enumerate(greater):
            arr[new_pivot_idx + 1 + i] = val
        
        # Rang du pivot (basé sur 1) par rapport au sous-tableau actuel
        pivot_rank = new_pivot_idx - left + 1
        
        # Enregistrer le couple (pivot, rang du pivot)
        pivot_sequence.append((pivot_val, pivot_rank))
        
        if k == pivot_rank:
            return arr[new_pivot_idx][0]
        elif k < pivot_rank:
            return select(arr, k, left, new_pivot_idx - 1)
        else:
            return select(arr, k - pivot_rank, new_pivot_idx + 1, right)
    
    result = select(indexed_arr, k)
    return result, pivot_sequence

# Tableau d'entrée
arr = [ 986, 371, 773, 508, 393, 922, 522, 647, 498, 423 ]

# Recherche de l'élément de rang k
k = 2
element, pivot_sequence = stable_quickselect(arr, k)

print(f"L'élément de rang {k} est: {element}")
print("\nSéquence de couples (pivot, rang du pivot):")
for pivot, rank in pivot_sequence:
    print(f"({pivot}, {rank})")

# Affichage du format attendu pour Moodle
print("\nFormat pour Moodle:")
print("[", end="")
for i, (pivot, _) in enumerate(pivot_sequence):
    print(f"[{pivot}]", end="")
    if i < 9:  # Pour avoir 10 emplacements
        print(" ", end="")
for i in range(len(pivot_sequence), 10):
    print("[---]", end="")
    if i < 9:
        print(" ", end="")
print("]")

print("[", end="")
for i, (_, rank) in enumerate(pivot_sequence):
    print(f"[{rank}]", end="")
    if i < 9:
        print(" ", end="")
for i in range(len(pivot_sequence), 10):
    print("[-]", end="")
    if i < 9:
        print(" ", end="")
print("]")

# Tri du tableau pour vérification
sorted_arr = sorted(arr)
print("\nTableau trié:", sorted_arr)
print(f"Vérification: Le {k}ème élément du tableau trié est {sorted_arr[k-1]}")