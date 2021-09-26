# Importing Relevant Libraries 
import cv2
from matplotlib import pyplot as plt 
import numpy as np

import argparse

parser = argparse.ArgumentParser(description='.')
parser.add_argument('--a1', metavar='image', default="assets/1.png",
                    help='Enter the path for Template Image')
parser.add_argument('--a2', metavar='image', default="assets/2.png",
                    help='Enter the path for Transformation Image')

args = parser.parse_args()


# Reading images used for stitching
# a1 is the template Image on which a2 would be tranformed 
a1 = cv2.imread(args.a1).astype('uint8')
a2 = cv2.imread(args.a2).astype('uint8')
gray1 = cv2.cvtColor(a1, cv2.COLOR_RGB2GRAY)
gray2 = cv2.cvtColor(a2, cv2.COLOR_RGB2GRAY)

plt.imshow(a1)
plt.imshow(a2)

# Creating SIFT detector object 
sift = cv2.ORB_create()

# Finding Keypoints and Descriptors using SIFT detector 
keypoints1, descriptors1 = sift.detectAndCompute(a1,None)
a_1 = cv2.drawKeypoints(gray1,keypoints1, None, color=(255,0,0))
keypoints2, descriptors2 = sift.detectAndCompute(a2,None)
a_2 = cv2.drawKeypoints(gray2,keypoints2, None, color=(255,0,0))

plt.imshow(a_1)
plt.imshow(a_2)

# Creating Brute Force Matcher object with L2 Norm 
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

# Finding Matches between 2 descriptors using the created Matcher
matches = bf.match(descriptors1, descriptors2)
# Sorting the Matches based on the distance between Descriptors
matches = sorted(matches, key = lambda x:x.distance)
# Shortlisiting best of them 
matches = matches[:80]

a_matched = cv2.drawMatches(a1, keypoints1, a2, keypoints2, matches ,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

plt.figure(figsize=(20,10))
plt.imshow(a_matched)

# Extracting coordinates from each Keypoint
keypoints1_pt = [kp.pt for kp in keypoints1]
keypoints2_pt = [kp.pt for kp in keypoints2]

# Matched points from matched descriptors 
matched_pts1 = np.array([keypoints1_pt[m.queryIdx] for m in matches])
matched_pts2 = np.array([keypoints2_pt[m.trainIdx] for m in matches])

# Finding Homography Matrix using Matched Points 
(H, status) = cv2.findHomography(matched_pts2, matched_pts1, cv2.RANSAC, 5)

width = a1.shape[1] + a2.shape[1]
height = a2.shape[0]

# Applying perspective Transform on the second Image and merging it with the First Image 
result = cv2.warpPerspective(a2, H, (width, height))
result[0:a1.shape[0], 0:a1.shape[1]] = a1

plt.imshow(result)