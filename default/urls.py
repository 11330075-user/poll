from django.urls import path,reverse_lazy
from . import views
from  django.views.generic import RedirectView
urlpatterns = [
    path('poll/', views.PollList.as_view(),name='poll_list'),
    path('poll/<int:pk>/', views.PollDetail.as_view()),
    path('option/<int:pk>/', views.PollVote.as_view()),
    path('', RedirectView.as_view(url=reverse_lazy('poll_list')))
]