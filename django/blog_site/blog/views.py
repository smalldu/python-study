from django.shortcuts import render
from .models import Post,Comment
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm,CommentForm
from taggit.models import Tag

# 暂时不对
# class PostListView(ListView):
# 	queryset = Post.published.all()
# 	context_object_name = 'posts'
# 	paginate_by = 3
# 	tempate_name = 'blog/post/list.html'

# 列表
def post_list(request,tag_slug=None):
	object_list = Post.published.all()
	tag = None
	paginator = Paginator(object_list,3) # 每页3个元素
	page = request.GET.get('page')
	if tag_slug:
		tag = get_object_or_404(Tag,slug=tag_slug)
		object_list = object_list.filter(tags__in = [tag])
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request,
				'blog/post/list.html',
				{ 'page': page , 
				'tag':tag,
				'posts':posts})


# 详细页面
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    # List of active comments for this post
    comments = post.comments.filter(active=True)
    new_comment = None
        
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'blog/post/detail.html',
                  {'post': post,
                  'comments': comments, 
                  'new_comment': new_comment,
                  'comment_form': comment_form})



# 分享
def post_share(request , post_id):
	# retrieve post by id
	post = get_object_or_404(Post, id = post_id , status = 'published')
	cd = None
	sent = False
	if request.method == 'POST':
		# Form was submitted
		form = EmailPostForm(request.POST)
		if form.is_valid():
			# form field passed validation
			# 获取验证过的数据。这个属性是一个表单字段和值的字典。
			cd = form.cleaned_data
			# TODO: - send email ... 
			sent = True
	else:
		# 创建一个空表单 非 POST 请求
		form = EmailPostForm()
	return render(request,'blog/post/share.html',
				{
				'post':post,
				'form':form,
				'cd':cd ,
				'sent':sent
				})

	





















