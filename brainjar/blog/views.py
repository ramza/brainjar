from django.shortcuts import render
from blog.models import Post
from django.utils import timezone
from django.views.generic import (TemplateView, ListView,
                                DetailView,)

class AboutView(TemplateView):
    template_name = 'about.html'

class IndexView(TemplateView):
    template_name = 'index.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class TheMadGearView(TemplateView):
    template_name = 'the_mad_gear.html'

class CosmicTrashView(TemplateView):
    template_name = 'cosmic-trash.html'

class GaspardView(TemplateView):
    template_name = 'gaspard.html'

class TutorialsView(TemplateView):
    template_name = 'tutorials.html'
