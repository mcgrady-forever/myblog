from django.shortcuts import render_to_response
from django import template
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse
from django.core.cache import cache
from django.core.cache import caches
from apps.home.tasks import add

def homepage(request):
	context = template.RequestContext(request)
	
	res = request.GET["res"] 
	
	print 'ft add 2'
	print 'dev add1'
	print 'add1'
	print 'ft add1'
	print 'git not staged'
	print 'git not staged1'
	#import pdb;pdb.set_trace() 
	tmp = cache.get('res')
	
	if tmp > res:
		res = tmp 
	else:
		cache.set('res', res, 30)

	result = add.delay(8, 8)  
	res = result.get()
	 
	context.update({
            "res": res,
        })

	return render_to_response("base.html", context)


def redis_cache(request):
	#import pdb;pdb.set_trace()
	context = template.RequestContext(request)

	redis_cache = caches['default']

	res = request.GET["res"] 

	print 'add1'
	print 'ft add1'
	 
	tmp = redis_cache.get('res')
	
	if tmp > res:
		res = tmp 
	else:
		redis_cache.set('res', res)  
	
	context.update({
            "res": res,
        })

	return render_to_response("base.html", context)


def kvs_cache(request):
	context = template.RequestContext(request)

	redis_cache = caches['kvs']
	res = request.GET["res"] 
	tmp = redis_cache.get('res')
	
	if tmp > res:
		res = tmp 
	else:
		redis_cache.set('res', res)  
	
	context.update({
            "res": res,
        })

	return render_to_response("base.html", context)


def memcached_cache(request):
	#import pdb;pdb.set_trace()
	context = template.RequestContext(request)

	redis_cache = caches['memcached']

	res = request.GET["res"] 
	 
	tmp = redis_cache.get('res')
	
	if tmp > res:
		res = tmp 
	else:
		redis_cache.set('res', res)  
	
	context.update({
            "res": res,
        })

	return render_to_response("base.html", context)


def ocs_cache(request):
	#import pdb;pdb.set_trace()
	context = template.RequestContext(request)

	cache = caches['ali_ocs']

	res = request.GET["res"] 
	 
	tmp = cache.get('res')
	
	if tmp > res:
		res = tmp 
	else:
		cache.set('res', res)  
	
	context.update({
            "res": res,
        })

	return render_to_response("base.html", context)

def send_mail(request):
	sendmail.delay(dict(to='396184333@qq.com'))
	context = template.RequestContext(request)
	context.update({
        			"res": "Using celery send mail.",
   				})

	return render_to_response("base.html", context)
