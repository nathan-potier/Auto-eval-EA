def verifier_suite_abr(suite):
    """
    Vérifie si une suite donnée peut représenter un chemin valide dans un ABR.
    Dans un ABR, si on va à gauche, le nœud suivant doit être < que le nœud actuel.
    Si on va à droite, le nœud suivant doit être > que le nœud actuel.

    Args:
        suite: Liste d'entiers représentant un chemin dans un ABR.

    Returns:
        True si la suite est valide dans un ABR, False sinon.
    """
    if len(suite) <= 1:
        return True

    for i in range(1, len(suite)):
        # Si on va à gauche (suite[i] < suite[i-1]), tous les éléments du sous-arbre
        # gauche doivent être < suite[i-1]
        if suite[i] < suite[i-1]:
            for j in range(i, len(suite)):
                if suite[j] >= suite[i-1]:
                    return False
        # Si on va à droite (suite[i] > suite[i-1]), tous les éléments du sous-arbre
        # droit doivent être > suite[i-1]
        elif suite[i] > suite[i-1]:
            for j in range(i, len(suite)):
                if suite[j] <= suite[i-1]:
                    return False

    return True


def analyser_suites(suites):
    """
    Analyser un tableau de chaînes représentant des suites dans un ABR.

    Args:
        donnees: Tableau de chaînes de caractères où chaque chaîne est une suite de nombres séparés par '→'.

    Returns:
        Liste de résultats d'analyse pour chaque suite.
    """

    # Vérifier chaque suite
    print("Résultats de l'analyse des suites dans un ABR:")
    print("-" * 50)
    for i, suite in enumerate(suites):
        valide = verifier_suite_abr(suite)
        print(f"Suite {i+1}: {' →→ '.join(map(str, suite))}")
        if valide:
            print(f"  ✓ VALIDE: Cette suite peut représenter un chemin dans un ABR")
        else:
            print(f"  ✗ NON VALIDE: Cette suite ne peut pas représenter un chemin dans un ABR")
        print("-" * 50)


# Exemple d'entrée sous forme de tableau de chaînes
donnees = [[806, 249, 528, 666, 555, 546, 549, 541]]

print(donnees)

# Appeler la fonction avec le tableau de chaînes
analyser_suites(donnees)
