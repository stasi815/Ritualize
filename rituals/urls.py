from django.urls import path
from rituals.views import CeremonyListView, CeremonyDetailView, CeremonyCreateView, CeremonyEditView, CeremonyDeleteView

urlpatterns = [
    path("", CeremonyListView.as_view(), name='ceremony-list-page'),
    path('new-ceremony/', CeremonyCreateView.as_view(), name='new-ceremony-page'),
    path('rituals/<str:slug>/', CeremonyDetailView.as_view(), name='ceremony-details-page'),
    path('rituals/<str:slug>/update', CeremonyEditView.as_view(), name= 'ceremony-update-page'),
    path('rituals/<str:slug>/delete', CeremonyDeleteView.as_view(), name= "ceremony-delete"),
]