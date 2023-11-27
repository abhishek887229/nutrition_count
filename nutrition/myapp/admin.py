from django.contrib import admin
from .models import food,Consumed,goal
# Register your models here.
admin.site.register(food)

admin.site.register(Consumed)
admin.site.register(goal)