## File Sharing System by Adarsh Kumar

### Overview:

This is a django web app that is used for file sharing.

### Setup:

1. Install Python 3.9.6

2. Install/Setup Python VirtualEnv and activate it
  * python -m venv venv
  * source venv/bin/activate (for MacOS)
  * venv/scripts/activate (for Windows)

3. Install Required Files
  * pip install -r requirements.txt

4. Before running the service setup the required tables:
  * python manage.py migrate
  * python manage.py createsuperuser (and enter the details)
  
8. To Run Service:
  * python manage.py runserver

### Points to remember

Users registered using Signup URL are Client Users and they have permission only to view and download files.
Only Operation users can upload the file. Ops user can only be enterred from Admin Panel as of now.
Before creating any user, create Groups (if already not existing). 
  * Id - 1, Name = 'Users'
  * Id - 2, Name = 'Ops'