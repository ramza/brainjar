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
]
