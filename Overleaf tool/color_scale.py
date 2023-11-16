import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# color = np.array(["#28AFAF", "#54bebe", "#76c8c8", "#98d1d1", "#badbdb", "#dedad2", "#e4bcad", "#df979e", "#d7658b", "#c80064"])
# color = color[:-2]
# color = np.array(['#68ABAF', '#8EC5D0', '#ADD2D4', '#CEBECA'])
color = np.array(['#4C8F93', '#68ABAF', '#ADD2D4', '#F0F6FA', '#CEBECA', '#df979e '])
# color = np.array(["#115f9a", "#1984c5", "#22a7f0", "#48b5c4", "#76c68f", "#a6d75b", "#c9e52f", "#d0ee11", "#d0f400"])
color = color[::-1]
rgb = []
for cc in color:
    hex_code = cc.lstrip('#')
    print(hex_code)
    rgb.append(list(int(hex_code[i:i + 2], 16) for i in (0, 2, 4)))
rgb = np.array(rgb)
print(rgb)

palette_sample = np.linspace(0, 1, rgb.shape[0] + 2)
palette_mask = np.ones(len(palette_sample), )
palette_mask[[-5,  -4]] = 0
palette_sample = palette_sample[np.nonzero(palette_mask)]
print(palette_sample)

r = interp1d(palette_sample, rgb[:, 0])
g = interp1d(palette_sample, rgb[:, 1])
b = interp1d(palette_sample, rgb[:, 2])
color_inter = [r, g, b]


def trait_table():
    scale_value = np.array([[0.19, 0.03, 0.06, 0.11, 0.19, 0.11, 0.17, 0.06, 0.08],
                            [0.08, 0.14, 0.03, 0.11, 0.14, 0.06, 0.14, 0.11, 0.19],
                            [0.06, 0.06, 0.11, 0.14, 0.17, 0.17, 0.08, 0.19, 0.03],
                            [0.06, 0.17, 0.08, 0.19, 0.08, 0.06, 0.19, 0.08, 0.08],
                            [0.08, 0.14, 0.03, 0.11, 0.08, 0.06, 0.22, 0.17, 0.11],
                            [0.17, 0.17, 0.14, 0.06, 0.08, 0.08, 0.06, 0.08, 0.17],
                            [0.17, 0.17, 0.06, 0.03, 0.14, 0.06, 0.08, 0.14, 0.17],
                            [0.08, 0.03, 0.08, 0.14, 0.11, 0.14, 0.17, 0.19, 0.06],
                            [0.08, 0.17, 0.11, 0.06, 0.17, 0.14, 0.06, 0.08, 0.14],
                            [0.08, 0.11, 0.06, 0.08, 0.22, 0.11, 0.08, 0.08, 0.17]
                            ])

    person = np.array(['Camila', 'Gad', 'Jianpeng', 'Jules', 'Max', 'Nicolas', 'Rusudan', 'Teus', 'Wesley', 'Zhangyi'])

    scale_range = np.max(scale_value) - np.min(scale_value)
    scale_map = (scale_value - np.min(scale_value)) / scale_range

    map_color = np.empty(scale_value.shape, dtype='object')
    text_white = np.empty(scale_value.shape, dtype=bool)
    luma_weight = np.array([0.299, 0.587, 0.114, 186])
    # luma_weight = np.array([0.2126, 0.7152, 0.0722, 40])
    for row in range(scale_value.shape[0]):
        for col in range(scale_value.shape[1]):
            color_tuple = []
            for d in color_inter:
                color_tuple.append(int(d(scale_map[row, col])))
            map_color[row, col] = "#{0:02x}{1:02x}{2:02x}".format(*color_tuple)
            text_white[row, col] = np.sum(np.array(color_tuple)* luma_weight[0:3]) < luma_weight[-1]

    for row in range(map_color.shape[0]):
        latex = f'{person[row]} & '
        for col in range(map_color.shape[1]):
            if text_white[row, col]:
                trait_value = f'\\textcolor{{white}}{{{scale_value[row, col]}}}'
            else:
                trait_value = f'{scale_value[row, col]}'
            latex += f'\\cellcolor[HTML]{{{map_color[row, col][1:]}}} {trait_value} & '
        latex = latex[:-2]
        latex += '\\\\ \\hline'
        print(latex)

    return map_color


def test_palette(color_map=None):
    if color_map is None:
        seq = np.linspace(0, 1, 20)
        for i in range(len(seq)):
            palette_color = []
            for c in range(3):
                palette_color.append(int(color_inter[c](seq[i])))
            palette_color = "#{0:02x}{1:02x}{2:02x}".format(*palette_color)
            plt.plot([0, 1], [i, i], color=palette_color, linewidth=5)
    else:
        for row in range(color_map.shape[0]):
            for col in range(color_map.shape[1]):
                plt.plot([2 * col, 2 * col + 1], [-2 * row, -2 * row], color=color_map[row, col], linewidth=20)
        plt.scatter(palette_sample * color_map.shape[1] * 1.9, np.ones_like(palette_sample) * 1)
    plt.show()


if __name__ == '__main__':
    cmap = trait_table()
    test_palette(cmap)

