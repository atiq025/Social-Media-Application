# Social Media Application
## Project Overview
This is a basic social media application built using Django for the backend and HTML, CSS, and JavaScript for the frontend. The app includes fundamental features like user registration, authentication, post creation, and management. It serves as a demonstration of Django's core functionality and frontend integration.
Features
## Core Features
1. User Management:
    * User registration and login/logout functionality.
    * Authentication using Django's built-in authentication system.
    * Profile page for viewing user-specific posts.
2. Post Management:
    * Global feed displaying all user posts.
    * Profile-specific feed with options to edit or delete posts.
    * Create posts with optional image uploads.
3. Feedback and Notifications:
    * User feedback via Django's message framework (e.g., "Post created successfully").
## Additional Features
* User-specific access control to ensure only the owner can edit or delete posts.
* Template inheritance for consistent layouts.
* Secure pages using LoginRequiredMixin and login_required decorators.
## Technology Stack
* Backend: Django
* Frontend: HTML, CSS (with optional Bootstrap/Tailwind for styling), JavaScript
* Database: SQLite (default Django configuration)
* Version Control: Git (GitHub for repository hosting)
## Installation and Setup
## Prerequisites
1. Python 3.8+
2. pip (Python package manager)
3. Virtual environment setup (recommended)
## Installation Steps
1. Clone the repository:
```bash git clone 
cd social_app
``` 
2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Apply migrations to set up the database:
```bash
python manage.py migrate
``` 
5. Create a superuser for administrative access:
```bash
python manage.py createsuperuser
``` 
6. Start the development server:
```bash
python manage.py runserver
``` 

20. Open your browser and visit http://127.0.0.1:8000/.
## Usage
## Testing Credentials
Use the following credentials for testing:
* Superuser:
    * Username: admin
    * Password: admin
* Regular User Accounts:
    * Username: anika, Password: pass@123
    * Username: anisa, Password: pass@123
## Key Functionalities
1. Register a new user or log in using the provided credentials.
2. Create, edit, or delete posts from your profile page.
3. View all posts in the global feed (homepage).
## ER Diagram
Below is the ER diagram representing the application's database structure:
￼![ERD](https://github.com/user-attachments/assets/c215f7d2-3c92-40fd-a6e4-0c98d110f0f1)

## Description of the Entities:
1. User:
    * Fields: username, email, password
2. Post:
    * Fields: id, content, image, created_at, user (ForeignKey)
## Evaluation Criteria
1. Functionality: All features implemented as per the requirements.
2. Code Quality: Clean, well-organized, and follows Django best practices.
3. User Interface: Simple, responsive, and user-friendly design.
4. Documentation: Clear README and comprehensive project instructions.
## Future Enhancements
1. Add a "Like" feature for posts.
2. Implement user profile pictures.
3. Include a comments section for posts.
4. Enable post filtering or searching by keywords.
## Conclusion
This project demonstrates a basic social media application's core functionalities using Django. The application is scalable and serves as a foundation for more complex projects.
