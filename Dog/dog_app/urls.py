from django.urls import path, re_path
from . import views
urlpatterns = [

    path('', views.index, name='index'),
    path('login', views.auth_login, name = 'auth_login'),
    path('register', views.registration, name='register'),
    path('create', views.create),
    path('edit/<int:dog_id>', views.edit),
    path('edit/update/<int:id>', views.update),
    path('delete/<int:dog_id>', views.delete),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.activate,
            name='activate'),
]
