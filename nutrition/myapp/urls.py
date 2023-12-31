from django.contrib import admin
from django.urls import path
from .import views
app_name="main"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('<int:id>/',views.delete,name="del"),
    path("save/",views.insert, name="insert"),
    path("data/",views.SetGoal,name="setgoal"),
    path("register/",views.Registration,name="forms"),
]

