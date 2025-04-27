import os
import webbrowser
from urllib.parse import quote


class BinaryTreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        """Insère une valeur dans l'arbre binaire de manière récursive."""
        if self.value is None:
            self.value = value
        elif value < self.value:
            if self.left is None:
                self.left = BinaryTreeNode()
            self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinaryTreeNode()
            self.right.insert(value)

    def to_dot(self, node_id=0, result=None):
        """Convertit l'arbre en format DOT pour la visualisation."""
        if result is None:
            result = []
        
        current_id = node_id
        if self.value is not None:
            result.append(f'  node{current_id} [label="{self.value}"];')
        else:
            result.append(f'  node{current_id} [label=""];')

        next_id = current_id + 1

        # Si il y a un sous-arbre gauche, ajouter la relation
        if self.left is not None:
            result.append(f"  node{current_id} -> node{next_id};")
            next_id = self.left.to_dot(next_id, result)
        else:
            # Si il n'y a pas de valeur (nœud vide), on le marque aussi
            result.append(f"  node{current_id} -> node{next_id} [style=dotted];")
            next_id += 1

        # Si il y a un sous-arbre droit, ajouter la relation
        if self.right is not None:
            result.append(f"  node{current_id} -> node{next_id};")
            next_id = self.right.to_dot(next_id, result)
        else:
            # Si il n'y a pas de valeur (nœud vide), on le marque aussi
            result.append(f"  node{current_id} -> node{next_id} [style=dotted];")
            next_id += 1

        return next_id


def generate_dot_code(root):
    """Génère le code DOT à partir de l'arbre binaire."""
    lines = ["digraph BinaryTree {"]
    root.to_dot(0, lines)
    lines.append("}")
    return "\n".join(lines)


def open_graphviz_online(dot_code):
    """Ouvre GraphvizOnline dans le navigateur avec l'arbre."""
    encoded_dot = quote(dot_code)
    url = f"https://dreampuf.github.io/GraphvizOnline/?engine=dot#{encoded_dot}"
    webbrowser.open(url)
    print(f"Page GraphvizOnline ouverte avec le code .dot.")


def main():
    # Liste des valeurs pour construire l'arbre binaire
    values = [608, 849, 418, 321, 517, 697, 802, 212, 535, 924, 269, 357, 754, 152]
    
    # Créer un arbre binaire
    tree = BinaryTreeNode()
    for value in values:
        tree.insert(value)

    # Générer le code DOT
    dot_code = generate_dot_code(tree)

    # Ouvrir la page Web avec le code .dot
    open_graphviz_online(dot_code)


if __name__ == "__main__":
    main()
