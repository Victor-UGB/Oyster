from django.urls import path
# from django.conf.urls import url
from . import views
from .views import UserPearlListView, FolderView, UploadContentContext, PearlListView, FolderListView, UserListView, PearlView, TagListView, PearlCreateView, altar_call_request, register_request, login_request, logout_request, password_reset_request, archive_list, pearl_audio

urlpatterns = [
    path("password_reset/", views.password_reset_request, name="password/password_reset"),
    path('auth/register/', views.register_request, name='register'),
    path('auth/login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('users/', UserListView.as_view(), name='users'),
    # path('users/', UserListView.as_view(), 'users_list'),
    path('tags/', TagListView.as_view(), name='tags'),
    path('folder/list', FolderListView.as_view(), name='folders'),
    path('folder/<uuid:id>/', FolderView.as_view(), name="folder_update"),
    
    # path('pearl/<uuid:id>/', PearlDetailView.as_view(), name='pearl_detail'),

    # path('pearl/<int:pk>/podcast/', views.pearl_audio, name='pearl_audio'),
    # path('archive/<int:id>/', views.archive_pearl, name='archive_pearl'),
    # path('archive/', views.archive, name='archive'),
    path('pearl/<uuid:id>/', PearlView.as_view(), name='home_list'),
    path('pearl/create/', PearlCreateView.as_view(), name="create_pearl"),
    path('pearl/list/', PearlListView.as_view(), name="list_pearl"),
    path('pearl/update_context/<uuid:id>/', UploadContentContext.as_view(), name="content_context"),
    path('pearls/<str:username>/', UserPearlListView.as_view(), name="user_pearls"),
    # url(r'pearl/<int:pk>/podcast/$', views.pearl_audio, name='pearl_audio'),
    # url(r'(?P<id>\d+)/archived/$', views.archive_pearl, name='archive_pearl'),
    # url(r'archived/$', views.archive_list, name='archive_list'),
    # url(r'altar_call/$', views.altar_call_request, name='altar_call'),

]


