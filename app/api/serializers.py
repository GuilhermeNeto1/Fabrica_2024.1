from rest_framework.serializers import ModelSerializer
from ..models import ViaCep

class ViaCepSerializer(ModelSerializer):
    class Meta:
        model = ViaCep
        fields = '__all__'