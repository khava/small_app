from django.urls import path

from app import views


urlpatterns = [
    path('', views.MainPageView.as_view(), name='main'),
    path('reload/<int:id>/', views.ReloadView.as_view(), name='reload'),
    path('history/<int:id>/', views.PictureHistoryView.as_view(), name='history'),
]
