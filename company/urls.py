from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^home$', views.index, name='home'),
    url(r'^games/(?P<pag>\d+)$', views.games, name='games'),
    url(r'^news/(?P<pag>\d+)$', views.news, name='news'),
    url(r'^business$', views.business, name='business'),
    url(r'^joinUs$', views.joinUs, name='joinUs'),
    url(r'^aboutUs$', views.aboutUs, name='aboutUs'),
    url(r'^gameDetail/(?P<game_index>\d+)$', views.gameDetail, name='gameDetail'),
    url(r'^newsDetail/(?P<new_id>\d+)$', views.newsDetail, name='newsDetail'),
    url(r'^jobDesc/(?P<job_id>\d+)$', views.jobDesc, name='jobDesc'),
]
