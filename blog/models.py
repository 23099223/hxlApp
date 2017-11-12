from django.db import models
from django.db.models.fields.related import ManyToManyField


# Create your models here.

class PrintableModel(models.Model):
    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        opts = self._meta
        data = {}
        for f in opts.concrete_fields + opts.many_to_many:
            if isinstance(f, ManyToManyField):
                if self.pk is None:
                    data[f.name] = []
                else:
                    # print('f.name: ', f.name, 'f.value', f.value_from_object(self).values_list('pk', flat=True))
                    # data1 = [tag for tag in f.value_from_object(self).values_list('pk', flat=True)]
                    # print(data1)
                    # data[f.name] = list(f.value_from_object(self).values_list('pk', flat=True))
                    data[f.name] = [tag for tag in f.value_from_object(self).values_list('pk', flat=True)]
            else:
                data[f.name] = f.value_from_object(self)
        return data

    class Meta:
        abstract = True


class Tags(PrintableModel):
    tag = models.CharField(u'标签', max_length=20)  # 标签

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'


class Article(PrintableModel):
    id = models.AutoField(u"自增id", primary_key=True)  # 自增主键
    title = models.CharField(u"博客标题", max_length=100)  # 博客标题
    description = models.CharField(u'博客描述', max_length=200)  # 博客描述
    pub_date = models.DateTimeField(u"发布日期", auto_now_add=True, editable=True)  # 博客发布日期
    view_count = models.IntegerField(u"阅读次数", default=100)  # 博客阅读次数
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)
    icones = models.ImageField(u'插图', blank=True, null=True)
    content = models.TextField(u'正文', blank=True, null=True)  # 博客文章正文
    tag = models.ManyToManyField(Tags, related_name='ref1')

    def __str__(self):
        return '%s %s %s %s %s' % (self.id, self.title, self.pub_date, self.view_count, self.update_time)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = '文章'
        verbose_name_plural = '文章'


class Comment(models.Model):
    comment = models.ForeignKey(Article, on_delete=models.CASCADE)
    reply_name = models.CharField(u'评论人', max_length=50, default='guest')
    pub_date = models.DateTimeField(u'评论时间', auto_now_add=True, editable=True)  # 评论时间
    content = models.CharField(u'评论内容', max_length=500)  # 评论内容

    def __str__(self):
        return '%s %s' % (self.comment, self.pub_date)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = '评论'
        verbose_name_plural = '评论'
