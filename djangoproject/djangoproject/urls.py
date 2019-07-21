"""everest-hack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


from account import views
from django.views.generic import TemplateView

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$',  TemplateView.as_view(template_name='index.html')),
    url(r'^register-student/',TemplateView.as_view(template_name='student/register.html')),
    url(r'^register-institute/',  TemplateView.as_view(template_name='institute/register.html')),
    url(r'^institute-registration', views.register_institute),
    url(r'^student-registration', views.register_student),
    url(r'^student-dashboard', views.student_dashboard),
    url(r'^institute-dashboard', views.institute_dashboard),
    url(r'^institute/profile/(?P<id>\d+)/', views.institute_profile),
    url(r'^student/profile/(?P<id>\d+)/', views.student_profile),
    url(r'^login', views.login),
    url(r'^apply', views.apply),
    url(r'^open-admission', views.open_admission),
    url(r'^close-admission', views.close_admission),
    url(r'^logout/', views.logout),
]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
