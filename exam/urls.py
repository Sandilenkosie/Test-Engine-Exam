from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exam/<int:exam_id>/take/', views.take_exam, name='take_exam'),
    path('exam/result/<int:exam_result_id>/', views.exam_result, name='exam_result'),
    path('box', views.box, name='box'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),

]
