# Master
Master - a system for recording the work of small and medium-sized enterprises.
## Installation
1. Install [Python 3.11](https://www.python.org/downloads/release/python-3114/)
2. Install [PostgreSQL](https://www.postgresql.org/download/)
3. Install [Git](https://git-scm.com/downloads)
4. Clone repository
```bash
git clone https://github.com/moonmoontra/Master.git
```
5. Create virtual environment
```bash
python -m venv venv
```
6. Activate virtual environment
```bash
venv\Scripts\activate
```
7. Install requirements
```bash
pip install -r requirements.txt
```
8. Create database
```bash
python manage.py migrate
```
9. Create superuser
```bash
python manage.py createsuperuser
```
10. Run server
```bash
python manage.py runserver
```
