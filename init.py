#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 14:05:18 2020

@author: abduhu

This codes are written to complete the application procedure to QOSF program.
Task 4:

    Find the lowest eigenvalue of the following matrix:
    
    '[1 0 0 0; 
     0 0 -1 0;
     0 -1 0 0; 
     0 0 0 1]'
    
    using VQE-like circuits, created by yourself from scratch.
"""

from vqe import (find_ground_state, H, pi)

# search varationally for the approximate ground state and its energy
ground_state = find_ground_state(n_points=10, n_shots=1000)

# Show results
print(f'\n Hamiltonian matrix: \n {H}')
print(f'\n min eigenvalue (ground energy) = {round(ground_state[0], 3)}')
print(f'\n \u03B8 parameter of the ground state =',
      f'{round(ground_state[1]/pi, 3)}*\u03C0')
