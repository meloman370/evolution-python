from rest_framework import generics
from api.serializers.block import BlockSerializer, BlockCreateSerializer
from api.models import Block

class BlockCreateView(generics.CreateAPIView):
    serializer_class = BlockCreateSerializer

class BlockUpdateView(generics.UpdateAPIView):
    serializer_class = BlockCreateSerializer
    queryset = Block.objects.all()

class BlockView(generics.RetrieveDestroyAPIView):
    serializer_class = BlockSerializer
    queryset = Block.objects.all()

class BlockListView(generics.ListAPIView):
    serializer_class = BlockSerializer
    queryset = Block.objects.order_by('weight')
