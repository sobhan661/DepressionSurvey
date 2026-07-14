from django import forms


GENDER_CHOICES = [("male", "Male"), ("female", "Female")]
PLATFORM_CHOICES = [
    ("Instagram", "Instagram"),
    ("TikTok", "TikTok"),
    ("Both", "Both"),
]
SOCIAL_INTERACTION_CHOICES = [("low", "Low"), ("medium", "Medium"), ("high", "High")]
LEVEL_CHOICES = [(level, str(level)) for level in range(1, 11)]


class SurveyForm(forms.Form):
    age = forms.IntegerField(min_value=13, max_value=19)
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    daily_social_media_hours = forms.FloatField(min_value=1.0, max_value=8.0)
    platform_usage = forms.ChoiceField(choices=PLATFORM_CHOICES)
    sleep_hours = forms.FloatField(min_value=4.0, max_value=9.0)
    screen_time_before_sleep = forms.FloatField(min_value=0.5, max_value=3.0)
    academic_performance = forms.FloatField(min_value=2.0, max_value=4.0)
    physical_activity = forms.FloatField(min_value=0.0, max_value=2.0)
    social_interaction_level = forms.ChoiceField(choices=SOCIAL_INTERACTION_CHOICES)
    stress_level = forms.TypedChoiceField(choices=LEVEL_CHOICES, coerce=int)
    anxiety_level = forms.TypedChoiceField(choices=LEVEL_CHOICES, coerce=int)
    addiction_level = forms.TypedChoiceField(choices=LEVEL_CHOICES, coerce=int)
