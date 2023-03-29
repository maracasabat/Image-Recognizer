import gdown
from os.path import exists

if not exists("mediauploadapp/model/model_cifar10.h5"):
    url = 'https://drive.google.com/file/d/1-oVU8YGdNXper8XTQCKj5Up67q0PTPFA/view?usp=sharing'
    output1 = "mediauploadapp/model/model_cifar10.h5"
    gdown.download(url, output1, quiet=False, fuzzy=True)


if not exists("mediauploadapp/model/model_cifar100.h5"):
    url = 'https://drive.google.com/file/d/1wGkwfOPPQQFDv-Ka8SpX1pJcwo-ks8yx/view?usp=sharing'
    output2 = "mediauploadapp/model/model_cifar100.h5"
    gdown.download(url, output2, quiet=False, fuzzy=True)

CIFAR10 = "mediauploadapp/model/model_cifar10.h5"
CIFAR100 = "mediauploadapp/model/model_cifar100.h5"
