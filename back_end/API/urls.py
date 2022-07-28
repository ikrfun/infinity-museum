"""API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.routers import DefaultRouter
from museum_api.views import ImageViewSet

router = DefaultRouter()
router.register('create_img', ImageViewSet, basename='create_img')

os = ImageViewSet.as_view({
	'get': 'os'
})

urlpatterns = [
	path('admin/', admin.site.urls),
	path('',include(router.urls)),
	# path('create/<int:pk>/', ImageViewSet, name='os'),
	# path('create_img/', CreateImageView.as_view()),
	path('create_img/os/', os, name='os'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

