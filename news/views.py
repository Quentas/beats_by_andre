from django.shortcuts import render
from .models import New_Text, New_Video, New_Track, Track
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone


def news_list(request):
	latest_news_list = New_Text.order_by('-date')[:10] 
	latest_tracks_list = New_Track.order_by('-date')[:10] 
	latest_videos_list = New_Video.order_by('-date')[:10] 
	return render(request, 'news/news_content.html', {
		'latest_news_list' : latest_news_list, 
		'latest_tracks_list' : latest_tracks_list,
		'latest_videos_list' : latest_videos_list
		})


def track_list(request):
	try:
		a = New_Track.objects.filter(endswith = '.mp3')
		all_tracks = a.order_by('-date')
	except:
		raise Http404("NOT FOUND")
	return render(request, 'tracks/tracks_content.html', {'all_tracks': all_tracks})