from cytonic import Cytonic
import numpy

def matrix_multiply(a,b):
    return numpy.matmul(a,b)

cyto = Cytonic(__name__)

cyto.add_method("Matrix multiplication", {
    "inputs": {"Matrix A":{"kind":"matrix"}, "Matrix B":{"kind":"matrix"}},
    "function": matrix_multiply,
    "outputs": {"Result":{"kind":"matrix"}}
})

cyto.run()

