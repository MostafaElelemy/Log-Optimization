from django.db import models

class LogStream(models.Model):
    raw_content = models.TextField()
    source = models.CharField(max_length=100, default="System Server")
    compressed_content = models.TextField(blank=True)
    original_size = models.IntegerField(default=0)
    compressed_size = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # ده الـ "Squash" logic البسيط
        lines = self.raw_content.split('\n')
        unique_lines = list(dict.fromkeys([line.strip() for line in lines if line.strip()]))
        self.compressed_content = '\n'.join(unique_lines)
        
        self.original_size = len(self.raw_content)
        self.compressed_size = len(self.compressed_content)
        super().save(*args, **kwargs)