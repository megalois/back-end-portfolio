from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from rest_framework.routers import DefaultRouter
from timestamp.views import TimestampList, TimestampDetail
from header_parser.views import RequestHeaderDetail
from url_shortener.views import URLList, URLDetail
from file_metadata.views import FileViewSet


router = DefaultRouter()
router.register(r'files', FileViewSet)


urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("back_end_portfolio.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    path('timestamp/', TimestampList.as_view(), name='timestamp-list'),
    path('timestamp/<ts>/', TimestampDetail.as_view(), name='timestamp-detail'),
    path('header-parser/', RequestHeaderDetail.as_view(), name='header-parser-detail'),
    path('url-shortener/', URLList.as_view(), name='url-list'),
    path('url-shortener/<slug:short_url>/', URLDetail.as_view(), name='url-detail'),
    path('file-metadata/', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
