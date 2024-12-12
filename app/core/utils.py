from fastapi import UploadFile
from PIL import Image
import io

def process_image_to_webp(file: UploadFile, quality: int = 95, method: int = 6) -> io.BytesIO:
    """
    Process an uploaded image file and compress it to WebP format.
    """
    try:
        # Load the image using Pillow
        image = Image.open(file.file)
        compressed_image_io = io.BytesIO()

        # Save the image to WebP with specified compression settings
        image.save(compressed_image_io, format="WEBP", quality=quality, method=method)
        compressed_image_io.seek(0)

        return compressed_image_io

    except Exception as e:
        raise ValueError(f"Image processing failed: {str(e)}")