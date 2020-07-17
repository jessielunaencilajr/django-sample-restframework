"""management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from schools import views

# from rest_framework import routers
# router = routers.DefaultRouter()
# router.register('schools', views.SchoolViewSet)
# router.register('students', views.StudentViewSet)

from rest_framework_nested import routers
router = routers.SimpleRouter()
router.register('schools', views.SchoolViewSet)
router.register('students', views.StudentViewSet)

school_router = routers.NestedSimpleRouter(router, 'schools', lookup='schools')
school_router.register('students', views.StudentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(school_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
