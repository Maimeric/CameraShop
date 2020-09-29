from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from .models import CameraImg, Camera, Comments, Categories, Basket, CameraInstance


def get_all_camers():
    return Camera.objects.all()


def get_camera_by_id(camera_id):
    return Camera.objects.filter(id=camera_id).get()


def get_all_category():
    return Categories.objects.all()


def get_camers_by_category(category_id):
    return Camera.objects.filter(category=category_id).all()


def get_user_cameras(user_id):
    return Camera.objects.filter(basket__user_id=user_id)


def create_basket(user_name):
    user = User.objects.get(username=user_name)
    basket = Basket(user_id=user.id)
    basket.save()


def add_to_cart(user, camera_id):
    basket = Basket.objects.get(user_id=user.id)
    camera = Camera.objects.get(id=camera_id)
    basket.product.add(camera)
    basket.save()


def remove_from_cart(user, camera_id):
    basket = Basket.objects.get(user_id=user.id)
    camera = Camera.objects.get(id=camera_id)
    basket.product.remove(camera)
    basket.save()


def change_instance_status(camera_id):
    try:
        instance = CameraInstance.objects.filter(camera_id=camera_id, status='s').first()
        instance.status = 'b'
        instance.save()
        return True
    except ObjectDoesNotExist:
        return None


def get_all_cameras_from_basket(request):
    return Camera.objects.filter(User=request.user.id).all()
