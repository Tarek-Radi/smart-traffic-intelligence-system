"""
Image enhancement utilities.

Functions:
    adjust_brightness_contrast: Adjust brightness and contrast.
    equalize_histogram: Enhance global contrast.
    apply_clahe: Enhance local contrast.
"""

import cv2
import numpy as np


def adjust_brightness_contrast(
    image: np.ndarray,
    alpha: float = 1.0,
    beta: float = 0.0,
) -> np.ndarray:
    """
    Adjust image brightness and contrast.

    Args:
        image: Input uint8 image.
        alpha: Contrast scaling factor.
        beta: Brightness offset.

# Keep the original image unchanged
result = adjust_brightness_contrast(image)

# Increase brightness
result = adjust_brightness_contrast(image, beta=50)

# Increase contrast
result = adjust_brightness_contrast(image, alpha=1.5)

# Adjust both
result = adjust_brightness_contrast(
    image,
    alpha=1.5,
    beta=-50,
)

    Returns:
        Enhanced uint8 image.
    """
    if image.size == 0:
        raise ValueError("Input image must not be empty.")

    if image.dtype != np.uint8:
        raise ValueError("Input image must have uint8 dtype.")

    if not np.isfinite(alpha) or alpha < 0:
        raise ValueError("Alpha must be finite and non-negative.")

    if not np.isfinite(beta):
        raise ValueError("Beta must be finite.")

    adjusted = image.astype(np.float32) * alpha + beta
    np.clip(adjusted, 0, 255, out=adjusted)

    return np.rint(adjusted).astype(np.uint8)

def equalize_histogram(image: np.ndarray) -> np.ndarray:  #ً Wrapper Function
    """Enhance global contrast in a grayscale uint8 image."""

    if image.size == 0:
        raise ValueError("Input image must not be empty.")

    if image.dtype != np.uint8:
        raise ValueError("Input image must have uint8 dtype.")

    if image.ndim != 2:
        raise ValueError("Input image must be grayscale.")

    return cv2.equalizeHist(image)

def apply_clahe(                                            #ً Wrapper Function
    image: np.ndarray,
    clip_limit: float = 2.0,
    tile_grid_size: tuple[int, int] = (8, 8),
) -> np.ndarray:
    """Enhance local contrast in a grayscale uint8 image."""

    if image.size == 0:
        raise ValueError("Input image must not be empty.")

    if image.dtype != np.uint8:
        raise ValueError("Input image must have uint8 dtype.")

    if image.ndim != 2:
        raise ValueError("Input image must be grayscale.")

    clahe = cv2.createCLAHE(
        clipLimit=clip_limit,
        tileGridSize=tile_grid_size,
    )

    return clahe.apply(image)