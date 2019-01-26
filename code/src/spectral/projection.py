from scipy import sparse
import numpy as np

class Projection:
    """
    Project inside and outside tree vectors down to a lower dimension
    """
    def __init__(self, nodes_set, u, v, proj_funcs, verbose):
        self.nodes_set = nodes_set
        self.u = u
        self.v = v
        self.proj_funcs = proj_funcs
        self.verbose = verbose
        self.__project()

    def __project(self):
        to_concat = list()
        for node in self.nodes_set:
            y = self.u.dot(self.proj_funcs.phi_func(node))
            z = self.v.dot(self.proj_funcs.psi_func(node))
            x = sparse.vstack([y, z]).toarray().transpose()
            to_concat.append(x)
            node.set_x(x)
        self.X = np.concatenate(to_concat, axis = 0)
