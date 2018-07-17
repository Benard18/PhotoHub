from django.shortcuts import render
from .models import Categorie,Image,Location
import datetime as dt
# Create your views here.
def index(request):
	date=dt.date.today()
	images=Image.todays_images()
	categories = Categorie.objects.all()
	return render(request, 'index.html',{'images':images,'date':date, 'categories':categories})

def search_results(request):
	if 'image' in request.GET and request.GET["image"]:
		search_term = request.GET.get("image")
		searched_images=Image.search_by_title(search_term)
		message = f"{search_term}"

		return render(request,'search.html',{'message':message,'images':searched_images})


	else:
		message = "You haven't searched for any term"
		return render(request,'search.html',{'message':message})	

def image(request,image_id):
	try:
		image = Image.objects.get(id = image_id)
	except DoesNotExist:
		raise Http404()
	return render(request,'image.html',{'image':image})		

def category(request,category_id):

	cat = Categorie.objects.get(pk = category_id)
	images = cat.images.all()#
	print(images)


	return render(request,'category.html',{'categories':images})	

def location(request,location_id):

	loc = Location.objects.get(pk = location_id)
	images = loc.images.all()

	return render(request,'location.html',locals())	
