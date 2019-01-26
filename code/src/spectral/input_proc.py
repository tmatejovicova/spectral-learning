from spectral.node import Node
from other.tree_methods import TreeMethods
from nltk import Tree

class InputProcessor:
    """
    Processes the raw inputs to produce input in the required format:
        - nodes_list list of Node of all the training nodes
        - nont_dict dictionary of nltk.grammar.Nonterminal to corresp. set of Nodes
        - br_dict dictionary of binary rules nltk.grammar.Production to corresp. set of Nodes
        - br_dict dictionary of terminal rules nltk.grammar.Production to corresp. set of Nodes
        - nont_list list of nltk.grammar.Nonterminal of all possible nonterminals
        - br_list list of nltk.grammar.Production of all possible binary rules
        - tr_list list of nltk.grammar.Production of all possible terminal rules
        - max_nw maximum number of words in a sentence
    """
    def __init__(self, parsed_sents, cutoff, verbose):
        self.parsed_sents = parsed_sents
        self.cutoff = cutoff
        self.verbose = verbose
        self.__process()

    def __process(self):
        self.vocab = self.__get_vocab()
        self.__replace_terminals()
        self.nodes_list = list()
        self.nont_dict = dict()
        self.br_dict = dict()
        self.tr_dict = dict()
        self.max_nw = 0
        for tree_id in range(len(self.parsed_sents)):
            parsed_sent = self.parsed_sents[tree_id]
            TreeMethods.norm_parse(parsed_sent)
            self.__iter_nodes(parsed_sent, tree_id)

    def __iter_nodes(self, tree, tree_id):
        for pos in (x for x in tree.treepositions() if TreeMethods.nont_node(tree, x)):
            node = Node(tree, tree_id, pos)
            self.nodes_list.append(node)
            rule = TreeMethods.get_rule(node.tree, node.pos)
            nont = rule.lhs()
            self.__add_to_dict(self.nont_dict, nont, node)

            if TreeMethods.binary_rule(node.tree, node.pos):
                self.__add_to_dict(self.br_dict, rule, node)
            else:
                self.__add_to_dict(self.tr_dict, rule, node)
            self.__check_max_sent_length(tree)
        self.__construct_lists()

    def __check_max_sent_length(self, parsed_sent):
        sent = parsed_sent.flatten()
        if len(sent) > self.max_nw:
            self.max_nw = len(sent)

    def __construct_lists(self):
        self.nont_list = list(self.nont_dict.keys())
        self.br_list = list(self.br_dict.keys())
        self.tr_list = list(self.tr_dict.keys())

    def __get_vocab(self):
        vocab = dict()
        for sent in self.parsed_sents:
            for leaf in sent.treepositions(order = 'leaves'):
                terminal = sent[leaf]
                if terminal not in vocab:
                    vocab[terminal] = 0
                vocab[terminal] += 1
        return vocab

    def __replace_terminals(self):
        num_cut = 0
        for sent in self.parsed_sents:
            for leaf in sent.treepositions(order = 'leaves'):
                term = sent[leaf]
                if self.vocab[term] < self.cutoff:
                    num_cut += 1
                    parent_pos = TreeMethods.get_parent_pos(sent, leaf)
                    pos_tag = TreeMethods.get_nonterminal(sent, parent_pos)
                    sent[leaf] = str(pos_tag)
        if self.verbose:
            print('Words replaced by POS tag: ' + str(num_cut))

    @staticmethod
    def __add_to_dict(dict, key, val):
        if key not in dict:
            dict[key] = set()
        dict[key].add(val)

    ### Public static methods ###
    @staticmethod
    def get_dicts(nodes_list):
        nont_dict = dict()
        br_dict = dict()
        tr_dict = dict()
        for node in nodes_list:
            rule = TreeMethods.get_rule(node.tree, node.pos)
            nont = rule.lhs()
            InputProcessor.__add_to_dict(nont_dict, nont, node)
            if TreeMethods.binary_rule(node.tree, node.pos):
                InputProcessor.__add_to_dict(br_dict, rule, node)
            else:
                InputProcessor.__add_to_dict(tr_dict, rule, node)
        return nont_dict, br_dict, tr_dict
