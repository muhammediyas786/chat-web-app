from Chatapp import views
from django.urls import path



urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('exist_group/', views.exist_group, name='exist_group'),
    path('group/', views.create_group, name='group'),
    path('inner_group/<str:pk>', views.Inner_group, name='Inner_group'),
    path('message_senting/<str:pk>',views.message_senting, name='message_senting'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),

]
