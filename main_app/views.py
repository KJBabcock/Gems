from django.shortcuts import render, redirect
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Gem, Attribute, Chain


# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Example(View):

    # Here we are adding a method that will be run when we are dealing with a GET request
    def get(self, request):
        # Here we are returning a generic response
        # This is similar to response.send() in express
        return HttpResponse("Gems Example")

class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["chains"] = Chain.objects.all()
        return context

class About(TemplateView):
    template_name = "about.html"

class GemList(TemplateView):
    template_name = "gem_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["gems"] = Gem.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["gems"] = Gem.objects.all()
            # default header for not searching 
            context["header"] = "Trending Gems"
        return context

class GemDetail(DetailView):
    model = Gem
    template_name = "gem_detail.html"

class GemCreate(CreateView):
    model = Gem
    fields = ['name', 'img', 'bio', 'verified_gem']
    template_name = "gem_create.html"
    # this will get the pk from the route and redirect to gem view
    def get_success_url(self):
        return reverse('gem_detail', kwargs={'pk': self.object.pk})
        
        
class GemUpdate(UpdateView):
    model = Gem
    fields = ['name', 'img', 'bio', 'verified_gem']
    template_name = "gem_update.html"

    def get_success_url(self):
        return reverse('gem_detail', kwargs={'pk': self.object.pk})

class GemDelete(DeleteView):
    model = Gem
    template_name = "gem_delete_confirmation.html"
    success_url = "/gems/"

class AttributeCreate(View):

    def post(self, request, pk):
        title = request.POST.get("title")
        value = request.POST.get("value")
        gem = Gem.objects.get(pk=pk)
        Attribute.objects.create(title=title, value=value, gem=gem)
        return redirect('gem_detail', pk=pk)

class ChainAttributeAssoc(View):

    def get(self, request, pk, attribute_pk):
        # get the query param from the url
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            # get the Chain by the id and
            # remove from the join table the given attribute_id
            Chain.objects.get(pk=pk).attributes.remove(attribute_pk)
        if assoc == "add":
            # get the Chain by the id and
            # add to the join table the given attribute_id
            Chain.objects.get(pk=pk).attributes.add(attribute_pk)
        return redirect('home')

class GemDetail(DetailView):
    model = Gem
    template_name = "gem_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["chains"] = Chain.objects.all()
        return context
