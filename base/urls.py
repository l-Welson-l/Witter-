from django.urls import path
from . import views
from .views import login, home, PostDetail, CreatePost, DeletePost, RegisterPage, LogoutPage, ReplyPost, UpdatePost

urlpatterns = [
    path('', home.as_view(), name="home"),
    path('login/', login.as_view(), name="login"),
    path('register/', RegisterPage.as_view(), name="register" ),
    path('post/<int:pk>', PostDetail.as_view(), name="post"),
    path('create-post/', CreatePost.as_view(), name="create-post"),
    path('delete-post/<int:pk>', DeletePost.as_view(), name="delete-post"),
    path('logout/', LogoutPage.as_view(next_page='home'), name="logout"),
    path('create-reply/', ReplyPost.as_view(), name="reply"),
    path('update/<int:pk>', UpdatePost.as_view(), name="update-post"),
]