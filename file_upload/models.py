from django.db import models

# Create your models here.
from utils.base_model import BaseModel


class FileModel(BaseModel):
    file_name = models.CharField(max_length=128, verbose_name='文件名')
    file = models.FileField(verbose_name='文件')
    file_path = models.FilePathField(verbose_name='文件存储路径', null=True, blank=True)

    class Meta:
        db_table = "tb_uploadfile"


# from easy_thumbnails.fields import ThumbnailerImageField
# class Dish(models.Model):
#     name = models.CharField(_(u'name'), max_length=100)
#     photo = ThumbnailerImageField(upload_to=dish_directory_path, null=True, blank=True, verbose_name='photo')
