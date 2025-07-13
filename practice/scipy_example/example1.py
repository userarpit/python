from scipy.stats import chi2_contingency
import numpy as np

observed_data = np.array([[250, 9750], 
                          [310, 9690]])

chi2, p_value, dof, expected = chi2_contingency(observed_data)

print(chi2)
print(p_value)
print(dof)
print(expected)
