import gdown
from os.path import exists

from django.conf import settings

if not exists(settings.BASE_DIR / "mediauploadapp/model/model_cifar10.h5"):
    url = 'https://drive.google.com/file/d/1-oVU8YGdNXper8XTQCKj5Up67q0PTPFA/view?usp=sharing'
    output1 = settings.BASE_DIR / "mediauploadapp/model/model_cifar10.h5"
    gdown.download(url, output1, quiet=False, fuzzy=True)


if not exists(settings.BASE_DIR / "mediauploadapp/model/model_cifar100.h5"):
    url = 'https://drive.google.com/file/d/1wGkwfOPPQQFDv-Ka8SpX1pJcwo-ks8yx/view?usp=sharing'
    output2 = settings.BASE_DIR / "mediauploadapp/model/model_cifar100.h5"
    gdown.download(url, output2, quiet=False, fuzzy=True)

CIFAR10 = settings.BASE_DIR / "mediauploadapp/model/model_cifar10.h5"
CIFAR100 = settings.BASE_DIR / "mediauploadapp/model/model_cifar100.h5"