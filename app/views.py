from django.shortcuts import render

# Create your views here.
def hi(request):
    return render(request,'hi.html')
def child(request):
    return render(request,'child.html')
    