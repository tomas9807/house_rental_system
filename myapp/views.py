from django.shortcuts import render
import os
# Create your views here.
def home(request):
    myapp_dir = os.path.dirname(os.path.abspath(__file__))
    houses_dir = os.path.join(myapp_dir,'static/myapp/imgs/houses/')
    context = {'list_imgs': [img if str(img).lower().endswith('jpg' or 'png' or 'jpeg') else None for img in os.listdir(houses_dir)]}
    return render(request,'myapp/home.html',context)