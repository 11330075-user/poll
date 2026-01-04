from django.urls import path,reverse_lazy
from . import views
from  django.views.generic import RedirectView
urlpatterns = [
    path('poll/', views.PollList.as_view(),name='poll_list'),
    path('poll/<int:pk>/', views.PollDetail.as_view()),
    path('option/<int:pk>/', views.PollVote.as_view()),
    path('poll/create/', views.PollCreate.as_view()),
    path('poll/<int:pk>/update/', views.PollUpdate.as_view()),
    path('poll/<int:pk>/delete/', views.PollDelete.as_view()),
    path('option/create/<int:pid>/', views.OptionCreate.as_view()),
    path('option/<int:pk>/update/', views.OptionUpdate.as_view()),
    path('', RedirectView.as_view(url=reverse_lazy('poll_list')))
]