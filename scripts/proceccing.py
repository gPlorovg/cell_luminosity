import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


class ROI:
    def __init__(self, x: int, y: int, r: int):
        self.x = x
        self.y = y
        self.r = r

    def measure(self, img: np.ndarray) -> float:
        xs, ys = np.indices(img.shape)
        mask = (xs - self.x) ** 2 + (ys - self.y) ** 2 <= self.r ** 2
        return np.median(img[mask])

    def get_info(self):
        return [self.x, self.y, self.r]


def open_image(url):
    return np.array(Image.open(url).convert('L'))


def make_graph(data, name):
    fig, ax = plt.subplots(figsize=(5, 5))

    for i, col in enumerate(zip(*data)):
        ax.plot(col, label=f'Region {i + 1}', linewidth=2)

    # Customize the appearance of the plot
    ax.set_xlabel('Frames', fontsize=12)  # Set the x-axis label and font size
    ax.set_ylabel('Relative Fluorescence', fontsize=12)  # Set the y-axis label and font size
    ax.legend(fontsize=10)  # Set the legend font size

    # Adjust the plot layout
    fig.tight_layout()

    # Show the plot
    url = f"../graphics/{name}.png"
    plt.savefig(url, dpi=100)
    return url

# image = np.random.randint(0, 256, size=144).reshape(-1, 12)
# roi = ROI(5, 5, 3)
#
#
# def make_graph():
#     fig, ax = plt.subplots()
#
#     ax.plot((1, 2), (1, 2))
#     ax.plot((2, 1), (1, 2))
#
#     ax.set_xlabel('$ Time, min $')
#     ax.set_ylabel('$ F / F_0 $')
#     plt.show()
#
#
# make_graph()