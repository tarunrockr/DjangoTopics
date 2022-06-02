from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def setsession_def(request):

	request.session['name'] = "Tarun Kumar Sharma"
	request.session['email']  = "mk@gmail.com"

	# Setting the test coolie 
	# request.session.set_test_cookie()

	# Setting session expiry age in seconds (20 seconds)
	#request.session.set_expiry(20)


	return render(request, 'demo/set_session.html')

def getsession_def(request):

	session_name  = request.session.get('name', "Name no exists")
	session_email = request.session.get('email',"Email not exists") 
	session_place = request.session.setdefault('place', 'Rajasthan')
	header        = "Session Data:"

	# Check test cookie
	#print(request.session.test_cookie_worked())

	print("Session cookie age: ", request.session.get_session_cookie_age(), " seconds")
	print("Session Expiry age: ",  request.session.get_expiry_age(), " seconds")
	print("Session Expiry Date: ", request.session.get_expiry_date())
	print("Session expire when browser closes: ", request.session.get_expire_at_browser_close())

	return render(request, 'demo/get_session.html', {'session_name': session_name, 'session_email': session_email, 'session_place': session_place, 'header': header})

def delsession_def(request):
	
	# if 'name' in request.session:
	# 	del request.session['name']

	# if 'email' in request.session:
	# 	del request.session['email']

	# if 'place' in request.session:
	# 	del request.session['place']

	# Deleting the test cookie
	#request.session.delete_test_cookie()

	request.session.flush()

	return render(request, 'demo/delete_session.html', {'data': 'Session name deleted successfully'})

