from rest_framework import generics
from api.serializers.option_group import OptionGroupSerializer
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

    def get_queryset(self):
        queryset = OptionGroup.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(machine_name=name)
        return queryset
