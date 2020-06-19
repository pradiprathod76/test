from django.urls import path

from .views import UserList, CreatePostView, DeletePost, UpdatePost, index, CgList, CreateCgView, DeleteCg, UpdateCg, \
    AudioList, AudioCreate, AudioUpdate, AudioDelete,PicList,PicCreate,PicUpdate,PicDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', index, name='index'),
    path('user/', login_required(UserList.as_view()), name='home'),
    path('post/', CreatePostView.as_view(), name='post'),
    path('delete/<int:pk>', DeletePost.as_view(), name='delete'),
    path('edit/<int:pk>', UpdatePost.as_view(), name='edit'),
    path('category/', login_required(CgList.as_view()), name='category'),
    path('cgcreate/', CreateCgView.as_view(), name='cgcreate'),
    path('cgdelete/<int:pk>', DeleteCg.as_view(), name='cgdelete'),
    path('cdedit/<int:pk>', UpdateCg.as_view(), name='cgupdate'),
    path('audio/', login_required(AudioList.as_view()), name='audio'),
    path('audiocreate/', AudioCreate.as_view(), name='audiocreate'),
    path('audioupdate/<int:pk>', AudioUpdate.as_view(), name='audioupdate'),
    path('audiodelete/<int:pk>', AudioDelete.as_view(), name='audiodelete'),
    path('pic',PicList.as_view(),name='pic'),
    path('piccreate',PicCreate.as_view(),name='piccreate'),
    path('picupdate/<int:pk>',PicUpdate.as_view(),name='picupdate'),
    path('picdelete/<int:pk>',PicDelete.as_view(),name='picdelete')

]
