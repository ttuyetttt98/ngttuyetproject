from django.db import models
from django.conf import settings


class Book(models.Model):
    CATEGORY_CHOICES = [
        ('fiction', '文学・小説'),
        ('business', 'ビジネス・経済'),
        ('manga', 'マンガ'),
        ('lnovel', 'ライトノベル'),
        ('history', '歴史'),
        ('hobby', '趣味・実用'),
        ('study', '学習参考書'),
        ('other', 'その他'),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='books/')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
