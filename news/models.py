from django.db import models  # импорт
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    rating = models.IntegerField(default=0)
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)

    def update(self):

        postRat = self.post_set.aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')
        commRat = self.user_name.comment_set.aggregate(commRating=Sum('rating'))
        cRat = 0
        cRat += commRat.get('commRating')

        self.rating = pRat *3 + cRat
        self.save()

    def __str__(self):
        return self.user_name.username


class Category(models.Model):
    category = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.category.title()


class Post(models.Model):
    news = "NW"
    articl = "AR"
    CHOICE_CONTENS = [(news,'Новости'), (articl,'Статья')]
    time_creates = models.DateTimeField(auto_now_add=True)
    choice_content = models.CharField(max_length=2, choices=CHOICE_CONTENS, default= news)
    heading = models.CharField(max_length=64)
    rating = models.IntegerField(default=0)
    article_text = models.TextField()
    autor = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        if len(self.article_text) <= 124:
            prev = self.article_text
        else:
            prev = self.article_text[:123]+"..."
        return prev

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.heading.title()}: {self.article_text[:20]}'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    time_creates = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()