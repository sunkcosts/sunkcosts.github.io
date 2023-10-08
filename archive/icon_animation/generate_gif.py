from rich.progress import track
from pathlib import Path
from PIL import Image, ImageDraw, ImageSequence


def resize_gif(input_path, output_path, base_width):
    """
    Resize the frames of a GIF and save to output path
    """
    with Image.open(input_path) as img:
        # Calculate the new height maintaining the aspect ratio
        w_percent = base_width / float(img.width)
        h_size = int(float(img.height) * float(w_percent))

        frames = [
            frame.copy().resize((base_width, h_size), Image.LANCZOS)
            for frame in track(ImageSequence.Iterator(img))
        ]
        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            loop=img.info.get("loop", 0),
            duration=img.info["duration"],
        )


def crop_circle(image, edge):
    """
    Crop a square image into a circle
    """
    # Ensure image is square
    assert image.width == image.height, "Image must be square"

    size = image.width
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0 + edge, 0 + edge, size - edge, size - edge), fill=255)

    result = Image.composite(image, Image.new("RGBA", image.size, (0, 0, 0, 0)), mask)
    return result


def process_gif(input_path, output_path, edge):
    """
    Open a GIF, and save each frame as a cropped circle image
    """
    with Image.open(input_path) as img:
        frames = [
            crop_circle(frame.copy().convert("RGBA"), edge)
            for frame in track(ImageSequence.Iterator(img))
        ]
        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            loop=img.info["duration"],
            duration=img.info["duration"],
        )


if __name__ == "__main__":
    print("Resize gif...")
    resize_gif(
        Path(__file__).parent / "data" / "03.unoptimized_output.gif",
        Path(__file__).parent / "data" / "04.output_resized.gif",
        256,
    )
    print("Crop gif to circle...")
    input_gif_path = Path(__file__).parent / "data" / "04.output_resized.gif"
    output_gif_path = Path(__file__).parent / "data" / "05.final_output_small.gif"
    process_gif(input_gif_path, output_gif_path, 5)
