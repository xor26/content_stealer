from django.db import models
import hashlib


class Post(models.Model):
    hash = models.CharField(max_length=35, primary_key=True, default="")
    title = models.TextField(default='')
    author = models.CharField(max_length=100, default='')
    content = models.TextField(default='')
    upvotes = models.IntegerField(default=0)
    is_posted = models.BooleanField(default=False)

    @classmethod
    def create_from_reddit_post(cls, reddit_post):
        hash = hashlib.md5(reddit_post['data']['permalink'].encode('utf-8')).hexdigest()
        try:
            post = cls.objects.get(hash=hash)
        except Post.DoesNotExist:
            return cls(
                hash=hash,
                title=reddit_post['data']['title'],
                content=reddit_post['data']['selftext'],
                upvotes=reddit_post['data']['score'],
                author=reddit_post['data']['author'],
                is_posted=False
            )

        return post


