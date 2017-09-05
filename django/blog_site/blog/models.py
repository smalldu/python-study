

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Django将会为models.py中的每一个定义的模型（model）创建一张表。当你创建好一个模型（model），
# Django会提供一个非常实用的API来方便的查询数据库

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                    self).get_queryset().filter(status='published')
    

# 我们定义一个POST模型（model）

class Post(models.Model):
    objects = models.Manager() 
    published = PublishedManager()

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                                related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                                choices=STATUS_CHOICES,
                                default='draft')
                            
    class Meta:
        # publish 进行降序  
        ordering = ('-publish',)
        
    def __str__(self):
        return self.title

    # 使用之前定义的post_detail URL给Post对象构建标准URL。Django的惯例是给模型（model）添加get_absolute_url()方法用来返回一个对象的标准URL。在这个方法中，我们使用reverse()方法允许你通过它们的名字和可选的参数来构建URLS
    # 我们通过使用strftime()方法来保证个位数的月份和日期需要带上0来构建URL
    def get_absolute_url(self):
        return reverse('blog:post_detail',
            args=[self.publish.year , 
            self.publish.strftime('%m'),
            self.publish.strftime('%d'),
            self.slug
            ])



    
        


    
        
    

    
        





