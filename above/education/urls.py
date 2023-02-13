from django.urls import path
from . import views

# register app here
app_name = "education"

urlpatterns = [
    path('', views.index, name="index"),
    path('about_us/', views.about_us, name="about_us"),
    path('courses/', views.courses, name="courses"),
    path('contact/', views.contact, name="contact"),
    path('pricing/', views.pricing, name="pricing"),
    path('portfolio/', views.portfolio, name="portfolio"),

    path('course/<int:course_id>', views.course, name="course")
]
