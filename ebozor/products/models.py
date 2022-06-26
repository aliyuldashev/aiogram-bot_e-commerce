from django.db import models

# Create your models here.
class oshxonalar(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=200)
    product = models.ForeignKey('Product', on_delete=models.DO_NOTHING,null=True, verbose_name='Maxsulotlar')
    delivary_payment = models.BigIntegerField(verbose_name='dastavka narxi', default=0)
    delivary_zero = models.BigIntegerField(verbose_name='dastavka limit', default=0)
    def __str__(self):
        return self.name
class User(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(verbose_name="Ism", max_length=100)
    telegram_id = models.BigIntegerField(verbose_name='Telegram ID', unique=True, default=1)
    oshxona = models.ForeignKey('oshxonalar',verbose_name='Oshxona',on_delete=models.DO_NOTHING, default=None)
    def __str__(self):
        return f"{self.id} - {self.telegram_id} - {self.full_name}"

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    productname = models.CharField(verbose_name="Mahsulot nomi", max_length=50)
    photo = models.ImageField(verbose_name="Rasm file_id",upload_to='images', null=True)
    price = models.BigIntegerField(verbose_name="Narx")
    description = models.TextField(verbose_name="Mahsulot haqida", max_length=3000, null=True)
    first_tag = models.ForeignKey('First_tag', verbose_name='Birinchi Turini', default=None,on_delete=models.DO_NOTHING)
    second_tag = models.ForeignKey('Second_tag',verbose_name='Ikkinchi turini:', default=0,null=True,on_delete=models.DO_NOTHING)
    def __str__(self):
        return f"№{self.id} - {self.productname}"

class Buyurtma(models.Model):
    id = models.AutoField(primary_key=True)
    zakaz_name = models.CharField(verbose_name="Mahsulot nomi", max_length=50)
    m_price = models.DecimalField(verbose_name="Maxsulot narxi kg(da)", decimal_places=2, max_digits=8)
    m_soni = models.PositiveIntegerField(verbose_name="Buyurtma miqdori (kg) da")
    s_price = models.DecimalField(verbose_name="Umumiy Narx", decimal_places=2, max_digits=10)
    m_name = models.CharField(verbose_name="MIjoz nomi", max_length=50)
    m_tel = models.CharField(verbose_name="MIjoz telefon raqami", max_length=13)
    m_man = models.CharField(verbose_name="Yetkazib berish manzili nomi", max_length=50)
    m_agent = models.CharField(verbose_name="Agent nomi", max_length=50,)
    m_time = models.DateTimeField(auto_now_add=True,verbose_name="Buyurma vaqti")
    agent_id = models.BigIntegerField(verbose_name='Telegram ID', unique=False, default=1)
    t_turi = models.CharField(verbose_name="To`lov turi", max_length=50)
    def __str__(self):
        return f"№{self.id} - {self.zakaz_name}-{self.m_soni}-{self.s_price}"
class First_tag(models.Model):
    name = models.CharField(max_length=200,unique=True)
    def __str__(self):
        return self.name
class Second_tag(models.Model):
    name = models.CharField(max_length=200,unique=True)
    def __str__(self):
        return self.name