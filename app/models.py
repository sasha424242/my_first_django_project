from django.db import models

class Category(models.Model):
    title = models.CharField("Наименивание", max_length=225, null=False, blank=False)
    parent_category = models.ForeignKey("Category", null=True, blank=True, on_delete=models.CASCADE, verbose_name="Категория")
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title
class product(models.Model):
    title = models.CharField("Наименивание", max_length=225, null=False, blank=False)
    cost = models.DecimalField("Цена", max_digits=11, decimal_places=2, null=False, blank=False)
    description = models.TextField("Описание", null=False, blank=False)
    category = models.ForeignKey("Category", null=False, blank=False, on_delete=models.CASCADE, verbose_name="Категория")
    image_url = models.URLField("Изображение", max_length=225, null=False, blank=False)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
    
    def __str__(self):
        return self.title