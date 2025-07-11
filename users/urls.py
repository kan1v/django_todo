from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import CustomAuthenticationForm


app_name = 'users'

urlpatterns = [
    path('login/', 
        auth_views.LoginView.as_view(authentication_form=CustomAuthenticationForm),
        name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Адреса для смены пароля 
    path('password-change/', auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    # url-адреса сброса пароля
    path('password-reset/',
        auth_views.PasswordResetView.as_view(),
        name='password_reset'),
    path('password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    path('password-reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),
    
]