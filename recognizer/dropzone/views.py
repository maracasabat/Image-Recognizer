from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Image


# Create your views here.

class DropzoneView(TemplateView):
    template_name = 'pages/imageClassifier.html'


def file_upload_view(request):
    if request.method == 'POST':
        my_file = request.FILES.get('file')
        Image.objects.create(image=my_file)
        # print(request.FILES)
        return HttpResponse('')
    return JsonResponse({'post': 'false'})
