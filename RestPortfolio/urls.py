from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import routers, permissions
from restapi.views import (
    MeViewSet,
    ProjectViewSet,
    PricingViewSet,
    SkillViewSet,
    ContactViewSet
)

schema_view = get_schema_view(
    openapi.Info(
    title="Portfolio API Documentation",
    default_version='v1',
    description="Backend Portfolio API Documentation",
    terms_of_service="https://www.itcbootcamp.com/info_pages/privacy_policy",

    contact=openapi.Contact(
    name="Yeraly Turarbekov",
    url="https://t.me/YeralyyT",
    email="turarbekoveraly17@gmail.com"
    ),

    licence=openapi.License(
    name="MIT Licence",
    url="https://opensource.org/licences/MIT",
)
),
)

public=True
permissions_classes=[permissions.AllowAny]

router = routers.DefaultRouter()

router.register(r'me', MeViewSet)
router.register(r'project', ProjectViewSet)
router.register(r'pricing', PricingViewSet)
router.register(r'skill', SkillViewSet)
router.register(r'contact', ContactViewSet)

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('redoc/', include('django.contrib.admindocs.urls')),
    path('graphql/', include('graphapi.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)