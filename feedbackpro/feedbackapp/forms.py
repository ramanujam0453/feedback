from django import forms
from . models import EmpFeedBack
# from django.contrib.auth import get_user_model

# User = get_user_model()


class EmpFeedBackForm(forms.Form):
    eid = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your eid'
            }
        )
    )
    fbeid = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter feedback eid'
            }
        )
    )
    rating = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your rating 1-5'
            }
        )
    )
    feedback = forms.CharField(
        help_text='Write a brief feedback on the employee',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your feedback'
            }
        )
    )

# validation for the rating
    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        # qs = int(EmpFeedBack.objects.filter(rating=rating))
        if rating < 0 or rating > 5:
            raise forms.ValidationError('Rating should be between 0 and 5')
        return rating

# validation for the feedback text box
    def clean_feedback(self):
        feedback = self.cleaned_data.get('feedback')
        # qs = EmpFeedBack.objects.filter(feedback=feedback)
        if len(feedback) < 20 or len(feedback) > 300:
            raise forms.ValidationError('Minimum 20 characters maximum 300 characters')
        return feedback

# validation to check eid and fbeid are equal or not
    def clean(self):
        data = self.cleaned_data
        eid = self.cleaned_data.get('eid')
        fbeid = self.cleaned_data.get('fbeid')
        if fbeid == eid:
            raise forms.ValidationError('eid and fbeid must not be equal')
        return data
