"""
URL configuration for proje project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp.views import *


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='home'),
    path('about/',about,name='hakkinda'),
    path('contact/',contact,name='iletisim'),
    path('found500/',yetkierror,name='yetkisiz'),
    path('gir/',giris,name='giris'),
    path('kayit/',register,name='kayit'),
    path('myfav/',add_my_fav,name='fav'),
    path('products/',products,name='products'),
    path('basket/',basket,name='sepet'),
    path('exit/',exit,name='cikis'),
    path('setting/<userid>',myprofil,name='setting'),
    #comment delete btn
    path('urun/<urunid>',productdetail,name='bireysel'),
    path('urun/<urunid>/comment/<commentid>/update',comment_update,name='update'),
    path('remove/urun/<urunid>/comment/<commentid>',deletebtn,name='sil'),
    path('errorpage/',error,name='hata'),


    #API start
    path('api/urun/<urunid>',urunAPI),
    #FavIp
    
    path('api/fav/urun/<urunid>',favAPI)
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



