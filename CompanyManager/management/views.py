from django.shortcuts import render
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Company, Employee, Device, CheckOut, CheckIn

def home(request):
    return render(request, 'management/home.html')

class CompanyCreateView(CreateView):
    model = Company
    fields = ['name','address','contact_info']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    template_name = 'management/company_form.html'
    success_url = reverse_lazy('management:home')

class CompanyUpdateView(UpdateView):
    model = Company
    fields = ['name','address','contact_info']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    template_name = 'management/company_form.html'
    success_url = reverse_lazy('management:home')

class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'management/company_confirm_delete.html'
    success_url = reverse_lazy('management:home')

class EmployeeCreateView(CreateView):
    model = Employee
    fields = ['name','email', 'phone_number']
    def form_valid(self, form):
        form.instance.company = self.request.user.company
        return super().form_valid(form)
    template_name = 'management/employee_form.html'
    success_url = reverse_lazy('management:home')

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ['name','email', 'phone_number']
    def form_valid(self, form):
        form.instance.company = self.request.user.company
        return super().form_valid(form)
    success_url = reverse_lazy('management:home')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'management/employee_confirm_delete.html'
    success_url = reverse_lazy('management:home')

class EmployeeList(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'management/employee_list.html'
    context_object_name = 'employees'

    def get_queryset(self):
        return Employee.objects.filter(company=self.request.user.company)


class DeviceCreateView(CreateView):
    model = Device
    fields = ['device_type','serial_number']
    def form_valid(self, form):
        form.instance.company = self.request.user.company
        return super().form_valid(form)
    template_name = 'management/device_form.html'
    success_url = reverse_lazy('management:home')

class DeviceUpdateView(UpdateView):
    model = Device
    fields = ['device_type','serial_number']
    def form_valid(self, form):
        form.instance.company = self.request.user.company
        return super().form_valid(form)
    template_name = 'management/device_form.html'
    success_url = reverse_lazy('management:home')

class DeviceDeleteView(DeleteView):
    model = Device
    template_name = 'management/device_confirm_delete.html'
    success_url = reverse_lazy('management:home')

class DeviceList(LoginRequiredMixin, ListView):
    model = Device
    template_name = 'management/Device_list.html'
    context_object_name = 'devices'

    def get_queryset(self):
        return Employee.objects.filter(company=self.request.user.company)

class CheckoutCreateView(CreateView):
    model = CheckOut
    fields = '__all__'
    template_name = 'management/checkout_form.html'
    success_url = reverse_lazy('management:home')

class CheckinCreateView(CreateView):
    model = CheckIn
    fields = '__all__'
    template_name = 'management/checkin_form.html'
    success_url = reverse_lazy('management:home')

class DeviceLogListView(ListView):
    model = CheckIn
    template_name = 'management/devicelog_list.html'
