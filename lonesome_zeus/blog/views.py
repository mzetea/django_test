from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from django.http import HttpResponse
from django.template import RequestContext

from .models import Page

class PageListView(ListView):
    model = Page
    template_name = "page_list.html"


def index(request):
    pages = Page.objects.all()

    return render_to_response(
        "page_list.html",
        context={'object_list': pages},
        context_instance=RequestContext(request))

def page(request, page_id):
    page_obj = Page.objects.get(pk=page_id)

    # page_obj.title = "I changed the title"
    # page_obj.save()

    return render_to_response(
        "page.html",
        context={'page': page_obj},
        context_instance=RequestContext(request))