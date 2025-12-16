
if image is None:
    print("Error: Could not load image.")
else:
    x = 1022 # column index
    y = 216 # row index

    if y < 0 or y >= image.shape[0] or x < 0 or x >= image.shape[1]:

        print("Error: Coordinates are out of bounds.")

    else:

        pixel_value = image[y, x]
        print(f"Pixel value at ({y}, {x}): {pixel_value}")


