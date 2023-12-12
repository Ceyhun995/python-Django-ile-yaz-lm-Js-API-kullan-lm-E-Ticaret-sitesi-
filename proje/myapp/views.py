from django.shortcuts import render, redirect
from .models import *
from .form import *

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# json
from django.http import JsonResponse


def index(request):
    context = {}
    model = Product.objects.all()

    explores = Explore.objects.all().order_by('?')

    sosials =Sosial_media.objects.all().order_by('?')

    model_type = request.GET.get("filtrele")

    if model_type == "erkek":
        model = Product.objects.filter(product_category__category= "Erkek")
        context["only_men"] = True

    elif model_type == "kadın":
        model = Product.objects.filter(product_category__category= "Kadın")
        context["only_women"] = True

    elif model_type == "cocuk":
        model = Product.objects.filter(product_category__category="Cocuk")
        context["only_kids"] = True

    context["model"] = model
    mens=Product.objects.filter(product_category__category= "Erkek")
    context["mens"]=mens

    womens =Product.objects.filter(product_category__category="Kadın")
    context["womens"]=womens

    kids = Product.objects.filter(product_category__category="Cocuk")
    context["kids"]=kids

    context["explores"]=explores
    context['sosials']=sosials

    return render(request, "index.html", context)


def about(request):
    context = {}

    aboutpage = About.objects.all()
    employess = Employee.objects.all()
    services = Services.objects.all()

    context["aboutpage"] = aboutpage
    context["employess"] = employess
    context["services"] = services
    return render(request, "about.html", context)


def contact(request):
    return render(request, "contact.html")


def products(request):
    context = {}

    urunler = Product.objects.all()

    context["urunler"] = urunler
    return render(request, "products.html", context)


def productdetail(request, urunid):
    context = {}
    detail = Product.objects.filter(id=urunid).first()

    if detail is None:
        return redirect("cikis")

    else:
        context["detail"] = detail

    if request.method == "POST":
        comment = CommentForm(request.POST)
        if comment.is_valid():
            new_comment = comment.save(commit=False)
            new_comment.comment_username = request.user
            new_comment.post = detail
            new_comment.save()
            return redirect("bireysel", urunid)

    else:
        context["commentform"] = CommentForm()
        yorm = detail.productdetail.all()
        data = {}
        for comment in yorm:
            data[comment.id] = UpdateCommentForm(instance=comment)
        print(data)

        context["updateform"] = data.items()
        return render(request, "productdetail.html", context)


def comment_update(request, urunid, commentid):
    context = {}
    detail = Product.objects.filter(id=urunid).first()
    comment = Comment.objects.filter(id=commentid).first()

    context["detail"] = detail
    context["comment"] = comment

    if request.method == "POST":
        comment_form = UpdateCommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.comment_username = request.user
            new_comment.post = detail
            new_comment.save()
            return redirect("bireysel", urunid)
    else:
        comment_form = UpdateCommentForm(instance=comment)

    context["comment_form"] = comment_form
    return render(request, "productdetail.html", context)


def add_my_fav(request):
    return render(request, "myfav.html")


def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if email and username and password:
            email_control = User.objects.filter(email=email).first()

            if email_control:
                messages.warning(request, "Mail Mevcut ")
                return redirect("kayit")
            else:
                # Şifreyi doğrudan kaydetmek yerine make_password fonksiyonunu kullanmalısınız
                user = User.objects.create(email=email, username=username)
                user.set_password(password)
                user.save()
                messages.success(request, "Başarılı")
                return redirect("giris")
        else:
            messages.error(request, "Boş Bırakılamaz")
            return redirect("kayit")
    else:
        return render(request, "register.html")

def giris(request):
    if request.method == "POST":
        username = request.POST.get(
            "username"
        )  # Kullanıcı adını "email" olarak alıyorsunuz, bu kullanıcıyı şifreliyorsa "username" olarak almalısınız.
        password = request.POST.get("password")

        if username and password:
            user = authenticate(
                request, username=username, password=password
            )  # "authenticate" fonksiyonuna "request" parametresini eklemelisiniz.

            if user:
                login(request, user)
                print("true")
                return redirect("home")
            else:
                print("false")
                return redirect("giris")

        else:
            messages.error(
                request, "Kullanıcı adı ve parola boş bırakılamaz."
            )  # Hata mesajını daha açıklayıcı hale getirdim.
            return redirect("giris")

    else:
        return render(request, "giris.html")


def basket(request):
    return render(request, "sepetim.html")


# api


def urunAPI(request, urunid):
    response = {}

    urunid = int(urunid)

    urun = Product.objects.filter(id=urunid).first()

    if urun:
        response["id"] = urunid
        response["category"] = urun.product_category.category
        response["name"] = urun.product_name
        response["fiyat"] = urun.product_price
        response["image"] = urun.product_image.url

    else:
        response["message"] = "ürün bulunamadı"

    # response['message']="ceyhun"

    return JsonResponse(response)


# FavAPI

# adım 2 apı contexte gönder


def favAPI(request, urunid):
    response = {}
    # neye göre alım yapacaksan onu almamız gerek burada id ye göre
    urunid = int(urunid)

    # ORM yapısını çağır

    urun = Product.objects.filter(id=urunid).first()

    if urun:
        # response["message"]="ürünü aldım"
        response["id"] = urunid
        response["category"] = urun.product_category.category
        response["name"] = urun.product_name
        response["content"] = urun.product_content
        response["price"] = urun.product_price
        response["image"] = urun.product_image.url
        response["stok"] = urun.product_stok
    else:
        response["message"] = "Ürün Bulunmadı"

    return JsonResponse(response)


# exit


def exit(request):
    logout(request)
    return redirect("home")


def myprofil(request, userid):
    context = {}

    user = User.objects.filter(id=userid).first()

    if user is None:
        return redirect("cikis")
    else:
        if request.user.id == user.id:
            context["user"] = user
        else:
            return redirect("hata")

    return render(request, "user-profile.html", context)


def error(request):
    return render(request, "hata.html")


def yetkierror(request):
    return render(request, "yetki.html")


# comment delete btn
def deletebtn(request, urunid, commentid):
    product = Product.objects.filter(id=urunid).first()
    commentbtn = Comment.objects.filter(id=commentid).first()

    if request.user == commentbtn.comment_username or request.user.is_superuser:
        commentbtn.delete()
        return redirect("bireysel", urunid)
    else:
        return redirect("yetkisiz")



