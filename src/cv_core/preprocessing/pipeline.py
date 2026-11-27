"""
Composable image preprocessing pipeline.

Functions:
    preprocess_frame: Apply sequential transformations to a frame.
"""

from collections.abc import Callable, Iterable

import numpy as np


def preprocess_frame(
    frame: np.ndarray,
    transforms: Iterable[Callable[[np.ndarray], np.ndarray]],
) -> np.ndarray:
    """Apply preprocessing transformations sequentially."""

    for transform in transforms:
        frame = transform(frame)

    return frame