import numpy as np

def replace_outliers(data):
    """
    Replaces outliers in a dataset with the maximum and minimum values on either side.

    Args:
        data (list or numpy array): The dataset to process.

    Returns:
        list or numpy array: The processed dataset with outliers replaced.
    """
    data = np.array(data)  # Convert to numpy array for easier calculations
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    for i, value in enumerate(data):
        if value < lower_bound:
            data[i] = data[data > lower_bound].min()  # Replace with min of non-outliers below
        elif value > upper_bound:
            data[i] = data[data < upper_bound].max()  # Replace with max of non-outliers above

    return data.tolist()  # Convert back to list if original input was a list


if __name__ == '__main__':
    # Example usage:
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]  # Example data with an outlier
    processed_data = replace_outliers(data)
    print("Original data:", data)
    print("Processed data:", processed_data)