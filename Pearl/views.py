from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post
from django.template import loader
from django.urls import reverse, reverse_lazy
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, Http404, request
from django.contrib.auth.models import User
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
from vecugoinc import settings


# Create your views here.


class PearlListView(ListView):
    # model = Post
    queryset = Post.objects.all()
    context_object_name = 'home_list'
    template_name = 'pearl/home.html'

    def get_context_data(self, **kwargs):
        context = super(PearlListView, self).get_context_data(**kwargs)
        context['newest_post'] = Post.objects.order_by('-created_date')[:1]
        context['previous_post'] = Post.objects.order_by('-created_date')[1:2]
        return context

 # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Post.objects.order_by('-created_date')[:1]

    # def get_context_data(self, **kwargs):
    #     context = super(PearlListView, self).get_context_data(**kwargs)
    #     context.update({
    #         'yesterday_post': Post.objects.order_by('-created_date')[1:2]
    #     })


 # class PreviousPostView(ListView):
    #     model = Post
    #     template_name = 'pearl/home.html'
    #     context_object_name = 'previous_post'
    #
    #     def get_queryset(self):
    #         return Post.objects.order_by('created_date')[1:2]


class PearlDetailView(DetailView):
    model = Post
    template_name = 'pearl/pearl_detail.html'


    #REVISIT!!!!!!!! (ALERT FOR EXPIRING PEARLS) 50% complete

    def get_context_data(self, **kwargs): 
        current_date = datetime.today()
        post = Post
        post.created_date = F('created_date') 
        expiry_date = post.created_date + timedelta(days=14)
        days_left = 14
        counter_date = current_date - expiry_date
        context = super(PearlDetailView, self).get_context_data(**kwargs)
        if counter_date == expiry_date:  
            days_left -=1
            # day_difference = day_difference + datetime.timedelta(days=1) 
        context['days_left'] = days_left
        return context

    ########################## 

# class ArchiveListView(ListView):
    #     model = Post
    #     template_name = 'pearl/archive.html'
    #     context_object_name = 'archived_post'

    # return post that have been archived for less than 30 days
    # def get_queryset(self):
    #     return Post.object.filter(Archive.life_span < timedelta(30))


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
   

# def archive(request):
    #     new = Post.objects.all()
    #     return render(request, 'pearl/archive.html', {'new': new})

    # def archive_detail(self, request, id):
    #     post = get_object_or_404(Post, id=id)
    #     is_archived = False
    #     if post.archived.filter(id=request.user.id).exists():
    #         is_archived = True


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


# def auto_delete_archived_pearl(request):
    #     user = request.user
    #     post = Post.archived.filter(id=request.user.id)
    #     for i in post:
    #         if i.
    #         post.archived.remove(request.user)

def register_request(request):
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


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home_list')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request=request, template_name="pearl/login.html", context={"login_form": form})

def altar_call_request(request):
    return render(request, 'pearl/altar_call.html', {})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home_list")


def password_reset_request(request):
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

