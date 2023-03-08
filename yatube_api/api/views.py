# TODO:  Добавить пагинацию в GroupViewSet, CommentViewSet, FollowViewSet
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from .serializers import (
    PostSerializer,
    GroupSerializer,
    CommentSerializer,
    FollowSerializer
)

from .permissions import IsAuthenticatedIsAuthorOrReadOnly
from posts.models import Post, Group


class CreateListViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Пользовательский вьюсет для создания объекта или выдачи списка объектов.
    """
    pass


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для Post"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedIsAuthorOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для Group"""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedIsAuthorOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для Comment"""
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedIsAuthorOrReadOnly]

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs.get("post_id"))

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(
            post=self.get_post(),
            author=self.request.user
        )


class FollowViewSet(CreateListViewSet):
    """Вьюсет для Follow"""
    serializer_class = FollowSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
