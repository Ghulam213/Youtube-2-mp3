import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import YoutubeForm
from .youtubeConverter import youtubeConverter

# Create your views here.


title = ""


def index(request):
    global title
    form = YoutubeForm()
    if request.method == "POST":
        filled_form = YoutubeForm(request.POST)
        title = youtubeConverter(filled_form.get_url())
        return redirect("Youtube2Audio:thankYou")
    return render(request, "Youtube2Audio/index.html", context={"form": form})


def download(request):
    file_path = os.path.join(settings.MEDIA_ROOT, f"Youtube2Audio\\download\\{title}.mp3")
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="audio/mpeg")
            response['Content-Disposition'] = f"attachment; filename={title}.mp3"
            return response
    return HttpResponse("file not found")


def thankYou(request):
    return render(request, "Youtube2Audio/thanks.html")

