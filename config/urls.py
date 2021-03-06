# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

urlpatterns = [
                  url(r'^$', TemplateView.as_view(template_name='homepage.html'), name='home'),
                  url(r'^about/$', TemplateView.as_view(template_name='about_nectr.html'), name='about'),

                  # Django Admin, use {% url 'admin:index' %}
                  url(settings.ADMIN_URL, admin.site.urls),

                  # User management
                  url(r'^users/', include('nectr.users.urls', namespace='users')),
                  url(r'^accounts/', include('allauth.urls')),
                  url(r'^tutor/', include('nectr.tutor.urls', namespace='tutors')),

                  # Dashboard Management
                  url(r'^dashboard/', include('nectr.dashboard.urls', namespace='dashbaord')),

                  # Your stuff: custom urls includes go here
                  url(r'^search/', include('nectr.search.urls')),

                  # Search the Hive
                  # url(r'^search_the_hive', TemplateView.as_view(template_name='look_nectr.html')),
                  # Join the Hive
                  url(r'^join_the_hive', TemplateView.as_view(template_name='joinpage_nectr.html'), name='join'),

                  # How it Works
                  url(r'^how_it_works', TemplateView.as_view(template_name='how_nectr.html'), name='how_it_works'),

                  # url(r'^test_look_nectr', TemplateView.as_view(template_name='look_nectr.html'), name='test4'),
                  # url(r'^test_joinpage_nectr', TemplateView.as_view(template_name='joinpage_nectr.html'), name='test5'),

                  # Messaging Include
                  url(r'^messages/', include('postman.urls', namespace='postman', app_name='postman')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]
