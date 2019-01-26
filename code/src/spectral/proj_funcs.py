from scipy import sparse
import numpy as np
from nltk.grammar import Nonterminal
from other.tree_methods import TreeMethods

class ProjectionFunctions:
    """
    Define the inside and outside tree projection functions
    """
    def __init__(self, ins_ftrs, outs_ftrs, nont_list, br_list, tr_list, max_nw, verbose):
        self.ins_ftrs =  ins_ftrs
        self.outs_ftrs = outs_ftrs
        self.nont_list = nont_list
        self.br_list = br_list
        self.tr_list = tr_list
        self.max_nw = max_nw
        self.verbose = verbose
        self.__construct_all_codes()

    def phi_func(self, node):
        """
        Inside tree projection function
        """
        to_join = list()
        if self.ins_ftrs[0]:
            first = self.__first_ins_ftr(node)
            to_join.append(first)
        if self.ins_ftrs[1]:
            second = self.__second_ins_ftr(node)
            to_join.append(second)
        if self.ins_ftrs[2]:
            third = self.__third_ins_ftr(node)
            to_join.append(third)
        if self.ins_ftrs[3]:
            fourth = self.__fourth_ins_ftr(node)
            to_join.append(fourth)
        joined = sparse.vstack(to_join)
        self.ins_len = joined.shape[0] # Known as d
        return joined

    def psi_func(self, node):
        """
        Outside tree projection function
        """
        to_join = list()
        if self.outs_ftrs[0]:
            first = self.__first_outs_ftr(node)
            to_join.append(first)
        if self.outs_ftrs[1]:
            second = self.__second_outs_ftr(node)
            to_join.append(second)
        if self.outs_ftrs[2]:
            third = self.__third_outs_ftr(node)
            to_join.append(third)
        if self.outs_ftrs[0]:
            fourth = self.__fourth_outs_ftr(node)
            to_join.append(fourth)
        joined = sparse.vstack(to_join)
        self.outs_len = joined.shape[0] # Known as d'
        return joined

    ### Inside tree features ###
    def __first_ins_ftr(self, node):
        """
        Root rule a -> bc or a -> x
        """
        rule = TreeMethods.get_rule(node.tree, node.pos)
        code = self.rules_codes[rule]
        vec = self.__get_sparse_vector(code, len(self.rules_codes))
        return vec

    def __second_ins_ftr(self, node):
        """
        Non-terminal b
        """
        ins_tree = node.tree[node.pos]
        if not TreeMethods.binary_rule(node.tree, node.pos):
            return self.__get_sparse_vector(None, len(self.nont_codes))
        left_child = Nonterminal(ins_tree[0].label())
        code = self.nont_codes[left_child]
        vec = self.__get_sparse_vector(code, len(self.nont_codes))
        return vec

    def __third_ins_ftr(self, node):
        """
        Non-terminal c
        """
        ins_tree = node.tree[node.pos]
        if not TreeMethods.binary_rule(node.tree, node.pos):
            return self.__get_sparse_vector(None, len(self.nont_codes))
        # print(node.tree)
        # print(node.pos)
        right_child = Nonterminal(ins_tree[1].label())
        code = self.nont_codes[right_child]
        vec = self.__get_sparse_vector(code, len(self.nont_codes))
        return vec

    def __fourth_ins_ftr(self, node):
        """
        Number of words dominated by the tree
        """
        num_words = len(node.tree[node.pos].flatten())
        code = num_words - 1
        vec = self.__get_sparse_vector(code, self.max_nw)
        return vec
    ### End of inside tree features ###

    ### Outside tree features ###
    def __first_outs_ftr(self, node):
        """
        Parent of the node (if any)
        """
        parent_pos = TreeMethods.get_parent_pos(node.tree, node.pos)
        if parent_pos == None:
            return self.__get_sparse_vector(None, len(self.nont_codes))
        parent = Nonterminal(node.tree[parent_pos].label())
        code = self.nont_codes[parent]
        vec = self.__get_sparse_vector(code, len(self.nont_codes))
        return vec

    def __second_outs_ftr(self, node):
        """
        Grandparent of the node (if any)
        """
        grandparent_pos = TreeMethods.get_grandparent_pos(node.tree, node.pos)
        if grandparent_pos == None:
            return self.__get_sparse_vector(None, len(self.nont_codes))
        grandparent = Nonterminal(node.tree[grandparent_pos].label())
        code = self.nont_codes[grandparent]
        vec = self.__get_sparse_vector(code, len(self.nont_codes))
        return vec

    def __third_outs_ftr(self, node):
        """
        Rule above the node
        """
        parent_pos = TreeMethods.get_parent_pos(node.tree, node.pos)
        if parent_pos == None:
            return self.__get_sparse_vector(None, len(self.rules_codes))
        rule = TreeMethods.get_rule(node.tree, parent_pos)
        code = self.rules_codes[rule]
        vec = self.__get_sparse_vector(code, len(self.rules_codes))
        return vec


    def __fourth_outs_ftr(self, node):
        """
        Rule two levels above the node
        """
        grandparent_pos = TreeMethods.get_grandparent_pos(node.tree, node.pos)
        if grandparent_pos == None:
            return self.__get_sparse_vector(None, len(self.rules_codes))
        rule = TreeMethods.get_rule(node.tree, grandparent_pos)
        code = self.rules_codes[rule]
        vec = self.__get_sparse_vector(code, len(self.rules_codes))
        return vec
    ### End of outside tree features ###

    def __construct_all_codes(self):
        """
        Construct dictionaries to be used for creation of vectors
        """
        self.nont_codes = self.__construct_codes(self.nont_list)
        self.br_codes = self.__construct_codes(self.br_list)
        self.rules_codes = self.__construct_codes_from_two_lists(self.tr_list, self.br_list)

    ### Static private methods ###
    @staticmethod
    def __construct_codes(key_list):
        key_dict = dict()
        for i in range(len(key_list)):
            key_dict[key_list[i]] = i
        return key_dict

    @staticmethod
    def __construct_codes_from_two_lists(key_list_first, key_list_second):
        key_dict = dict()
        i = 0
        for key in key_list_first:
            key_dict[key] = i
            i += 1
        for key in key_list_second:
            key_dict[key] = i
            i += 1
        return key_dict

    @staticmethod
    def __get_sparse_vector(code, length):
        data = np.array([])
        rows = np.array([])
        cols = np.array([])

        if code != None:
            data = np.array([1])
            rows = np.array([code])
            cols = np.array([0])

        return sparse.csr_matrix((data, (rows, cols)), shape = (length, 1), dtype = float)
