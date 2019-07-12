""" This script can visualize a BVH file frame by frame.
    Each frame will be visualized in a separate widnow
    Continuous animation is implemented at 3dAnimation.py"""

#@author: Taras Kucherenko

import BeeVeeH.bvh_helper as BVH
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def show_frame(current_node, ax):

    coords = current_node.coordinates

    ax.scatter3D(coords[2], coords[0], coords[1], c='c')

    if current_node.children:

        for kid in current_node.children:
            show_frame(kid, ax)

            # Draw a line to a kid
            x = coords[0]
            xline = np.array([coords[0][0], kid.coordinates[0][0]])
            yline = np.array([coords[1][0], kid.coordinates[1][0]])
            zline = np.array([coords[2][0], kid.coordinates[2][0]])

            ax.plot3D( zline, xline, yline, 'gray')

def visualize(root):
    """
    Visualize a given frame of the motion
    :param root: root of the BVH structure
    :return: nothing, will create 3D plot for this frame
    """

    ax = plt.axes(projection='3d')
    show_frame(root, ax)
    plt.show()


if __name__ == '__main__':

    file_path = 'tests/bvh_files/0007_Cartwheel001.bvh'
    root, frames, frame_time = BVH.load(file_path)
    print('number of frames = %d' % len(frames))
    # "number of frames = 2111"

    for fr in range(len(frames)):

        root.load_frame(frames[fr])
        root.apply_transformation()

        # Visualize the frame
        visualize(root)
