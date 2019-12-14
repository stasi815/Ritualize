from rest_framework.serializers import ModelSerializer

from rituals.models import Ceremony

class CeremonySerializer(ModelSerializer):
    class Meta:
        model = Ceremony
        fields = '__all__'
    