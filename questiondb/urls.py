"""questiondb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin_site_clash16/', include(admin.site.urls)),
    url(r'^$','portal.views.home'),
    url(r'^signup$','portal.views.signup'),
    url(r'^login_function$','portal.views.login_function'),
    url(r'^store$','portal.views.question_store'),
    url(r'^question$','portal.views.questionpage'),
    url(r'^leaderboard$','portal.views.leaderboard'),
    url(r'^log_out$','portal.views.log_out'),
    url(r'^questionlist$','portal.views.question_list'),
    url(r'^go_question$','portal.views.go_question'),
    url(r'^next_question$','portal.views.next_question'),
    url(r'^leaderboard_senior$','portal.views.senior_leaderboard'),
    url(r'^senior_question$','portal.views.leaderboard_redirect'),
]
