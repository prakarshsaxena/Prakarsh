from . import views
from django.urls import path

app_name='music'

urlpatterns = [

    path('<int:album_id>/', views.detail, name='detail'),
    path('', views.index, name= 'index'),
    path('<int:album_id>/favorite/', views.favorite, name='favorite'),

]
