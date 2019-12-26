from p_library.views import nav 
from django.urls import path  
from p_library.views import RegisterView, CreateUserProfile
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy  
from allauth.account.views import login, logout
  
app_name = 'p_library'  
urlpatterns = [  
    path('', nav, name='nav'), 
    path('login/', login, name='login'),  
    path('logout/', logout, name='logout'),
    path('register/', RegisterView.as_view(  
            template_name='register.html',  
            success_url=reverse_lazy('profile-create')  
        ), name='register'),  
    path('profile-create/', CreateUserProfile.as_view(), name='profile-create'), 
]