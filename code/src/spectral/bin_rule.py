from collections import namedtuple
from spectral.grammar_file_gen import GrammarFileGenerator

class BinaryRule:
    """
    A class to represent a binary rule with latent states and its probabilities
    """
    ProbKey = namedtuple('ProbKey', ['h1', 'h2', 'h3'])
    def __init__(self, bin_rule, br_mat, lhs_vec, num_ls):
        self.br = bin_rule
        self.lhs = bin_rule.lhs()
        self.left_child = bin_rule.rhs()[0]
        self.right_child = bin_rule.rhs()[1]
        self.br_mat = br_mat
        self.m = br_mat.shape[0]
        self.lhs_vec = lhs_vec
        self.num_ls = num_ls
        self.__calc_prob()

    def __str__(self):
        string = str(self.br) + "\n"
        string += "lhs_vec " + str(self.lhs_vec) + "\n"
        string += "br_mat \n" + str(self.br_mat) + "\n"
        string += "prob_dict " + str(self.prob_dict) + "\n"
        string += "pruned_prob " + str(self.pruned_prob) + "\n"
        string += "num_ls " + str(self.num_ls) + "\n"
        return string

    def __repr__(self):
        return self.__str__()

    def __calc_prob(self):
        self.prob_dict = dict()
        self.pruned_prob = 0
        for h1 in range(self.m):
            for h2 in range(self.m):
                for h3 in range(self.m):
                    if self.br_mat[h1, h2, h3] != 0:
                        prob = self.br_mat[h1, h2, h3] / self.lhs_vec[h1]
                        prob_key = self.ProbKey(h1, h2, h3)
                        self.prob_dict[prob_key] = prob
                        self.pruned_prob += prob

    def get_string(self):
        string = self.__get_rule_string()
        for num_ls in self.num_ls:
            string += str(num_ls)
            string += GrammarFileGenerator.SPACE

        for prob_key, prob in self.prob_dict.items():
            string += self.__get_prob_key_string(prob_key)
            string += str(prob)
            string += GrammarFileGenerator.SPACE

        return string

    def get_pruned_string(self):
        string = self.__get_rule_string()
        for num_ls in self.num_ls:
            string += GrammarFileGenerator.ONE
            string += GrammarFileGenerator.SPACE

        string += GrammarFileGenerator.ONE
        string += GrammarFileGenerator.COMMA
        string += GrammarFileGenerator.ONE
        string += GrammarFileGenerator.COMMA
        string += GrammarFileGenerator.ONE
        string += GrammarFileGenerator.COLON

        string += str(self.pruned_prob)
        string += GrammarFileGenerator.SPACE

        return string

    def __get_rule_string(self):
        string = str(self.lhs)
        string += GrammarFileGenerator.SPACE
        string += GrammarFileGenerator.ARROW
        string += GrammarFileGenerator.SPACE
        string += str(self.left_child)
        string += GrammarFileGenerator.SPACE
        string += str(self.right_child)
        string += GrammarFileGenerator.SPACE
        return string

    def __get_prob_key_string(self, prob_key):
        string = str(prob_key.h1 + 1)
        string += GrammarFileGenerator.COMMA
        string += str(prob_key.h2 + 1)
        string += GrammarFileGenerator.COMMA
        string += str(prob_key.h3 + 1)
        string += GrammarFileGenerator.COLON
        return string
