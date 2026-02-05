from django.urls import path
from django.conf.urls import url
from . import views
from .views import PearlView, TagListView, PearlCreateView, PearlDetailView, altar_call_request, register_request, login_request, logout_request, password_reset_request, archive_list, pearl_audio

urlpatterns = [
    path("password_reset/", views.password_reset_request, name="password/password_reset"),
    path('auth/register/', views.register_request, name='register'),
    path('auth/login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    # path('users/', UserListView.as_view(), 'users_list'),
    path('tags/', TagListView.as_view(), name='tag_list '),
    
    path('pearl/<int:pk>/', PearlDetailView.as_view(), name='pearl_detail'),

    # path('pearl/<int:pk>/podcast/', views.pearl_audio, name='pearl_audio'),
    # path('archive/<int:id>/', views.archive_pearl, name='archive_pearl'),
    # path('archive/', views.archive, name='archive'),
    path('pearl/<int:pk>', PearlView.as_view(), name='home_list'),
    path('pearl/create', PearlCreateView.as_view(), name="create_pearl"),
    # url(r'pearl/<int:pk>/podcast/$', views.pearl_audio, name='pearl_audio'),
    url(r'(?P<id>\d+)/archived/$', views.archive_pearl, name='archive_pearl'),
    url(r'archived/$', views.archive_list, name='archive_list'),
    url(r'altar_call/$', views.altar_call_request, name='altar_call'),
    # path('', PearlListView.as_view(), name='home'),
    # path('', PreviousPostView.as_view(), name='home'),
]


