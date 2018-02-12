# Overview

The goal of this part of the assignment is to create hybrid images using the approach described in the SIGGRAPH 2006 paper by Oliva, Torralba, and Schyns. Hybrid images are static images that change in interpretation as a function of the viewing distance. The basic idea is that high frequency tends to dominate perception when it is available, but, at a distance, only the low frequency (smooth) part of the signal can be seen. By blending the high frequency portion of one image with the low-frequency portion of another, you get a hybrid image that leads to different interpretations at different distances.

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

 
![hybrid_fft.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/gray/fft_img1_filtered.jpg)

### img2:

 
![hybrid_fft.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/gray/fft_img2.jpg)

### filtered img2:

 
![hybrid_fft.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/gray/fft_img2_filtered.jpg)

# Bells & Whistles (Extra Points)

 
## colored images:

 
![output_colored.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/colored/output0.jpg)
![output_colored.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/colored/output1.jpg)
![output_colored.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/colored/output2.jpg)
![output_colored.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/colored/output3.jpg)
![output_colored.jpg](https://github.com/victorygod/Hybrid_Image/blob/master/colored/output4.jpg)

Using color for both of the high-frequency component and the low-frequency component will enhance the performance.
