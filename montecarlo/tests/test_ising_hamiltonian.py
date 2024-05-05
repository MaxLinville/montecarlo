"""
 test for ising hamiltonian class in the montecarlo package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import montecarlo
import numpy as np
from numpy.testing import assert_array_equal
import networkx as nx


def test_montecarlo_ising_hamiltonian():
    """
    Tests if ising hamiltonian class can be initialized and functions work properly.
    This uses the in-class ising_ensemble_avg_package tests without plotting or printing
    """
    N = 6
    Jval = 2.0
    G = nx.Graph()
    G.add_nodes_from([i for i in range(N)])
    G.add_edges_from([(i,(i+1)% G.number_of_nodes() ) for i in range(N)])
    for e in G.edges:
        G.edges[e]['weight'] = Jval
        
    def get_IsingHamiltonian(G, mus=None):
        if mus == None:
            mus = np.zeros(len(G.nodes()))

        if len(G.nodes()) != len(mus):
            error("DimensionMismatch")

        if len(G.nodes()) != len(mus):
            error(" Dimension Mismatch")
        J = [[] for i in G.nodes()]
        for e in G.edges:
            J[e[0]].append((e[1], G.edges[e]['weight']))
            J[e[1]].append((e[0], G.edges[e]['weight']))
        return montecarlo.IsingHamiltonian(J,mus)
    # Define a new configuration instance for a 6-site lattice
    conf = montecarlo.BitString(N)
    ham = get_IsingHamiltonian(G)

    # Compute the average values for Temperature = 1
    E, M, HC, MS = ham.compute_average_values(1)

    assert(np.isclose(E,  -11.95991923))
    assert(np.isclose(M,   -0.00000000))
    assert(np.isclose(HC,   0.31925472))
    assert(np.isclose(MS,   0.01202961))


