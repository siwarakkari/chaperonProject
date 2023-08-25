from django.urls import path
from . import views, viewsW

urlpatterns = [
    # path('trans/', views.transcribe),
    # path('real', viewsW.real_time_transcription, name='transcribe_audio_r'),
    path('api/transcriptions/', views.get_transcription_summary, name='get_transcription_summary'),
    # path('gett', viewsW.get_transcription),
]