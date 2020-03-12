from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView
from .models import Profile
from .forms import SignUpForm, UserProfileForm, UserEditForm
from Posts.forms import PostForm
from registration.backends.default.views import RegistrationView


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
        return HttpResponseRedirect('../home/')
    else:
        form = PostForm()
    return render(request, "addpost.html", {"form": form})


class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/login/'

    def register(self, form_class):
        # logging.debug("Registering")
        new_user = super(MyRegistrationView, self).register(form_class)
        new_user.save()
        return new_user

# def signup(request):
#     form = SignUpForm(request.POST or None)
#     # print("it is here")
#     if form.is_valid():
#         # print("inside is here")
#         user = form.save(commit=False)
#         user.save()
#         return HttpResponseRedirect('/login/')#login
#     else:
#         return render(request, 'signup.html', {'form': form})



@login_required
def profile(request):
    prof = Profile.objects.all()
    return render(request, "profile.html", {"prof": prof})


class UpdateProfileView(UpdateView):
    form_class = UserProfileForm
    template_name = 'profile update.html'
    success_url = '.'

    def get_object(self, queryset=None):
        return self.request.user.profile


class UpdateUserView(UpdateView):
    form_class = UserEditForm
    template_name = 'user_info.html'
    success_url = '.'

    def get_object(self, queryset=None):
        return self.request.user
