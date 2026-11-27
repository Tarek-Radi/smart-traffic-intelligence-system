"""
Unit tests for video reading utilities.

Tests:
    Reading video frames.
    Frame shape and data type.
    Invalid video source handling.
"""

import cv2
import numpy as np
import pytest

from cv_core.video.reader import read_frames


@pytest.fixture
def sample_video(tmp_path):
    """Create a temporary video containing five frames."""
    video_path = tmp_path / "sample.mp4"

    writer = cv2.VideoWriter(
        str(video_path),
        cv2.VideoWriter_fourcc(*"mp4v"),
        25,
        (64, 64),
    )

    try:
        if not writer.isOpened():
            pytest.fail("Could not create test video.")

        for _ in range(5):
            frame = np.zeros((64, 64, 3), dtype=np.uint8)
            writer.write(frame)
    finally:
        writer.release()

    return video_path


def test_frame_count(sample_video):
    frames = list(read_frames(sample_video))

    assert len(frames) == 5


def test_frame_properties(sample_video):
    for frame in read_frames(sample_video):
        assert frame.shape == (64, 64, 3)
        assert frame.dtype == np.uint8


def test_invalid_source(tmp_path):
    with pytest.raises(RuntimeError):
        list(read_frames(tmp_path / "missing.mp4"))