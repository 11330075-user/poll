from django.shortcuts import render
from django.views.generic import ListView
from .models import *

## Create your views here.
## 投票主題列表
class PollList(ListView):
    model = Poll