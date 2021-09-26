# Vision Algorithms

## Feature Matching and Image Stitching

Report: [Link](https://docs.google.com/document/d/1ASMuHsMyIP9ura363d7i0G01wRINR_yhr09VyZq8PBc/edit?usp=sharing)

## Requirements

```bash
pip install opencv-python
pip install opencv-contrib-python==3.4.2.17
pip install argparse
pip install numpy
git clone https://github.com/mradul2/vision-tasks
```

`opencv-contrib-python` is installed for using SIFT detector.

## Installation

```bash
git clone https://github.com/mradul2/vision-tasks
```

### Usage

```bash
python3 main.py [--a1 IMAGE1] [--a2 IMAGE2]
```

### Demo

#### Input Images

Template Image

<img src="assets/1.png" alt="1" width="400"/>

Transformed Image

<img src="assets/2.png" alt="2" width="400"/>

#### Detected Keypoints

Template Image

<img src="assets/3.png" alt="3" width="400"/>

Transformed Image

<img src="assets/4.png" alt="4" width="400"/>

#### Matched Keypoints

<img src="assets/5.png" alt="4" width="800"/>

#### Stitched Image

<img src="assets/5.png" alt="4" width="800"/>
