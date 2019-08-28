from django.db import models

	# 'sponsor' field, is the company that the client works for/represents
	# if the client is a company, then this 'academic' variable is not nessessary
class Client(models.Model):
	UserID = models.IntegerField(primary_key=True)
	sponsor = models.ForeignKey(Sponsor)
	academic = models.ForeignKey(Academic)
	
	firstName = modelsCharField()
	lastName = modelsCharField()
	title = modelsCharField(max_length = 20)
	username = modelsCharField()
	password = modelsCharField()
	mobile = models.IntegerField();
	email = companyDescription = modelsCharField(max_length = 200)
	





# 'supervisor' variable holds the projects main Supervisor/manager name/ID
# 'sponsor' variable contains the details of the company 'sponsoring' the project for students
# 'time required' field, is just a simple text explanation about how long the project is going to take, eg "The project takes 6 months"
class Project(models.Model):
	ProjectID = models.IntegerField(primary_key=True)
	supervisor = models.ForeignKey(Client)
	
	noOfStudents = models.IntegerField()
	description = modelsCharField(max_length = 90000)
	timeRequired = companyDescription = modelsCharField(max_length = 1000)
	confirmed = models.BooleanField(default=False)
	viewable = models.BooleanField(default=False)
	creation_date = models.DateField()
	deadline_date = models.DateField()
	
	#checkboxes
	chemical = models.BooleanField(default=False)
	civil = models.BooleanField(default=False)
	elec = models.BooleanField(default=False)
	envir = models.BooleanField(default=False)
	materials = models.BooleanField(default=False)
	mechanical = models.BooleanField(default=False)
	mechatronic = models.BooleanField(default=False)
	mining = models.BooleanField(default=False)
	oilGas = models.BooleanField(default=False)
	Petroleum = models.BooleanField(default=False)
	Software = models.BooleanField(default=False)
	other = models.BooleanField(default=False)
	
	
	
	
	
	
class Sponsor(models.Model):
	sponsorID = models.IntegerField(primary_key=True);
		
	companyName = models.CharField(max_length = 100)
		
	companyDescription = modelsCharField(max_length = 9000)
	
	
	
	
	
class Academic(models.Model):
	academicID = models.IntegerField(primary_key=True)
	department = modelsCharField(max_length = 1000)
