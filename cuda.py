"""This module demonstrates grayscale conversion of an image using CPU and GPU (CUDA) implementations."""


__authors__ = "Matej Bredik"\
              "Mgr. Ing. Matúš Jókay, PhD., " \
              "Tomáš Vavro"
__email__ = "xbredik@stuba.sk"
__licence__ = "MIT"


import time
import matplotlib.pyplot as plt
import numpy as np
from numba import cuda


def transform_to_grayscale_cpu(image):
    """
    Convert image to grayscale using the luminosity method.

    Arguments:
        image: RGB image as a numpy array.

    Returns:
        numpy array: Grayscale image as a numpy array.
    """
    red = image[:, :, 0]
    green = image[:, :, 1]
    blue = image[:, :, 2]
    grayscale = 0.21 * red + 0.72 * green + 0.07 * blue
    return np.uint8(grayscale)


@cuda.jit
def transform_to_grayscale_cuda(image, grayscale):
    """
    Convert image to grayscale using the luminosity method.

    Arguments:
        image: RGB image as a numpy array.
        grayscale: Output grayscale image as a numpy array.
    """
    row, col = cuda.grid(2)
    if row < image.shape[0] and col < image.shape[1]:
        red = image[row, col, 0]
        green = image[row, col, 1]
        blue = image[row, col, 2]
        grayscale[row, col] = 0.21 * red + 0.72 * green + 0.07 * blue


def transform_to_grayscale(image):
    """
    Convert image to grayscale using CUDA.

    Arguments:
        image: RGB image as a numpy array.

    Returns:
        numpy array: Grayscale image as a numpy array.
    """
    grayscale = np.empty(image.shape[:2], dtype=np.uint8)
    tpb = (16, 16)
    bpg_x = (image.shape[0] + tpb[0] - 1) // tpb[0]
    bpg_y = (image.shape[1] + tpb[1] - 1) // tpb[1]
    bpg = (bpg_x, bpg_y)

    d_image = cuda.to_device(image)
    d_grayscale = cuda.to_device(grayscale)

    transform_to_grayscale_cuda[bpg, tpb](d_image, d_grayscale)

    d_grayscale.copy_to_host(grayscale)

    return grayscale


def zad():
    """
    Perform grayscale conversion on the input image using both CPU and GPU,
    and measure the execution time for comparison.
    """
    pixels = plt.imread("pic2.jpg")

    # CPU
    start_time_cpu = time.time()
    new_pixels_cpu = transform_to_grayscale_cpu(pixels)
    end_time_cpu = time.time()

    # GPU
    start_time_gpu = time.time()
    new_pixels_gpu = transform_to_grayscale(pixels)
    end_time_gpu = time.time()

    plt.imsave("pic2gray_cpu.jpg", new_pixels_cpu, cmap='gray', format='jpg')
    plt.imsave("pic2gray_gpu.jpg", new_pixels_gpu, cmap='gray', format='jpg')
    print("CPU Time:", end_time_cpu - start_time_cpu)
    print("GPU Time:", end_time_gpu - start_time_gpu)


if __name__ == "__main__":
    # print(cuda.is_available())  # add ;NUMBA_ENABLE_CUDASIM=1 to env vars
    zad()
