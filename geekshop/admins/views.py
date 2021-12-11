from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, TemplateView
from django.urls import reverse, reverse_lazy

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductCreateForm, CategoryCreateForm, \
    CategoryUpdateForm, ProductUpdateForm
from authapp.models import User
from mainapp.mixin import BaseClassContextMixin, CustomDispatchMixin
from mainapp.models import Product, ProductCategory


class IndexTemplateView(TemplateView):
    template_name = 'admins/admin.html'


class UserListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-read.html'
    title = 'Geekshop - Админ | Список пользователей'


class UserCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'Geekshop - Админ | Создать пользователя'


class UserUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'Geekshop - Админ | Изменить пользователя'


class UserDeleteView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'Geekshop - Админ | Удалить пользователя'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class CategoryListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-read.html'
    title = 'Geekshop - Админ | Список категорий'


class CategoryCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-create.html'
    form_class = CategoryCreateForm
    success_url = reverse_lazy('admins:admin_category')
    title = 'Geekshop - Админ | Создать категорию'


class CategoryUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-update-delete.html'
    form_class = CategoryUpdateForm
    success_url = reverse_lazy('admins:admin_category')
    title = 'Geekshop - Админ | Обновление категории'


class CategoryDeleteView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-update-delete.html'
    success_url = reverse_lazy('admins:admin_category')
    title = 'Geekshop - Админ | Удаление категории'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ProductListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-product-read.html'
    title = 'Geekshop - Админ | Список товаров'


class ProductCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-product-create.html'
    form_class = ProductCreateForm
    success_url = reverse_lazy('admins:admin_products')
    title = 'Geekshop - Админ | Создать товар'


class ProductUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-product-update-delete.html'
    form_class = ProductUpdateForm
    success_url = reverse_lazy('admins:admin_products')
    title = 'Geekshop - Админ | Изменение товара'


# @user_passes_test(lambda u: u.is_superuser)
# def admin_products_update(request, pk):
#     product_select = Product.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = ProductUpdateForm(data=request.POST, instance=product_select, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_products'))
#     else:
#         form = ProductUpdateForm(instance=product_select)
#     context = {
#         'title': 'Geekshop - Админ | Обновление товара',
#         'form': form,
#         'product_select': product_select
#     }
#     return render(request, '', context)

class ProductDeleteView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-product-update-delete.html'
    success_url = reverse_lazy('admins:admin_products')
    title = 'Geekshop - Админ | Удаление товара'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
