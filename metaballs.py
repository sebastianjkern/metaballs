# %%

import numpy as np
from vectors import Point
import matplotlib.pyplot as plt

WIDTH = 150
HEIGHT = 150

THRESHOLD = .004
COLOR = (100, 100, 100)

image = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

# Position of the metaballs is given in pixel coordinates
metaballs = [
    Point(40, 90, 0),
    Point(45, 40, 0),
    Point(70, 70, 0),
]

def strength(pixel, center):
    divider = (pixel.x - center.x)**2 + (pixel.y - center.y)**2
    if divider == 0:
        return THRESHOLD
    else:
        return 1/divider

for x in range(WIDTH):
    for y in range(HEIGHT):
        strengths = 0

        for ball in metaballs:
            strengths += strength(pixel = Point(x, y, 0), center=ball)

        if strengths <= THRESHOLD:
            image[x, y] = COLOR

plt.imshow(image)
plt.show()
# %%
