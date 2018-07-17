from django.db import models
import datetime as dt
# Create your models here.
class Location(models.Model):
	country=models.CharField(max_length =30)
	image = models.ImageField(upload_to = 'location/')
	def __str__(self):
		return	self.country

class Categorie(models.Model):
	name=models.CharField(max_length=30)
	image = models.ImageField(upload_to = 'category/')
	def __str__(self):
		return self.name

class Image(models.Model):
	title=models.CharField(max_length =30)
	description=models.CharField(max_length =30)
	location = models.ForeignKey(Location, related_name='images')
	category = models.ForeignKey(Categorie, related_name='images')
	date = models.DateTimeField(auto_now_add=True)				
	image = models.ImageField(upload_to = 'images/')
	def __str__(self):
		return self.title
	class Meta:
			ordering=['title']
	def save_Image(self):
		self.save()
	def update_Image(self):
		self.update()
	def delete_Image(self):
		self.delete()

	@classmethod
	def todays_images(cls):
		today = dt.date.today()
		image_date=cls.objects.filter(date__date =today)
		return image_date

	@classmethod
	def days_images(cls,date):
		image_news=cls.object.filter(date__date=date)
		return image_date	

	@classmethod
	def search_by_title(cls,search_term):
		image = cls.objects.filter(title__icontains=search_term)
		return image	

	@classmethod
	def get_images(cls,category_id):
		image = cls.objects.filter(category_id=id)
		return image	