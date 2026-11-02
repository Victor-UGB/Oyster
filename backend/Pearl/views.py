
# Pearl app Import
from .models import Post, User, Tag, Folder
from .serializers import ContentContextSerializer, FolderSerializer, PasswordResetSerializer, UserSerializers, PostSerializer, RegisterUserSerializer, TagListSerializer, LoginSerializer


# Rest Framework Imports
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.parsers import MultiPartParser, FormParser
from drf_spectacular.utils import extend_schema, OpenApiParameter


# Django Imports
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.template import loader
from django.urls import reverse, reverse_lazy
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.core.mail import send_mail, BadHeaderError
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, Http404, request
# from django.contrib.auth.models import User
from django.template.loader import render_to_string
import datetime
from django.db.models.query_utils import Q
from django.db.models import F
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.urls import reverse
from datetime import date, datetime, time, timedelta,timezone
import os
from  config import settings


# Create your views here.

""" Insert your art here """

# Registeration API

class RegisterUserView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer = RegisterUserSerializer


class TagListView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TagListSerializer
    queryset =  Tag.objects.all()


class FolderListView(ListCreateAPIView):
    serializer_class = FolderSerializer
    queryset = Folder.objects.all()
    permission_classes = [IsAuthenticated]


class FolderView(RetrieveUpdateAPIView):
    lookup_field = "id"
    serializer_class =FolderSerializer
    queryset = Folder.objects.all()
    permission_classes = [IsAuthenticated]


class UserListView(ListCreateAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()


# API for pearl query 
@extend_schema(
        request=PostSerializer,
        responses={200: None}, 
        parameters= [
            OpenApiParameter(
                name= "id",
                type=str,
                location=OpenApiParameter.PATH,
                description="UUID of the user"
            )
        ]
)
class PearlView(RetrieveUpdateDestroyAPIView):
    lookup_field= "id"
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    context_object_name = 'home_list'
    template_name = 'pearl/home.html'
    audio_file = Post.pearl_audio

    
class PearlCreateView(CreateAPIView):
    # Create pearl only when authenticated
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    

# Transforming a url to a pearl
# Recieve url
# Destructure metadata
# Create pearl with Ai or manaually. 
# Manually:
#   url is saved, title, descrition and other 
#   necessary fields is entered 
# Automatically GAi:
#   LLM analysis of link to return title and other necessary information
# Save if valid





class PearlListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer    


class UserPearlListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    lookup_field = "user"

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(user = user)
    


@extend_schema(
    request= ContentContextSerializer
    ,
    parameters=[
        OpenApiParameter(
            name= "id",
            type= str,
            location=OpenApiParameter.PATH,
            description="UUID of the pearl"
        )
    ]
)
class UploadContentContext(RetrieveUpdateAPIView):
    http_method_names= ["patch"]
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ContentContextSerializer
    parser_classes = [MultiPartParser, FormParser]
    lookup_field = "id"


    #REVISIT!!!!!!!! (ALERT FOR EXPIRING PEARLS) 50% complete

# def get_context_data(self, **kwargs): 
#     current_date = datetime.today()
#     post = Post
#     post.created_date = F('created_date') 
#     expiry_date = post.created_date + timedelta(days=14)
#     days_left = 14
#     counter_date = current_date - expiry_date
#     context = super(PearlDetailView, self).get_context_data(**kwargs)
#     if counter_date == expiry_date:  
#         days_left -=1
#         # day_difference = day_difference + datetime.timedelta(days=1) 
#     context['days_left'] = days_left
#     return context



def download_pearl(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb')as fh:
            response = HttpResponse(fh.read(), content_type='application/pearl')
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response

    raise Http404



# function for saving post in archive model using the in_archive attribute of Archive model
def archive_pearl(request, id):
    post = get_object_or_404(Post, id=id)
    if post.archived.filter(id=request.user.id).exists():
        post.archived.remove(request.user)
        messages.success(request, 'Not Archived')
    else:
        post.archived.add(request.user)
        messages.success(request, 'Archived')
    
    return redirect('home_list')


def archive_list(request):
    user = request.user
    newest_post = Post.objects.order_by('-created_date')[:1]
    # archived_at = user.archived_by.all()
    current_date = datetime.today()
    two_weeks_ago = current_date + timedelta(days=-14)
    archived_post = user.archived_by.filter(created_date__range = [two_weeks_ago, current_date])
    
    context = {
        'archived_post': archived_post,
        'newest_post': newest_post,
    }
    return render(request, 'pearl/archive_list.html', context)


@extend_schema(
        request=RegisterUserSerializer,
        responses={200: None}
)
@api_view(['POST'])
@permission_classes([AllowAny])
def register_request(request):
    serializer = RegisterUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        # Create a Profile 

        return Response(
            {
                "message": "User Registered Successfully"
            },
             status= status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)



def register_page(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect("altar_call")
        messages.error(request, 'Unsuccessful registration.')
    form = NewUserForm

    return render(request=request, template_name='pearl/register.html', context={'register_form': form})


@throttle_classes([ScopedRateThrottle])
@extend_schema(
        request=LoginSerializer,
        responses={200: None}
)
@api_view(['POST'])
@permission_classes([AllowAny])
def login_request(request):
    request.throttle_scope = 'login'
    
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                # Generate JWT token
                from rest_framework_simplejwt.tokens import RefreshToken
                refresh = RefreshToken.for_user(user)
                # Get the user detail / profile
                short_profile = User.objects.filter(username = username).values('id', 'is_superuser', 'is_staff')
                return Response({
                    'access': str(refresh.access_token),
                    'refresh': str(refresh),
                    'message': 'Login successful',
                    'user': short_profile
                }, status=status.HTTP_200_OK)
            else:
                return Response({'message': "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

def altar_call_request(request):
    return render(request, 'pearl/altar_call.html', {})

def pearl_audio(request):
    return render(request, 'pearl/pearl_audio.html', {})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home_list")


@extend_schema(
        request=PasswordResetSerializer,
        responses={200: None}
)
@permission_classes([AllowAny])
@api_view(['POST'])
def password_reset_request(request):
    queryset = User.objects.all()
    serializer = PasswordResetSerializer(data = request.data)
    if serializer.is_valid():
        user_query = queryset.filter(request["username"])
        user = User.objects.filter(username = request.data['username'])
        # if user is not None:
        #     username = user
        #     return Response ({'username': ""})
        return Response({'Query Filter': user_query, 'Model Filter' : user}, status=status.HTTP_200_OK)
    return Response({'message': 'serializer invalid'}, status= status.HTTP_400_BAD_REQUEST)

def password_reset_request_page(request):
    serializer = PasswordResetSerializer
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password/password_reset.html",
            context={"password_reset_form": password_reset_form})

