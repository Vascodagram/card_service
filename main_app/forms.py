from django import forms
from .models import Card, Series, Balance

CHOICES_STATUS = (
    ('not activated', 'Деактивувати'),
    ('activated', 'Активувати'),
)


class ActivateForm(forms.ModelForm):
    status = forms.ChoiceField(choices=CHOICES_STATUS)

    class Meta:
        model = Card
        fields = ('status', )


class GenerationForm(forms.ModelForm):
    series = forms.ModelChoiceField(queryset=Series.objects.all())
    value = forms.IntegerField()
    year = forms.IntegerField()
    month = forms.IntegerField(max_value=12)

    class Meta:
        model = Card
        fields = ['series', ]


class TransactionForm(forms.ModelForm):
    name = forms.CharField(max_length=15)
    transaction = forms.FloatField()

    class Meta:
        model = Balance
        fields = ['name', 'transaction']


