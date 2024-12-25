from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'tracks'
urlpatterns = [
    path('list/', views.music_list, name='list'),
    path('detail/<int:pk>/', views.music_detail, name='detail'),
    path('create/', views.music_create, name='create'),
    path('update/<int:pk>/', views.music_update, name='update'),
    path('delete/<int:pk>/', views.music_del_confirm, name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
