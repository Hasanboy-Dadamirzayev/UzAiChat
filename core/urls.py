# core/urls.py yoki project/urls.py
from django.contrib import admin
from django.urls import path
from main.views import chat_view


urlpatterns = [
    path('admin/', admin.site.urls),         # HTML sahifa
    path('chat/', chat_view),    # JavaScript orqali POST so‘rov
]
