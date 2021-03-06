from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from todos import views

urlpatterns = [
    path('todos/', views.TodosList.as_view()),
    path('todos/<int:pk>/', views.TodoDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)