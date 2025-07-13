from scipy import stats
import numpy as np

# Example: Comparing test scores of two independent groups
group_a_scores = np.array([85, 90, 78, 92, 88, 75, 80, 95])
group_b_scores = np.array([85, 90, 68, 80, 72, 65, 78, 82])

t_stat, p_value = stats.ttest_ind(group_a_scores, group_b_scores, equal_var=False)
print(t_stat, p_value)

print(np.mean(group_a_scores))
print(np.mean(group_b_scores))
