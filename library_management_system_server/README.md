# Library Management System API

## Cloning Existing Project

1. Clone the repository:

   ```bash
   git clone https://github.com/dabananda/library_management_system_server.git
   cd library_management_system_server
   ```

2. Set up a virtual environment:

   ```bash
   # Create a virtual environment
   python -m venv .venv

   # Activate the virtual environment (Windows)
   venv\Scripts\activate

   # Activate the virtual environment (macOS/Linux)
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables (if needed):

   ```bash
   # Copy the example environment file
   copy .env.example .env  # Windows
   # cp .env.example .env  # macOS/Linux

   # Edit the environment file with your settings
   ```

5. Set up the database:

   ```bash
   # Run migrations
   python manage.py migrate

   # Create a superuser for the admin panel
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

   The site should now be available at http://127.0.0.1:8000/

7. Accessing the admin panel:

   After creating a superuser, you can access the admin panel at:
   http://127.0.0.1:8000/admin/

## Additional Commands

```bash
# Run tests
python manage.py test

# Create a new Django app
python manage.py startapp [app_name]

# Generate requirements.txt file
pip freeze > requirements.txt

# Install dependencies:
pip install -r requirements.txt
```

## Deactivating the Virtual Environment

When you're done working on the project:

```bash
deactivate
```

---

<div align="center">
<h1> Dabananda Mitra </h1>
</div>

<div align="center">
  <img src="https://res.cloudinary.com/djz3p8sux/image/upload/v1742125099/dabananda_mitra_formal_Small_1x1_o8uxit.png" width="250" height="250" style="border-radius: 50%">
</div>

<h3 align="center">Software Engineer | Problem Solver | Open Source Enthusiast</h3>

---

### 🌐 Connect with Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dabananda) [![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/dabananda) [![Twitter](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/dabanandamitra) [![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.om/imdmitra/) [![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/8801304080014) [![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discordapp.com/users/dabanandamitra)

---

### 💻 Online Judge Profiles

[![LeetCode](https://img.shields.io/badge/-LeetCode-FFA116?style=for-the-badge)](https://leetcode.com/u/dabananda/) [![Codeforces](https://img.shields.io/badge/-Codeforces-1F8ACB?style=for-the-badge)](https://codeforces.com/profile/dabananda) [![CodeChef](https://img.shields.io/badge/-CodeChef-5B4638?style=for-the-badge)](https://www.codechef.com/users/dabananda) [![HackerRank](https://img.shields.io/badge/-HackerRank-00EA64?style=for-the-badge)](https://www.hackerrank.com/profile/dabananda) [![CodingNinjas](https://img.shields.io/badge/-Coding_Ninjas-FFA500?style=for-the-badge)](https://www.naukri.com/code360/profile/48a35475-0af2-4d4e-8f26-2d793b64843a) [![UVa](https://img.shields.io/badge/-UVa-00B388?style=for-the-badge)](https://uhunt.onlinejudge.org/id/1167157) [![Beecrowd](https://img.shields.io/badge/-Beecrowd-009688?style=for-the-badge)](https://judge.beecrowd.com/en/profile/467832) [![Vjudge](https://img.shields.io/badge/-Vjudge-8A2BE2?style=for-the-badge)](https://vjudge.net/user/dabanandamitra)
