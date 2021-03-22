from django.urls import path
from django.urls.conf import include

from accounts import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('account/<str:login>/', views.UserAccountView.as_view(), name='account'),
]
