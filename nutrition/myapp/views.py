from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import food, Consumed

@login_required
def index(request):
    if request.method == "POST":
        consumed_food_name = request.POST.get("consumed_food")
        consumed_food = get_object_or_404(food, name=consumed_food_name)

        active_user = request.user

        consumed_entry = Consumed(user=active_user, consumed=consumed_food)
        consumed_entry.save()

        # We were facing a problem of repeating object when we click add button one object get added 
        #to the data base becouse url was not chaning to fix that problem we redirect to index after 
        #we save one data at time to the database then redirect to main url.
        return redirect('main:index') 
    # Fetch all food items regardless of the request method
    else:
        data = food.objects.all()
    # Fetch consumed food by the user
    consumed_food_by_user = Consumed.objects.filter(user=request.user)

    return render(request, 'myapp/index.html', {'food': data, 'consumed_food': consumed_food_by_user})
