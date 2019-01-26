from spectral.input_proc import InputProcessor
from other.tree_methods import TreeMethods
from spectral.bin_rule import BinaryRule
from spectral.term_rule import TerminalRule
from spectral.root_prob import RootProbability
from collections import namedtuple
from spectral.spectral_learning import SpectralLearning
import numpy as np

from other import obj_methods
class FinalParameters:
    """
    Use the anotated corpus to calculate relative frequencies of rules and roots
    """
    NodeKey = namedtuple('NodeKey', ['tree_id', 'pos'])
    ROOT_POS = ()
    def __init__(self, m, nodes_list, nont_dict, br_dict, tr_dict, verbose):
        self.m = m
        self.nodes_list = nodes_list
        self.nont_dict = nont_dict
        self.br_dict = br_dict
        self.tr_dict = tr_dict
        self.verbose = verbose
        self.__get_final_params()

    def __get_final_params(self):
        self.nodes_dict = self.__get_nodes_dict()
        self.lhs_dict = self.__get_lhs_dict()
        self.bin_rules = self.__get_bin_rules()
        self.term_rules = self.__get_term_rules()
        self.root_probs = self.__get_root_probs()
        self.interminals, self.preterminals = self.__get_interminals_preterminals()

    def __get_bin_rules(self):
        bin_rules = list()
        for br, nodes_set in self.br_dict.items():
            br_mat = np.zeros((self.m, self.m, self.m))
            for node in nodes_set:
                h1 = node.h
                left_child, right_child = self.__get_children(node)
                h2 = left_child.h
                h3 = right_child.h
                br_mat[h1, h2, h3] += 1
            bin_rule = BinaryRule(br, br_mat, self.lhs_dict[br.lhs()], [node.m, left_child.m, right_child.m])
            bin_rules.append(bin_rule)
        if self.verbose:
            print('Number of binary rules: ' + str(len(bin_rules)))
        return bin_rules

    def __get_term_rules(self):
        term_rules = list()
        for tr, nodes_set in self.tr_dict.items():
            tr_mat = np.zeros((self.m))
            for node in nodes_set:
                tr_mat[node.h] += 1
            term_rule = TerminalRule(tr, tr_mat, self.lhs_dict[tr.lhs()], node.m)
            # if self.verbose:
            #     print(term_rule)
            term_rules.append(term_rule)
        if self.verbose:
            print('Number of terminal rules: ' + str(len(term_rules)))
        return term_rules

    def __get_root_probs(self):
        root_probs = list()
        num_roots = 0
        roots_count_dict = dict()
        i = 1
        for nont, nodes_set in self.nont_dict.items():
            for node in nodes_set:
                if node.pos == self.ROOT_POS:
                    i += 1
                    num_roots += 1
                    if nont not in roots_count_dict:
                        roots_count_dict[nont] = np.zeros((self.m))
                    roots_count_dict[nont][node.h] += 1
        for nont, nodes_set in self.nont_dict.items():
            node = next(iter(nodes_set))
            if nont in roots_count_dict:
                root_prob = RootProbability(nont, roots_count_dict[nont], num_roots, node.m)
                root_probs.append(root_prob)
        if self.verbose:
            print('Number of possible roots: ' + str(len(root_probs)))
        return root_probs

    def __get_interminals_preterminals(self):
        interminals = list()
        preterminals = list()

        for nont, nodes_set in self.nont_dict.items():
            node = next(iter(nodes_set))
            if TreeMethods.binary_rule(node.tree, node.pos):
                interminals.append(nont)
            else:
                preterminals.append(nont)
        return interminals, preterminals

    def __get_nodes_dict(self):
        nodes_dict = dict()
        for node in self.nodes_list:
            node_key = self.NodeKey(node.tree_id, node.pos)
            nodes_dict[node_key] = node
        return nodes_dict

    def __get_lhs_dict(self):
        lhs_dict = dict()
        for nont, nodes_set in self.nont_dict.items():
            count = np.zeros((self.m,))
            for node in nodes_set:
                count[node.h] += 1
            lhs_dict[nont] = count
        return lhs_dict

    def __get_children(self, node):
        tree_id = node.tree_id
        left_child_pos, right_child_pos = TreeMethods.get_children_pos(node.pos)
        left_child_node_key = self.NodeKey(tree_id, left_child_pos)
        left_child = self.nodes_dict[left_child_node_key]
        right_child_node_key = self.NodeKey(tree_id, right_child_pos)
        right_child = self.nodes_dict[right_child_node_key]
        return left_child, right_child
