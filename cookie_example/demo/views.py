from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
# Create your views here.


def set_cookie_def(request):

	# Syntex to set cookie - HttpResponse.set_cookie(key, value="", max_age=None, expires=None, path='/'), domain = None, secure = false, httponly = False, samesite = None)
	# 1. key = ""
	# 2. value = ""
	# 3. max_age = "It takes seconds as input to set the age."
	# 4. expires = "It takes time in datetime format"

	# response = render(request, 'cookie_example/set_cookie.html')
	# # response.set_cookie('name', 'Tarun') 
	# # response.set_cookie('name', 'Tarun', max_age = 60) 
	# response.set_cookie('name', 'Tarun', expires = datetime.utcnow()+timedelta(days=2)) 

	# Setting up the signed cookie
	response = render(request, 'cookie_example/set_cookie.html')
	response.set_signed_cookie('name', 'Yogesh', salt= 'nt1', expires = datetime.utcnow()+timedelta(days=2))


	return response

def get_cookie_def(request):

	# cookie_name = request.COOKIES.get('name','Not exists')
	# header = "Cookie data"

	cookie_name = request.get_signed_cookie('name', salt = 'nt1', default="Guest")
	header = "Cookie data"
	return render(request, 'cookie_example/get_cookie.html', {'header': header, 'name': cookie_name})

def delete_cookie_def(request):

	response = render(request, 'cookie_example/delete_cookie.html')
	response.delete_cookie('name')
	return response