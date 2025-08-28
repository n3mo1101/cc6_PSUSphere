from django.contrib import admin
from .models import College, Program, Organization, Student, OrgMember

# Register your models here.
# Refactor admin.py
@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ("college_name", "created_at", "updated_at")
    search_fields = ("college_name",)
    list_filter = ("created_at",)


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("prog_name", "college__college_name")
    search_fields = ("prog_name", "college__college_name",)
    list_filter = ["college"]


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "get_org_college", "description")
    search_fields = ("name", "description",)
    list_filter = ["college"]

    def get_org_college(self, obj):
        try:
            org = Organization.objects.get(id=obj.id)
            return org.college
        except Organization.DoesNotExist:
            return None


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "lastname", "firstname", "middlename", "program")
    search_fields = ("lastname", "firstname",)


@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ("student", "get_member_program", "organization", "date_joined",)
    search_fields = ("student__lastname", "student__firstname",)

    def get_member_program(self, obj):
        try:
            member = Student.objects.get(id=obj.student_id)
            return member.program
        except Student.DoesNotExist:
            return None