from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('api/get/list/num/', views.get_num_list),
    # path('admin/', admin.site.urls),
]