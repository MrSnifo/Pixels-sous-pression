import io
from PIL import Image
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse, StreamingResponse
from ..core import process_image_to_webp


router = APIRouter()

@router.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        return JSONResponse(status_code=400, content={"detail": "Uploaded file is not an image"})

    try:
        # Process the image and compress it to WebP
        compressed_image = process_image_to_webp(file)
        return StreamingResponse(compressed_image, media_type="image/webp")

    except ValueError as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})
