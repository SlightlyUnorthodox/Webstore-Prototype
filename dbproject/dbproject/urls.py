from django.conf.urls import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'webstore.views.browse'),
	url(r'^login/','webstore.views.login_user'),
	url(r'^register/','webstore.views.register_user'),
	url(r'^browse/','webstore.views.browse'),
	url(r'^search/','webstore.views.search'),	
	url(r'^order/','webstore.views.order'),
	url(r'^updateOrder/','webstore.views.updateOrder'),
	url(r'^placeOrder/','webstore.views.placeOrder'),
	url(r'^staffUpdate/','webstore.views.staffUpdate'),
	url(r'^staffUpdateItems/','webstore.views.staffUpdateItems'),
	url(r'^staffSaveUpdates/','webstore.views.staffSaveUpdates'),
	url(r'^account/','webstore.views.account'),
    url(r'^index/', 'webstore.views.index'),
    url(r'^admin/', include(admin.site.urls)),
)
