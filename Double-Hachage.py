def h1(k, m=None):
    m = 13 if m is None else m
    return k % m

def h2(k, m=None):
    m = 13 if m is None else m
    return (k % (m - 1)) + 1

def insert_double_hash(table, key, verbose=False):
    m = len(table)
    i = h1(key, m)
    step = h2(key, m)
    for attempt in range(m):
        index = (i + attempt * step) % m
        if table[index] is None:
            table[index] = key
            if verbose:
                print(f"Inserted {key} at index {index}")
            return True
    return False

def resize_table_double(old_table):
    new_size = len(old_table) * 2
    print(f"Redimensionnement de la table de taille {len(old_table)} à {new_size}")
    new_table = [None] * new_size
    for key in old_table:
        if key is not None:
            success = insert_double_hash(new_table, key)
            if not success:
                raise Exception(f"Échec de réinsertion de la clé {key} après redimensionnement")
    return new_table

def extend_table_with_keys(initial_table, new_keys, verbose=False,resize_before_insert=False):
    table = initial_table.copy()
    if resize_before_insert:
        print("Redimensionnement avant insertion de 48")
        table = resize_table_double(table)

    for key in new_keys:
        if key is not None:
            success = insert_double_hash(table, key, verbose=verbose)
            if not success:
                raise Exception(f"Échec d’insertion de la clé {key} après redimensionnement.")
    return table

def print_table_as_tiles(table):
    tiles = [f"[{x}]" if x is not None else "[_]" for x in table]
    print('\t'.join(tiles))

def search_key(table, key):
    m = len(table)
    i = h1(key, m)
    step = h2(key, m)
    visited = []
    for t in range(m):
        idx = (i + t * step) % m
        visited.append(idx)
        if table[idx] is None:
            break
        if table[idx] == key:
            return idx, visited
    return None, visited

def insert_key(table, key):
    m = len(table)
    i = h1(key, m)
    step = h2(key, m)
    visited = []
    for t in range(m):
        idx = (i + t * step) % m
        visited.append(idx)
        if table[idx] is None:
            table[idx] = key
            break
    return visited

def delete_key(table, key):
    idx, visited = search_key(table, key)
    if idx is not None:
        table[idx] = None
    return visited

def simulate_operations():
    print("=== Simulation selon l'image : suppression(1) → insertion(9) → insertion(1) → suppression(9) ===")
    table = [56, 27,None,1,17,25,30,33,None,None,None,11,12]
    operations = [
        ("delete", 25),
        ("insert", 30),
        ("insert", 25),
        ("delete", 30)
    ]
    for op, key in operations:
        if op == "delete":
            visited = delete_key(table, key)
            print(f"Suppression de {key} → cases visitées : {visited}")
        elif op == "insert":
            visited = insert_key(table, key)
            print(f"Insertion de {key} → cases visitées : {visited}")

    print("\nÉtat final de la table :")
    for i, val in enumerate(table):
        print(f"{i:02}: {val if val is not None else '_'}")

# === Exemples précédents ===
def run_all():
    simulate_operations()

    print("\n=== Table taille 13, sans redimensionnement ===")
    keys_13 = [50  ,  23  ,  57  ,  63  ,  2  ,  36  ,  10  ,  38  ,  8  ,  27]
    initial_table_13 = [None] * 13
    table13 = extend_table_with_keys(initial_table_13, keys_13)
    print_table_as_tiles(table13)

    print("\n=== Table taille 9 avec redimensionnement avant insertion de 48 ===")
    initial_table_9 = [21,	34,	29,	30	,None,None,  	  	43	,7,None]
    table18 = extend_table_with_keys(initial_table_9, [3], verbose=True,resize_before_insert=True)
    print_table_as_tiles(table18)

# Lancer tout
run_all()
