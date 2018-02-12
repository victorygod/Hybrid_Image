import matplotlib.pyplot as plt
from align_image_code import align_images
import numpy as np
from scipy import signal
from scipy import misc
from scipy import ndimage

# First load images
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
# high sf
im1 = plt.imread('./cat.jpg')/255

# low sf
im2 = plt.imread('./dog.jpg')/255

# Next align images (this code is provided, but may be improved)
im1_aligned, im2_aligned = align_images(im1, im2)
#
#plt.imsave('im1.jpg', im1_aligned)
#
#plt.imsave('im2.jpg', im2_aligned)



#
#laplacian_filter = [[0,1,0],[1,-4,1],[0,1,0]]
#gray = rgb2gray(im2_aligned)
#im_edge = signal.convolve2d(gray, laplacian_filter, 'same')

#def hybrid_image(im1, im2, sigma1, sigma2):
#    #im_blur = ndimage.gaussian_filter(im1, sigma1)
#    im1 = rgb2gray(im1)
#    h1 = np.zeros(im1.shape)
#    for x in range(int(-im1.shape[0]/2), int(im1.shape[0]/2)):
#        for y in range(int(-im1.shape[1]/2), int(im1.shape[1]/2)):
#            D = (x**2+y**2)**0.5
#            h1[x+int(im1.shape[0]/2), y+int(im1.shape[1]/2)] = 1 - np.exp(-(D*D)/(2*sigma1*sigma1))
#    G1 = h1*np.fft.fftshift(np.fft.fft2(im1))
#    misc.imsave('fft_1.jpg', np.log(np.abs(G1)+0.5))
#    im_blur = np.real(np.fft.ifft2(np.fft.fftshift(G1)))
#
#    misc.imsave('output.jpg', im_blur)
#    im_blur2 = ndimage.gaussian_filter(im2, sigma2)
#    
#    misc.imsave('fft_2.jpg', np.log(np.abs(np.fft.fftshift(np.fft.fft2(rgb2gray(im_blur2))))))
#    im_hybrid = im_blur + rgb2gray(im_blur2)
#    return im_hybrid

def hybrid_image(im11, im22, sigma1, sigma2):
    im1 = rgb2gray(im11)
    im2 = rgb2gray(im22)
    im_blur = ndimage.gaussian_filter(im11, sigma1)
    im_blur2 = ndimage.gaussian_filter(im22, sigma2)
    misc.imsave('fft_img1_filtered.jpg', np.log(np.abs(np.fft.fftshift(np.fft.fft2(im1-rgb2gray(im_blur))))))
    misc.imsave('fft_img2_filtered.jpg', np.log(np.abs(np.fft.fftshift(np.fft.fft2(rgb2gray(im_blur2))))))
    im_hybrid = im1 - rgb2gray(im_blur) + rgb2gray(im_blur2)
#    misc.imsave('output.jpg', im1-im_blur)
    return im_hybrid

def frequency_analysis(img, name):
    misc.imsave(name, np.log(np.abs(np.fft.fftshift(np.fft.fft2(rgb2gray(img))))))

def hybrid_image_colored(im1, im2, sigma1, sigma2):
    im_blur = np.zeros(im1.shape)
    im_blur2 = np.zeros(im2.shape)
    for i in range(3):
        im_blur[:,:,i] = ndimage.gaussian_filter(im1[:,:,i], sigma1)
        im_blur2[:,:,i] = ndimage.gaussian_filter(im2[:,:,i], sigma2)
    misc.imsave('fft_img1_filtered.jpg', np.log(np.abs(np.fft.fftshift(np.fft.fft2(rgb2gray(im1-im_blur))))))
    misc.imsave('fft_img2_filtered.jpg', np.log(np.abs(np.fft.fftshift(np.fft.fft2(rgb2gray(im_blur2))))))
    im_hybrid = im1 - im_blur + im_blur2
#    misc.imsave('output.jpg', im1-im_blur)
    return im_hybrid

def pyramids(hybrid, N):
    misc.imsave('output0.jpg', hybrid)
    for i in range(N-1):
        h= hybrid.shape[0]
        w = hybrid.shape[1]
        hybrid = misc.imresize(hybrid, (int(h/2), int(w/2)))
        misc.imsave('output' + str(i+1) + '.jpg', hybrid)

#hybrid = hybrid_image_colored(im1_aligned, im2_aligned, 10, 4)
hybrid = hybrid_image_colored(im1_aligned, im2_aligned, 10, 5)
frequency_analysis(im1, "fft_img1.jpg")
frequency_analysis(im2, "fft_img2.jpg")
frequency_analysis(im1_aligned, "fft_img1_aligned.jpg")
frequency_analysis(im2_aligned, "fft_img2_aligned.jpg")
frequency_analysis(hybrid, "fft_hybrid.jpg")


## You will provide the code below. Sigma1 and sigma2 are arbitrary 
## cutoff values for the high and low frequencies

#sigma1 = arbitrary_value_1
#sigma2 = arbitrary_value_2
#hybrid = hybrid_image(im1, im2, sigma1, sigma2)
#
#plt.imshow(hybrid)
#plt.show
#
### Compute and display Gaussian and Laplacian Pyramids
### You also need to supply this function
#N = 5 # suggested number of pyramid levels (your choice)
pyramids(hybrid, 5)