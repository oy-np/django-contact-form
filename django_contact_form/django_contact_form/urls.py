from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from contact import views as contact_views
from comments import views as comments_views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^contact/$', contact_views.ContactView.as_view(), name='contact'),
    url(r'^thank/$', contact_views.ThankYouView.as_view(), name='thank'),
    url(r'^comments/$', comments_views.CommentsView.as_view(), name='comments'),

    # Examples:
    # url(r'^$', 'django_contact_form.views.home', name='home'),
    # url(r'^django_contact_form/', include('django_contact_form.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
