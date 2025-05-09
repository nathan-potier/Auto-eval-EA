def h(k, m):
    return k % m  # Hachage simple

def insert_simple_hash(table, key, verbose=False):
    m = len(table)
    i = h(key, m)
    for attempt in range(m):
        index = (i + attempt) % m  # Sondage linéaire : on explore les cases suivantes
        if table[index] is None:
            table[index] = key
            if verbose:
                print(f"Inserted {key} at index {index}")
            return True
    return False

def resize_table_simple(old_table):
    new_size = len(old_table) * 2
    print(f"Redimensionnement de la table de taille {len(old_table)} à {new_size}")
    new_table = [None] * new_size
    for key in old_table:
        if key is not None:
            success = insert_simple_hash(new_table, key)
            if not success:
                raise Exception(f"Échec de réinsertion de la clé {key} après redimensionnement")
    return new_table

def extend_table_with_keys_simple(initial_table, new_keys, verbose=False,resize_before_insert=False):
    table = initial_table.copy()
    # Redimensionner la table avant l'insertion de 48 si nécessaire
    if resize_before_insert :  # 
        print("Redimensionnement avant insertion de 48")
        table = resize_table_simple(table)

    # Insérer les clés dans la table
    for key in new_keys:
        if key is not None:
            success = insert_simple_hash(table, key, verbose=verbose)
            if not success:
                raise Exception(f"Échec d’insertion de la clé {key} après redimensionnement.")
    return table

def print_table_as_tiles(table):
    tiles = [f"[{x}]" if x is not None else "[_]" for x in table]
    print('\t'.join(tiles))

# === Exemple 1 : Table de taille 13, sans redimensionnement ===
print("Table taille 13, sans redimensionnement :")

"""Remplacer"""
keys_13 = [55  ,  16  ,  41  ,  36  ,  43  ,  54  ,  60  ,  32  ,  44  ,  15  ]
initial_table_13 = [None] * 13


table13 = extend_table_with_keys_simple(initial_table_13, keys_13)
print_table_as_tiles(table13)

# === Exemple 2 : Table de taille 9 avec redimensionnement avant insertion de 48 ===
print("\nTable taille 9 avec redimensionnement avant insertion de 48 :")

"""Remplacer"""
initial_table_9 = [None ,1,	2	,21,	40	,38,	39,None,None]
Inser_key = [4]

# Redimensionner avant l'insertion de 48
table18 = extend_table_with_keys_simple(initial_table_9, Inser_key, verbose=True, resize_before_insert=True)
print_table_as_tiles(table18)
