from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# from newsapp.views import get_news
# from book_app.views import main as phonebook_main
# from note_app.views import main as note_main
# from mediauploadapp.views import main as media_main


# # Create your views here.
@login_required
def homepage(request):
    # return render(request, "main/homePage.html")
    return render(request, "main/galleryPage.html")
    # return redirect(get_news)


#
#
@login_required
def phonebook_page(request):
    # return render(request, "main/phoneBookPage.html")
    return render(request, "main/galleryPage.html")


#
#
@login_required
def notebook_page(request):
    # return render(request, "main/noteBookPage.html")
    return render(request, "main/galleryPage.html")


@login_required
def gallery_page(request):
    return render(request, "main/galleryPage.html")
    # return redirect(media_main)


@login_required
def settings_page(request):
    return render(request, "main/settingsPage.html")
