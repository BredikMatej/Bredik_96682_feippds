# Assignment 05 - CUDA
## About assignment
CUDA (Compute Unified Device Architecture) is a parallel computing platform and programming model created by NVIDIA.
CUDA enables developers to use the power of NVIDIA GPUs for general-purpose computing tasks, rather than being 
limited to graphics-related calculations. CUDA provides a programming model and a set of tools that allow developers 
to write high-performance parallel code for GPUs. It allows for massive parallelism by utilizing hundreds or even 
thousands of cores available on modern GPUs. This parallelism can significantly accelerate computationally intensive 
tasks, such as scientific simulations, data analysis, machine learning, and image processing.
 
The goal of our assignment was to load images in jpg format, convert them to grayscale using GPU and CPU method, save 
the converted images to new files, and compare the conversion times.[1,2]
## How to run
All you need to successfully run this implementation is to install Numba from which you will need cuda, install NumPy 
and matplotlib.
This can be done by running `pip install numba`, `pip install numpy` and `pip install matplotlib` in the terminal.
Check if you have CUDA installed by running `nvcc --version` in the terminal. This command should display the 
CUDA version if it's installed. If CUDA is not installed, you can download and install it from the NVIDIA website
(https://developer.nvidia.com/cuda-downloads). We used `release 11.8`. 
If you're using PyCharm you should also Edit environment variables and add `NUMBA_ENABLE_CUDASIM` and set it to 
value `1`.
Finally, in command line write `set NUMBA_ENABLE_CUDASIM=1` on Windows and `export NUMBA_ENABLE_CUDASIM=1` on Linux.

## Implementation
This module provides implementations of grayscale conversion using both CPU and GPU methods, allowing for a 
performance comparison between the two.  
The functions for grayscale conversions are `transform_to_grayscale_cpu` and `transform_to_grayscale_cuda`. Both 
functions use "luminosity method". It calculates the grayscale intensity of each pixel based on the weighted average 
of its red, green, and blue color channels. The formula for conversion is `0.21 * red + 0.72 * green + 0.07 * blue` 
which should be specifically formula BT.709 according to [3]. While both of these functions do the same 
`transform_to_grayscale_cuda` is a CUDA kernel, and it utilizes parallel execution to process multiple pixels 
simultaneously. The CUDA kernel is invoked using specific grid and block dimensions to distribute the workload 
across the GPU cores efficiently.   
The `transform_to_grayscale` function acts as a wrapper that invokes the CUDA kernel for grayscale conversion. 
It sets up the necessary data structures, transfers the image data to the GPU memory, launches the CUDA kernel,
and retrieves the grayscale image back to the CPU memory. 
The `zad` function demonstrates the usage of both CPU and GPU grayscale conversion methods. It loads an image, 
performs grayscale conversion using the CPU and the GPU implementation, measures the both execution times, and saves 
both grayscale images. This allows for a comparison of the execution times between the CPU and GPU approaches. [1,2,3]

During testing, we created grayscale conversions of different images to evaluate the methods. 
Here are examples of the original images and their grayscale versions.

<img src="https://i.imgur.com/jVIHyp8.jpeg" width="500"  alt="house"/> <img src="https://i.imgur.com/7JVaiIg.jpeg" width="500"  alt="gray house"/>
<img src="https://i.imgur.com/cP5w3in.jpeg" width="500"  alt="dog"/> <img src="https://i.imgur.com/TYwRWFr.jpeg" width="500"  alt="gray dog"/>
<img src="https://i.imgur.com/y5Ln2BP.jpeg" width="500"  alt="car"/> <img src="https://i.imgur.com/7mjkYH0.jpeg" width="500"  alt="gray car"/>


## Testing
When testing this implementation we used multiple images of different sizes. The minimum `Image size`we tested was 
200x200, while the maximum value was 8000x8000. The shortest time for CPU conversion was 0.001s and the longest was 
0.921035s. For GPU the time varied anywhere from 0.196227s to 0.321052s. You can see all the different image sizes and 
their respective conversion times in the table below.

| Num | Image size | CPU time  | GPU time |
|-----|------------|-----------|----------|
| 1.  | 480x400    | 0.003999  | 0.213853 |
| 2.  | 1200x800   | 0.013556  | 0.223498 |
| 3.  | 3024x4032  | 0.171679  | 0.242554 |
| 4.  | 500x500    | 0.004001  | 0.230058 |
| 5.  | 1800x1200  | 0.034000  | 0.229073 |
| 6.  | 728x410    | 0.004082  | 0.222326 |
| 7.  | 1230x768   | 0.014440  | 0.223133 |
| 8.  | 1024x768   | 0.012417  | 0.221682 |
| 9.  | 800x537    | 0.005999  | 0.215017 |
| 10. | 200x200    | 0.001000  | 0.214707 |
| 11. | 1920x1080  | 0.043929  | 0.223356 |
| 12. | 1000x556   | 0.008018  | 0.229362 |
| 13. | 2560x1080  | 0.041092  | 0.222760 |
| 14. | 6000x4000  | 0.375724  | 0.258955 |
| 15. | 8000x4000  | 0.466603  | 0.287658 |
| 16. | 1600x1598  | 0.039265  | 0.224300 |
| 17. | 723x386    | 0.003998  | 0.216446 |
| 18. | 320x390    | 0.002000  | 0.196227 |
| 19. | 8000x8000  | 0.921035  | 0.321052 |
| 20. | 400x400    | 0.002750  | 0.209961 |

And these were the Average times

| Average CPU time | Average GPU time |
|------------------|------------------|
| 0.0676549        | 0.2316787        | 

## Conclusion
While testing both grayscale implementations on multiple images showed us that average CPU time of conversion is faster 
than the average GPU time, we could observe that when the image size was larger, the GPU implementation using CUDA 
started to showcase its advantage by outperforming the CPU implementation. 

In conclusion, utilizing CUDA and GPU computing can offer substantial speed advantages over traditional CPU-based 
implementations for large-scale image processing.


## Sources - documentation
[1] https://blogs.nvidia.com/blog/2012/09/10/what-is-cuda-2/  
[2] https://chat.openai.com  
[3] https://tannerhelland.com/2011/10/01/grayscale-image-algorithm-vb6.html  
## Sources - code
https://nyu-cds.github.io/python-numba/05-cuda/  
https://blog.finxter.com/how-to-convert-an-image-from-rgb-to-grayscale-in-python/  
https://chat.openai.com  