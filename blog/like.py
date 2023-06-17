# from xml.etree.ElementTree import Comment
from . models import My_blog, Like, Slider,Comment
from django.contrib import messages

def new_likes(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('like')
        post_obj = My_blog.objects.get(id =post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, blog_id =post_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value ='Like'
        like.save()
    return new_likes


def messages(request, id):
    blog = My_blog.objects.get(id=id)
    comment =Comment.objects.filter(blog =blog)
    comment_count =comment.count()

    return comment_count

def authmessage(request):
    messages.info(request, 'email exist')
    return authmessage

def slider(request):
    Slider.objects.all()
    return slider