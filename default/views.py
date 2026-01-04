from django.shortcuts import render
from django.views.generic import ListView, DetailView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *

## Create your views here.
## 投票主題列表
class PollList(ListView):
    model = Poll
    ## 投票主題檢視
class PollDetail(DetailView):
    model = Poll
    # 取得額外資料供頁面範本顯示
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        options = Option.objects.filter(poll_id=self.kwargs['pk'])
        context['options'] = options
        return context
## 投票
class PollVote(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        option = Option.objects.get(id=self.kwargs['pk'])
        option.count += 1   # 將選項的票數+1
        option.save()       # 儲存至資料庫
        return "/poll/"+str(option.poll_id)+"/"
## 新增投票主題
class PollCreate(CreateView):
    model = Poll
    fields = ['subject']    # 指定要顯示的欄位
    success_url = '/poll/'  # 成功新增後要導向的路徑
    template_name = 'general_form.html' # 要使用的頁面範本