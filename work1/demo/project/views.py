from django.shortcuts import render
from django.views.generic import ListView,CreateView
from django.views.generic.edit import UpdateView,DeleteView
from .models import Post,Category,Audio,Pic
from django.urls import reverse_lazy,reverse
from .forms import CgForm,AudioForm,UserCreateForm,PicForm
from rest_framework import viewsets
from .serializers import UserSerializer,AudioSerializer,CategorySerializer
from django.core.mail import send_mail
from demo.settings import EMAIL_HOST_USER
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages





def index(request):
    qs_pic = Pic.objects.all()
    context = {
        'pic':qs_pic
    }
    return render(request,'index.html',context)




class UserList(ListView):
    model = User
    template_name = 'home.html'

class CreatePostView(CreateView): # new
    model = User
    form_class = UserCreateForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')

class UpdatePost(UpdateView):
    model = User
    fields = ['username','email']
    template_name = 'post.html'
    success_url = reverse_lazy('home')

class DeletePost(DeleteView):
    model = User
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

class CgList(ListView):
    model = Category
    template_name = 'category.html'

class CreateCgView(CreateView):
    model = Category
    form_class = CgForm
    template_name = 'cgform.html'
    success_url = reverse_lazy('category')

class UpdateCg(UpdateView):
    model = Category
    fields = ['img','name','des']
    template_name = 'cgform.html'
    success_url = reverse_lazy('category')

class DeleteCg(DeleteView):
    model = Category
    template_name = 'cgdelete.html'
    success_url = reverse_lazy('category')

class AudioList(ListView):
    model = Audio
    template_name = 'audio.html'

class AudioCreate(CreateView):
    model = Audio
    form_class = AudioForm
    template_name = 'audioform.html'
    success_url = reverse_lazy('audio')

class AudioUpdate(UpdateView):
    model = Audio
    fields = ['img','name','des','audio','cg','sub','date']
    template_name = 'audioform.html'
    success_url = reverse_lazy('audio')

class AudioDelete(DeleteView):
    model = Audio
    template_name = 'audiodelete.html'
    success_url = reverse_lazy('audio')

class PicList(ListView):
    model = Pic
    template_name = 'pic.html'

class PicCreate(CreateView):
    model = Pic
    form_class = PicForm
    success_url = reverse_lazy('pic')

class PicUpdate(UpdateView):
    model = Pic
    fields = ['img']
    success_url = reverse_lazy('pic')

class PicDelete(DeleteView):
    model = Pic
    success_url = reverse_lazy('pic')

class UserViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = UserSerializer

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AudioViewset(viewsets.ModelViewSet):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer


class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            # Important!
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })
def Reset_password(request):
    return render(request,'password_reset_form.html')


