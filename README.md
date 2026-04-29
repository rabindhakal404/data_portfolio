# Portfolio Website — Django

A modern single-page-style portfolio for a student data analyst with light/dark mode.

## Pages
- `/` — Home (Hero + Skills + Featured Projects + Contact all in one scrolling page)
- `/projects/` — All projects listing
- `/projects/<id>/` — Project detail
- `/download-cv/` — Downloads CV PDF
- `/admin/` — Django admin panel

## Setup

1. `git clone` or unzip the project
2. `python -m venv venv`
3. Windows: `venv\Scripts\activate` | Mac/Linux: `source venv/bin/activate`
4. `pip install -r requirements.txt`
5. Set a real `SECRET_KEY` in `.env`
6. `python manage.py migrate`
7. `python manage.py createsuperuser`
8. (Optional) `python manage.py seed_data` — loads sample profile, skills, and projects
9. `python manage.py runserver`
10. Open `http://localhost:8000`

## Admin Panel
Go to `http://localhost:8000/admin` to:
- Add your **Profile** (name, bio, photo, CV PDF, email, GitHub, LinkedIn, Instagram)
- Add **Skills** (name, category, emoji icon)
- Add **Projects** (title, description, tools, image, mark as featured)

## Features
- Light / Dark mode toggle (persisted in localStorage)
- Smooth scroll with 70px navbar offset
- Cross-page scroll: clicking Skills/Contact from /projects/ navigates home and scrolls
- Hamburger menu on mobile
- IntersectionObserver fade-in animations on scroll
- Active nav link highlighting via IntersectionObserver
- CV download via `/download-cv/`
- Fully responsive: desktop → tablet → mobile

## Project Structure
```
portfolio/
├── core/                        # Main Django app
│   ├── models.py                # Profile, Skill, Project
│   ├── views.py                 # home, projects, project_detail, download_cv
│   ├── urls.py
│   ├── admin.py
│   ├── templates/core/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── projects.html
│   │   └── project_detail.html
│   └── management/commands/
│       └── seed_data.py
├── static/
│   ├── css/style.css            # Full custom CSS design system
│   └── js/main.js               # All JS: theme, nav, scroll, animations
├── media/                       # Uploaded files (photos, CV, project images)
├── portfolio/
│   ├── settings.py
│   └── urls.py
├── .env
├── manage.py
└── requirements.txt
```
