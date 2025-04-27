import os
import urllib.parse
import webbrowser


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def to_dot(self):
        """Génère le code .dot pour visualiser l'arbre avec Graphviz"""
        lines = ["digraph BST {"]
        lines.append("  node [shape=circle, fixedsize=true, width=0.6];")

        if self.root:
            self._to_dot_recursive(self.root, lines)

        lines.append("}")
        return "\n".join(lines)

    def _to_dot_recursive(self, node, lines, parent_id=None, node_id=None):
        if node is None:
            return

        if node_id is None:
            node_id = f"node{node.key}"

        lines.append(f'  {node_id} [label="{node.key}"];')

        if parent_id:
            lines.append(f"  {parent_id} -> {node_id};")

        if node.left or node.right:
            left_id = f"node{node.key}L"
            right_id = f"node{node.key}R"
            
            # Ajouter les nœuds vides pour les enfants manquants
            if node.left:
                left_id = f"node{node.left.key}"
                self._to_dot_recursive(node.left, lines, node_id, left_id)
            else:
                lines.append(f'  {left_id} [label=""];')  # Nœud vide à gauche
                lines.append(f"  {node_id} -> {left_id};")  # Lien avec le nœud parent
            
            if node.right:
                right_id = f"node{node.right.key}"
                self._to_dot_recursive(node.right, lines, node_id, right_id)
            else:
                lines.append(f'  {right_id} [label=""];')  # Nœud vide à droite
                lines.append(f"  {node_id} -> {right_id};")  # Lien avec le nœud parent


def main():
    keys = [652, 459, 621, 543, 785, 938, 731, 879, 206, 120, 496, 340, 253, 385]
    bst = BinarySearchTree()
    
    for key in keys:
        bst.insert(key)

    dot_code = bst.to_dot()

    # URL encode le code .dot
    encoded_dot = urllib.parse.quote(dot_code)

    # Créer l'URL pour le site GraphvizOnline
    graphviz_url = f"https://dreampuf.github.io/GraphvizOnline/?engine=dot#{encoded_dot}"

    # Ouvrir automatiquement le lien dans le navigateur
    print(f"Ouverture automatique de l'arbre sur GraphvizOnline...")
    webbrowser.open(graphviz_url)


if __name__ == "__main__":
    main()
