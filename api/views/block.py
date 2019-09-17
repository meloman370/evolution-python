from rest_framework import generics
from api.serializers.block import BlockSerializer, BlockCreateSerializer
from api.models import Block

class BlockCreateView(generics.CreateAPIView):
  serializer_class = BlockCreateSerializer

class BlockView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = BlockSerializer
  queryset = Block.objects.all()

class BlockListView(generics.ListAPIView):
  serializer_class = BlockSerializer
  queryset = Block.objects.all()
