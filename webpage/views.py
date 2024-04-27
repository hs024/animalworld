from django.shortcuts import render
from .models import animals
# Create your views here.
def index(request):
    name_list=[]
    photo_list=[]
    des_list=[]
    a=animals.objects.all()
    for i in a:
        photo_list.append(i.photo_bg)
        des_list.append(i.description)
        name_list.append(i.name)
    context={
        "name_list":name_list,
        "photo_list":photo_list,
        "des_list":des_list,
    }
    zipped_list = zip(name_list, des_list, photo_list)
    # return render(request,"index.html",context=context)
    return render(request,"index.html",{"ziplist":zipped_list,"imgnamelist":zip(photo_list,name_list)})