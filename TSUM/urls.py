"""TSUM URL Configuration

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
from CUM import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('category', views.CategoryViewSet)
router.register('item', views.ItemViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/category/', views.CategoryViewSet.as_view(), name = 'category'),
    path('api/item/', views.ItemViewSet.as_view(), name = 'item'),
    path('api/item_name/<int:pk>', views.ItemRetrieveUpdateDelete.as_view(), name = 'item_name_detail'),
    path('api/', include(router.urls))
]
