import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Photo, User
from django.views.generic import TemplateView
from django.views import View
from .forms import PhotoForm
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from gpt_index.indices.tree.base import GPTTreeIndex

CIFAR10 = 'mediauploadapp/model/model_best_V.h5'
CIFAR100 = 'mediauploadapp/model/best_result_cifar100.h5'
CIFAR10_CATEGORIES = ['airplane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
CIFAR100_CATEGORIES = ['apple', 'aquarium_fish', 'baby', 'bear', 'beaver', 'bed', 'bee',
                       'beetle', 'bicycle', 'bottle', 'bowl', 'boy', 'bridge', 'bus',
                       'butterfly', 'camel', 'can', 'castle', 'caterpillar', 'cattle',
                       'chair', 'chimpanzee', 'clock', 'cloud', 'cockroach', 'couch',
                       'crab', 'crocodile', 'cup', 'dinosaur', 'dolphin', 'elephant',
                       'flatfish', 'forest', 'fox', 'girl', 'hamster', 'house',
                       'kangaroo', 'keyboard', 'lamp', 'lawn_mower', 'leopard', 'lion',
                       'lizard', 'lobster', 'man', 'maple_tree', 'motorcycle',
                       'mountain', 'mouse', 'mushroom', 'oak_tree', 'orange', 'orchid',
                       'otter', 'palm_tree', 'pear', 'pickup_truck', 'pine_tree',
                       'plain', 'plate', 'poppy', 'porcupine', 'possum', 'rabbit',
                       'raccoon', 'ray', 'road', 'rocket', 'rose', 'sea', 'seal',
                       'shark', 'shrew', 'skunk', 'skyscraper', 'snail', 'snake',
                       'spider', 'squirrel', 'streetcar', 'sunflower', 'sweet_pepper',
                       'table', 'tank', 'telephone', 'television', 'tiger', 'tractor',
                       'train', 'trout', 'tulip', 'turtle', 'wardrobe', 'whale',
                       'willow_tree', 'wolf', 'woman', 'worm']


# Create your views here.
class Home(TemplateView):
    template_name = 'mediauploadapp/index.html'


@login_required
def main(request):
    return render(request, 'mediauploadapp/index.html', {})


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


class DataBasePhotosList(View):
    def get(self, request):
        photos_list = Photo.objects.filter(author_id=request.user).all()
        return render(self.request, 'mediauploadapp/photo_list_basic.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.author_id = request.user
            photo.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return redirect('photo_list')


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


""" Add methods for CIFAR10 Predictions """


class BasicUploadViewCifar10(View):
    photo = ""

    def get(self, request):
        photos_list = Photo.objects.filter(author_id=request.user).all()
        return render(self.request, 'mediauploadapp/basic_upload_photo_cifar10.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.author_id = request.user
            photo.save()
            self.photo = photo.file.url
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}

        predict_pictures = predict_cifar(CIFAR10, self.photo, CIFAR10_CATEGORIES)

        return render(request, 'pages/imageClassifier.html', {'predict_pictures': predict_pictures, 'photo': self.photo})


@login_required
def predict_cifar10_dropdown(request, pk):
    if request.method == 'POST':
        file = Photo.objects.get(pk=pk, author_id=request.user)

        predict_pictures = predict_cifar(CIFAR10, file.file.url, CIFAR10_CATEGORIES)

    return render(request, 'pages/imageClassifier.html', {'predict_pictures': predict_pictures})


""" Add methods for CIFAR100 Predictions """


class BasicUploadViewCifar100(View):
    photo = ""

    def get(self, request):
        photos_list = Photo.objects.filter(author_id=request.user).all()
        return render(self.request, 'mediauploadapp/basic_upload_photo_cifar100.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.author_id = request.user
            photo.save()
            self.photo = photo.file.url
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}

        predict_pictures = predict_cifar(CIFAR100, self.photo, CIFAR100_CATEGORIES)

        return render(request, 'pages/imageClassifier.html', {'predict_pictures': predict_pictures, 'photo':self.photo})


@login_required
def predict_cifar100_dropdown(request, pk):
    if request.method == 'POST':
        file = Photo.objects.get(pk=pk, author_id=request.user)

        predict_pictures = predict_cifar(CIFAR100, file.file.url, CIFAR100_CATEGORIES)

    return render(request, 'pages/imageClassifier.html', {'predict_pictures': predict_pictures})


def predict_cifar(best_model, img_url, categories):
    model = load_model(best_model)

    img = keras.preprocessing.image.load_img('mediauploadapp' + img_url, target_size=(32, 32))
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)
    class_names = categories
    predict_pictures = class_names[np.argmax(predictions[0])]

    return predict_pictures


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


""" Add Chat bot based on Deep Learning with Python Book """
@login_required
def dl_chat_bot(request):
    index = GPTTreeIndex.load_from_disk('mediauploadapp/model/index.json')
    prompt = request.GET.get('prompt')
    if prompt:
        response = index.query(prompt)
    else:
        response = "..."
    return render(request, 'mediauploadapp/dl_chat_bot.html', {'response': response})
