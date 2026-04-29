import datetime
from django.core.management.base import BaseCommand
from core.models import Profile, Skill, Project


class Command(BaseCommand):
    help = 'Seed the database with sample profile, skills, and projects.'

    def handle(self, *args, **kwargs):
        Profile.objects.all().delete()
        Skill.objects.all().delete()
        Project.objects.all().delete()

        Profile.objects.create(
            name="Rabin Dhakal",
            title="Aspiring Data Analyst | Python & SQL",
            bio="A data enthusiast and final-year student who loves turning raw data into meaningful insights. I build dashboards, write SQL queries in my sleep, and believe every dataset has a story worth telling.",
            email="rabindhakal00000@gmail.com",
            github_url="https://github.com/rabindhakal404",
            linkedin_url="https://linkedin.com/in/rabindhakal404",
            instagram_url="https://instagram.com/rawbeen10",
        )
        self.stdout.write(self.style.SUCCESS('[OK] Profile created'))

        skills_data = [
            ("Python",         "Programming",   "\U0001f40d"),
            ("Pandas & NumPy", "Programming",   "\U0001f522"),
            ("SQL",            "Database",      "\U0001f5c4\ufe0f"),
            ("Excel",          "Tools",         "\U0001f4ca"),
            ("Power BI",       "Visualization", "\U0001f4c8"),
            ("Tableau",        "Visualization", "\U0001f3a8"),
        ]
        for name, category, emoji in skills_data:
            Skill.objects.create(name=name, category=category, icon_emoji=emoji)
        self.stdout.write(self.style.SUCCESS(f'[OK] {len(skills_data)} skills created'))

        Project.objects.create(
            title="Sales Dashboard Analysis",
            short_description="Analyzed 2 years of retail sales data to uncover trends and built an interactive Power BI dashboard.",
            long_description=(
                "This project involved collecting, cleaning, and analyzing 2 years of retail sales data using Python and Pandas. "
                "I identified seasonal trends, top-performing product categories, and regional sales patterns. "
                "The final deliverable was an interactive Power BI dashboard presenting key KPIs to stakeholders."
            ),
            tools_used="Python, Pandas, Matplotlib, Power BI, Excel",
            featured=True,
            date=datetime.date(2024, 3, 1),
        )

        Project.objects.create(
            title="Customer Churn Prediction",
            short_description="Built a machine learning model to predict customer churn for a telecom dataset with 82% accuracy.",
            long_description=(
                "Used a telecom customer dataset to build a churn prediction model. "
                "After extensive EDA using Seaborn and Matplotlib, I engineered features and trained a Random Forest classifier using Scikit-learn. "
                "The model achieved 82% accuracy and helped identify the top factors driving customer churn, "
                "presented in a Jupyter Notebook report."
            ),
            tools_used="Python, Scikit-learn, Pandas, Seaborn, Jupyter Notebook",
            featured=True,
            date=datetime.date(2024, 6, 15),
        )
        self.stdout.write(self.style.SUCCESS('[OK] 2 projects created'))
        self.stdout.write(self.style.SUCCESS('Seed complete! Run: python manage.py runserver'))
