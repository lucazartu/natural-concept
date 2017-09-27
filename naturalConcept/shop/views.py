from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from cart.forms import CartAddProductForm
from facade import Fachada
from .forms import ProductUpdateForm
from .models import Category, Product

def product_list(request, category_slug=None):
    fachada = Fachada()
    category = None
    categories = Category.objects.all()
    # metodo listar da fachada
    products = fachada.listar(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})

def product_delete(request, id, slug):
    fachada = Fachada()
    try:
        fachada.remover_produto(id=id, slug=slug)
    except Exception as e:
        print(e)
        messages.warning(request, "Produto não existe mais")
        return redirect(reverse_lazy('shop:product_list'))

    messages.success(request, "Produto removido com sucesso!")
    return redirect(reverse_lazy('shop:product_list'))

def product_update(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    if request.method == 'POST':
        form = ProductUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            fachada = Fachada()
            cd = form.cleaned_data
            if cd['image']:
                fs = FileSystemStorage()
                fs.save(cd['image'].name, cd['image'])

            if not cd['image']:
                del cd['image']

            try:
                fachada.atualizar_produto(idProduto=id, **cd)
            except Exception as e:
                messages.warning(request, str(e))
                return redirect(reverse_lazy('shop:product_list'))
            messages.success(request, "Produto atualizado com sucesso!")
            return redirect(reverse_lazy('shop:product_list'))
        else:
            form = ProductUpdateForm()
            return render(request, 'shop/product/update.html', {'form': form})
    form = ProductUpdateForm(instance=product)
    return render(request, 'shop/product/update.html', {'form': form})

def product_create(request):
    if request.method == 'POST':
        form = ProductUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            fachada = Fachada()
            cd = form.cleaned_data
            if cd['image']:
                fs = FileSystemStorage()
                fs.save(cd['image'].name, cd['image'])

            try:
                fachada.adicionar_produto(**cd)
            except Exception as e:
                messages.warning(request, str(e))
                return redirect(reverse_lazy('shop:product_list'))
            messages.success(request, "Produto adicionado com sucesso!")
            return redirect(reverse_lazy('shop:product_list'))
        else:
            form = ProductUpdateForm()
            return render(request, 'shop/product/create.html', {'form': form})
    form = ProductUpdateForm()
    return render(request, 'shop/product/create.html', {'form': form})