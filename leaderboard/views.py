import re
from datetime import datetime, timedelta

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response

# Create your views here.
from django.template import RequestContext
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError

from leaderboard.models import Score, ScoreForm


def leaderboard(request):
    return render(request,"leaderboard/leaderboard.html",{"scores":
                                                              [x for x in
                                                               Score.objects.order_by('-duration')
                                                               if x.is_valid()]}
                                                          )

def added(request):
    return render(request,"leaderboard/added.html")

def add(request):
    form = ScoreForm()
    if request.method == "POST":
        form = ScoreForm(request.POST, request.FILES)
        print(form.errors.as_data())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('leaderboard:added'))

    return render(request, "leaderboard/scoreform.html", {"form": form})

def scoreform(request):
    return render(request, "leaderboard/scoreform.html", {"form": ScoreForm()})