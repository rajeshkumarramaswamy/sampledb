from django.shortcuts import render
from customer_data.models import *
from django.utils.encoding import smart_str, smart_unicode

def index(request):
    lines_records = Productlines.objects.all()

    product_data = []
    productlines_data = []
    prod_and_lines = {}

    for pl in lines_records:
        productlines_data.append(str(pl.productline))
        prod_and_lines.setdefault(str(pl.productline), [])
	product_records = Products.objects.filter(productline=pl.productline)

        for pd in product_records:
	    try:
            	product_data.append(str(pd.productname.replace(u'\u2019', "'")))
	    except:
	    	import pdb;pdb.set_trace()
            prod_and_lines[str(pl.productline)].append(str(pd.productname.replace(u'\u2019', "'")))


    return render(request, 'index.html',
{'product_data': product_data, 'productlines_data': productlines_data, 'prod_and_lines': prod_and_lines})
