from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    category =models.CharField(("kategoris"), max_length=50)
    link =models.CharField(("link"), max_length=50,blank=True)

    def __str__(self):
        return self.category

class Product(models.Model):
    product_category =models.ForeignKey(Category, verbose_name=("Ürün_Kategorisi"), on_delete=models.CASCADE)
    product_name =models.CharField(("ismi"), max_length=50)
    product_content=models.CharField(("açıklama"), max_length=50)
    product_price =models.PositiveIntegerField(("fiyat"))
    product_image =models.FileField(("resmi"), upload_to='Photos', blank=True,max_length=100)
    product_image2 =models.FileField(("resm2"), upload_to='Photos',blank=True,null=True, max_length=100)
    product_stok =models.PositiveIntegerField(("stok"),default=1)

    def __str__(self):
        return self.product_name
    
class About(models.Model):
    about_title =models.CharField(("title"), max_length=50)
    about_image =models.FileField(("resim"), upload_to='Photos', max_length=100)
    about_content =models.TextField(("content start"))
    about_content1 =models.TextField(("content center"),blank=True,null=True)
    about_content2 =models.TextField(("content end"),blank=True,null=True)
    about_fb =models.URLField(("https://www.facebook.com/"), max_length=200)
    about_x =models.URLField((" https://x.com/"), max_length=200)
    about_linkedin =models.URLField(("linkedin"), max_length=200)
    about_site =models.URLField(("http://127.0.0.1:8000/"), max_length=200)

    def __str__(self) -> str:
        return self.about_title
    
class Employee(models.Model):
    employee_image =models.FileField(("image"), upload_to='Photos', max_length=100)
    employee_fb =models.URLField(("https://www.facebook.com/"), max_length=200)
    employee_x =models.URLField((" https://x.com/"), max_length=200)
    employee_linkedin =models.URLField(("linkedin"), max_length=200)
    employee_site =models.URLField(("http://127.0.0.1:8000/"), max_length=200)
    employee_name =models.CharField(("isim"), max_length=50)
    employee_duty =models.CharField(("görevi"), max_length=50)

    def __str__(self) -> str:
        return self.employee_name
    
class Services(models.Model):
    service_title =models.CharField(("title"), max_length=50)
    service_content =models.CharField(("content"),blank=True, max_length=50)
    service_image =models.FileField(("image"), upload_to='Photos', max_length=100)

    def __str__(self) -> str:
        return self.service_title

class Comment(models.Model):
    comment_username =models.ForeignKey(User, verbose_name=("kullanıcı_adi"), related_name='k_adi',on_delete=models.CASCADE)
    post =models.ForeignKey(Product, verbose_name=("nereye"),related_name='productdetail',blank=True,null=True, on_delete=models.CASCADE)
    comment_message =models.TextField(())
    comment_date =models.DateField(("yorum_saati"), auto_now=True)

    def __str__(self) -> str:
        return self.comment_username.username
    
class ExpPhoto(models.Model):
    explore_title=models.CharField(("title"),blank=True, max_length=50)
    explore_title2=models.CharField(("title2"),blank=True, max_length=50)
    image=models.FileField(("image"),blank=True, upload_to='Explore', max_length=100)

class Explore(models.Model):
    explore_first_title =models.CharField(("title_first"), blank=True,null=True,max_length=50)
    explore_content1=models.TextField(("content1"),blank=True, max_length=500)
    explore_content2=models.TextField(("content2"),blank=True, max_length=500)
    explore_content3=models.TextField(("content3"),blank=True, max_length=500)
    explore_content4=models.TextField(("content4"),blank=True, max_length=500)


    

class Sosial_media(models.Model):
    sosial_link =models.URLField(("Link"), max_length=200)
    sosial_title =models.CharField(("title"), max_length=50)
    sosial_image =models.FileField(("image"), upload_to='Sosial', max_length=100)

    def __str__(self) -> str:
        return self.sosial_title