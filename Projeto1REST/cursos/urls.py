from .views import CursoAPIView, AvaliacaoAPIView
from django.urls import path

urlpatterns=[
    #ENDPOINTS DE ACORDO COM A NOMENCLATURA
    path('cursos/',CursoAPIView.as_view(),name='cursos'),
    path('avaliacoes/',AvaliacaoAPIView.as_view(), name='avaliacoes')
]