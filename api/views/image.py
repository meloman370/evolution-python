from rest_framework import generics
from api.serializers.image import ImageSerializer, ImageCreateSerializer
from api.models import Image

class ImageCreateView(generics.CreateAPIView):
    serializer_class = ImageCreateSerializer

class ImageUpdateView(generics.UpdateAPIView):
    serializer_class = ImageCreateSerializer
    queryset = Image.objects.all()

class ImageView(generics.RetrieveDestroyAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()

class ImageListView(generics.ListAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
