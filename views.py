from django.shortcuts import render
from customer_data.models import *
from django.utils.encoding import smart_str, smart_unicode

def index(request):
    lines_records = Productlines.objects.all()
    emp_records = Employees.objects.all()

    product_data = []
    productlines_data = []
    prod_and_lines = {}
    emp_records_output = []
    productcode_order = {}

    order_date_vs_orders = {}

    for emp in emp_records:
	emp_records_output.append(', '.join((str(emp.lastname), str(emp.firstname))))	
	
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

	    orderdetails_records = Orderdetails.objects.filter(productcode=str(pd.productcode))
	    productcode_order.setdefault(str(pd.productcode), [])

	    for ordr in orderdetails_records:
		productcode_order[str(pd.productcode)].append(str(ordr.ordernumber.ordernumber))


	    orders_records = Orders.objects.filter(ordernumber=str(ordr.ordernumber.ordernumber))
	    for orecord in orders_records:
		order_date_vs_orders.setdefault(orecord.orderdate, [])
		order_date_vs_orders[orecord.orderdate].append(str(orecord.ordernumber))
	
    return render(request, 'index.html',
				{'product_data': product_data,
				'productlines_data': productlines_data, 'prod_and_lines': prod_and_lines,
				 'emp_records_output': emp_records_output, 'productcode_order': productcode_order, 
				'emp_records_output': emp_records_output, 'order_date_vs_orders': order_date_vs_orders})

def layout(request):
	return render(request, 'layout.html')
