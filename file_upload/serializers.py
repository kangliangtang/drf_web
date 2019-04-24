from rest_framework import serializers
from .models import FileModel


class UploadFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileModel
        fields = '__all__'


class ThumbnailImageField(serializers.ImageField):
    """
    从 easy_thumbnails.fields.ThumbnailerImageField 字段类型中解析出缩略图信息
    """

    def __init__(self, *args, **kwargs):
        self.size_alias = kwargs.pop('size_alias', 'large')
        kwargs['read_only'] = True
        super(ThumbnailImageField, self).__init__(*args, **kwargs)

    def to_representation(self, value):
        try:
            return value[self.size_alias].url
        except Exception:
            return None

# class DishSerializer(serializers.ModelSerializer):
#     thumb = ThumbnailImageField(source="photo", size_alias='medium')
#     class Meta:
#         model = Dish
