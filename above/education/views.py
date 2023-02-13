from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render

from education.models import Course, Contact
from education.forms import ContactFrom


def index(request):
    courses_qs = Course.objects.all()

    context = {
        'title': 'Above Site',
        'courses': courses_qs,
    }
    return render(request, "education/index.html", context)


def about_us(request):
    context = {
        'title': 'About Us',
    }
    return render(request, "education/about_us.html", context)


def courses(request):
    courses_qs = Course.objects.all()

    context = {
        'title': 'Courses',
        'courses': courses_qs,
    }
    return render(request, "education/courses.html", context)


def portfolio(request):
    context = {
        'title': 'Portfolio',
    }
    return render(request, "education/portfolio.html", context)


def pricing(request):
    context = {
        'title': 'Pricing',
    }
    return render(request, "education/pricing.html", context)


def contact(request):
    if request.method == 'POST':
        form = ContactFrom(request.POST)
        if form.is_valid():
            contact_model = form.save()
            messages.add_message(request, messages.SUCCESS, "Your request was sent successfully")
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        form = ContactFrom()

    context = {
        'title': 'Contact',
        'form': form,
    }
    return render(request, "education/contact.html", context)


def course(request, course_id):
    course_ = Course.objects.filter(id=course_id).first()
    if not course_:
        raise Http404()

    context = {
        'title': course_.name,
        'course': course_,
    }
    return render(request, "education/course.html", context)
