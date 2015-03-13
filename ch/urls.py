from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from tracker import views
from rest_framework.routers import DefaultRouter
from authentication.views import AccountViewSet

router = DefaultRouter()
router.register(r'medications', views.MedicationViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'accounts', AccountViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ch.views.home', name='home'),
    # url(r'^ch/', include('ch.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^', include('tracker.urls'))
)

urlpatterns += [

    url('^api/v1', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url('^.*$', IndexView.as_view(), name='index'),
]