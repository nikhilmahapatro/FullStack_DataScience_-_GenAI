import numpy as np
import matplotlib.pyplot as plt
from PIL import Image                  # PIL- Python Imaging Library

ones_arr = np.ones((5,5), dtype= int)
print(ones_arr)

# every pixel range is 1-255
print(ones_arr * 255)

cap_image = Image.open(r"C:\Users\nikhi\PycharmProjects\NARESH_IT\01_NARESH_IT_PYTHON\Naresh_IT_05_Matplotlib\peakpx.jpg")
# cap_image.show()
print(type(cap_image))

cap_arr = np.asarray(cap_image)
print(cap_arr)
print(type(cap_arr))

plt.imshow(cap_arr)
plt.show()
print(cap_arr.shape)

cap_red = cap_arr.copy()
print(cap_red)
print(cap_arr==cap_red)

# Changing colour of the array.
# R-G-B
# 0=blue, 1=red, 2=green
plt.imshow(cap_red[:,:,0])
plt.show()
plt.imshow(cap_red[:,:,0],cmap='Greys')
plt.show()
plt.imshow(cap_red[:,:,1],cmap='grey')
plt.show()
plt.imshow(cap_red[:,:,1],cmap='Blues')
plt.show()
plt.imshow(cap_red[:,:,2],cmap='YlGn')
plt.show()

# When Image colour is changed, the array values also change
print(cap_red[:,:,0])
print(cap_red[:,:,1])
print(cap_red[:,:,2])

# Changing all values of the array to 0
cap_red[:,:,1] = 0
plt.imshow(cap_red[:,:,1])
plt.show()

arr1 = np.asarray(cap_image)
print(type(arr1))
print(arr1.shape)
cap_img1 = arr1.copy()
cap_img1[:,:,0] = 0
plt.imshow(cap_img1)
plt.show()


