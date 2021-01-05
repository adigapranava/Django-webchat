from django.urls import path, include
from django.conf import settings
from . import views
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='chat-home'),
    # path('allposts/', views.allposts, name='pcube-posts'),
    path('chat/<int:pk>/', views.chat, name='chat-page'),
    path('chat/msgs/<int:pk>/', views.chat_messages, name='chat-msgs-page'),
    path('chat/latest_msgs/<int:pk>/', views.latest_chat_messages, name='latest-chat-msgs-page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)