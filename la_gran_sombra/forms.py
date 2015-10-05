from django import forms


class TimerForm(forms.Form):
    minutes = forms.IntegerField()

    class Meta:
        fields = [
            "minutes",
        ]
