from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers.option import OptionSerializer, ProductOptionSerializer
from api.models import Option, ProductOptions

class OptionCreateView(generics.CreateAPIView):
    serializer_class = OptionSerializer

class OptionView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OptionSerializer
    queryset = Option.objects.all()

class OptionListView(generics.ListAPIView):
    serializer_class = OptionSerializer
    queryset = Option.objects.all()

class ProductOptionsCreateView(generics.CreateAPIView):
    serializer_class = ProductOptionSerializer

class ProductOptionDeleteByProduct(APIView):
    def delete(self, request, pk):
        """
        Delete all by product
        """
        product_option = ProductOptions.objects.filter(product=pk)
        product_option.delete()
        return Response(status=status.HTTP_200_OK)
