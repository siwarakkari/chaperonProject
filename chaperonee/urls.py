from django.urls import path
from . import views, viewsW

urlpatterns = [
    path('trans/', views.transcribe),
    # path('real', viewsW.real_time_transcription, name='transcribe_audio_r'),
    # path('gett', viewsW.get_transcription),
]