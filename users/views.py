import json
from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import FormView, CreateView, RedirectView, DetailView, View, ListView
from braces.views import AnonymousRequiredMixin, LoginRequiredMixin, JSONResponseMixin, AjaxResponseMixin
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from timeline.api.serializers import PostSerializer
from timeline.forms import CreatePostForm, CreatePostCommentForm
from users.forms import RegistrationForm, LoginForm, SearchForm
from users.models import UserProfile


class LoginView(AnonymousRequiredMixin, FormView):
    template_name = 'users/login.html'
    form_class = LoginForm

    def _get_user_profile_url(self):
        username = self.request.user.username
        return reverse('users:profile', kwargs={'slug': username})

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return self._get_user_profile_url()

    def get_authenticated_redirect_url(self):
        return self._get_user_profile_url()


class LogoutView(LoginRequiredMixin, RedirectView):
    login_url = reverse_lazy('users:login')

    def get_redirect_url(self, *args, **kwargs):
        return reverse('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class RegisterView(AnonymousRequiredMixin, CreateView):
    template_name = 'users/register.html'
    form_class = RegistrationForm
    authenticated_redirect_url = reverse_lazy('home')

    # TODO: Log in and redirect to the new user's profile
    def get_success_url(self):
        return reverse('home')


class ProfileView(DetailView):
    model = UserProfile
    slug_field = 'username'
    context_object_name = 'profile_user'
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)

        profile_user = context['profile_user']
        user = self.request.user

        context['are_friends'] = user.friends.filter(username=profile_user.username).exists()
        context['own_profile'] = user == profile_user
        context['post_form'] = CreatePostForm()
        context['comment_form'] = CreatePostCommentForm()

        return context


# TODO: Move to Django REST Framework view/viewset
class ToggleFriendshipView(LoginRequiredMixin, AjaxResponseMixin, JSONResponseMixin, View):
    login_url = reverse_lazy('users:login')

    def post_ajax(self, request, *args, **kwargs):
        target_username = json.loads(request.body)['target_username']
        target = UserProfile.objects.get(username=target_username)
        current_user = request.user

        are_friends = current_user.friends.filter(username=target_username).exists()

        if are_friends:
            current_user.friends.remove(target)
        else:
            current_user.friends.add(target)

        current_user.save()

        response = {
            'success': True,
            'areFriends': not are_friends,
        }

        return self.render_json_response(response)


class SearchView(ListView):
    model = UserProfile
    context_object_name = 'results'
    template_name = 'users/search-results.html'
    form_class = SearchForm

    def get_queryset(self):
        query = self.request.GET['q']
        return UserProfile.objects.filter(username__icontains=query).order_by('username')


@api_view(['GET'])
def get_user_posts(request, username):
    user = get_object_or_404(UserProfile, username=username)
    posts = user.timeline_posts.all()
    post_serializer = PostSerializer(posts, many=True)

    return Response(post_serializer.data, status=status.HTTP_200_OK)
