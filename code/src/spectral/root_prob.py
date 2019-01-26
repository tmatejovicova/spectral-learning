from spectral.grammar_file_gen import GrammarFileGenerator

class RootProbability:
    """
    A class to represent a root with latent states and its probabilities
    """
    ONE = '1'
    def __init__(self, nont, root_count_vec, num_roots, num_ls):
        self.nont = nont
        self.root_count_vec = root_count_vec
        self.num_roots = num_roots
        self.num_ls = num_ls
        self.__calc_prob()

    def __str__(self):
        string = str(self.nont) + "\n"
        string += "nont_vec " + str(self.root_count_vec) + "\n"
        string += "prob_dict " + str(self.prob_dict) + "\n"
        string += "pruned_prob " + str(self.pruned_prob) + "\n"
        string += "num_ls " + str(self.num_ls) + "\n"
        string += "num_roots " + str(self.num_roots) + "\n"
        return string

    def __repr__(self):
        return self.__str__()

    def __calc_prob(self):
        self.prob_dict = dict()
        self.pruned_prob = 0

        for h in range(self.root_count_vec.shape[0]):
            if self.root_count_vec[h] != 0:
                prob = self.root_count_vec[h] / self.num_roots
                self.prob_dict[h] = prob
                self.pruned_prob += prob

    def get_string(self):
        string = str(self.nont)
        string += GrammarFileGenerator.SPACE
        string += str(self.num_ls)
        string += GrammarFileGenerator.SPACE
        for ls, prob in self.prob_dict.items():
            string += str(ls + 1)
            string += GrammarFileGenerator.COLON
            string += str(prob)
            string += GrammarFileGenerator.SPACE
        return string

    def get_pruned_string(self):
        string = str(self.nont)
        string += GrammarFileGenerator.SPACE
        string += GrammarFileGenerator.ONE
        string += GrammarFileGenerator.SPACE
        string += GrammarFileGenerator.ONE
        string += GrammarFileGenerator.COLON
        string += str(self.pruned_prob)
        string += GrammarFileGenerator.SPACE
        return string
