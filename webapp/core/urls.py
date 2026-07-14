from django.urls import path
from django.views.generic import RedirectView

from core.views import Home, SurveyView

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="home", permanent=False)),
    path("home", Home.as_view(), name="home"),
    path("survey", SurveyView.as_view(), name="survey"),
    path("quiz.html", RedirectView.as_view(pattern_name="survey", permanent=False)),
]

