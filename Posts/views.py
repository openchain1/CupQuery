from django.db.models import Q
from datetime import datetime
from django.http import (Http404, HttpResponse) 
from django.shortcuts import render
from Posts.forms import PostForm
from accounts.models import Profile
from Comments.forms import CommentForm
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin, UpdateView, DeleteView
from Posts.models import Post
from Comments.models import Comment


class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    extra_context = {"prof": Profile.objects.all()}
    context_object_name = 'posts'
    paginate_by = 4
    queryset = Post.objects.order_by('-date')  # Default: Model.objects.all()


class PostDetail(FormMixin, DetailView):
    template_name = 'post_detail.html'
    model = Post
    form_class = CommentForm

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'post': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.post = self.object
        comment.save()
        # want to save post instance here.
        return super(PostDetail, self).form_valid(form)


class EditPost(UpdateView):
    model = Post
    form_class = PostForm
    template_name ="edit_post.html"

    def test_func(self):
        post_user = self.request.user.pk
        print(post_user)
        post_made = Post.objects.get(user='user')
        print(post_made)
        if post_user == post_made:
            return reverse('post_detail')
        else:
            if self.request.user.is_authenticated():
                raise HttpResponse("You are not allowed to edit this Post")

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            return Http404("You are not allowed to edit this Post")
        return super(EditPost, self).dispatch(request, *args, **kwargs)


class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    template_name = 'post_confirm_delete.html'
    success_message = 'Post Deleted Successfully..!'

    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter(user=user)


def postsearch(request):
    if request.method == "GET":
        input_text = request.GET["mysearch"]
        print(input_text)
        try :
            post_list = Post.objects.filter(Q(title__icontains=input_text)|Q(body__icontains=input_text))
            print(post_list)
            return render(request, "test.html", {"post_list":post_list})
        except:
            return render(request, "test.html", {"none":"No Result Found"})
    else:
        return redirect(".")

