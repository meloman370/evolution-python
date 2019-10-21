from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers.slider_block import SliderBlockSerializer
from api.serializers.slider_block import SliderBlockCreateSerializer
from api.serializers.slider_block import SliderProductSerializer
from api.models import SliderBlock, SliderProduct

class SliderBlockCreateView(generics.CreateAPIView):
    serializer_class = SliderBlockCreateSerializer

class SliderBlockUpdateView(generics.UpdateAPIView):
    serializer_class = SliderBlockCreateSerializer
    queryset = SliderBlock.objects.all()

class SliderBlockView(generics.RetrieveDestroyAPIView):
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

class SliderProductDeleteProducts(APIView):
    def delete(self, request, pk):
        """
        Delete all products in slider
        """
        slider_products = SliderProduct.objects.filter(slider=pk)
        slider_products.delete()
        return Response(status=status.HTTP_200_OK)
