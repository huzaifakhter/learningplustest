from django.urls import path
from .views import save_text, get_texts

urlpatterns = [
    path('save/', save_text, name='save_text'),
    path('texts/', get_texts, name='get_texts'),
]
