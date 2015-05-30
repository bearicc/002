from django.shortcuts import render


def home(request):
    return render(request, 'webgl/webgl.html')


def cube(request):
    return render(request, 'webgl/cube.html')


def cube_sphere(request):
    return render(request, 'webgl/cube_sphere.html')
