from other.obj_methods import ObjectMethods
class GrammarFileGenerator:
    """
    A class to generate files for grammar, pruned grammar and vocabulary
    """    
    INTERMINALS = 'interminals'
    PRETERMINALS = 'preterminals'
    ROOT = 'root'
    TERM_RULE = 'term'
    BIN_RULE = 'binary'
    COLON = ':'
    COMMA = ','
    SPACE = ' '
    ARROW = '->'
    SLASH = '/'
    NEWLINE = '\n'
    ONE = '1'

    def __init__(self, interminals, preterminals, bin_rules, term_rules, root_probs, vocab, folder_name, verbose):
        self.interminals = interminals
        self.preterminals = preterminals
        # self.interminals = ObjectMethods.load_obj('interminals', 'nonterminals')
        # self.preterminals = ObjectMethods.load_obj('preterminals', 'nonterminals')

        self.bin_rules = bin_rules
        self.term_rules = term_rules
        self.root_probs = root_probs
        self.vocab = vocab
        self.folder_name = folder_name
        self.verbose = verbose
        self.__generate_grammar(False, "grammar.txt")
        self.__generate_grammar(True, "grammar-pruned.txt")
        self.__generate_vocab()

    def __generate_grammar(self, pruned, file_name):
        file_path = self.folder_name + self.SLASH + file_name
        with open(file_path, 'w') as file:
            # interminals list
            file.write(self.INTERMINALS)
            file.write(self.SPACE)
            for interminal in self.interminals:
                file.write(str(interminal))
                file.write(self.SPACE)
            file.write(self.NEWLINE)

            # preterminals list
            file.write(self.PRETERMINALS)
            file.write(self.SPACE)
            for preterminal in self.preterminals:
                file.write(str(preterminal))
                file.write(self.SPACE)
            file.write(self.NEWLINE)

            # roots
            for root_prob in self.root_probs:
                file.write(self.ROOT)
                file.write(self.SPACE)
                if pruned:
                    file.write(root_prob.get_pruned_string())
                else:
                    file.write(root_prob.get_string())
                file.write(self.NEWLINE)

            # term rules
            for term_rule in self.term_rules:
                file.write(self.TERM_RULE)
                file.write(self.SPACE)
                if pruned:
                    file.write(term_rule.get_pruned_string())
                else:
                    file.write(term_rule.get_string())
                file.write(self.NEWLINE)

            # binary rules
            for bin_rule in self.bin_rules:
                file.write(self.BIN_RULE)
                file.write(self.SPACE)
                if pruned:
                    file.write(bin_rule.get_pruned_string())
                else:
                    file.write(bin_rule.get_string())
                file.write(self.NEWLINE)

    def __generate_vocab(self):
        file_path = self.folder_name + self.SLASH + "vocab.txt"
        with open(file_path, 'w') as file:
            for word, num in self.vocab.items():
                file.write(word)
                file.write(self.SPACE)
                file.write(str(num))
                file.write(self.NEWLINE)
