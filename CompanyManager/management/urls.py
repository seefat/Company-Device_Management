from django.urls import path
from .views import *

app_name = 'management'

urlpatterns = [
    path('', home, name='home'),
    path('company/create/', CompanyCreateView.as_view(), name='company_create'),
    path('company/update/<int:pk>/', CompanyUpdateView.as_view(), name='company_update'),
    path('company/delete/<int:pk>/', CompanyDeleteView.as_view(), name='company_delete'),
    path('employee/create/', EmployeeCreateView.as_view(), name='employee_create'),
    path('employee/update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee/delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee_delete'),
    path('employee/list/',EmployeeList.as_view(),name='employee_list'),
    path('device/create/', DeviceCreateView.as_view(), name='device_create'),
    path('device/list/', DeviceList.as_view(),name='device_list'),
    path('device/update/<int:pk>/', DeviceUpdateView.as_view(), name='device_update'),
    path('device/delete/<int:pk>/', DeviceDeleteView.as_view(), name='device_delete'),
    path('checkout/create/', CheckoutCreateView.as_view(), name='checkout_create'),
    path('checkin/create/', CheckinCreateView.as_view(), name='checkin_create'),
    path('devicelog/', DeviceLogListView.as_view(), name='devicelog_list'),
]
