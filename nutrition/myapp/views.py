from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import food, Consumed,goal
from django.http import JsonResponse
from .forms import User_Register

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

def delete(request,id):
    data=Consumed.objects.filter(id=id)
    
    if data:
        data.delete()
        return redirect('main:index')
    

    return render(request,'myapp/index.html')

def insert(request):
    if request.method == "POST":
        name = request.POST.get("name")
        carbs = request.POST.get("carbs")
        fats = request.POST.get("fats")
        protien = request.POST.get("protien")
        calories = request.POST.get("calories")

        x =food(name=name, carbs=carbs, protien=protien, fat=fats, calories=calories)
        x.save()

    return redirect('main:index')


def SetGoal(request):
    if request.method=="POST":
        user = request.user
        calories = request.POST.get("setgoal")

        # Assuming you have a Goal model with fields user, date, and daily_goal
        goal_instance = goal(user=user, date="", daily_goal=calories)
        goal_instance.save()

        # Send JSON response with the goal data
        response_data = {
            'success': True,
            'calories': calories,
        }

        return redirect('main:index')



def Registration(request):
    if request.method=="POST":
        user_form=User_Register(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:index')
    else:
        user_form=User_Register()
    
    return render(request,'myapp/register.html',{'form':user_form})
