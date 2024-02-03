#!/usr/bin/python3
""" Module for  matrix multiplication """


def matrix_mul(m_a, m_b):
   """Multiplies two matrices, performing input validation and raising appropriate exceptions."""

   # Validate input types
   if not isinstance(m_a, list):
       raise TypeError("m_a must be a list")
   if not isinstance(m_b, list):
       raise TypeError("m_b must be a list")

   # Validate matrix structure
   if not all(isinstance(row, list) for row in m_a):
       raise TypeError("m_a must be a list of lists")
   if not all(isinstance(row, list) for row in m_b):
       raise TypeError("m_b must be a list of lists")

   # Validate matrix dimensions
   if not m_a or not m_a[0]:
       raise ValueError("m_a can't be empty")
   if not m_b or not m_b[0]:
       raise ValueError("m_b can't be empty")

   # Validate matrix element types
   if not all(all(isinstance(element, (int, float)) for element in row) for row in m_a):
       raise TypeError("m_a should contain only integers or floats")
   if not all(all(isinstance(element, (int, float)) for element in row) for row in m_b):
       raise TypeError("m_b should contain only integers or floats")

   # Validate matrix shape consistency
   if not all(len(row) == len(m_a[0]) for row in m_a):
       raise TypeError("each row of m_a must be of the same size")
   if not all(len(row) == len(m_b[0]) for row in m_b):
       raise TypeError("each row of m_b must be of the same size")

   # Validate matrix multiplication compatibility
   if len(m_a[0]) != len(m_b):
       raise ValueError("m_a and m_b can't be multiplied")

   # Perform matrix multiplication
   result = [[0] * len(m_b[0]) for _ in range(len(m_a))]
   for i in range(len(m_a)):
       for j in range(len(m_b[0])):
           for k in range(len(m_b)):
               result[i][j] += m_a[i][k] * m_b[k][j]

   return result
