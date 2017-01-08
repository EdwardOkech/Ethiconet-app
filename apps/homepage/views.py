from django.shortcuts import render
from django.http import HttpResponse 
from django.template import RequestContext, loader
from django.template.loader import get_template
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, render_to_response,render, Http404

# Create your views here.



def homepage(request):
	# output = """
	# <html>
	#    <head><title>Ethiconet | Home </title></head>
	#    <body>
	#       <h3> Welcome to %s Home Page </h3>
	#       <h5> Developed by %s.</h5>
	#     </body>
	# </html>
	# """ %('Ethiconet','Edward Okech!!')
	# temp = loader.get_template('homepage/homepage.html')
	return render(request, 'homepage/index.html')

