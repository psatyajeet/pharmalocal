from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'orders.views.index'),
    #url(r'^orders/', include('orders.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^new/', 'orders.views.new_prescription'),
)