from django import forms

# Different options for Number of Students and IP
NUMBER_OF_STUDENTS =[(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)]
IP_OPTIONS = [("Sponsor will retain IP", "Sponsor will retain IP"), ("UWA will retain IP", "UWA will retain IP")]

# Form for project proposals including
class ProjectProposalForm(forms.Form):
    title = forms.CharField(label = 'Title of Project')
    description = forms.CharField(label = 'Description')
    supervisor2Title = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    supervisor2FirstName = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    supervisor2LastName = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    supervisor3Title = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    supervisor3FirstName = forms.CharField(label='', required=False,widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    supervisor3LastName = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    noOfStudents = forms.IntegerField(label = 'Number of Students Required', widget = forms.Select(choices=NUMBER_OF_STUDENTS))
    projectTags = forms.CharField(label = 'Project Tags', widget=forms.TextInput(attrs={'placeholder': 'E.g. Research, Community, Programming'}))
    prerequisites = forms.CharField(label = 'Prerequisites', widget=forms.TextInput(attrs={'placeholder': 'E.g. CITS2002, Python, Linear Regression'}))
    IP = forms.CharField(label = 'IP',  widget = forms.Select(choices=IP_OPTIONS))
    chemical = forms.BooleanField(label = 'Chemical', required=False)
    civil = forms.BooleanField(label = 'Civil', required=False)
    elec = forms.BooleanField(label = 'Electrical', required=False)
    envir = forms.BooleanField(label = 'Environmental', required=False)
    materials = forms.BooleanField(label = 'Materials', required=False)
    mechanical = forms.BooleanField(label = 'Mechanical', required=False)
    mechatronic = forms.BooleanField(label = 'Mechatronic', required=False)
    mining = forms.BooleanField(label = 'Mining', required=False)
    oilGas = forms.BooleanField(label = 'Oil and Gas', required=False)
    petroleum = forms.BooleanField(label = 'Petroleum', required=False)
    software = forms.BooleanField(label = 'Software', required=False)
    other = forms.BooleanField(label = 'Other', required=False)
