from django import forms
from django.utils.timezone import now


class MonthYearForm(forms.Form):
    month = forms.ChoiceField(choices=[(i, i) for i in range(1, 13)])
    year = forms.ChoiceField(choices=[(y, y)
                             for y in range(2000, now().year+1)])
