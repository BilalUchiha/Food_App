from django.shortcuts import render, redirect
from .models import Food, Pay, Order
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import OrderForm, CustomUser
from .decorators import allow_admin
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group


@allow_admin
@login_required(login_url='login')
def dashboard(request):
    foods = Food.objects.all()

    return render(request, 'base/dashboard.html', {'foods': foods})


@login_required(login_url='login')
def food_details(request, pk):
    food = Food.objects.get(id=pk)

    return render(request, 'base/food_details.html', {'food': food})


@allow_admin
@login_required(login_url='login')
def add_food(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        type = request.POST.get('type')
        image = request.FILES.get('image')

        food = Food.objects.create(
            name=name, price=price, type=type, image=image)
        food.save()
        return redirect('/menu')

    return render(request, 'base/add_food.html')


@login_required(login_url='login')
def add_order(request, user, phone, food, price):
    food = Food.objects.get(id=food)
    if request.method == 'POST':
        customer = request.user
        phone = phone
        food = food
        item = request.POST.get('item')
        price = price

        order = Order.objects.create(
            customer=customer, phone=phone, food=food, price=price, item=item)
        order.save()
        return redirect('/menu')

    return render(request, 'base/add_order.html')


def register(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        password = make_password(password)

        user = CustomUser.objects.create(
            username=username, email=email, password=password, mobile=mobile, address=address)
        if Group.objects.filter(name='customer').exists():
            user.groups.add(Group.objects.get(name='customer'))
        else:
            group = Group.objects.create(name='customer')
            user.groups.add(group)

        if user is not None:
            user = user.save()
            return redirect('/login')

    return render(request, 'base/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'base/login.html')


def logout_view(request):
    logout(request)
    return redirect('/login')


@login_required(login_url='/login')
def customer_page(request):
    foods = Food.objects.all()

    return render(request, 'base/customerpage.html', {'foods': foods})


@allow_admin
def orders_page(request):
    orders = Order.objects.all()

    return render(request, 'base/orders.html', {'orders': orders})


@allow_admin
@login_required(login_url='/login')
def all_users_page(request):
    users = CustomUser.objects.all()

    return render(request, 'base/users.html', {'users': users})


@allow_admin
@login_required(login_url='/login')
def delete_user(request, pk):
    user = CustomUser.objects.get(id=pk)

    if user is not None:
        user.delete()
        return redirect('all_users')


@allow_admin
@login_required(login_url='/login')
def edit_user(request, pk):
    user = CustomUser.objects.get(id=pk)

    if request.method == 'POST':
        password = request.POST.get('password')
        password = make_password(password)
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.mobile = request.POST.get('mobile')
        user.password = password

        user.save()

    return render(request, 'base/edit_user.html', {'user': user})


@allow_admin
@login_required(login_url='/login')
def delete_food(request, pk):

    food = Food.objects.get(id=pk)

    if food is not None:
        food.delete()
        return redirect('/')


@allow_admin
@login_required(login_url='/login')
def edit_food(request, pk):

    food = Food.objects.get(id=pk)
    if request.method == 'POST':
        food.name = request.POST.get('name')
        food.price = request.POST.get('price')
        food.type = request.POST.get('type')
        food.image = request.FILES.get('image')
        food.save()

        return redirect('/menu')

    return render(request, 'base/edit_food.html', {'food': food})


@login_required(login_url='/login')
def about_us(request):

    return render(request, 'base/about_us.html')


@login_required(login_url='/login')
def home(request):

    return render(request, 'base/home.html')


@login_required(login_url='/login')
def current_user(request):
    user = request.user

    return render(request, 'base/current_user.html', {'user': user})


@allow_admin
@login_required(login_url='/login')
def add_admin_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        password = make_password(password)

        user = CustomUser.objects.create(
            username=username, email=email, password=password, mobile=mobile, address=address)
        if Group.objects.filter(name='admin').exists():
            user.groups.add(Group.objects.get(name='admin'))
        else:
            group = Group.objects.create(name='admin')
            user.groups.add(group)

        return redirect('/all_users')

    return render(request, 'base/create_admin.html')
