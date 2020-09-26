from django.shortcuts import render
from .models import New_Text, New_Video, New_Track, Author
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone


def news_list(request):
	latest_news_list = New_Text.objects.order_by('-date')[:3] 
	latest_tracks_list = New_Track.objects.order_by('-date')[:3] 
	latest_videos_list = New_Video.objects.order_by('-date')[:3] 
	return render(request, 'news/news_content.html', {
		'latest_news_list' : latest_news_list, 
		'latest_tracks_list' : latest_tracks_list,
		'latest_videos_list' : latest_videos_list
		})


def track_list(request):
	try:
		
		all_tracks = New_Track.objects.order_by('-date')
	except:
		raise Http404("NOT FOUND")
	return render(request, 'tracks/tracks_content.html', {'all_tracks': all_tracks})

def about_author(request):
	try:
		author_info = Author.objects.all().order_by('-id')[0]
		try:
			links = author_info.author_links.split(";;")
			return render(request, 'author/about_author.html', {'author_info' : author_info , 'links' : links})
		except:
			return render(request, 'author/about_author.html', {'author_info' : author_info})
	except:
		raise Http404("NOT FOUND")
	
	