from django.test import TestCase
from django.urls import reverse
from unittest.mock import Mock, patch


class HealthCheckTests(TestCase):
    def test_health_check_returns_ok(self):
        response = self.client.get(reverse("health"), secure=True)

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"status": "ok"})


class SurveyTests(TestCase):
    @patch("core.views.get_model")
    def test_valid_survey_shows_a_screening_result(self, get_model):
        model = Mock()
        model.predict.return_value = [0]
        model.classes_ = [0, 1]
        model.predict_proba.return_value = [[0.8, 0.2]]
        get_model.return_value = model

        response = self.client.post(
            reverse("survey"),
            {
                "age": 16,
                "gender": "female",
                "daily_social_media_hours": 3,
                "platform_usage": "Both",
                "sleep_hours": 8,
                "screen_time_before_sleep": 1,
                "academic_performance": 3,
                "physical_activity": 1,
                "social_interaction_level": "medium",
                "stress_level": 5,
                "anxiety_level": 5,
                "addiction_level": 5,
            },
            secure=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "20.0%")
