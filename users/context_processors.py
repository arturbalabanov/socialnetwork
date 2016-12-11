from users.forms import SearchForm


def search_form(request):
    return {
        'user_search_form': SearchForm()
    }