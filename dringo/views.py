from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

def home(request, pyaudio=None):
    return HttpResponse("First Dringo Response")


from django.contrib.auth import authenticate, login
from django.shortcuts import render

def logout_request(request):
    logout(request)
    return redirect('/einloggen')
def login_request(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['username']
        print(username)
        password = request.POST['password']
        # Check username and password combination if correct
        user = authenticate(username=username, password=password)
        if user is not None:
            # Save session as cookie to login the user
            login(request, user)
            # Success, now let's login the user.
            print("Login Success")
            return redirect('/patienten')
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'login.html', {'error_message': 'Falsche Daten'})
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, 'login.html')


def new_case(request):
    return render(request, 'not_used.html')
