from django.shortcuts import render
from .models import Course, Lesson
from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson, UserProfile


# Create your views here.
def index(request):
    return render(request, "index.html")


def course_list(request):
    courses = Course.objects.all()
    print(courses)
    return render(request, 'course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = Lesson.objects.filter(course=course)
    return render(request, 'course_detail.html', {'course': course, 'lessons': lessons})

def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'lesson_detail.html', {'lesson': lesson})

def user_profile(request, username):
    user_profile = get_object_or_404(UserProfile, user__username=username)
    return render(request, 'user_profile.html', {'user_profile': user_profile})
