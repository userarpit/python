import numpy as np

print("--- Multidimensional uint8 Arrays ---")

# 1. Creating a 2D array (like a grayscale image)
#    A 3x4 array initialized with zeros (black)
print("\n--- Example 1: 2D Array (Grayscale Image) ---")
grayscale_image = np.zeros((3, 4), dtype=np.uint8)
print(f"Initial 2D Array (3x4):\n{grayscale_image}")

# Assign a single pixel value (row, column)
grayscale_image[0, 0] = 255  # Top-left pixel to white
grayscale_image[1, 2] = 128  # Middle pixel to gray
print(f"After assigning single pixels:\n{grayscale_image}")

# Assign an entire row
grayscale_image[2, :] = 100 # Set the entire last row to gray
print(f"After assigning a row:\n{grayscale_image}")

# Assign an entire column
grayscale_image[:, 0] = 50 # Set the entire first column to a darker gray
print(f"After assigning a column:\n{grayscale_image}")

# Assign a sub-region (slice)
grayscale_image[0:2, 1:3] = [[200, 201], [202, 203]] # Assign a 2x2 block
print(f"After assigning a sub-region:\n{grayscale_image}")

# 2. Creating a 3D array (like an RGB image)
#    A 2x2 image with 3 color channels (R, G, B)
#    Dimensions are typically (height, width, channels)
print("\n--- Example 2: 3D Array (RGB Image) ---")
rgb_image = np.zeros((2, 2, 3), dtype=np.uint8) # 2 rows, 2 columns, 3 channels
print(f"Initial 3D Array (2x2 RGB):\n{rgb_image}")

# Assign a single pixel's color (e.g., top-left pixel to red)
# rgb_image[row, col, channel]
rgb_image[0, 0, 0] = 255 # Red channel for top-left pixel
print(f"After setting top-left red channel:\n{rgb_image}")

# Assign an entire pixel's RGB value (e.g., top-right pixel to blue)
rgb_image[0, 1, :] = [0, 0, 255] # [R, G, B]
print(f"After setting top-right to blue:\n{rgb_image}")

# Assign an entire row of pixels (e.g., bottom row to green)
rgb_image[1, :, :] = [0, 255, 0]
print(f"After setting bottom row to green:\n{rgb_image}")

# 3. Operations that might lead to overflow/underflow in multidimensional arrays
print("\n--- Example 3: Overflow/Underflow in 3D Array ---")
test_image = np.full((1, 1, 3), 250, dtype=np.uint8) # A single pixel with R,G,B = 250
print(f"Initial test pixel: {test_image}")

# Add 10 to all channels (250 + 10 = 260, wraps around to 4)
test_image += 10
print(f"After adding 10 (overflow): {test_image}")

# Subtract 20 from all channels (4 - 20 = -16, wraps around to 240)
test_image -= 20
print(f"After subtracting 20 (underflow): {test_image}")

# 4. Creating a 3D array using `np.random.randint` for random pixel values
print("\n--- Example 4: Random Multidimensional uint8 Array ---")
# Create a 5x5 grayscale image with random pixel intensities
random_grayscale = np.random.randint(0, 256, size=(5, 5), dtype=np.uint8)
print(f"Random 5x5 grayscale image:\n{random_grayscale}")

# Create a 3x3 RGB image with random pixel colors
random_rgb = np.random.randint(0, 256, size=(3, 3, 3), dtype=np.uint8)
print(f"Random 3x3 RGB image:\n{random_rgb}")

# 5. Assigning based on conditions (Boolean indexing)
print("\n--- Example 5: Conditional Assignment in 2D Array ---")
grayscale_cond = np.array([
    [10, 200, 30],
    [150, 50, 220],
    [80, 10, 190]
], dtype=np.uint8)
print(f"Original array:\n{grayscale_cond}")

# Set all pixels brighter than 150 to 255 (white)
grayscale_cond[grayscale_cond > 150] = 255
print(f"After setting bright pixels to 255:\n{grayscale_cond}")

# Set all pixels darker than 50 to 0 (black)
grayscale_cond[grayscale_cond < 50] = 0
print(f"After setting dark pixels to 0:\n{grayscale_cond}")