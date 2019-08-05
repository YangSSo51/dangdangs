from django.urls import path
from . import views

urlpatterns = [
    path('', views.board, name="board"),

    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    path('detail/<int:board_id>/', views.detail, name="detail"),
    path('detail/<int:board_id>/delete', views.delete, name="delete"),
    path('detail/<int:board_id>/update', views.update, name="update"),
    path('search/', views.SearchFormView.as_view(), name='search'),
    
    path('detail/<int:board_id>/comment_write', views.comment_write, name="comment_write"),
]