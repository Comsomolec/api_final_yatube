from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):

    PATTERN = (
        'Author: {author}, Group: {group}, Date: {date}, Text: {text:.15}.'
    )

    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
    )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True
    )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name='posts', blank=True, null=True
    )

    # Умолчательная сортировка добавлена, но сделана по автору, так как
    # Сортировка по другим полям "ломает" тест ЯП № 39

    class Meta:
        ordering = ('author', '-pub_date',)

    def __str__(self):
        return self.PATTERN.format(
            author=self.author.username,
            group=self.group.title,
            date=self.pub_date,
            text=self.text,
        )


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )


class Follow(models.Model):

    PATTERN = '{user} follower {following}'

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower',
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'], name='unique_user_following')
        ]

    def __str__(self):
        return self.PATTERN.format(
            user=self.user.username,
            following=self.following.username,
        )
