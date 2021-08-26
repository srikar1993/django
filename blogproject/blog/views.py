from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import send_mail
from blog.forms import EmailSendForm
from blog.forms import CommentForm
from taggit.models import Tag

# Create your views here.

def post_list_view(request, tag_slug=None):
    post_list = Post.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])

    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page')
    try:
        post_list = paginator.page(page_number)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    return render(request, 'blog/post_list.html', {'post_list': post_list, 'tag': tag})

# class PostListView(ListView):
#     model = Post
#     paginate_by = 3

def post_detail_view(request, year, month, day, post):
    post_detail = get_object_or_404(Post, slug=post, status='published', 
                                    publish__year=year, publish__month=month, publish__day=day)
    comments = post_detail.comments.filter(active=True)
    comment_submit = False
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post_detail
            new_comment.save()
            comment_submit = True
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post':post_detail, 'comment_submit':comment_submit, 'form': form, 'comments':comments})

def mail_send_view(request, id):
    post = get_object_or_404(Post, id=id, status='published')
    sent = False
    if request.method == 'POST':
        form = EmailSendForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = f'''Hello! {cd['name']}({cd['email']}) recommends you to read "{post.title}"'''
            post_url = request.build_absolute_uri(post.get_absolute_url())
            body = f''' Read post at:\n{post_url}\n\n{cd['name']}'s comments:\n{cd['comments']} '''
            send_mail(subject, body, 'pythonsrikar@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailSendForm()
    return render(request,'blog/sharebyemail.html', {'form': form, 'post':post, 'sent':sent})
