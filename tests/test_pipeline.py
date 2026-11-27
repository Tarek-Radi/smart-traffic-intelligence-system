"""
Unit tests for the preprocessing pipeline.

Tests:
    Empty transformation pipeline.
    Frame resizing.
    Multiple sequential transformations.
    Transformation execution order.
"""

import cv2
import numpy as np
import pytest

from cv_core.preprocessing.pipeline import preprocess_frame


@pytest.fixture
def sample_frame() -> np.ndarray:
    """Create a sample color frame."""
    return np.full((100, 200, 3), 100, dtype=np.uint8)


def test_empty_pipeline(sample_frame):
    result = preprocess_frame(sample_frame, [])

    np.testing.assert_array_equal(result, sample_frame)


def test_resize(sample_frame):
    transforms = [
        lambda img: cv2.resize(img, (50, 50)),
    ]

    result = preprocess_frame(sample_frame, transforms)

    assert result.shape == (50, 50, 3)


def test_multiple_transforms(sample_frame):
    transforms = [
        lambda img: cv2.resize(img, (50, 50)),
        lambda img: cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
    ]

    result = preprocess_frame(sample_frame, transforms)

    assert result.shape == (50, 50)
    assert result.dtype == np.uint8


def test_transformation_order(sample_frame):
    transforms = [
        lambda img: img + 10,
        lambda img: img * 2,
    ]

    result = preprocess_frame(sample_frame, transforms)

    assert np.all(result == 220)