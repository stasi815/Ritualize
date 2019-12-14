from django.urls import path

from api.views import CeremonyList, CeremonyDetail

urlpatterns = [
    path('', CeremonyList.as_view(), name='ceremony_list'),
    path('rituals/<str:slug>/', CeremonyDetail.as_view(), name='ceremony_detail')
]