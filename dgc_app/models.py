from django.db import models


class School(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Institution(models.Model):
    title = models.CharField(max_length=100)
    num = models.CharField(max_length=3)
    list_id = models.IntegerField(unique=True)
    schools = models.ManyToManyField(School)
    requirements = models.TextField(max_length=300,null=True,blank=True)
    ordered_list = models.BooleanField()

    def __str__(self):
        return self.title




class Available_country(models.Model):
    url = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    nav_title = models.CharField(max_length=100)
    institution = models.ManyToManyField(Institution)
   

    def __str__(self):
        return self.title


class About(models.Model):
    description = models.TextField(max_length=2000,null=True,blank=True)

    def __str__(self):
        return self.description


class Services(models.Model):
    description = models.TextField(max_length=500,null=False)

    def __str__(self):
        return self.description


class Services_info(models.Model):
    description = models.TextField(max_length=700,null=True,blank=True)
    services = models.ManyToManyField(Services,null=True,blank=True)
    def __str__(self):
        return self.description


class Email(models.Model):
    email = models.EmailField()


class Phone_numbers(models.Model):
    phone_number = models.CharField(max_length=30)


class Contact_info(models.Model):
    address = models.CharField(max_length=200,null=True,blank=True)
    emails = models.ManyToManyField(Email,null=True,blank=True)
    phone_numbers = models.ManyToManyField(Phone_numbers,null=True,blank=True)


class Course(models.Model):
    title = models.CharField(max_length=70,null=True,blank=True)

    def __str__(self):
        return self.title


class Available_courses(models.Model):
    description = models.TextField(max_length=300,null=False,blank=True)
    course = models.ManyToManyField(Course,null=True,blank=True)

    def __str__(self):
        return self.description


class Social_media(models.Model):
    link = models.CharField(max_length=300,blank=True,null=True)

    def __str__(self):
        return self.link


class Home_page_info(models.Model):
    title = models.CharField(max_length=30,null=False,blank=True)
    description1 = models.TextField(max_length=700,null=True,blank=True)
    description2 = models.TextField(max_length=700,null=True,blank=True)

    def __str__(self):
        return self.title


class News_image(models.Model):
   image = models.ImageField(upload_to='static/assets/img')



class New(models.Model):
    
    
    title = models.CharField(max_length=70,null=True,blank=True)
    tag = models.CharField(max_length=100)
    descripion = models.TextField(blank=True,null=True)
    short_descripion = models.TextField()
    headline = models.CharField(max_length=100)
    image = models.ManyToManyField(News_image, null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
    def __str__(self) -> str:
        return self.short_descripion

class MetaData(models.Model):
    page_name = models.CharField(max_length=40)
    key_words = models.TextField()
    description = models.TextField()

    def __str__(self) -> str:
        return "{},{}".format(self.page_name,"".join(self.description.split()[:20]))