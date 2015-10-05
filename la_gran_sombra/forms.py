from django import forms


from .models import Sombra


class TimerForm(forms.Form):
    minutes = forms.IntegerField()

    class Meta:
        fields = [
            "minutes",
        ]


class SombraForm(forms.ModelForm):
    class Meta:
        fields = ['cadaver']
        model = Sombra
