from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from rituals.models import Ceremony
from api.serializers import CeremonySerializer


class CeremonyList(APIView):
    def get(self, request):
        ceremonies = Ceremony.objects.all()[:20]
        data = CeremonySerializer(ceremonies, many=True).data
        return Response(data)

class CeremonyDetail(APIView):
    def get(self, request, pk):
        ceremony = get_object_or_404(Ceremony, slug=slug)
        data = CeremonySerializer(ceremony).data
        return Response(data)