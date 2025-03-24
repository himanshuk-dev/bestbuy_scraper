# BestBuy Scraper

A full-stack web application that scrapes product listings from BestBuy, stores them in a PostgreSQL database, and provides a React-based UI to browse and filter those products.

##### BestBuy Scraper preview:
![bestbuy_scraper](https://github.com/user-attachments/assets/274f665e-5735-40a9-bfcc-7cdcb5db4043)

##### BestBuy Scraper Frontend preview:
<img width="1709" alt="bestbuy_scraper_frontend" src="https://github.com/user-attachments/assets/c2cfa250-5628-44ee-90c8-e8c82399d6cf" />

---

## Features

### Backend (Flask + PostgreSQL)
- Scrapes product data from BestBuy categories using Selenium
- Stores product and category data in a PostgreSQL database
- REST API endpoints:
  - `GET /data`: Paginated list of products
  - `GET /data/category/:category`: Products filtered by category
  - `DELETE /data/:id`: Delete a product by ID
- Test coverage using Pytest

### Database Schema
![bestbuy_scraper_schema](https://github.com/user-attachments/assets/682f6ba1-fc03-4470-99e6-2f0e67b932cc)

### Frontend (React + Material UI)
- Category filter dropdown
- Paginated product listing in a responsive table
- Elegant UI built using Material UI components
- Displays loading states and error messages

---

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- PostgreSQL
- (Optional) `virtualenv` or `venv` for Python

---

## Backend Setup

```
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Configure .env
- Create a `.env` file in `backend/`:
```env
DB_NAME=bestbuy_db
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

DATABASE_URL=postgresql://username:password@localhost:5432/bestbuy_db
```
*NOTE: Please copy `.env.example`, rename the file and update database credentials accordingly.*

---

## Running the Scraper

The scraper extracts product and category data from BestBuy.ca and stores it in your configured PostgreSQL database.

### 1. Ensure your database is configured in `.env`
Make sure your `.env` file inside the `backend/` directory is correctly set up with valid credentials.

### 2. Run the Scraper Script

From the root of the backend folder:

```
cd backend
source venv/bin/activate
python scraper.py
```

This will:
- Create the database (if it doesn’t exist)
- Create the necessary tables
- Scrape categories and product data from BestBuy.ca
- Insert the data into the database

The scraper uses `Selenium` and `webdriver-manager` to automate Chrome in headless mode.

---

### Run Flask App
```
cd backend/api
flask run
```
---

## Frontend Setup

```
cd frontend
npm install
npm start
```
*NOTE: The app runs on http://localhost:3000 and connects to backend at http://localhost:5000.*

---

## Running Tests

### Backend Tests (Pytest)
```
cd backend
pytest
```
*NOTE: Tests use a test database defined in `.env.test` and are cleaned up after each run. Please copy `.env.test.example`, rename the file and update database url with your credentials.*

### Frontend Tests (Jest + React Testing Library)
```
cd frontend
npm test
```

---

## Project Structure
```
bestbuy_scraper/
├── backend/
│   ├── api/
│   │   ├── app.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   ├── db.py
│   │   ├── test_api.py
│   ├── scraper.py
├── frontend/
│   ├── src/
│   │   ├── api/apiClient.js
│   │   ├── components/
│   │   │   ├── Filter.jsx
│   │   │   ├── ProductList.jsx
│   │   ├── pages/Home.jsx
│   │   ├── __tests__/
│   │   │   ├── ProductList.test.js
```

## Built With
- Backend: Flask, SQLAlchemy, PostgreSQL, Pytest
- Frontend: React, Material UI, Axios, React Testing Library
- Web Scraping: Selenium, WebDriverManager

## Included Documents
- [Design Decisions.md](design-decisions.md) : Explains design choices and the time spent on each section.
- [Ai usage.md](ai_usage.md) : Includes AI tools used for development and list of prompts.