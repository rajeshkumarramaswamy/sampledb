from django.shortcuts import render
from customer_data.models import *
from django.utils.encoding import smart_str, smart_unicode

def index(request):
    lines_records = Productlines.objects.all()
    product_records = Products.objects.all()

    lines_records_output = []
    products_records_output = []

    for pl in lines_records:
        lines_records.productline = pl.productline
        lines_records_output.append(pl.productline)

    for pr in product_records:
        product_records.productname = pr.productname
        products_records_output.append(pr.productname)

    product_data = []
    productlines_data = []
    prod_and_lines = {}
    for pl in lines_records:
        productlines_data.append(str(pl.productline))
        prod_and_lines.setdefault((str(pl.productline)), [])
        for pd in product_records:
            product_data.append((smart_str(pd.productname), smart_str(pl.productline)))
            prod_and_lines[pl.productline].append(pd.productname)


    return render(request, 'index.html',
                  {'product_data': product_data, 'productlines_data': productlines_data, 'prod_and_lines': prod_and_lines})
