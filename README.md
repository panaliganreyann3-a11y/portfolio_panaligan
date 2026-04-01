# Personal Portfolio Website — Django

**ITS 305 Midterm Project | Section A**

---

## What This Project Is About

This is a **personal portfolio website** built using the Django web framework. It displays your name, background, skills, projects, education, and contact information in a clean, professional layout.

All content is managed through the **Django Admin panel** — no code editing needed after setup. Just log in to `/admin`, fill in your details, and the website updates automatically.

The color scheme follows a dark navy and teal palette (`#191E29`, `#132D46`, `#01C38D`) for a modern, professional look.

---

## Project Structure

```
portfolio/
├── main/                         # Django app
│   ├── static/
│   │   ├── css/style.css         # All styles
│   │   └── js/script.js          # All JavaScript
│   ├── templates/
│   │   └── home.html             # Main template (all sections)
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── portfolio_panaligan/         # Project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

## Website Sections

| # | Section   | What it shows                              |
|---|-----------|---------------------------------------------|
| 1 | Home      | Name, tagline, profile photo, navigation    |
| 2 | About     | Personal background and career goals        |
| 3 | Skills    | Skills with progress bars                   |
| 4 | Projects  | Project cards with tools and GitHub links   |
| 5 | Education | Timeline of schools and degrees             |
| 6 | Contact   | Email, GitHub, LinkedIn + message form      |

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/portfolio_panaligan.git
cd portfolio_panaligan
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run database migrations
```bash
python manage.py migrate
```

### 5. Create an admin account
```bash
python manage.py createsuperuser
```

### 6. Start the server
```bash
python manage.py runserver
```

- Website: `http://127.0.0.1:8000`
- Admin panel: `http://127.0.0.1:8000/admin`

---

## Adding Your Content

Log in to the admin panel and add your data:

- **Profile** — name, tagline, photo, background, career goals
- **Skills** — skill name, Font Awesome icon class, level %
- **Projects** — title, description, tools (space-separated), GitHub link
- **Education** — school, degree, year
- **Contact Info** — email, GitHub URL, LinkedIn URL

---

## Deployment (PythonAnywhere)

1. Upload or clone project to PythonAnywhere
2. Create a virtual environment and install requirements
3. Set WSGI file to point to `portfolio_panaligan.wsgi`
4. Add static files mapping: `/static/` → `/home/username/portfolio/staticfiles/`
5. Run `python manage.py collectstatic`
6. Reload the web app

Live URL format: `https://firstname_lastname.pythonanywhere.com`

---

## Technologies Used

- Python 3.x + Django 4.x
- SQLite (database)
- HTML5, CSS3, Vanilla JavaScript
- Font Awesome (icons)
- Google Fonts — Outfit + Inter
- PythonAnywhere (hosting)
- GitHub (version control)

---

## Author

**[Your Full Name]**  
ITS 305 — Section A  
`https://firstname_lastname.pythonanywhere.com`
