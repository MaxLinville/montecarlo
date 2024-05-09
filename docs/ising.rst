Ising Hamiltonian Class
=======================

The `Ising Hamiltonian` class models the Ising model for a set of spins, providing methods to compute energy, magnetization, heat capacity, and magnetic susceptibility.

.. class:: IsingHamiltonian(J, mu)

   Initializes a new instance of the IsingHamiltonian.

   :param J: A nested list where each element contains tuples of connected nodes and their interaction strengths.
   :param mu: A NumPy array of magnetic moments corresponding to each node.

   .. attribute:: J

      Interaction matrix defining the couplings between different spins in the system.

   .. attribute:: mu

      Magnetic moments associated with each spin.

   .. attribute:: nodes

      List of nodes in the Hamiltonian system.

   .. attribute:: js

      List of coupling strengths corresponding to the nodes.

   .. attribute:: N

      Total number of spins in the system.

Methods
-------

.. method:: IsingHamiltonian.__init__(self, J=[[()]], mu=np.zeros(1))

   Constructor method for creating an Ising Hamiltonian with specified interactions and magnetic moments.

.. method:: IsingHamiltonian.energy(self, bs)

   Computes the energy of a given spin configuration.

   :param bs: A `BitString` object of the spin configuration.
   :return: The energy of the configuration.

.. method:: IsingHamiltonian.compute_average_values(self, T)

   Computes average values for energy, magnetization, heat capacity, and magnetic susceptibility at a given temperature.

   :param T: Temperature to compute average values.
   :return: A tuple containing the average energy, magnetization, heat capacity, and magnetic susceptibility.

.. method:: IsingHamiltonian.get_lowest_energy_config(self, verbose=0)

   Finds the configuration of spins that has the lowest energy.

   :param verbose: Lists the specific configuration where the lowest energy was found.
   :return: The lowest energy and bitstring configuration if set to verbose is 1.

