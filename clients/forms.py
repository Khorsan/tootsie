from django.views.generic import CreateView
from .models import Session
from django import forms
from django.contrib.auth.models import User
from clients.models import Client, Modalidade
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)


class SessionDetails():
    model = Session
    template_name = 'sessions/sessions-details.html'
    fields = ('ID', 'client', 'driver',
              'instructor', 'Boat', 'time', 'price', 'modalidade', 'dateSession')


class ClientUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Client
        fields = ['name', 'email', 'gender', 'birthday',
                  'country', 'phone', 'nIF', 'saldo', 'divida', 'desconto', 'notes']


class SessionFilterForm(forms.Form):
    payed = forms.ChoiceField(
        choices=(
            ("1", "All"),
            ("2", "yes"),
            ("3", "no"),
        ),
        label='Payed',
    )

    choicesModalidade = []
    count = 1
    for modalidade in Modalidade.objects.all():
        choicesModalidade.append((f"{count}", modalidade.name))
        count = count + 1

    print(choicesModalidade)

    modality = forms.ChoiceField(
        choices=choicesModalidade,
        label='Modality',
    )

    class Meta:
        fields = ('payed', 'modality')
