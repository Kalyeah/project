import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Define the maze array
maze = np.array([
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
[1, 0, 2, 2, 2, 0, 1, 0, 5, 0, 0, 5, 0, 0, 1, 0, 2, 2, 0, 1],
[1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 1],
[1, 0, 2, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 2, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 0, 0, 2, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 2, 0, 0, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 5, 0, 0, 1, 0, 0, 0, 0, 4, 0, 0, 0, 0, 1, 0, 0, 5, 1],
[1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 4, 0, 0, 0, 1, 1, 1, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 2, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 2, 0, 1],
[1, 1, 0, 2, 0, 5, 0, 0, 0, 0, 6, 0, 0, 0, 0, 5, 0, 2, 0, 1],
[1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1],
[1, 0, 0, 0, 1, 1, 0, 0, 2, 2, 2, 2, 2, 0, 0, 1, 1, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 5, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 5, 1],
[1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1],
[1, 0, 0, 0, 2, 0, 0, 0, 1, 1, 3, 1, 1, 0, 0, 0, 2, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

# Define tile colors
colors = {
    0: 'white',
    1: 'black',
    2: 'gray',
    3: 'green',
    4: 'lightblue',
    5: 'gold',
    6: 'orange',
    7: 'red'
}

# Draw the maze
fig, ax = plt.subplots(figsize=(10, 8))
for (i, j), val in np.ndenumerate(maze):
    ax.add_patch(plt.Rectangle((j, len(maze) - 1 - i), 1, 1, color=colors[val], ec='black'))

ax.set_xlim(0, maze.shape[1])
ax.set_ylim(0, maze.shape[0])
ax.set_aspect('equal')
ax.axis('off')

# Legend
legend_patches = [
    mpatches.Patch(color=colors[val], label=f'{val}: {desc}') for val, desc in {
        0: 'Empty',
        1: 'Wall',
        2: 'Decorative Wall',
        3: 'Exit',
        4: 'Marker',
        5: 'Relic',
        6: 'Scroll',
        7: 'Guardian'
    }.items()
]
ax.legend(handles=legend_patches, loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=4)

plt.tight_layout()
plt.show()
