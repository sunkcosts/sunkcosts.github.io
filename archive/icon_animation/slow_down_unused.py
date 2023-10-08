# slowing down makes effect imperceptible

from rich.progress import track
from PIL import Image, ImageSequence


def slow_down_gif(input_path, output_path, slowdown_factor):
    """
    Increase the duration of each frame to slow down the GIF.
    """
    with Image.open(input_path) as img:
        frames = [frame.copy() for frame in ImageSequence.Iterator(img)]

        # Retrieve original frame durations and multiply by slowdown factor
        durations = [
            (frame.info["duration"] * slowdown_factor)
            for frame in track(ImageSequence.Iterator(img))
        ]

        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            loop=img.info.get("loop", 0),
            duration=durations,
        )
