import os
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.responses import JSONResponse

from PIL import Image
import io
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

router = APIRouter()

# Directory where the uploaded images will be saved
STATIC_DIR = os.path.join(os.getcwd(), "static")

# Ensure the 'static' directory exists
os.makedirs(STATIC_DIR, exist_ok=True)

# Create a FastAPI app instance
app = FastAPI()

# Serve static files for the 'static' directory
app.mount("/static", StaticFiles(directory="static"), name="static")

@router.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    # Ensure that the uploaded file is an image
    if not file.content_type.startswith("image/"):
        return JSONResponse(status_code=400, content={"detail": "Uploaded file is not an image"})

    # Read the image file into memory
    image = Image.open(file.file)

    # Compress the image (resize or adjust quality)
    compressed_image_io = io.BytesIO()
    image.save(compressed_image_io, format="JPEG", quality=85)  # Compressing the image to 85% quality
    compressed_image_io.seek(0)  # Reset pointer to the start of the BytesIO object

    # Return the compressed image as a response
    return StreamingResponse(compressed_image_io, media_type="image/jpeg")

