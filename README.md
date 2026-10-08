# WADP-L4 Demonstration-5 [Event-Scheduling-System]
# 🎉 Event Management System

A simple and user-friendly **Event Management Web Application** built with **Python and Django**.

This project allows users to manage their events by creating, viewing, updating, and deleting events. Users can organize events based on event type, date, status, and location.

The project demonstrates practical implementation of **Django Custom User Models, Authentication, CRUD Operations, Foreign Key Relationships, Forms, Templates, and Database Management**.

---

## 🚀 Features

### 👤 User Management

* Custom User Model using Django `AbstractUser`
* User registration and login
* Full name support
* Phone number support
* User authentication
* Each user can manage their own events

### 📅 Event Management

* Create events
* View event details
* Update events
* Delete events
* Display event lists
* Assign events to users

### 🎯 Event Types

Users can organize events into different categories:

* 🏢 Conference
* 🎵 Concert
* 💍 Wedding

### 📊 Event Status

Events can have different progress statuses:

* ⏳ Not Started
* 🔄 In Progress
* ✅ Completed

### 📍 Event Location

Each event can have a specific location.

### 📆 Event Date

Users can specify the date on which an event will take place.

---

## 🛠️ Technologies Used

* **Python**
* **Django**
* **SQLite**
* **HTML5**
* **CSS3**
* **Bootstrap** *(if used)*
* **Django Templates**
* **Git & GitHub**

---

---

## 🔗 Database Relationship

Each user can create multiple events.

```text
EventUserModel
      │
      │  One-to-Many
      ↓
EventModel
      │
      ├── Event Title
      ├── Event Type
      ├── Description
      ├── Event Date
      ├── Status
      └── Location
```

The relationship is implemented using:

```python
user = models.ForeignKey(
    EventUserModel,
    on_delete=models.CASCADE,
    related_name='events'
)
```

The `related_name='events'` allows you to access a user's events like:

```python
request.user.events.all()
```

---

## 📂 Project Structure

```text
Event Management/
│
├── manage.py
│
├── project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── EventApp/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── media/
├── static/
├── db.sqlite3
└── manage.py
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository.git
```

### 2. Navigate to the Project

```bash
cd your-repository
```

### 3. Create a Virtual Environment

```bash
python -m venv env
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
env\Scripts\activate
```

**Mac/Linux:**

```bash
source env/bin/activate
```

### 5. Install Dependencies

```bash
pip install django
```

Or, if `requirements.txt` is available:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configure Custom User Model

Because this project uses `EventUserModel` as the custom user model, add the following to `settings.py`:

```python
AUTH_USER_MODEL = 'EventApp.EventUserModel'
```

Replace `EventApp` with your actual Django app name.

---

## 🗄️ Database Setup

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create an admin user:

```bash
python manage.py createsuperuser
```

---

## ▶️ Run the Project

Start the Django development server:

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

---

## 🔐 Django Admin

Access the Django admin panel:

```text
http://127.0.0.1:8000/admin/
```

From the admin panel, you can manage:

* Users
* Events
* Event types
* Event status
* Event dates
* Event locations

---

## 📌 Event Workflow

```text
Register / Login
       ↓
Create Event
       ↓
Select Event Type
       ↓
Set Event Date
       ↓
Set Location
       ↓
Not Started
       ↓
In Progress
       ↓
Completed
```

---

## 📋 Event Fields

| Field       | Description                     |
| ----------- | ------------------------------- |
| User        | Owner of the event              |
| Event Title | Name of the event               |
| Event Type  | Conference, Concert, or Wedding |
| Description | Details about the event         |
| Event Date  | Date of the event               |
| Status      | Current event progress          |
| Location    | Event venue/location            |
| Created At  | Event creation date             |

---

## 💡 Example Events

| Event                | Type       | Status     | Location |
| -------------------- | ---------- | ---------- | -------- |
| Tech Conference 2026 | Conference | InProgress | Dhaka    |
| Music Night          | Concert    | NotStarted | Gazipur  |
| Wedding Ceremony     | Wedding    | Completed  | Dhaka    |

---

## 🎯 Learning Objectives

This project demonstrates practical knowledge of:

* Python
* Django
* Django Custom User Model
* `AbstractUser`
* Django Authentication
* CRUD Operations
* Django Models
* Foreign Key Relationships
* `related_name`
* Django Forms
* Django Templates
* SQLite Database
* Django Admin
* Git & GitHub

---

## 🔮 Future Improvements

The project can be enhanced with:

* 🔎 Event search
* 🔍 Filter events by type
* 📊 Event dashboard
* 📅 Calendar view
* 🔔 Event reminders
* 📧 Email notifications
* 👥 Event participants
* 📱 Responsive design
* 🌙 Dark mode
* 📈 Event statistics
* 🔐 Password reset
* 🚀 Deployment with Render or PythonAnywhere

---

## 👨‍💻 Developer

**Oren Michael Dessai**

### 💻 Backend Development Focus

**Python | Django | Backend Development | REST APIs**

Building web applications with Django and continuously learning new backend technologies.

---

## ⭐ Support

If you find this project useful, please consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project was created for **learning and educational purposes**.
