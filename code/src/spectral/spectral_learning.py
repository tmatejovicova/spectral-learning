from spectral.node import Node
from spectral.input_proc import InputProcessor
from spectral.proj_funcs import ProjectionFunctions
from spectral.sing_val_decomp import SingularValueDecomp
from spectral.projection import Projection
from spectral.clustering import Clustering
from other import obj_methods
from other import tree_methods

class SpectralLearning:
    """
    Perform all the spectral algorithm steps with the given parameters
    """
    # OBJ_FOLDER = 'obj'
    def __init__(self, corpus, ins_ftrs, outs_ftrs, k, m, cutoff, verbose):
        self.corpus = corpus
        self.ins_ftrs = ins_ftrs
        self.outs_ftrs = outs_ftrs
        self.k = k
        self.m = m
        self.cutoff = cutoff
        self.verbose = verbose
        self.__annotate()


    def __annotate(self):
        if self.verbose:
            print("Processing input")
        input_proc = InputProcessor(self.corpus, self.cutoff, self.verbose)
        self.nodes_list = input_proc.nodes_list
        self.nont_dict = input_proc.nont_dict
        self.br_dict = input_proc.br_dict
        self.tr_dict = input_proc.tr_dict
        self.vocab = input_proc.vocab

        proj_funcs = ProjectionFunctions(self.ins_ftrs, self.outs_ftrs, input_proc.nont_list, input_proc.br_list, input_proc.tr_list, input_proc.max_nw, self.verbose)

        # Initiate proj_funcs
        node = input_proc.nodes_list[4]
        ins_vec = proj_funcs.phi_func(node)
        outs_vec = proj_funcs.psi_func(node)

        if self.verbose:
            print("Inside tree vector length: " + str(ins_vec.shape[0]))
            print("Outside tree vector length: " + str(outs_vec.shape[0]))
            print("Number of nonterminals: " + str(len(input_proc.nont_dict.keys())) + '\n')
            print("Calculating omega matrices, Projecting x, y, z: ")

        i = 0
        for nont, nodes_set in input_proc.nont_dict.items():
            if self.verbose:
                print(str(i) + ". " + str(nont) + " (" + str(len(nodes_set)) + " node/s)")
            i += 1
            sing_val_decomp = SingularValueDecomp(nodes_set, self.k, proj_funcs, self.verbose)
            projection = Projection(nodes_set, sing_val_decomp.u, sing_val_decomp.v, proj_funcs, self.verbose)
            clustering = Clustering(projection.X, nodes_set, self.m, self.verbose)
