from functools import lru_cache

import joblib
import pandas as pd
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from core.forms import SurveyForm


MODEL_PATH = settings.BASE_DIR.parent / "ml" / "models" / "depression_classifier.joblib"


@lru_cache(maxsize=1)
def get_model():
    """Load the trained pipeline once per Django worker process."""
    return joblib.load(MODEL_PATH)


class Home(TemplateView):
    template_name = "home.html"


def health_check(request):
    return JsonResponse({"status": "ok"})


class SurveyView(View):
    template_name = "survey.html"

    def get(self, request):
        return render(request, self.template_name, {"form": SurveyForm()})

    def post(self, request):
        form = SurveyForm(request.POST)

        if not form.is_valid():
            return render(request, self.template_name, {"form": form})

        survey_data = pd.DataFrame([form.cleaned_data])
        model = get_model()
        prediction = int(model.predict(survey_data)[0])
        positive_class_index = list(model.classes_).index(1)
        risk_percentage = round(
            float(model.predict_proba(survey_data)[0][positive_class_index]) * 100,
            1,
        )

        return render(
            request,
            "result.html",
            {
                "elevated_risk": prediction == 1,
                "risk_percentage": risk_percentage,
            },
        )
