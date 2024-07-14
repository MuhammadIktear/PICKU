from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationsApiView.as_view(), name='register'),
    path('login/', views.UserLoginApiView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('deposit/', views.DepositAPIView.as_view(), name='deposit'),  
    path('change-password/', views.PasswordChangeView.as_view(), name='change-password'),        
    path('activate/<uidb64>/<token>/', views.activate_user, name='activate'),
]