from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# # Create your views here.
@login_required
def homepage(request):
    return render(request, "pages/about.html")


@login_required
def image_classifier(request):
    return render(request, "pages/imageClassifier.html")


@login_required
def image_generator(request):
    return render(request, "pages/imageGenerator.html")


@login_required
def settings_page(request):
    return render(request, "pages/settings.html")


@login_required
def team(request):
    return render(request, "pages/team.html")
