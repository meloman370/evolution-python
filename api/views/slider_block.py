from rest_framework import generics
from api.serializers.slider_block import SliderBlockSerializer, SliderBlockCreateSerializer, SliderProductSerializer
from api.models import SliderBlock, SliderProduct

class SliderBlockCreateView(generics.CreateAPIView):
  serializer_class = SliderBlockCreateSerializer

class SliderBlockView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = SliderBlockSerializer
  queryset = SliderBlock.objects.all()

class SliderBlockListView(generics.ListAPIView):
  serializer_class = SliderBlockSerializer
  queryset = SliderBlock.objects.all()

class SliderProductCreateView(generics.CreateAPIView):
  serializer_class = SliderProductSerializer

class SliderProductView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = SliderProductSerializer
  queryset = SliderProduct.objects.all()

class SliderProductListView(generics.ListAPIView):
  serializer_class = SliderProductSerializer
  queryset = SliderProduct.objects.all()
