from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    # Health check
    path("health/", include("health_check.urls")),
    # Admin panel
    path("admin/", admin.site.urls),
    # DRF Spectacular schema generation endpoint
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Swagger UI
    path("api/docs/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    # Redoc UI
    path("api/docs/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    # Add your app-specific API paths here
    # path("api/v1/", include("your_app.urls")),
]
