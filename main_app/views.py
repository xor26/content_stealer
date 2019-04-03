import json
import requests
from rest_framework import viewsets

from main_app.VkontaktGateway import VkontaktGateway
from main_app.models import Post
from main_app.serializers import PostSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics


class PostGetSet(viewsets.ModelViewSet):
    """
    API endpoint that shows all reddit posts
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostSendSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@csrf_exempt
def receive_posts(request):
    """
    List all code snippets, or create a new snippet.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/39.0.2171.95 Safari/537.36'
    }
    respond = requests.get("https://www.reddit.com/hot.json?sort=hot", headers=headers)
    content = json.loads(respond.content)
    # check for requests exceptions will be there someday
    # -----------------------------------------

    posts = []
    for i in range(len(content['data']['children'])):
        reddit_post = content['data']['children'][i]
        posts.append(Post.create_from_reddit_post(reddit_post))

    if request.method == 'GET':
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        post_to_add_hash = request.POST.get("hash")

        for post in posts:
            if post.hash == post_to_add_hash:
                post.save()
                break
        return JsonResponse({"result": "success"})


class ListPostsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@csrf_exempt
def send_posts(request):
    if request.method == 'GET':
        try:
            post = Post.objects.get()
        except Post.DoesNotExist:
            return HttpResponse(status=404)

        serializer = PostSerializer(post)

        return JsonResponse(serializer.data)

    if request.method == 'POST':
        post_to_send_hash = request.POST.get("hash")
        try:
            post = Post.objects.get(hash=post_to_send_hash)
            VkontaktGateway().send_post(post)
        except Post.DoesNotExist:
            return HttpResponse(status=404)

        return JsonResponse({"result": "success"})


