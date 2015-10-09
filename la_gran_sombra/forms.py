from django import forms


from .models import Sombra


class TimerForm(forms.Form):
    minutes = forms.IntegerField(
        label='',
    	widget = forms.TextInput(attrs={"class":"form-control input-timer sombra"}),
    	)

    class Meta:
        fields = [
            "minutes",
        ]


class SombraForm(forms.ModelForm):
    cadaver = forms.CharField(
    	label="",
    	widget = forms.Textarea(attrs={"class":"form-control sombra"}),
    	)
    class Meta:
        fields = ['cadaver']
        model = Sombra
