from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse

from posts.models import Post, Category

class PostsListView(ListView):
    queryset = Post.objects.filter(status="published")
    #Даем название списку объектов, по которому будем обращаться к списку в шаблоне
    #По умолчанию список объектов назывался бы object_list 
    context_object_name = "posts"
    template = "posts/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['categories'] = Category.objects.all()
        
        return context


def json_list_category_posts(request):
    posts = Post.objects.filter(status="published")
    
    return JsonResponse(
        {
            "posts": [
                {
                    "title": p.title,
                    "slug": p.slug,
                    "id": p.id,
                    "published": p.when_published,
                }
                for p in posts
            ]
        }
    )

def json_detail_category_posts(request, pk):
    cat = Category.objects.filter(id=pk)
    if cat.count():
        posts = cat[0].posts.all()
        return JsonResponse(
            {
                "posts": [
                    {
                        "title": p.title,
                        "slug": p.slug,
                        "id": p.id,
                        "published": p.when_published,
                    }
                    for p in posts
                ]
            }
        )
    else:
        return JsonResponse({"category":"Category doesn't exist"})