from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    UserCreationForm,
    PasswordChangeForm
)
from django.contrib import messages
from django.contrib.auth.forms import (
    UserChangeForm,
    PasswordChangeForm
)
from .forms import UserRegisterForm
from clients.models import Session, Event
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from datetime import datetime, timedelta, date
from django.views import generic
from django.utils.safestring import mark_safe
import calendar
from clients.models import *
from clients.utils import Calendar
from .forms import EventForm
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect


class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.now()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    # define o driver e instructor por default a aparecer quando e criada uma nova sessao
    for staff in Profile.objects.all():
        if staff.firstName == "User":
            instance.instructor = staff
            instance.driver = staff

    for boat in Boat.objects.all():
        if boat.name == "teste":
            instance.Boat = boat

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('calendar'))
    return render(request, 'session/event.html', {'form': form})


def event_show(request, event_id=None):
    #form = EventForm(request.POST or None)
    # return render(request, 'session/event_show.html', {'form': form})
    event = get_object_or_404(Event, pk=event_id)
    context = {'event': event}
    return render(request, 'session/event_show.html', context)


def client_show(request, client_id=None):
    #form = EventForm(request.POST or None)
    # return render(request, 'session/event_show.html', {'form': form})
    client = get_object_or_404(Client, pk=client_id)

    sessions_qs = Event.objects.all()
    sessions_qs = Event.objects.order_by('-start_time')

    context = {"client": client, "sessions": sessions_qs}
    return render(request, 'client/client_show.html', context)


def staff_show(request, staff_id=None):
    #form = EventForm(request.POST or None)
    # return render(request, 'session/event_show.html', {'form': form})
    staff = get_object_or_404(Profile, pk=staff_id)
    context = {'staff': staff}
    return render(request, 'staff/staff_show.html', context)


def event_edit(request, event_id=None):
    instance = Event()
    if id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    if request.method == 'POST':
        form = EventForm(request.POST, instance=instance)

        if request.POST and form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('sessions-list'))

    else:
        form = EventForm(instance=instance)

    context = {
        'form': form,
    }

    return render(request, 'session/event_edit.html', context)


class SessionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/calendar'

    def test_func(self):
        return True


@login_required
def about_page(request):
    return render(request, "about.html", {"title": "About"})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            return redirect('staff-list')
        else:
            messages.error(request, 'Invalid registration')
            return redirect('register')
    else:
        form = UserRegisterForm()

        args = {'form': form}
        return render(request, 'staff/register.html', args)


def login(request):
    return render(request, 'registration/login.html', {'title': 'Login'})


def sessions(request):
    return render(request, 'session/sessions.html', {'title': 'sessions'})


def sessions_Details(request):
    return render(request, 'session/sessions_details.html', {'title': 'sessions'})


def sessions_Details_Edit(request):
    return render(request, 'session/session_edit.html', {'title': 'sessions'})


def profile_edit(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
        else:
            messages.error(request, _('Please correct the error below.'))

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'account/edit.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'account/profile.html', context)


class SessionCreateView(LoginRequiredMixin, CreateView):
    model = Session
    fields = ['client', 'driver', 'instructor',
              'Boat', 'price', 'modalidade', 'notes']


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = ['name', 'email', 'gender', 'birthday',
              'country', 'phone', 'nIF', 'saldo', 'divida', 'desconto', 'notes']


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {
        'form': form
    })
