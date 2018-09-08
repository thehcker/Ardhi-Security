from django.shortcuts import render,redirect
from myprofile.models import titledeed

# Create your views here.
def home(request):
	context = locals()
	template = 'home.html'
	return render(request,template,context)
def about(request):
	context = locals()
	template = 'about.html'
	return render(request,template,context)
def index(request):
	context = locals()
	template = 'index.html'
	return render(request,template,context)

def login(request):
	context = locals()
	template = 'login.html'
	return render(request,template,context)

def signup(request):
	context = locals()
	template = 'signup.html'
	return render(request,template,context)

def logout(request):
	context = locals()
	template = 'logout.html'
	return render(request,template,context)

def titleDeed(request):
	template = 'titledeed.html'
	return render(request,template)

def Deed(request):
	owners_name = request.GET['owners_name']
	ref_no = request.GET['ref_no']
	demographic = request.GET['demographic']
	size = request.GET['size']
		#price = request.GET['price']
	title = titledeed.objects.create(
		owners_name = owners_name,
		ref_no = ref_no,
		demographic = demographic,
		size = size,
		date = date
		)
	title.save()
	return redirect('title')

def title(request):
	title = titledeed.objects.all()
	template = 'title.html'
	return render(request,template,{"Title":title})