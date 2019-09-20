
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Groove
from .forms import GrooveForm
import requests
from django.http import Http404, JsonResponse
import urllib 
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('dashboard')
    template_name = 'registration/signup.html'

class login(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('dashboard')
    template_name = 'registration/login.html'

@login_required
def dashboard(request):
   list_of_my_grooves = Groove.objects.filter(user=request.user)
   return render(request, 'grooves/dashboard.html', {'list_of_my_grooves': list_of_my_grooves})

@login_required
def all_grooves(request):
    list_of_grooves = Groove.objects.all()
    return render(request, 'grooves/grooves.html', {'list_of_grooves': list_of_grooves})

class CreateGroove(LoginRequiredMixin, generic.CreateView):
    model = Groove
    fields = ['groove','duration','date']
    template_name = 'grooves/create_groove.html'
    success_url = reverse_lazy('dashboard')
    success_message = "Groove %(groove) successfully created"

    def form_valid(self, form):
        
        form.instance.user = self.request.user
        super(CreateGroove, self).form_valid(form)
       
        return redirect('dashboard')

class DetailGroove(LoginRequiredMixin, generic.DetailView):
    model = Groove
    template_name = 'grooves/detail_groove.html'


class UpdateGroove(LoginRequiredMixin, generic.UpdateView):
    model = Groove
    template_name = 'grooves/update_groove.html'
    fields = ['groove', 'duration', 'date']
    success_url = reverse_lazy('dashboard')

    def get_object(self):
        groove = super(UpdateGroove, self).get_object()
        if not groove.user == self.request.user:
            raise Http404
        return groove


class DeleteGroove(LoginRequiredMixin, generic.DeleteView):
    model = Groove
    template_name = 'grooves/delete_groove.html'
    success_url = reverse_lazy('dashboard')

    