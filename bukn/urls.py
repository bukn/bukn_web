from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'lifetracer.views.index', name='index'),
    url(r'^user/(?P<user_id>\d+)/$', 'lifetracer.views.user', name='user'),
    url(r'^ajaxlogin/$', 'lifetracer.views.ajax_login', name='ajaxlogin'),
    url(r'^rp/$', 'lifetracer.views.rp', name='register'),
    # url(r'^$', 'bukn.views.home', name='home'),
    # url(r'^bukn/', include('bukn.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
