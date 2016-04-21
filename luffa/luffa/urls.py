from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from luffa.views.learn_django import hello
from luffa.views.learn_django import current_datetime
from luffa.views.learn_django import hours_ahead
from luffa.views.index import index

urlpatterns = patterns('luffa.views.learn_django',
    # Examples:
    # url(r'^$', 'luffa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^hello/$', hello),
    url('^showtime/$', current_datetime),
    url('^addtime/(\d{1,2})/$', hours_ahead),
    url('^index/$', index),
    url('^$', index),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_PATH)
