from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenRefreshView
from . import views


schema_view = get_schema_view(
    openapi.Info(
        title="Blog-site",
        default_version="v1",
        description="Blog site where you can post.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)


urlpatterns = [
    path('sign-up/', views.SingUpCreateAPIView.as_view(), name='sing-up'),
    path('sign-in/', views.CustomTokenObtainPairView.as_view(), name='login'),
    path('refresh/token/', TokenRefreshView.as_view(), name='refresh-token'),
    path('user/detail/<int:pk>', views.UserRetrieveAPIView.as_view(), name='user-detail'),
    path('my/profile/<int:pk>/', views.UserRetrieveUpdateDestroyAPIView.as_view(), name='my-profile'),
    path('verify/email/<int:pk>/<str:token>/', views.VerifyEmailAPIView.as_view(), name='verify-email'),
    path('swagger/', schema_view.as_view(), name='swagger-docs')
]