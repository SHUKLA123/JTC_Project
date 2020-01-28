from django.shortcuts import render, get_object_or_404, redirect

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Product, ProductComment, Service

from django.contrib import messages

from django.contrib.auth.models import User

from django.db.models import Avg
# Create your views here.

def index(request):
    products = Product.objects.all().order_by('-list_date').filter(is_published=True)

    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
        'category' : 'P',
        'products': paged_products,
    }

    return render(request, 'products/products.html', context)


def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    comments = ProductComment.objects.filter(product=product_id)
    # print(comments)

    avg_rating = comments.aggregate(Avg('rating'))
    avg_rating = avg_rating['rating__avg']

    if not avg_rating:
        avg_rating = 0

    # print(avg_rating.rating__avg)
    context = {
        'product': product,
        'comments': comments,
        'avg_rating': avg_rating
    }
    return render(request, 'products/product.html', context)



# To-Do: Add searching with both products and services
def search(request):

    search_choices = {
      'P':'Products',
      'S':'Services',
    }

    queryset_list = Product.objects.all().order_by('-list_date')

    # Category
    if 'category' in request.GET:
        category = request.GET['category']

        if category == "P":
            queryset_list = Product.objects.all().order_by('-list_date')

        if category == "S":
            queryset_list = Service.objects.all().order_by('-list_date')

    else:
        context = {
            'products': queryset_list,
            'values': request.GET,
            'search_choices': search_choices
        }
        messages.error(request, "Wrong way to Search. Please select Product or Services.")
        return render(request, 'products/search.html', context)

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # pattern
    if 'property' in request.GET:
        property = request.GET['property']
        if property:
            if queryset_list.filter(description__icontains=property):
                queryset_list = queryset_list.filter(description__icontains=property)

    context = {
        'products': queryset_list,
        'values': request.GET,
        'search_choices': search_choices
    }
    return render(request, 'products/search.html', context)


def services(request):

    services = Service.objects.all()
    values = {
    'category' : 'S',
    }
    return render(request,'products/services.html', {'services':services, 'values':values})


def service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    #comments = ProductComment.objects.filter(produc=service_id)
    #print(comments)
    context = {
        'service': service,
        #'comments': comments
    }
    return render(request, 'products/service.html', context)


def productcomment(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        product_id = request.POST['product_id']
        rating = request.POST['rating']
        comment = request.POST['comment']

        productinstance = Product.objects.get(id=product_id)

        first_name = User.objects.get(id=user_id).first_name
        last_name = User.objects.get(id=user_id).last_name

        name = first_name + ' ' + last_name

        if user_id == 0:
            messages.error(request, 'Sorry, You are not Authenticated. Try Creating Account.')
            return redirect('/products/'+product_id)

        newproductcomment = ProductComment(product=productinstance, name=name, comment=comment, rating=rating)
        newproductcomment.save()

        messages.success(request, 'Thanks for reviewing our Product. Explore our other Products.')
        return redirect('/products/'+product_id)
