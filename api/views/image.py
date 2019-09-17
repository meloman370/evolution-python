from rest_framework import generics
from api.serializers.image import ImageSerializer, ImageCreateSerializer
from api.models import Image
from api.helper import getWebpImage

class ImageCreateView(generics.CreateAPIView):
  serializer_class = ImageCreateSerializer

class ImageView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = ImageSerializer
  queryset = Image.objects.all()

class ImageListView(generics.ListAPIView):
  serializer_class = ImageSerializer
  queryset = Image.objects.all()
