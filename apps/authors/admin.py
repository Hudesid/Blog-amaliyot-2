from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AdminPasswordChangeForm
from .models import User, UserToken
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'bio')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    change_password_form = AdminPasswordChangeForm
    list_display = ('id', 'username', 'email', 'is_active', 'is_verify_email')
    list_filter = ('date_joined', 'updated_at', 'is_active', 'is_verify_email')
    search_fields = ('username', 'email', 'id')
    ordering = ('email', 'username')
    readonly_fields = ('last_login', 'date_joined', 'id')
    fieldsets = (
        ('Personal Info', {
        'fields': ('id', 'username', 'email', 'is_active', 'is_verify_email', 'bio')
        }),
        ('Permission', {
            'fields': ('is_staff', 'is_superuser')
        }),
        ('Change Password', {
            'fields': ('password',),
            'classes': ('collapse',)
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'bio', 'is_active', 'is_staff', 'is_superuser', 'is_verify_email')

        }))


admin.site.register(User, CustomUserAdmin)


@admin.register(UserToken)
class UserTokenAdmin(admin.ModelAdmin):
    list_display = ('id', 'expires_at', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('id', 'token', 'user__username')