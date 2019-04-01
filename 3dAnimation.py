import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FixedLocator, FormatStrFormatter
import matplotlib, time

import BeeVeeH.bvh_helper as BVH

class plot3dClass( object ):

    def __init__( self, root, frames ):

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot( 111, projection='3d' )

        self.root = root
        self.frames = frames

        self.scatter = self.ax.scatter3D(0,0,0)


    def drawNow( self, fr ):

        self.ax.remove()

        # Reinitialize the axis
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.set_zlim3d(0, 70)
        self.ax.set_xlim3d(-80, 80)
        self.ax.set_ylim3d(-80, 80)

        self.root.load_frame(self.frames[fr])
        self.root.apply_transformation()

        self.show_frame(self.root)

        # redraw the canvas
        plt.draw()
        self.fig.canvas.flush_events()

        plt.pause(0.001)

    def show_frame(self, current_node):

        coords = current_node.coordinates

        self.scatter = self.ax.scatter3D(coords[2], coords[0], coords[1], c='c')

        if current_node.children:

            for kid in current_node.children:
                self.show_frame(kid)

                # Draw a line to a kid
                x = coords[0]
                xline = np.array([coords[0][0], kid.coordinates[0][0]])
                yline = np.array([coords[1][0], kid.coordinates[1][0]])
                zline = np.array([coords[2][0], kid.coordinates[2][0]])

                self.ax.plot3D( zline, xline, yline, 'gray')


if __name__ == '__main__':

    file_path = '/home/taras/Dropbox/2017_PhD_at_KTH/Code/Git/BeeVeeH/tests/bvh_files/0007_Cartwheel001.bvh'

    root, frames, frame_time = BVH.load(file_path)

    p = plot3dClass(root, frames)

    print('number of frames = %d' % len(frames))
    # "number of frames = 2111"

    for fr in range(len(frames)):
        p.drawNow(fr)
