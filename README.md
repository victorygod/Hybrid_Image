# Overview

The goal of this part of the assignment is to create hybrid images using the approach described in the SIGGRAPH 2006 paper by Oliva, Torralba, and Schyns. Hybrid images are static images that change in interpretation as a function of the viewing distance. The basic idea is that high frequency tends to dominate perception when it is available, but, at a distance, only the low frequency (smooth) part of the signal can be seen. By blending the high frequency portion of one image with the low-frequency portion of another, you get a hybrid image that leads to different interpretations at different distances.

# Method

I use a a standard 2D Gaussian filter to get the low-pass information. Then I use another standard 2D Gaussian filter to be substracted by the original image and get the high-pass information.

To get the hybrid image, I average the two information.

# Best result

 
![hybrid.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/gray/output0.jpg)

# Pyramids
 
 
![hybrid.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/gray/output0.jpg)
![hybrid.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/gray/output1.jpg)
![hybrid.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/gray/output2.jpg)
![hybrid.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/gray/output3.jpg)
![hybrid.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/gray/output4.jpg)

## Frequency analysis


### the original two images:

 
![hybrid_fft.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/gray/cat.jpg)
![hybrid_fft.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/gray/dog.jpg)

### hybrid image:

 
![hybrid_fft.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/gray/fft_hybrid.jpg)

### img1:


![hybrid_fft.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/gray/fft_img1.jpg)

### filtered img1:

 
![hybrid_fft.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/gray/filtered_img1.jpg)
![hybrid_fft.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/gray/fft_img1_filtered.jpg)

The cutoff-frequency I choose for img1 is 10 as the variance of the Gaussian filter.

Img1 is supposed to reserve the high-pass information. From the frequncy image you can see high frequncy information is reserved. From the filtered image you can see there is mainly edge information.

### img2:

 
![hybrid_fft.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/gray/fft_img2.jpg)

### filtered img2:

 
![hybrid_fft.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/gray/filtered_img2.jpg)
![hybrid_fft.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/gray/fft_img2_filtered.jpg)

The cutoff-frequency I choose for img2 is 4 as the variance of the Gaussian filter.

Img2 is supposed to reserve the low-pass information. From the frequncy image you can see low frequncy information is reserved. From the filtered image you can see the image is blured.

## Other results


![output_colored.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/other/output0.jpg)
![output_colored.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/other/output1.jpg)
![output_colored.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/other/output2.jpg)
![output_colored.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/other/output3.jpg)
![output_colored.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/other/output4.jpg)

origine images:

![output_colored.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/other/1.jpg)
![output_colored.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/other/2.jpg)


You can see clearly one image has one eye and the other has two eyes. And the hybrid images will transform from two eyes to one eyes.

# Bells & Whistles (Extra Points)

 
## colored images:

 
![output_colored.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/colored/output0.jpg)
![output_colored.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/colored/output1.jpg)
![output_colored.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/colored/output2.jpg)
![output_colored.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/colored/output3.jpg)
![output_colored.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/colored/output4.jpg)

Using color for both of the high-frequency component and the low-frequency component will enhance the performance.
