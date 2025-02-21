# Django Backend for Personal Website

🚀 A backend for my personal website, built with Django and Django Rest Framework (DRF).

## 🔧 Features
- **Django & DRF**: RESTful API for dynamic content.
- **Authentication**: Secure user authentication.
- **Database Support**: Uses PostgreSQL (configurable via environment variables).
- **Docker Support**: Easily deployable with Docker.
- **CI/CD**: Automated testing with GitHub Actions.

## 🚀 Getting Started

### **1️⃣ Clone the Repository**
```bash
 git clone https://github.com/amirdavoodi98/django-backend-personal-website.git
 cd django-backend-personal-website
```

### **2️⃣ Create Environment File**
```bash
cp envs/.env.example envs/.env.local
```
Modify `envs/.env.local` with your environment variables.

### **3️⃣ Install Dependencies**
#### Using Virtual Environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### **4️⃣ Run Migrations**
```bash
python manage.py migrate
```

### **5️⃣ Start Development Server**
```bash
python manage.py runserver
```
Access the API at: **http://127.0.0.1:8000/**

## 🧪 Running Tests
```bash
python manage.py test
```

## 🛠️ Docker Support
Build and run the project with Docker:
```bash
docker-compose up --build
```

## 🚀 Deployment
- Use **Gunicorn & Nginx** for production.
- Configure **CI/CD** with GitHub Actions.

## 📄 License
This project is licensed under the MIT License.

---
Feel free to contribute or report issues! 🎉

