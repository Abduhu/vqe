#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 10:19:26 2020

@author: Abdellah TOUNSI

This module includes tools to find the decomposition of the hamiltonian's
matrix in terms of the given Pauli matrices and coefficients.
"""

import numpy as np
from copy import deepcopy

# Hamiltonian matrix
H = np.matrix([[1, 0, 0, 0],
               [0, 0, -1, 0],
               [0, -1, 0, 0], 
               [0, 0, 0, 1]])

# Pauli matrices
I = np.matrix([[1, 0],
               [0, 1]])
X = np.matrix([[0, 1],
               [1, 0]])
Y = (1j) * np.matrix([[0, -1],
               [1, 0]])
Z = np.matrix([[1, 0],
               [0, -1]])

# Decomposition matrices for H
II = np.kron(I, I)
XX = np.kron(X, X)
YY = np.kron(Y, Y)
ZZ = np.kron(Z, Z)

COEFFICIENTS = [-1, -0.5, 0, 0.5, 1]
MATRICES = [II, XX, YY, ZZ]

def compose(coefs):
    """
    calculates the result matrix = aII + bXX + cYY + dZZ
    such that [a, b, c, d]=coefs
    Inputs:
        coefs: list: decomposition coefficients.
    """
    return coefs[0] * II + coefs[1] * XX + coefs[2] * YY + coefs[3] * ZZ

def iterate(list, values):
    for ii, element in enumerate(list):
        if element == values[-1]:
            list[ii] = values[0]
        else:
            list[ii] = values[values.index(element)+1]
            break
    return list

def decompose(matrix):
    """
    decomposes 4x4 hamiltonian matrix to II, XX, YY, ZZ with coefficients 
    [-1, -1/2, 0, 1/2, 1]
    Inputs:
        matrix: numpy.matrix: Hamiltonian matrix representation.
    """
    INIT_DECOMPOSITION = [-1, -1, -1, -1]
    FINAL_DECOMPOSITION = [1, 1, 1, 1]
    
    new_decomposition = deepcopy(INIT_DECOMPOSITION)
    decomposition = new_decomposition
    found = False
    while new_decomposition != FINAL_DECOMPOSITION:

        if not (compose(new_decomposition)-matrix).any():
            decomposition = new_decomposition
            found = True
            break
            
        new_decomposition = iterate(new_decomposition, COEFFICIENTS)
    
    if not (compose(new_decomposition)-matrix).any():
            decomposition = new_decomposition
            found = True
    
    if found:
        return decomposition
    else:
        raise BaseException('Bad decomposition choice!')

    