from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone


class Camera(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    cost = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.CharField(max_length=2000, blank=True, null=True)
    short_description = models.CharField(max_length=50, blank=True, null=True)
    viewing_angle = models.IntegerField(blank=True, null=True)
    video_resolution = models.IntegerField(blank=True, null=True)
    carcass = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_instance_count(self):
        return self.camerainstance_set.filter(status='s').count()


class CameraImg(models.Model):
    img = models.URLField()
    Camera = models.ForeignKey('Camera', on_delete=models.CASCADE, related_name='imgs', blank=True, null=True)

    def __str__(self):
        return self.Camera.title


class Comments(models.Model):
    camera = models.ForeignKey(Camera, on_delete=models.SET_NULL, related_name='comment', blank=False, null=True)
    sender = models.ForeignKey(User, blank=False, null=True, on_delete=models.CASCADE)
    text = models.TextField('Комментарий', blank=True, null=True)
    pub_date = models.DateTimeField('Дата комментария', default=timezone.now)

    def __str__(self):
        return self.sender.username


class Categories(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    camera = models.ManyToManyField(Camera, related_name='category')

    def __str__(self):
        return self.name


class CameraInstance(models.Model):
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)
    STATUS = (
        ('s', 'In stok'),
        ('b', 'Booked')
    )
    status = models.CharField(choices=STATUS, max_length=1, default='s')

    def __str__(self):
        return "{0} ({1})".format(self.camera.title, self.get_status_display())


class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Camera, blank=True)

    def __str__(self):
        return self.user.username


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Orders'
        verbose_name_plural = 'Order'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Camera, related_name='order_items', on_delete=models.SET_NULL, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
