from django.db import models
from blog.models import YazilarModel, DateAbstractModel
from account.models import CustomUserModel

class YorumModel(DateAbstractModel):
    yazan = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='yorum')
    yazi = models.ForeignKey(YazilarModel, on_delete=models.CASCADE, related_name='yorumlar')
    yorum = models.TextField()

    class Meta:
        db_table = 'yorum'
        verbose_name = 'Yorum'
        verbose_name_plural = 'Yorumlar'

    def __str__(self):
        return self.yazan.username