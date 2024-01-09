from django.db import models

# Create your models here.


#creat a blog model
class Blog(models.Model):
	title = models.CharField(max_length = 100)
	pub_date = models.DateTimeField()
	body = models.CharField(max_length = 200)
	image = models.ImageField(upload_to = 'images/')

	def summary(self):
		if len(self.body)>150:
			return self.body[:200]
		else:
			return self.body

	def pubDate(self):
		return self.pub_date.strftime('%b %e %Y')

	def __str__(self):
		return self.title
		#to return the titel as the name of the AdminBlog

