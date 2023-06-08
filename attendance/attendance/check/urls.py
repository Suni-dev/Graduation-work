from django.urls import path
from .views import *

app_name = 'check'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('find_id/', find_id, name='find_id'),
    path('find_id/result/', find_id_result, name='find_id_result'),
    path('password_reset_user/', password_reset_user, name='password_reset_user'),
    path('password_reset_reset/<str:user_id>/', password_reset_reset, name='password_reset_reset'),
    path('register/', register, name='register'),
    path('student_main/', student_main, name='student_main'),
    path('professor_main/', professor_main, name='professor_main'),
    path('attendance/', attendance_view, name='attendance'),
    path('a/', attendance_view1, name='a'),
    path('api/', api_view, name='api'),
    path('agreement/', agreement, name='agreement'),
    path('logout/', logout_view, name='logout'),
    path('student_att/',student_att_view, name='student_att'),
]
