from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views 

urlpatterns = [
    path('' ,views.store, name='store'),
    path('cart/' ,views.cart, name='cart'),
    path('update_item/' ,views.updateItem, name='update_item'),
    
  
    
    

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)