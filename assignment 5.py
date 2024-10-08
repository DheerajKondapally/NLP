# -*- coding: utf-8 -*-
"""Untitled22.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17XgR_dx2Vv_G75nbgh0H7T_2iq1-VfJn
"""

import numpy as np
states = ['Sunny', 'Rainy']
observations = ['Dry', 'Damp', 'Wet']
obs_sequence = ['Dry', 'Damp', 'Wet', 'Dry']

A = np.array([[0.6, 0.4],
              [0.4, 0.6]])

B = np.array([[0.6, 0.3, 0.2],
              [0.1, 0.4, 0.5]])

pi = np.array([0.8, 0.2])

obs_map = {obs: i for i, obs in enumerate(observations)}

def viterbi(obs_seq, A, B, pi):
    n_states = A.shape[0]
    T = len(obs_seq)
    delta = np.zeros((T, n_states))
    backpointer = np.zeros((T, n_states), dtype=int)

    for s in range(n_states):
        delta[0, s] = pi[s] * B[s, obs_map[obs_seq[0]]]

    for t in range(1, T):
        for s in range(n_states):
            max_prob, max_state = max(
                (delta[t-1, s_prime] * A[s_prime, s] * B[s, obs_map[obs_seq[t]]], s_prime)
                for s_prime in range(n_states)
            )
            delta[t, s] = max_prob
            backpointer[t, s] = max_state

    max_prob = max(delta[T-1, s] for s in range(n_states))
    best_path_pointer = np.argmax(delta[T-1, :])

    best_path = [best_path_pointer]
    for t in range(T-1, 0, -1):
        best_path.insert(0, backpointer[t, best_path[0]])

    best_state_sequence = [states[i] for i in best_path]

    return best_state_sequence, max_prob

best_sequence, probability = viterbi(obs_sequence, A, B, pi)
print("Best state sequence:", best_sequence)
print("Probability of the sequence:", probability)