from spectral.grammar_file_gen import GrammarFileGenerator

class TerminalRule:
    """
    A class to represent a terminal rule with latent states and its probabilities
    """
    def __init__(self, term_rule, tr_mat, lhs_vec, num_ls):
        self.tr = term_rule
        self.lhs = term_rule.lhs()
        self.rhs = term_rule.rhs()[0]
        self.tr_mat = tr_mat
        self.lhs_vec = lhs_vec
        self.num_ls = num_ls
        self.__calc_prob()

    def __str__(self):
        string = str(self.tr) + "\n"
        string += "lhs_vec " + str(self.lhs_vec) + "\n"
        string += "tr_mat \n" + str(self.tr_mat) + "\n"
        string += "prob_dict " + str(self.prob_dict) + "\n"
        string += "pruned_prob " + str(self.pruned_prob) + "\n"
        string += "num_ls " + str(self.num_ls) + "\n"
        return string

    def __repr__(self):
        return self.__str__()

    def __calc_prob(self):
        self.prob_dict = dict()
        self.pruned_prob = 0
        for h in range(self.tr_mat.shape[0]):
            if self.tr_mat[h] != 0:
                prob = self.tr_mat[h] / self.lhs_vec[h]
                self.prob_dict[h] = prob
                self.pruned_prob += prob

    def get_string(self):
        string = self.__get_rule_string()
        string += str(self.num_ls)
        string += GrammarFileGenerator.SPACE
        for ls, prob in self.prob_dict.items():
            string += str(ls + 1)
            string += GrammarFileGenerator.COLON
            string += str(prob)
            string += GrammarFileGenerator.SPACE
        return string

    def get_pruned_string(self):
        string = self.__get_rule_string()
        string += GrammarFileGenerator.ONE
        string += GrammarFileGenerator.SPACE
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
        string += str(self.rhs)
        string += GrammarFileGenerator.SPACE
        return string
