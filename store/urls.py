from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views 

urlpatterns = [
    path('' ,views.store, name='store'),
    path('cart/' ,views.cart, name='cart'),
    path('update_item/' ,views.updateItem, name='update_item'),
    path('checkout/' ,views.checkout, name='checkout'),
    path('process_order/' ,views.processOrder, name='process_order'),
    path('search/',views.search_results, name='search_results'),
    path('project/<int:id>',views.single_post,name='post'),
    
  
    
    

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)