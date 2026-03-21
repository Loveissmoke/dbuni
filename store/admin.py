from django.contrib import admin
from .models import Brand, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand','description', 'gram', 'pieces_per_case', 'price','color_preview')
    def color_preview(self, obj):
        return format_html(
            '<div style="width:50px;height:20px;background:{};"></div>',
            obj.bg_color
        )

admin.site.register(Brand)
admin.site.register(Product)
