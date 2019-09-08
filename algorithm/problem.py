import numpy as np
from algorithm.problem_setup import load_parameter


def load_problem(problem_path, dim):
    save_path = "../datasets_ncs/format/function%d.rw" % problem_path
    p = load_parameter(save_path)
    if p.o is not None:
        p.o = p.o[0:dim]

    if p.a is not None:
        p.a = p.a[0:dim][:, 0:dim]

    if p.b is not None:
        p.b = p.b[0:dim][:, 0:dim]

    if p.alpha is not None:
        p.alpha = p.alpha[0:dim]

    p.lu = np.asarray([p.lu] * dim)  # D X 2
    return p