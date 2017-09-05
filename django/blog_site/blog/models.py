

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Django将会为models.py中的每一个定义的模型（model）创建一张表。当你创建好一个模型（model），
# Django会提供一个非常实用的API来方便的查询数据库

# Create your models here.


class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager,
					self).get_queryset().filter(status='published')
	

# 我们定义一个POST模型（model）

class Post(models.Model):
	objects = models.Manager() # The default manager
	published = PublishedManager() # our custom manager


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



    
    	


	
        
    

    
		





