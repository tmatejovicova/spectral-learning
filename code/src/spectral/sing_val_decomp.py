from scipy import sparse

class SingularValueDecomp:
    """
    Calculate omega from the given nodes and obtain U, V
    """
    def __init__(self, nodes_set, k, proj_funcs, verbose):
        self.nodes_set = nodes_set
        self.k = k
        self.proj_funcs = proj_funcs
        self.verbose = verbose
        self.sing_val_decomp()

    def sing_val_decomp(self):
        omega = sparse.csr_matrix((self.proj_funcs.ins_len, self.proj_funcs.outs_len))
        for node in self.nodes_set:
            ins_vec = self.proj_funcs.phi_func(node)
            outs_vec = self.proj_funcs.psi_func(node)
            omega += ins_vec.dot(outs_vec.transpose())

        uh, s, vh = sparse.linalg.svds(omega)
        uh = uh.transpose()
        self.u = sparse.csr_matrix(uh[0:self.k,]) # k times d
        self.v = sparse.csr_matrix(vh[0:self.k,]) # k times d'
