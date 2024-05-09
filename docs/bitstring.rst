BitString Class
===============

.. class:: BitString(N)

   Simple class to implement a configuration of spins as a string array of bits.

   :param N: Number of bits in the bit string.

   The `BitString` class represents a configuration of spins (bits) that can be modified or read in different ways.

   .. attribute:: N

      The number of bits in the bit string.

   .. attribute:: config

      An array of integers representing the bit string. Each integer is either 0 or 1.

Methods
------------

.. method:: BitString.__repr__(self)

   Returns the string representation of the bit string.

.. method:: BitString.__eq__(self, other)

   Compares this bit string to another for equality.

   :param other: Another instance of `BitString` to compare against.

   :return: True if both instances represent the same bit string, otherwise False.

.. method:: BitString.__len__(self)

   Returns the length of the bit string.

.. method:: BitString.on(self)

   Counts the number of '1's (on bits) in the bit string.

.. method:: BitString.off(self)

   Counts the number of '0's (off bits) in the bit string.

.. method:: BitString.flip_site(self, i)

   Flips the bit at the specified index.

   :param i: Index of the bit to flip.

.. method:: BitString.int(self)

   Returns the integer representation of the bit string.

.. method:: BitString.set_config(self, s)

   Sets the configuration of the bit string from a list of integers.

   :param s: A list of integers (each either 0 or 1) representing the bit string.

.. method:: BitString.set_int_config(self, dec)

   Sets the configuration of the bit string from an integer.

   :param dec: An integer whose binary representation sets the bit string.

Basic Example
--------

.. code-block:: python

   # Create a BitString of length 5
   bits = BitString(5)
   print(bits)  # Outputs: 00000

   # Flip the third bit
   bits.flip_site(2)
   print(bits)  # Outputs: 00100

   # Set configuration using an integer
   bits.set_int_config(18)
   print(bits)  # Outputs: 10010