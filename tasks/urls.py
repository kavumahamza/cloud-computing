from django.urls import path
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from tasks import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user_login/', views.login_user, name='login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('dashboard', views.index, name = 'dashboard'),
     path('add_task/<str:pk>/', views.create_task, name='create-task'),
    path('add_new_task/', views.create_new_task, name='create-new-task'),
    path('update_task/<str:pk>/', views.updateTask, name = 'update-task'),
    path('update_plan/<str:pk>/', views.updatePlan, name = 'update-plan'),
    path('confirm task delete/<str:pk>/', views.deleteViewTask, name = 'confirm-task-delete'),
    path('confirm plan delete/<str:pk>/', views.deleteViewPlan, name = 'confirm-plan-delete'),
    path('delete-task/<str:pk>/', views.deleteTask, name = 'delete-task'),
    path('delete-plan/<str:pk>/', views.deletePlan, name = 'delete-plan'),
    path('statistics/', views.statistics, name ='statistics'),
    path('task-list/', views.task_list, name='task_list'),
    path('add_plan/', views.createPlan, name ='add-plan'),
    path('task/<str:pk>/', views.task_view, name='task_view'),
    path('logout/', views.logoutUser, name='logout'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
  ]
    # 
    # 
    # path('change_password/', views.change_password, name='change_password'),
    # path('profile/', views.profile, name='profile'),
    # path('update_profile/', views.update_profile, name='update_profile'),
