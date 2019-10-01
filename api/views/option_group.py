from rest_framework import generics
from api.serializers.option_group import OptionGroupSerializer, CategoryOptionGroupSerializer
from api.serializers.option_group import OptionGroupCreateSerializer
from api.models import OptionGroup

class OptionGroupCreateView(generics.CreateAPIView):
    serializer_class = OptionGroupCreateSerializer

class OptionGroupView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OptionGroupSerializer
    queryset = OptionGroup.objects.all()

class OptionGroupListView(generics.ListAPIView):
    serializer_class = OptionGroupSerializer
    queryset = OptionGroup.objects.all()

class CategoryOptionGroupCreateView(generics.CreateAPIView):
    serializer_class = CategoryOptionGroupSerializer
