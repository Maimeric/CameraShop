from django.contrib import admin

from catalog import models
from .models import Order, OrderItem

admin.site.register(models.Camera)
admin.site.register(models.CameraImg)
admin.site.register(models.Comments)
admin.site.register(models.Categories)
admin.site.register(models.Basket)
admin.site.register(models.CameraInstance)
admin.site.register(OrderItem)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
