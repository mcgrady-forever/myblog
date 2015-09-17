from django.shortcuts import render_to_response
from django import template
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse
from django.core.cache import cache

def homepage(request):
	context = template.RequestContext(request)

	res = request.GET["res"] 

	 
	tmp = cache.get('res')
	
	if tmp > res:
		res = tmp 
	else:
		cache.set('res', res, 30)  
	
	context.update({
            "res": res,
        })

	return render_to_response("base.html", context)
	#return HttpResponse("Hello!")