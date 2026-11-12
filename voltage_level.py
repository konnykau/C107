# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.patches import FancyArrowPatch

# levels = [
#     "5V CMOS",
#     "5V TTL",
#     "3.3V LVTTL",
#     "2.5V CMOS",
#     "1.8V CMOS"
# ]

# # 入力（矩形）
# low_input = [(0.0,1.5),(0.0,0.8),(0.0,0.8),(0.0,0.7),(0.0,0.6)]
# high_input = [(3.5,5.0),(2.0,5.0),(2.0,3.3),(1.7,2.5),(1.2,1.8)]

# # 出力（矢印）
# low_output = [(0.5,0.3),(0.45,0.0),(0.45,0.0),(0.5,0.0),(0.5,0.0)]
# high_output = [(4.5,4.7),(2.4,2.6),(2.4,2.6),(2.0,2.2),(1.3,1.5)]

# def arrow_barh(ax, y, x_start, x_end, height=0.25,
#                color="tomato", alpha=0.9):
#     arrow = FancyArrowPatch(
#         (x_start, y),
#         (x_end, y),
#         arrowstyle='-|>',
#         mutation_scale=15,
#         linewidth=2,
#         color=color,
#         alpha=alpha,
#         capstyle='butt'
#     )
#     ax.add_patch(arrow)

# y = np.arange(len(levels))
# offset = 0.18
# bar_h = 0.30

# fig, ax = plt.subplots(figsize=(9, 3.5))

# for i in range(len(levels)):
#     # ----- Input（矩形）-----
#     ax.barh(y[i]+offset,
#             low_input[i][1]-low_input[i][0],
#             left=low_input[i][0],
#             height=bar_h,
#             color="royalblue",
#             alpha=0.8)

#     ax.barh(y[i]+offset,
#             high_input[i][1]-high_input[i][0],
#             left=high_input[i][0],
#             height=bar_h,
#             color="tomato",
#             alpha=0.8)

#     # ----- Output（矢印）-----
#     arrow_barh(ax, y[i]-offset,
#                low_output[i][0], low_output[i][1],
#                height=0.22,
#                color="royalblue")

#     arrow_barh(ax, y[i]-offset,
#                high_output[i][0], high_output[i][1],
#                height=0.22,
#                color="tomato")

#     # 右側ラベル
#     ax.text(5.25, y[i]+offset, "input", va="center", fontsize=9)
#     ax.text(5.25, y[i]-offset, "output", va="center", fontsize=9)

# ax.set_yticks(y)
# ax.set_yticklabels(levels)
# ax.set_xlabel("Voltage [V]")
# ax.set_xlim(0, 5.6)

# ax.grid(axis="x", linestyle="--", alpha=0.5)

# plt.tight_layout()
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

levels = [
    "5V CMOS",
    "5V TTL",
    "3.3V LVTTL",
    "2.5V CMOS",
    "1.8V CMOS"
]

# --- 電圧範囲 [V] ---
# (min, max)
# # 入力（矩形）
low_input = [(0.0,1.5),(0.0,0.8),(0.0,0.8),(0.0,0.7),(0.0,0.6)]
high_input = [(3.5,5.0),(2.0,5.0),(2.0,3.3),(1.7,2.5),(1.2,1.8)]

# # 出力（矢印）
low_output = [(0.5,0.0),(0.45,0.0),(0.45,0.0),(0.5,0.0),(0.5,0.0)]
high_output = [(4.5,5.0),(2.4,5),(2.4,3.3),(2.0,2.5),(1.3,1.8)]

y_base = np.arange(len(levels))
offset = 0.18
bar_h = 0.30

fig, ax = plt.subplots(figsize=(9, 3.5))

for i in range(len(levels)):
    # --- Input ---
    ax.barh(y_base[i] + offset,
            low_input[i][1] - low_input[i][0],
            left=low_input[i][0],
            height=bar_h,
            color="royalblue",
            alpha=0.8)

    ax.barh(y_base[i] + offset,
            high_input[i][1] - high_input[i][0],
            left=high_input[i][0],
            height=bar_h,
            color="tomato",
            alpha=0.8)

    # --- Output ---
    ax.barh(y_base[i] - offset,
            low_output[i][1] - low_output[i][0],
            left=low_output[i][0],
            height=bar_h,
            color="royalblue",
            alpha=0.8,
            hatch="//")

    ax.barh(y_base[i] - offset,
            high_output[i][1] - high_output[i][0],
            left=high_output[i][0],
            height=bar_h,
            color="tomato",
            alpha=0.8,
            hatch="//")
    
    ax.text(5.25, y_base[i]+offset, "input", va="center", fontsize=9)
    ax.text(5.25, y_base[i]-offset, "output", va="center", fontsize=9)

# 軸・ラベル設定
ax.set_yticks(y_base)
ax.set_yticklabels(levels)
ax.set_xlabel("Voltage [V]")
ax.set_xlim(0, 5.2)

ax.grid(axis="x", linestyle="--", alpha=0.5)

# 凡例（ダミー）
ax.barh(-1, 0, color="royalblue", label="LOW")
ax.barh(-1, 0, color="tomato", label="HIGH")
ax.barh(-1, 0, color="gray", hatch="//", label="Output")



plt.tight_layout()
plt.show()
