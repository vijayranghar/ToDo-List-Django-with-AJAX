from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'todoApp.views.home', name='home'),
	url(r'^delete/(?P<id>\d+)/$', 'todoApp.views.delete', name='delete'),
	url(r'^post/', 'todoApp.views.todoPost', name='home'),
    # url(r'^todoListProject/', include('todoListProject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
