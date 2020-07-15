from django.urls import path, include
from . import views
urlpatterns = [
	path('news_list/', views.news_list, name = 'news_list'),
	path('track_list/', views.track_list, name = 'track_list'),
]
