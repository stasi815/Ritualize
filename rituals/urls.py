from django.urls import path
from rituals.views import CeremonyListView, CeremonyDetailView, CeremonyCreateView

urlpatterns = [
    path("", CeremonyListView.as_view(), name='ceremony-list-page'),
    path('new-ceremony/', CeremonyCreateView.as_view(), name='new-ceremony-page'),
    path('<str:slug>/', CeremonyDetailView.as_view(), name='ceremony-details-page'),
]