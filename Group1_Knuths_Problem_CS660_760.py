# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 18:54:03 2021

@author: Group 1 CS 660/760
"""

import Queue, math

q = queue.Queue

def evaluate(current_state, n, q):
    if current_state > n:
        q.put('square_root')
        actions('square_root', current_state)
    elif current_state.type == float:
        q.put('floor')
        actions('floor')
    elif current_state < n:
        q.put('factorial')
        actions('factorial')
    

def actions(action, current_state):
    if action == 'square_root':
        current_state = math.sqrt(current_state)
    elif action == 'floor':
        current_state = int(current_state)
    else:
        current_state = math.factorial(current_state)
    
        