from django.shortcuts import render
from django.http import Http404, HttpResponse
from . import models


def index(request):
    courses = models.Course.objects.all()
    return render(request, 'shop/courses.html', {'courses': courses})


def single_course(request, course_id):
    try:
        course = models.Course.objects.get(pk=course_id)
        return render(request, 'shop/single_course.html', {'course': course})
    except models.Course.DoesNotExist:
        raise Http404()
