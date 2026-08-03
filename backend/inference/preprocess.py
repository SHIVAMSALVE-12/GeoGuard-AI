"""
Image Preprocessing for Inference
"""

from PIL import Image
import torchvision.transforms as transforms

from backend.config.segformer_config import IMAGE_SIZE

transform = transforms.Compose([
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
    transforms.ToTensor(),
])


def preprocess_image(image_path):

    original_image = Image.open(image_path).convert("RGB")

    resized_image = original_image.resize(
        (IMAGE_SIZE, IMAGE_SIZE)
    )

    tensor = transform(original_image)

    return original_image, resized_image, tensor