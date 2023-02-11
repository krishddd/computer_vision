from skimage import io, filters
from scipy import ndimage
import matplotlib.pyplot as plt
from skimage import measure
im = io.imread('ba3g0.jpg', as_grey=True)
val = filters.threshold_otsu(im)
drops = ndimage.binary_fill_holes(im < val)
plt.imshow(drops, cmap='gray')
plt.show()

labels = measure.label(drops)
print(labels.max())
print('coverage is %f' %(drops.mean()))