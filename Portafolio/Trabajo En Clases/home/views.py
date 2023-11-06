from django.shortcuts import render

from django.views import generic

# Create your views here.

class Index(generic.View):
    template_name = "home/index.html"
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)



class About(generic.View):
    template_name = "home/about.html"
    context = {}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)


class Contact(generic.View):
    template_name = "home/contact.html"
    context = {}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)