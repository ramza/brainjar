from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post-list'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^post/(?P<pk>\d+)/$', views.PostDetailView.as_view(),name='post_detail'),
    url(r'^the-mad-gear/$', views.TheMadGearView.as_view(), name='the-mad-gear'),
    url(r'^cosmic-trash/$', views.CosmicTrashView.as_view(), name='cosmic-trash'),
    url(r'^gaspard/$', views.GaspardView.as_view(), name='gaspard'),
    url(r'^tutorials/$', views.TutorialsView.as_view(), name='tutorials'),
    url(r'^breakout/$', views.BreakOutView.as_view(), name='breakout'),
    url(r'^breakout2/$', views.BreakOut2View.as_view(), name='breakout2'),
    url(r'^game-of-life/$', views.GameOfLifeView.as_view(), name='game-of-life'),
    url(r'^bunny-world/$', views.BunnyWorldView.as_view(), name='bunny-world'),
]
