import logging

from django.http import Http404
from django.shortcuts import render
from .models import *

# Create your views here.

logger = logging.getLogger('django')


def courses(request):
    '''课程页'''
    courses = Course.objects.only('title', 'cover_url', 'teacher__positional_title').filter(is_delete=False)
    context = {
        'courses': courses
    }
    return render(request, 'course/course.html', context=context)


def couresDetail(request, course_id):
    '''课程详情'''
    course = Course.objects.only('title', 'cover_url', 'video_url', 'profile', 'outline', 'teacher__name',
                                        'teacher__profile', 'teacher__positional_title',
                                        'teacher__avatar_url').select_related('teacher').filter(is_delete=False,
                                                                                                id=course_id).first()
    if course:
        return render(request, 'course/course_detail.html', locals())
    else:
        raise Http404('page not found')
