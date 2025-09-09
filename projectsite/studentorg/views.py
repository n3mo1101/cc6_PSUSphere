from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, OrgMember, Student
from studentorg.forms import OrganizationForm, OrgMemberForm, StudentForm
from django.urls import reverse_lazy


# Create your views here.
class HomePageView(ListView):
    model = Organization
    context_object_name = "home"
    template_name = "home.html"


# Organization Views
class OrganizationList(ListView):
    model = Organization
    context_object_name = "organization"
    template_name = "org_list.html"
    paginate_by = 5


class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')


class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')


class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')


# Org. Members Views
class OrgMemberList(ListView):
    model = OrgMember
    context_object_name = 'org_member'
    template_name = 'org_member_list.html'
    paginate_by = 5


class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'org_member_form.html'
    success_url = reverse_lazy('org-member-list')


class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'org_member_form.html'
    success_url = reverse_lazy('org-member-list')


class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'org_member_del.html'
    success_url = reverse_lazy('org-member-list')


# Student Views
class StudentList(ListView):
    model = Student
    context_object_name = "student"
    template_name = "student_list.html"
    paginate_by = 5


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('student-list')