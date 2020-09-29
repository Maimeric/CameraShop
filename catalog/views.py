from django.contrib import auth
from django.contrib.auth import authenticate, login

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from catalog import services
from catalog.form import SignUpForm, CommentForm, OrderCreateForm
from catalog.models import Camera, Comments, OrderItem, Basket


def home(request):
    category = services.get_all_category()
    camera = services.get_all_camers()
    return render(request, 'catalog/home_page.html', {'camera': camera,
                                                      'category': category})


def category(request, category_id):
    category = services.get_all_category()
    camera = services.get_camers_by_category(category_id)
    return render(request, 'catalog/home_page.html', {'camera': camera,
                                                      'category': category})


def camera_page(request, camera_id):
    camera = services.get_camera_by_id(camera_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comments()
            comment.camera = camera
            comment.sender = auth.get_user(request)
            comment.text = form.cleaned_data['comment_area']
            comment.save()
        return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()
        comments = camera.comment.all()

    return render(request, 'catalog/camera_page.html', {'camera': camera, 'comment': comments,
                                                        'form': form})


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            my_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=my_password)
            login(request, user)
            basket = services.create_basket(username)
            return redirect('home')
        return render(request, 'registration/registration.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'registration/registration.html', {'form': form})


def basket(request, user_id):
    cameras = services.get_user_cameras(user_id)
    if cameras:
        cost = 0
        for camera in cameras:
            cost += camera.cost
        return render(request, 'catalog/basket.html', context={'cameras': cameras, 'cost': cost})
    else:
        return redirect('home')


def add_to_cart(request, camera_id):
    services.add_to_cart(request.user, camera_id)
    return redirect('home')
    # return redirect('basket', user_id=request.user.id)


def remove_from_cart(request, camera_id):
    services.remove_from_cart(request.user, camera_id)
    return redirect('basket', user_id=request.user.id)


def order_create(request):
    cart = services.get_user_cameras(request.user.id)
    price = 0
    for item in cart:
        price += item.cost
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item,
                                         price=item.cost,
                                         quantity=1,
                                         )
                services.change_instance_status(item.id)

            return render(request, 'catalog/successful_order.html',
                          {'order': order})
        else:
            return redirect('order_create')
    else:
        form = OrderCreateForm

    return render(request, 'catalog/order_page.html',
                  {'cart': cart, 'form': form, 'price': price})
