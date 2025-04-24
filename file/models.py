from django.db import models

# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=255)
    link = models.FileField(upload_to='uploads/')  # Lưu file vào thư mục media/uploads/
    is_delete = models.BooleanField(default=False)  # Đánh dấu file bị xóa mềm
    created_at = models.DateTimeField(auto_now_add=True)  # Tự động lưu ngày tạo
    updated_at = models.DateTimeField(auto_now=True)  # Tự động lưu ngày cập nhật

    def __str__(self):
        return self.name
    class Meta:
      db_table = 'files'
      verbose_name = "Tài liệu"
      verbose_name_plural = "Các tài liệu"