from django.conf.urls import patterns, include, url


urlpatterns = patterns('users.views',
    # Examples:
    # url(r'^$', 'buildchange.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'add','addUser'),

)
