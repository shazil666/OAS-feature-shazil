from django.shortcuts import render
from products.models import products
from django.core import paginator
from django.core.paginator import Paginator

def home(request):
    return render(request, 'index.html')
def store(request):
    return render(request, 'store list.html')
def vendor_abcde(request):
    return render(request, 'abcde.html')
def vendor_mally(request):
    return render(request, 'mally.html')
def vendor_roadscooter(request):
    return render(request, 'roadscooter.html')
def vendor_ricky(request):
    return render(request, 'ricky.html')
def vendor_rest(request):
    return render(request, 'rest.html')
def blog(request):
    productData = products.objects.all()
    paginator = Paginator(productData,5)
    page_number = request.GET.get('page')
    productDataFinal = paginator.get_page(page_number)
    totolpage = productDataFinal.paginator.num_pages


    data = {
        "products":productDataFinal,
        "lastpage":totolpage,
        "totolpagelist":[n+1 for n in range(totolpage)]
    }


    return render(request, 'blog.html', data)
    


def blogDetail(request):
    return render(request, 'blog detail.html')