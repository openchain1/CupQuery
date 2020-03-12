from django.http import HttpResponse

from Comments.models import Comment

try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


@login_required
@require_POST
def like(request):
    if request.method == 'POST':
        user = request.user
        slug = request.POST.get('slug', None)
        comments = get_object_or_404(Comment, slug=slug)

        if comments.likes.filter(id=user.id).exists():
            # user has already liked this company
            # remove like/user
            comments.likes.remove(user)
            message = 'You disliked this'
        else:
            # add a new like for a company
            comments.likes.add(user)
            message = 'You liked this'

    ctx = {'likes_count': comments.total_likes, 'message': message}
    # use mimetype instead of content_type if django < 5
    return HttpResponse(json.dumps(ctx), content_type='application/json')