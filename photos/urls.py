from django.urls import path
from . import views


app_name = 'photos'

urlpatterns = [
    path('', views.RedirectToPhotowall, name='redirect'),
    path('uploadphoto', views.UploadPhoto, name="uploadphoto"),
    path('photowall', views.ViewPhotos, name='photos'),
    path('signup', views.SignUpUser, name='signup'),
    path('login', views.LogInUser, name='login'),
    path('logout', views.LogOutUser, name='logout')
]