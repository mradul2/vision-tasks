# Vision Algorithms

## Feature Matching and Image Stitching

Report: [Link](https://docs.google.com/document/d/1ASMuHsMyIP9ura363d7i0G01wRINR_yhr09VyZq8PBc/edit?usp=sharing)

## Requirements

```bash
pip install opencv-contrib-python==3.4.2.17
pip install argparse
git clone https://github.com/mradul2/vision-tasks
```

`opencv-contrib-python` is installed for implementing SIFT detection algorithm.

## Installation

```bash
git clone https://github.com/mradul2/vision-tasks
```

## Usage

```bash
python3 main.py [--a1 PATH_IMAGE1] [--a2 PATH_IMAGE2]
```

## Demo

### Input Images

Template Image

<img src="assets/1.png" alt="1" width="400"/>

Transformed Image

<img src="assets/2.png" alt="2" width="400"/>

### Detected Keypoints

Template Image

<img src="assets/3.png" alt="3" width="400"/>

Transformed Image

<img src="assets/4.png" alt="4" width="400"/>

### Matched Keypoints

<img src="assets/5.png" alt="5" width="800"/>

### Stitched Image

<img src="assets/6.png" alt="6" width="800"/>

## About

`SIFT detectors` are used to detect `Keypoints` and their descriptions, furthermore Descriptor Matches are found using `Brute Force Matcher`. Then `.pt` attribute (Coordinates of Keypoints) are extracted from each Keypoints and a list of individual coordinates is created from matched descriptors for both Images. Finally `Homography Matrix` is found using those matched points and `warp perspective` is applied on the second Image to combine it with the First Image.

## Refrences

- Keypoints: [Link](https://docs.opencv.org/3.4/d2/d29/classcv_1_1KeyPoint.html)
- Homography: [Link](https://docs.opencv.org/4.5.2/d9/dab/tutorial_homography.html)
- `cv::warpPerspective`: [Link](https://docs.opencv.org/4.5.2/da/d54/group__imgproc__transform.html#gaf73673a7e8e18ec6963e3774e6a94b87)
