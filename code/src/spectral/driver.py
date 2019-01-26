from spectral.spectral_learning import SpectralLearning
from spectral.final_params import FinalParameters
from spectral.grammar_file_gen import GrammarFileGenerator
from other.data_proc import DataProcessor
import time

class Driver:
    """
    Class to perform all steps to estimate a L-PCFG
    """
    def __init__(self, corpus, ins_ftrs, outs_ftrs, k, m, cutoff, verbose, folder_name):
        self.corpus = corpus
        self.ins_ftrs = ins_ftrs
        self.outs_ftrs = outs_ftrs
        self.k = k
        self.m = m
        self.cutoff = cutoff
        self.verbose = verbose
        self.folder_name = folder_name
        self.__run_algorithm()

    def __run_algorithm(self):
        # 1 Run the spectral algorithm
        if self.verbose:
            print("1. RUNNING SPECTRAL LEARNING")
            print("Number of train sentences: " + str(len(self.corpus)))
            print("Singular value: " + str(self.k) + '\n')
        start = time.time()
        spectral_learn = SpectralLearning(self.corpus, self.ins_ftrs, self.outs_ftrs, self.k, self.m, self.cutoff, self.verbose)

        # 2 Calculate final parameters
        if self.verbose:
            print("\n2. CALCULATING PARAMETERS")
        final_params = FinalParameters(self.m, spectral_learn.nodes_list, spectral_learn.nont_dict, spectral_learn.br_dict, spectral_learn.tr_dict, self.verbose)
        end = time.time()
        elapsed = end - start

        if self.verbose:
            print("Time elapsed (s): " + str(elapsed))
        DataProcessor.save_time(self.folder_name, elapsed)

        # 3 Generate grammar file
        if self.verbose:
            print("\n3. GENERATING GRAMMAR FILES")
            print(self.folder_name + "/grammar.txt")
            print(self.folder_name + "/grammar-pruned.txt")
            print(self.folder_name + "/vocab.txt\n")
        grammar_file_gen = GrammarFileGenerator(final_params.interminals, final_params.preterminals, final_params.bin_rules, final_params.term_rules, final_params.root_probs, spectral_learn.vocab, self.folder_name, self.verbose)
