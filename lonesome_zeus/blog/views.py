from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic import ListView

from blog.forms import PageForm
from .models import Page


class PageListView(ListView):
    model = Page
    template_name = "page_list.html"


def index(request):
    pages = Page.objects.all()

    return render_to_response(
        "page_list.html",
        context={'object_list': pages})


def page(request, page_id):
    page_obj = Page.objects.get(pk=page_id)

    # page_obj.title = "I changed the title"
    # page_obj.save()

    return render_to_response(
        "page.html",
        context={'page': page_obj})


def page_edit(request, page_id):
    page_obj = Page.objects.get(pk=page_id)
    if request.method == "POST":
        form = PageForm(request.POST, instance=page_obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = "TESTTEST"
            obj.save()
            return HttpResponseRedirect(reverse("page_detail", kwargs={"page_id": page_obj.id}))
    else:
        form = PageForm(instance=page_obj)

    context = {"form": form, "page_obj": page_obj}
    return render_to_response("page_edit.html", context)