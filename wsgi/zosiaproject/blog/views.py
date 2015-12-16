from django.shortcuts import (
    get_object_or_404, render_to_response
)

from common.forms import LoginForm
from common.models import ZosiaDefinition
from .models import *

def index(request):
    title      = 'Blog'
    blog_posts = BlogPost.objects.order_by('-pub_date')
    user       = request.user
    login_form = LoginForm()
    definition = get_object_or_404(ZosiaDefinition, active_definition=True)

    return render_to_response('blog.html', locals())
