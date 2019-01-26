from nltk import Tree
class TreeMethods:
    """
    Various methods to manipulate objects of type nltk.Tree
    """
    def __init__(self):
        return

    @staticmethod
    def nont_node(tree, pos):
        """
        Return true if this position of the tree corresponds to a nonterminal node
        :rtype boolean
        """
        return isinstance(tree[pos], Tree)

    @staticmethod
    def binary_rule(tree, pos):
        """
        """
        child_pos_list = list(pos)
        child_pos_list.append(0)
        child_pos = tuple(child_pos_list)
        return TreeMethods.nont_node(tree, child_pos)

    @staticmethod
    def get_rule(tree, pos):
        return tree[pos].productions()[0]

    @staticmethod
    def get_nonterminal(tree, pos):
        return TreeMethods.get_rule(tree, pos).lhs()

    @staticmethod
    def get_children_pos(pos):
        left_child_pos_list = list(pos)
        left_child_pos_list.append(0)
        left_child_pos = tuple(left_child_pos_list)
        right_child_pos_list = list(pos)
        right_child_pos_list.append(1)
        right_child_pos = tuple(right_child_pos_list)
        return left_child_pos, right_child_pos

    @staticmethod
    def get_parent_pos(tree, pos):
        if len(pos) < 1:
            return None
        list_pos = list(pos)
        del list_pos[-1]
        return tuple(list_pos)

    @staticmethod
    def get_grandparent_pos(tree, pos):
        if len(pos) < 2:
            return None
        list_pos = list(pos)
        del list_pos[-1]
        del list_pos[-1]
        return tuple(list_pos)

    @staticmethod
    def norm_parse(parsed_sent):
        parsed_sent.chomsky_normal_form()
        parsed_sent.collapse_unary(collapsePOS = True, collapseRoot = True)

    @staticmethod
    def get_tree_string(tree):
        tree_string = str(tree)
        return TreeMethods.get_tree_string_spaces(tree_string)

    @staticmethod
    def get_tree_string_spaces(tree_string):
        strings =  tree_string.split()
        return ' '.join(strings)
