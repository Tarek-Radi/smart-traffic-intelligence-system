"""
Unit tests for image enhancement functions.

Tests:
    Brightness and contrast adjustment.
    Histogram equalization.
    CLAHE enhancement.
    Input validation and edge cases.
"""


"""Unit tests for image enhancement utilities."""

import numpy as np
import pytest

from cv_core.preprocessing.enhancement import (
    adjust_brightness_contrast,
    apply_clahe,
    equalize_histogram,
)


@pytest.fixture
def sample_image() -> np.ndarray:
    """Create a sample grayscale image."""
    return np.array(
        [[0, 50], [100, 250]],
        dtype=np.uint8,
    )


def test_identity_transformation(sample_image):
    result = adjust_brightness_contrast(sample_image)
    np.testing.assert_array_equal(result, sample_image)


def test_increase_brightness(sample_image):
    result = adjust_brightness_contrast(
        sample_image, beta=50
    )

    expected = np.array(
        [[50, 100], [150, 255]],
        dtype=np.uint8,
    )

    np.testing.assert_array_equal(result, expected)


def test_decrease_brightness(sample_image):
    result = adjust_brightness_contrast(
        sample_image, beta=-50
    )

    expected = np.array(
        [[0, 0], [50, 200]],
        dtype=np.uint8,
    )

    np.testing.assert_array_equal(result, expected)


@pytest.mark.parametrize(
    "func",
    [
        adjust_brightness_contrast,
        equalize_histogram,
        apply_clahe,
    ],
)
def test_output_properties(func, sample_image):
    result = func(sample_image)

    assert result.shape == sample_image.shape
    assert result.dtype == np.uint8


@pytest.mark.parametrize(
    "func",
    [
        adjust_brightness_contrast,
        equalize_histogram,
        apply_clahe,
    ],
)
def test_empty_image(func):
    image = np.empty((0, 0), dtype=np.uint8)

    with pytest.raises(ValueError):
        func(image)


@pytest.mark.parametrize(
    "func",
    [equalize_histogram, apply_clahe],
)
def test_invalid_color_image(func):
    image = np.zeros((10, 10, 3), dtype=np.uint8)

    with pytest.raises(ValueError):
        func(image)