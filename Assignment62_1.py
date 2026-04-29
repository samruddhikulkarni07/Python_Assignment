# ------------------------------------------------------------
# 6x6 Grayscale Image
# Top Half = Black (0)
# Bottom Half = White (255)
# Apply 3x3 Kernel for Edge Detection
# Show Feature Map
# ------------------------------------------------------------

import numpy as np

# ------------------------------------------------------------
# Step 1 : Create 6x6 Image
# ------------------------------------------------------------
image = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
])

print("\nOriginal 6x6 Image")
print(image)


# ------------------------------------------------------------
# Step 2 : 3x3 Kernel for Horizontal Edge Detection
# ------------------------------------------------------------
kernel = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
])

print("\n3x3 Kernel")
print(kernel)

# ------------------------------------------------------------
# Step 3 : Convolution Operation
# Output Size = (5-3+1) x (5-3+1) = 3x3
# ------------------------------------------------------------
feature_map = np.zeros((3,3))

for i in range(3):
    for j in range(3):
        print("\n\n==================================================")
        print(f"Kernel Position -> Row: {i} to {i+2}, Column: {j} to {j+2}")
        print("==================================================")

        # Extract 3x3 region from image
        region = image[i:i+3, j:j+3]

        print("Region:")
        print(region)

        # Element-wise multiplication
        multiplied = region * kernel
        print("multiplication:")
        print(multiplied)

        # Sum all elements
        result = np.sum(multiplied)
        print("\nSum of all values =")
        print(result)

        # Store in feature map
        feature_map[i][j] = result

        print("Feature Map Built So Far", feature_map)

# ------------------------------------------------------------
# Step 4 : Show Feature Map
# ------------------------------------------------------------
print("\nFeature Map (Detected Edge)")
print(feature_map)