__author__ = 'tomnahass'
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MedicationViewSet, UserViewSet, api_root



# medication_list = MedicationViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
#
# medication_detail = MedicationViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# user_list = UserViewSet.as_view({
#     'get':'list'
# })
#
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
#
#
# urlpatterns = [
#     url(r'^$', api_root),
#     url(r'^medications/$', medication_list, name='medication-list'),
#     url(r'^medications/(?P<pk>[0-9]+)/$', medication_detail, name='medication-detail'),
#     url(r'^users/$', user_list, name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)