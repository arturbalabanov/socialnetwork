from rest_framework.permissions import BasePermission, SAFE_METHODS


class PostPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return request.user.is_authenticated()

    def has_object_permission(self, request, view, post):
        if request.method in SAFE_METHODS:
            return True

        return post.author == request.user


class PostCommentPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return request.user.is_authenticated()

    def has_object_permission(self, request, view, comment):
        if request.method in SAFE_METHODS:
            return True

        return comment.author == request.user
