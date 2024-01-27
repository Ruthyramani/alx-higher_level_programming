#!/usr/bin/python3
"""
Defines a matrix multiplication function using numpy.
"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """ return the multiplication of two matrices.
    Args:
        m_a (list of lists of ints/floats): the first matrix.
        m_b (list of lists of ints/floats): the seconf matrix.
    """

    return (np.matmul(m_a, m_b))
