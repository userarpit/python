from scipy import stats
import numpy as np

# Observed frequencies
observed_counts = np.array([25, 18, 22, 15, 21, 19])

# Expected frequencies (for a fair die, 120 rolls / 6 sides = 20 per side)
expected_counts = np.array([20, 20, 20, 20, 20, 20])

chi_stat, p_value = stats.chisquare(f_obs=observed_counts, f_exp=expected_counts)
print(chi_stat)
print(p_value)