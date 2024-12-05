import io
from PIL import Image
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse, StreamingResponse

router = APIRouter()

@router.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        return JSONResponse(status_code=400, content={"detail": "Uploaded file is not an image"})

    try:
        # Load the image using Pillow
        image = Image.open(file.file)

        # Save the image to WebP with near-lossless compression
        compressed_image_io = io.BytesIO()
        image.save(compressed_image_io, format="WEBP", quality=95, method=6)  # High quality, slow compression
        compressed_image_io.seek(0)

        # Return the compressed image
        return StreamingResponse(compressed_image_io, media_type="image/webp")

    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": "Image processing failed", "error": str(e)})
