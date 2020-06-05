from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import FormView
from django.contrib import messages
from django.http import Http404
from django.core.files import File
from django.db.models import Max
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.utils.encoding import smart_text
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.conf import settings
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from tootsie.forms import UserUpdateForm, ProfileUpdateForm
from .models import Client, Session, Event, Profile
from django.urls import reverse
from .forms import ClientUpdateForm
from .forms import SessionFilterForm


# Create your views here.


@login_required
def client_list_view(request):
    clients_qs = Client.objects.all()
    template_name = 'clients/list.html'

    context = {'clients': clients_qs}
    return render(request, template_name, context)


@login_required
def client_detail_view(request, id):
    client_obj = get_object_or_404(Client, id=id)

    session_list = Session.objects.filter(client=client_obj).order_by('date')
    context = {"client": client_obj, "sessions": session_list}
    template_name = 'clients/detail.html'
    return render(request, template_name, context)


class client_delete_view(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Client
    success_url = '/'  # Home

    def test_func(self):
        return True


class staff_delete_view(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Profile
    success_url = '/staff-list'

    def test_func(self):
        return True


def client_edit_view(request, id=None):
    instance = Client()
    if id:
        instance = get_object_or_404(Client, pk=id)
    else:
        instance = Client()

    if request.method == 'POST':
        form = ClientUpdateForm(request.POST, instance=instance)

        if request.POST and form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))

    else:
        form = ClientUpdateForm(instance=instance)

    context = {
        'form': form,
    }

    return render(request, 'clients/edit.html', context)


def staff_edit_view(request, id=None):
    instance = Profile()
    if id:
        instance = get_object_or_404(Profile, pk=id)
    else:
        instance = Profile()

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=instance.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=instance)

        if request.POST and u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return HttpResponseRedirect(reverse('staff-list'))

    else:
        u_form = UserUpdateForm(instance=instance.user)
        p_form = ProfileUpdateForm(instance=instance)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'staff/edit.html', context)


def delete_staff(request, id):
    obj = get_object_or_404(Profile, id=id)
    if request.method == "POST":
        obj.delete_user()
        return redirect('staff-list')
    context = {
        "object": obj
    }
    return render(request, "staff/profile_delete.html", context)


@login_required
def session_list_view(request):
    sessions_qs = Event.objects.all()
    template_name = 'Session/sessions_list.html'

    context = {'events': sessions_qs, 'form': SessionFilterForm}
    return render(request, template_name, context)


@login_required
def staff_list_view(request):
    profile_qs = Profile.objects.all()
    template_name = 'staff/list.html'

    context = {'profile': profile_qs}
    return render(request, template_name, context)


# filtrar -> ver melhor
def teste(request):
    sessions_qs = Event.objects.filter(client__id=request.user.id)

    sessios2 = sessions_qs.filter()
    template_name = 'Session/sessions_list.html'

    context = {'events': sessions_qs}
    return render(request, template_name, context)
