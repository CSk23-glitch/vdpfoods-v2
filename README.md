# Videeptha Foods Website

This project is a full-stack e-commerce and content management web application for **Videeptha Foods**. It includes a modern, responsive frontend built with React and a robust backend built with Django and MongoDB.

## Project Structure

The repository is divided into two main directories:
- `Veediptha_Website-backend/`: The Django REST Framework backend.
- `website-frontend/`: The React frontend application.

---

## Backend Architecture

- **Framework:** Django / Django Rest Framework
- **Database:** MongoDB (using `django_mongodb_backend`)
- **Key Domains:**
  - **E-Commerce:** Products, Categories, Orders, Coupons, Inventory (Stock), Promotions.
  - **Content Management (CMS):** Dynamic Pages, Sections, Blocks, Stories, Heroes, Navigation, and Policies.
  - **Branding & Theming:** Website Branding, Typography, Global Themes, and Footer configurations.
  - **Customer Support:** Support Ticket system.
- **Includes:** Management scripts for data seeding (`seed_db_defaults.py`, `seed_stories.py`), migrations, and testing.

### Getting Started (Backend)

1. Navigate to the backend directory:
   ```bash
   cd Veediptha_Website-backend
   ```
2. Activate your virtual environment:
   ```bash
   source venv/bin/activate  # On macOS/Linux
   # or venv\Scripts\activate on Windows
   ```
3. Install dependencies (if not already installed):
   ```bash
   pip install -r requirements.txt
   ```
4. Run the development server:
   ```bash
   python manage.py runserver
   ```

---

## Frontend Architecture

- **Framework:** React 19 setup via Vite
- **Styling:** Tailwind CSS with Framer Motion for sophisticated UI animations
- **State Management & Routing:** React Router DOM (v7), React Query (`@tanstack/react-query`), and custom Contexts (Cart, Auth, Theme).
- **Authentication:** Google OAuth (`@react-oauth/google`)
- **Key Features & Pages:**
  - **E-Commerce:** Product catalog, Product details, Categories, and Checkout flows.
  - **Dynamic Content:** CMS-driven pages (`/page/:slug`), Stories, and Policies.
  - **User Management:** Login, Signup, and Account settings.
  - **Layout:** Includes global Cart Drawer, Mobile Bottom Navigation bar, and a WhatsApp floating button.

### Getting Started (Frontend)

1. Navigate to the frontend directory:
   ```bash
   cd website-frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```

---

## Database Setup
Ensure that you have a running MongoDB instance and that your environment variables inside `Veediptha_Website-backend/.env` are correctly pointing to it.
