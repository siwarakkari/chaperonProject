from django.urls import path
from . import views, viewsW

urlpatterns = [
    path('api/transcriptions/', views.get_transcription_summary, name='get_transcription_summary'),
]