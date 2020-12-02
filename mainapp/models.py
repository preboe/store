from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse



User = get_user_model()



def get_product_url(obj,viewname, model_name):
    ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})


class MinResolutionErrorException(Exception):

    pass


class MaxResolutionErrorException(Exception):

    pass


class LatestProductsManager:

    @staticmethod
    def get_products_for_main_page(*args, **kwargs):
        with_respect_to = kwargs.get('with_respect_to')
        products = []
        ct_models = ContentType.objects.filter(models_in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().ordel_by('-id')[:10]
            products.extend(model_products)
        if with_respect_to:
            ct_models = ContentType.objects.filter(model=with_respect_to)
            if ct_models.extra():
                if with_respect_to in args:
                    return sorted(products, key=lambda x: x.__class__._mata.model_name.startswith(with_respect_to),
                                  reverse=True)
        return products








class LatestProducts:

    abjects = LatestProductsManager()


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name




class Product(models.Model):

    MIN_RESOLUTION = (400, 400)
    MAX_RESOLUTION = (400, 400)
    MAX_IMAGE_SIZE = 3145728


    class Meta:
        abstract = True


    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименования')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображения')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title




#мыло
class soap(Product):
    the_brand = models.CharField(max_length=255, verbose_name='Бренд')
    composition = models.CharField(max_length=255, verbose_name='Состав')
    year_creation = models.CharField(max_length=255, verbose_name='Год создание')
    porfumer = models.CharField(max_length=255, verbose_name='Порфюмер')
    country = models.CharField(max_length=50, verbose_name='Страна')


    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')





#косметика
class cosmetics(Product):
    the_brand = models.CharField(max_length=255, verbose_name='Бренд')
    composition = models.CharField(max_length=255, verbose_name='Состав')
    year_creation = models.CharField(max_length=255, verbose_name='Год создание')
    porfumer = models.CharField(max_length=255, verbose_name='Порфюмер')
    country = models.CharField(max_length=50, verbose_name='Страна')


    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')




#парфюм
class perfume(Product):
    tas_notes = models.CharField(max_length=255, verbose_name='Базовые ноты')
    the_brand = models.CharField(max_length=255, verbose_name='Бренд')
    year_creation = models.CharField(max_length=255, verbose_name='Год создание')
    group = models.CharField(max_length=255, verbose_name='Группа')
    porfume = models.CharField(max_length=255, verbose_name='Порфюмер')
    floor = models.CharField(max_length=255, verbose_name='Пол')
    top_notes = models.CharField(max_length=255, verbose_name='Верхние ноты')
    middle_notes = models.CharField(max_length=255, verbose_name='Средние ноты')
    country = models.CharField(max_length=50, verbose_name='Страна')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')




class CartProduct(models.Model):

    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Карзина', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return "Продукт: {} (для карзины)".format(self.product.title)





class Cart(models.Model):

    owner = models.ForeignKey('Customer', verbose_name='Владелиц', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return str(self.id)





class Customer(models.Model):


    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.CharField(max_length=255, verbose_name='Адрес')

    def __str__(self):
        return "Пользователь {} {}".format(self.user.first_name, self.user.last_name)



class Specification(models.Model):

    pass

    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField()
    # name = models.CharField(max_length=255, verbose_name='Имя товара для хоротеристики')
    #
    # def __str__(self):
    #     return "Харатеристики для товара: {}".format(self.name)