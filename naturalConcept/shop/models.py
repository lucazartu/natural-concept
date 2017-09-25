from django.db import models
from django.core.urlresolvers import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name="Categoria", related_name='products')
    name = models.CharField("Nome", max_length=200, db_index=True)
    slug = models.SlugField("Slug", max_length=200, db_index=True)
    image = models.ImageField("Imagem", upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField("Descrição", blank=True)
    price = models.DecimalField("Preço", max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField("Estoque")
    available = models.BooleanField("Disponivel", default=True)
    created = models.DateTimeField("Criado em", auto_now_add=True)
    updated = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
