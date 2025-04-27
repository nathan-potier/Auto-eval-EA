swap_counter = 1


def tri_rapide_en_place(T, debut=0, fin=None):
    if fin is None:
        fin = len(T)
    if fin - debut < 2:
        return
    indice_pivot = partition_en_place(T, debut, fin)
    tri_rapide_en_place(T, debut, indice_pivot)
    tri_rapide_en_place(T, indice_pivot + 1, fin)


def partition_en_place(T, debut, fin):
    global swap_counter
    pivot = T[debut]
    gauche, droite = debut + 1, fin - 1

    while gauche <= droite:
        if T[gauche] < pivot:
            gauche += 1
        elif T[droite] > pivot:
            droite -= 1
        else:
            print(
                f"Swap #{swap_counter}: indices {gauche} <-> {droite} | valeurs {T[gauche]} <-> {T[droite]}"
            )
            T[gauche], T[droite] = T[droite], T[gauche]
            swap_counter += 1

    print(
        f"Swap #{swap_counter}: indices {debut} <-> {droite} | valeurs {pivot} <-> {T[droite]}"
    )
    T[debut], T[droite] = T[droite], pivot
    swap_counter += 1
    return droite


if __name__ == "__main__":
    tableau = [77, 61, 85, 29, 36, 94, 42, 18, 53]
    print("État initial:", tableau)
    tri_rapide_en_place(tableau)
    print("État final trié:", tableau)
