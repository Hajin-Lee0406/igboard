from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    #전체 게시판
    path('', views.board_list, name='board_list'),
    path('search/', views.board_search, name='board_search'),
    #일반인 페이지
    path('public/', views.board_public_list, name='board_public_list'),
    path('public/write/', views.board_public_write, name='board_public_write'),
    path('public/detail/<int:pk>/', views.board_public_detail, name='board_public_detail'),
    path('public/download/', views.file_download, name='file_download'),
    path('public/detail/<int:pk>/delete/', views.board_public_delete, name='board_public_delete'),
    path('public/detail/<int:pk>/modify/', views.board_public_modify, name='board_public_modify'),
    path('public/search/', views.board_public_search, name='board_public_search'),

    #과학자 페이지
    path('science/', views.board_science_list, name='board_science_list'),
    path('science/write/', views.board_science_write, name='board_science_write'),
    path('science/detail/<int:pk>/', views.board_science_detail, name='board_science_detail'),
    path('science/download/', views.file_download, name='file_download'),
    path('science/detail/<int:pk>/delete/', views.board_science_delete, name='board_science_delete'),
    path('science/detail/<int:pk>/modify/', views.board_science_modify, name='board_science_modify'),
    path('science/search/', views.board_science_search, name='board_science_search'),
]