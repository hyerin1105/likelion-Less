from django.urls import path
from .views import signup, login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', signup, name="signup"),
    path('login/', login, name="login"),
    path('logout/', LogoutView.as_view(next_page='main'), name="logout"),
]