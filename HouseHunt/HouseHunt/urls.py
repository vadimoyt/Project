"""
URL configuration for HouseHunt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from catalog.views import BuildingDetail, CreateBuilding, ListOfMyBuilding, DeleteMyObject, UpdateMyBuilding, sorted_building, BuildingList
from django.conf import settings
from django.conf.urls.static import static
from user.views import register, login_view, logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BuildingList.as_view(), name='index'),
    path('building/<int:pk>', BuildingDetail.as_view(), name='building'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('creation/', CreateBuilding.as_view(), name='creation'),
    path('my_catalog/<int:pk>', ListOfMyBuilding.as_view(), name='my_catalog'),
    path('delete/<int:pk>', DeleteMyObject.as_view(), name='delete'),
    path('change_data/<int:pk>', UpdateMyBuilding.as_view(), name='change_data'),
    path('sorted_building/', sorted_building, name='sorted_building')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)