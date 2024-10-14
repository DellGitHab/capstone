from django.urls import reverse  # Import reverse instead of reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Personnel, Visitors
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import PersonnelForm

# CRUD for Personnel
# ListView - Read all Personnel
class PersonnelListView(ListView):
    model = Personnel
    template_name = 'personnel_list.html'  # Your template name
    context_object_name = 'personnel_list'

# CreateView - Create new Personnel
class PersonnelCreateView(CreateView):
    model = Personnel
    template_name = 'personnel_form.html'  # Your template name
    fields = ['first_name', 'last_name', 'email', 'address', 'contact_number', 'rfid_tag']

    def get_success_url(self):
        return reverse('personnel_list')  # Use reverse to define success URL

# UpdateView - Update existing Personnel
class PersonnelUpdateView(UpdateView):
    model = Personnel
    template_name = 'personnel_form.html'  # Reusing the create form template
    fields = ['first_name', 'last_name', 'email', 'address', 'contact_number', 'rfid_tag']

    def get_success_url(self):
        return reverse('personnel_list')  # Use reverse to define success URL

# DeleteView - Delete existing Personnel
class PersonnelDeleteView(DeleteView):
    model = Personnel
    template_name = 'personnel_confirm_delete.html'  # Your delete confirmation template

    def get_success_url(self):
        return reverse('personnel_list')  # Use reverse to define success URL


# CRUD for Visitors

# ListView - Read all Visitors
class VisitorsListView(ListView):
    model = Visitors
    template_name = 'visitors_list.html'  # Template for listing Visitors
    context_object_name = 'visitors_list'

# CreateView - Create new Visitors
class VisitorsCreateView(CreateView):
    model = Visitors
    template_name = 'visitors_form.html'  # Template for creating/updating Visitors
    fields = ['first_name', 'last_name', 'address', 'contact_number', 'sector', 'rfid_tags']

    def get_success_url(self):
        return reverse('visitors_list')  # Use reverse to define success URL

# UpdateView - Update existing Visitors
class VisitorsUpdateView(UpdateView):
    model = Visitors
    template_name = 'visitors_form.html'  # Reusing the create form template
    fields = ['first_name', 'last_name', 'address', 'contact_number', 'sector', 'rfid_tags']

    def get_success_url(self):
        return reverse('visitors_list')  # Use reverse to define success URL

# DeleteView - Delete existing Visitors
class VisitorsDeleteView(DeleteView):
    model = Visitors
    template_name = 'visitors_confirm_delete.html'  # Template for confirming deletion

    def get_success_url(self):
        return reverse('visitors_list')  # Use reverse to define success URL


# Registration View
class EmployeeRegisterView(CreateView):
    template_name = 'employee_register.html'
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('personnel_list')  # Use reverse to define success URL

    def form_valid(self, form):
        # Save the user (creates an account)
        user = form.save()
        
        # Automatically log in the new user
        login(self.request, user)

        # Create an associated Personnel object
        personnel_form = PersonnelForm(self.request.POST)
        if personnel_form.is_valid():
            personnel = personnel_form.save(commit=False)
            personnel.user = user  # Link the Personnel to the newly created user
            personnel.save()

        return redirect(self.get_success_url())  # Redirect using get_success_url

    def get_context_data(self, **kwargs):
        # Add the Personnel form to the context
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['personnel_form'] = PersonnelForm(self.request.POST)
        else:
            context['personnel_form'] = PersonnelForm()
        return context
