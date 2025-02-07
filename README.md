# Cybersecurity Blog 
This website blog is created in partial requirement of our CMSC134: Cybersecurity class. 

## Setup 
1. Add your device's SSH key to your GitHub account: `Github > Profile > Settings > SSH & GPG Key > New SSH Key`
2. Clone the repository: `git@github.com:omoraisu/134-Cybersecurity-Blog.git`
3. Setup Python virtual environment.
4. Install dependencies: `pip install -r requirements.txt`
5. Setup database: `python manage.py migrate`
6. Collect static files: `python manage.py collectstatic`
7. Run server: `python manage.py runserver`
