""" This script can read a BVH file frame by frame.
    Each frame will be converted into 3d Coordinates
    """

#@author: Taras Kucherenko

import BeeVeeH.bvh_helper as BVH
import numpy as np

def append(current_node, current_coords, main_joints):


    # check if we want this coordinate
    if current_node.name in main_joints:
        # append it to the coordinates of the current node
        curr_point = current_node.coordinates.reshape(3)
        current_coords.append(curr_point)

    for kids in current_node.children:
        append(kids, current_coords, main_joints)

def obtain_coords(root, frames, duration, main_joints):

    total_coords = []

    for fr in range(duration):

        current_coords = []

        root.load_frame(frames[fr])
        root.apply_transformation()

        # Visualize the frame
        append(root, current_coords, main_joints)

        total_coords.append(current_coords)

    return total_coords


if __name__ == '__main__':

    file_path = 'tests/bvh_files/0007_Cartwheel001.bvh'

    root, frames, frame_time = BVH.load(file_path)
    duration = len(frames)
    print('number of frames = %d' % duration)

    main_joints =  ['Hips', 'Spine', 'Spine1', 'Spine2', 'Spine3', 'Neck', 'Neck1', 'Head',  # Head and spine
                   'RightShoulder', 'RightArm', 'RightForeArm', 'RightHand', 'RightHandThumb1',
                   'RightHandThumb2', 'RightHandThumb3', 'RightHandIndex1', 'RightHandIndex2', 'RightHandIndex3',
                   'RightHandMiddle1', 'RightHandMiddle2', 'RightHandMiddle3', 'RightHandRing1', 'RightHandRing2',
                   'RightHandRing3', 'RightHandPinky1', 'RightHandPinky2', 'RightHandPinky3',  # Right hand
                   'LeftShoulder', 'LeftArm', 'LeftForeArm', 'LeftHand', 'LeftHandThumb1',
                   'LeftHandThumb2', 'LeftHandThumb3', 'LeftHandIndex1', 'LeftHandIndex2', 'LeftHandIndex3',
                   'LeftHandMiddle1', 'LeftHandMiddle2', 'LeftHandMiddle3', 'LeftHandRing1', 'LeftHandRing2',
                   'LeftHandRing3', 'LeftHandPinky1', 'LeftHandPinky2', 'LeftHandPinky3',  # left hand
                   ]

    coord = obtain_coords(root, frames, 100, main_joints)

    coords = np.array(coord)

    print(coords.shape)