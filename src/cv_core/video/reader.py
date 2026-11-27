"""
Video reading utilities.

Functions:
    read_frames: Stream video frames sequentially.
"""

from collections.abc import Iterator
from pathlib import Path

import cv2
import numpy as np


def read_frames(
    source: str | Path | int,
) -> Iterator[np.ndarray]:
    """Yield video frames from a file or camera."""

    if isinstance(source, Path):
        source = str(source)

    cap = cv2.VideoCapture(source)

    try:
        if not cap.isOpened():
            raise RuntimeError(f"Could not open source: {source}")

        while True:
            ret, frame = cap.read()

            if not ret:
                break

            yield frame

    finally:
        cap.release()