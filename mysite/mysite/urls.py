from django.conf.urls import patterns, include, url
from orders.models import Order
from django.contrib import admin

admin.autodiscover()
admin.site.register(Order)


urlpatterns = patterns('',
    url(r'^$', 'orders.views.index'),
    #url(r'^orders/', include('orders.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^new/', 'orders.views.new_prescription'),
    url(r'^choose/', 'orders.views.choose_location'), 
)