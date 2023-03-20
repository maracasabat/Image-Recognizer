import random

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .models import File, Book, Photo, User
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView, ListView, CreateView
from django.views import View
from .forms import FileForm, BookForm, PhotoForm
from django.urls import reverse_lazy


# Create your views here.
class Home(TemplateView):
    template_name = 'mediauploadapp/index.html'


@login_required
def main(request):
    return render(request, 'mediauploadapp/index.html', {})


""" Add method for the simple upload """


@login_required
def upload(request):
    context = {}
    try:
        if request.method == 'POST':
            uploaded_file = request.FILES['document']
            fs = FileSystemStorage()
            name = fs.save(uploaded_file.name, uploaded_file)
            context['url'] = fs.url(name)
        return render(request, 'mediauploadapp/upload.html', context)
    except KeyError:
        return render(request, 'mediauploadapp/upload.html', {})


""" Add methods for the file upload """


@login_required
def file_list(request):
    files = File.objects.filter(author_id=request.user).all()
    files_video = File.objects.all().filter(category="video", author_id=request.user)
    files_image = File.objects.all().filter(category="image", author_id=request.user)
    files_document = File.objects.all().filter(category="document", author_id=request.user)
    files_music = File.objects.all().filter(category="music", author_id=request.user)
    files_other = File.objects.all().filter(category="other", author_id=request.user)
    return render(request, 'mediauploadapp/file_list.html', {
        'files': files,
        'files_video': files_video,
        'files_image': files_image,
        'files_document': files_document,
        'files_music': files_music,
        'files_other': files_other
    })


@login_required
def file_list_image(request):
    files_image = File.objects.all().filter(category="image", author_id=request.user)
    return render(request, 'mediauploadapp/file_list_image.html', {
        'files_image': files_image,
    })


@login_required
def file_list_video(request):
    files_video = File.objects.all().filter(category="video", author_id=request.user)
    return render(request, 'mediauploadapp/file_list_video.html', {
        'files_video': files_video,
    })


@login_required
def file_list_document(request):
    files_document = File.objects.all().filter(category="document", author_id=request.user)
    return render(request, 'mediauploadapp/file_list_document.html', {
        'files_document': files_document,
    })


@login_required
def file_list_music(request):
    files_music = File.objects.all().filter(category="music", author_id=request.user)
    return render(request, 'mediauploadapp/file_list_music.html', {
        'files_music': files_music,
    })


@login_required
def file_list_other(request):
    files_other = File.objects.all().filter(category="other", author_id=request.user)
    return render(request, 'mediauploadapp/file_list_other.html', {
        'files_other': files_other,
    })


@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.author_id = request.user
            file.save()
            return redirect('file_list')
    else:
        form = FileForm()
    return render(request, 'mediauploadapp/upload_file.html', {
        'form': form
    })


@login_required
def delete_file(request, pk):
    if request.method == 'POST':
        file = File.objects.get(pk=pk, author_id=request.user)
        file.delete()
    return redirect('file_list')


""" Add methods for the book upload """


@login_required
def book_list(request):
    books = Book.objects.filter(author_id=request.user).all()
    return render(request, 'mediauploadapp/book_list.html', {
        'books': books
    })


@login_required
def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.author_id = request.user
            book.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'mediauploadapp/upload_book.html', {
        'form': form
    })


@login_required
def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk, author_id=request.user)
        book.delete()
    return redirect('book_list')


class UploadBookView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('class_book_list')
    template_name = 'mediauploadapp/upload_book.html'


""" Add methods for the photos upload """


@login_required
def photo_list(request):
    photos = Photo.objects.filter(author_id=request.user).all()
    if photos:
        photo = random.choice(photos).file.url
        return render(request, 'mediauploadapp/photo_list_basic.html', {
            'photo': photo
        })
    else:
        return render(request, 'mediauploadapp/photo_list_basic.html', {
            'photo': "https://demofree.sirv.com/nope-not-here.jpg"
        })


class BasicUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.filter(author_id=request.user).all()
        return render(self.request, 'mediauploadapp/basic_upload_photo.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.author_id = request.user
            photo.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return redirect('basic_upload')


class ProgressBarUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.filter(author_id=request.user).all()
        return render(self.request, 'mediauploadapp/progress_bar_upload_photo.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.author_id = request.user
            photo.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


class DragAndDropUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.filter(author_id=request.user).all()
        return render(self.request, 'mediauploadapp/drag_and_drop_upload_photo.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.author_id = request.user
            photo.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


@login_required
def clear_database(request):
    for photo in Photo.objects.filter(author_id=request.user).all():
        photo.file.delete()
        photo.delete()
    return redirect(request.POST.get('next'))


@login_required
def delete_photo(request, pk):
    if request.method == 'POST':
        file = Photo.objects.get(pk=pk, author_id=request.user)
        file.delete()
    return redirect('basic_upload')
