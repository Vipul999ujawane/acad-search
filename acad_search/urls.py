"""acad_search URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from acads import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^upload/',views.upload,name="upload"),
    url(r'^$',views.home),
    url(r'^success/',views.success),
    url(r'^get_sub_list/(?P<dept>\D+)/$',views.get_sub_list),
    url(r'^files/(?P<dept>\D+)/(?P<year>\w+)/$',views.get_files),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
