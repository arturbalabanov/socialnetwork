from braces.views import LoginRequiredMixin, AjaxResponseMixin, JSONResponseMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View

from timeline.models import Post


# FIXME: This is dumb, I have to use all the features from the form
class MakeTimelinePostView(LoginRequiredMixin, AjaxResponseMixin, JSONResponseMixin, View):
    login_url = reverse_lazy('users:login')

    def post_ajax(self, request, *args, **kwargs):
        current_user = request.user
        text = request.POST['text']

        post = Post(author=current_user, text=text)

        post.save()

        response = {
            'success': True,
            'post': {
                'author': post.author.username,
                'created': post.created,
                'text': post.text,
            },
        }

        return self.render_json_response(response)


class LikeTimelinePostView(LoginRequiredMixin, AjaxResponseMixin, JSONResponseMixin, View):
    login_url = reverse_lazy('users:login')

    def post_ajax(self, request, *args, **kwargs):
        current_user = request.user
        post_id = request.POST['id']

        post = Post.objects.get(id=post_id)
        post.like(current_user)

        response = {
            'success': True,
            'likes': post.number_of_likes,
        }

        return self.render_json_response(response)
