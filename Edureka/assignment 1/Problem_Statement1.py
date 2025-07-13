import numpy as np

m_value = int(input("Enter Value M: "))
n_value = int(input("Enter Value N: "))
a_value = int(input("Enter Value A: "))

m_cross_n = np.random.rand(m_value,n_value)
n_cross_a = np.random.rand(n_value,a_value)

m_cross_a = np.dot(m_cross_n,n_cross_a)
print(m_cross_n)
print(n_cross_a)
print(m_cross_a)