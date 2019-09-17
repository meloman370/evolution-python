from PIL import Image as Img
from io import BytesIO
from webp import WebPPicture, WebPConfig, WebPPreset, WebPData
from django.core.files.uploadedfile import InMemoryUploadedFile
from os import path

def getWebpImage(origin_image):
  image = Img.open(origin_image)
  picture = WebPPicture.from_pil(image)
  config = WebPConfig.new()
  picture = picture.encode(config).decode()
  pilImage = Img.fromarray(picture)
  webpImage = BytesIO()
  pilImage.save(webpImage, format="WebP")
  filename = path.splitext(origin_image.name)[0]
  return InMemoryUploadedFile(webpImage, None, "%s.webp" %filename, 'image/webp', picture.size, None)

def getThumbImage(origin_image, size):
  image = Img.open(origin_image)
  image.thumbnail((size, size), Img.ANTIALIAS)
  thumbnail_image = BytesIO()
  image.save(thumbnail_image, format=image.format)
  return InMemoryUploadedFile(thumbnail_image, None, origin_image.name, 'image/%s' %image.format, origin_image.size, None)