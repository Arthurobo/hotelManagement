from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    #model = Profile
    template_name = 'pages/home.html'
    #context_object_name = 'profiles'



class AboutPageView(TemplateView):
    #model = Profile
    template_name = 'pages/about.html'
    #context_object_name = 'profiles'


class ContactPageView(TemplateView):
    #model = Profile
    template_name = 'pages/contact.html'
    #context_object_name = 'profiles'