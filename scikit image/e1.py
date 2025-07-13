import skimage as ski
# print(ski.__version__)
# image = ski.data.coins()
# # ... or any other NumPy array!
# edges = ski.filters.sobel(image)
# ski.io.imshow(edges)
# ski.io.show()

# camera = ski.data.camera()
# print(camera.mean())

# camera[10, 20]
# camera[10, 20] = 3
# print(len(camera))
cat = ski.data.chelsea()
# print(cat.shape)
# print(cat[10, 20,2])
# cat[50, 61] = [0, 255, 0] 
# print(cat)
edges = ski.filters.sobel(cat)
ski.io.imshow(edges)
ski.io.show()
# import os
# filename = open("download.png")
# moon = ski.io.imread(filename)