# from io import BytesIO
# from os import path
# from PIL import Image as Img
# from webp import WebPPicture, WebPConfig
# from django.core.files.uploadedfile import InMemoryUploadedFile

def get_webp_image(origin_image):
    pass
#     image = Img.open(origin_image)
#     picture = WebPPicture.from_pil(image)
#     config = WebPConfig.new()
#     picture = picture.encode(config).decode()
#     pil_image = Img.fromarray(picture)
#     webp_image = BytesIO()
#     pil_image.save(webp_image, format="WebP")
#     filename = path.splitext(origin_image.name)[0]
#     return InMemoryUploadedFile(webp_image, None, "%s.webp" %filename, 'image/webp', picture.size, None)

def get_thumb_image(origin_image, size):
    pass
#     image = Img.open(origin_image)
#     image.thumbnail((size, size), Img.ANTIALIAS)
#     thumbnail_image = BytesIO()
#     image.save(thumbnail_image, format=image.format)
#     return InMemoryUploadedFile(thumbnail_image, None, origin_image.name, 'image/%s' %image.format, origin_image.size, None)
