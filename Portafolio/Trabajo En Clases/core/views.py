from django.shortcuts import render

from django.views import generic
from django.urls import reverse_lazy

from .models import Category, SubCategory, Brand, Product
from .forms import ProductForm, UpdateProductForm

# Create your views here.

# # # # #  C R U D P R O D U C T S # # # # # 

## Create
class CreateProduct(generic.CreateView):
    template_name = "core/create_product.html"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("core:list_product")


## Retrieve
# List
class ListProduct(generic.View):
    template_name = "core/list_product.html"
    context = {}

    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(status=True)
        self.context = {
            "products": products
        }
        return render(request, self.template_name, self.context)

# Detail
class DetailProduct(generic.View):
    template_name = "core/detail_product.html"
    context = {}

    def get(self, request, pk, *args, **kwargs):
        product = Product.objects.get(pk=pk)
        self.context = {
            "product": product
        }
        return render(request, self.template_name,self.context)



## Update
class UpdateProduct(generic.UpdateView):
    template_name = "core/update_product.html"
    model = Product
    form_class = UpdateProductForm
    success_url = reverse_lazy("core:list_product")


## Delete
class DeleteProduct(generic.DeleteView):
    template_name = "core/delete_product.html"
    model = Product
    success_url = reverse_lazy("core:list_product")
