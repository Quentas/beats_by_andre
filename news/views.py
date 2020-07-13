from django.shortcuts import render
from .models import New_Text, New_Video, New_Track, Track
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
