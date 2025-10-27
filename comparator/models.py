from django.db import models

# Create your models here.

#pdf comaprision models with feilds

class PDFComparision(models.Model):
    pdf_file_1 = models.FileField(upload_to = 'pdfs/')
    pdf_file_2 = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add= True)
    is_identical = models . DateTimeField(null = True)
    comparison_result = models.TextField(blank=True)
    comparision_type = models.CharField(max_length=10,choices = [('byte','Byte'),('text','Text'),('visual','visual')],default='byte')
    
    def __str__(self):
        return f'comparison at {self.uploaded_at}'