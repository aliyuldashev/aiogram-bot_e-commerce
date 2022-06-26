from django.contrib import admin

# Register your models here.
from .models import User, Product, Buyurtma, oshxonalar,First_tag,Second_tag

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Buyurtma)
admin.site.register(oshxonalar)
admin.site.register(First_tag)
admin.site.register(Second_tag)


