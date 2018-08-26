from matplotlib import pyplot as plt
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from math import sqrt
from skimage.color import rgb2gray
import glob
from skimage.io import imread
#Convert to grey_scale
example_file = glob.glob(r"C:\Users\Kavin\Downloads\crowd.jpg")[0]
im = imread(example_file, as_grey=True)
plt.imshow(im ,cmap='gray')
plt.show()
#blobs identification
blobs_log = blob_log(im, max_sigma=30, num_sigma=100, threshold=.3)
blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)
numpeople = len(blobs_log)
print("number of people: " ,numpeople)
#shows the detected blobs
fig, ax = plt.subplots(1, 1)
plt.imshow(im, cmap='gray')
for blob in blobs_log:
    y, x, r = blob
    c = plt.Circle((x, y), r+5, color='lime', linewidth=2, fill=True)
    ax.add_patch(c)
