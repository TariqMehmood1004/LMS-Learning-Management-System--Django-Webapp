
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('courses/', views.course_list, name='course_list'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
]
