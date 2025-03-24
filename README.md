# BestBuy Scraper

A full-stack web application that scrapes product listings from BestBuy, stores them in a PostgreSQL database, and provides a React-based UI to browse and filter those products.

---

## Features

### Backend (Flask + PostgreSQL)
- Scrapes product data from BestBuy categories using BeautifulSoup
- Stores product and category data in a PostgreSQL database
- REST API endpoints:
  - `GET /data`: Paginated list of products
  - `GET /data/category/:category`: Products filtered by category
  - `DELETE /data/:id`: Delete a product by ID
- Test coverage using Pytest

### Database Schema
![Database Schema](./backend/assets/bestbuy_scraper_schema.png)


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

#### Configure .env
- Create a .env file in backend/:
```
DATABASE_URL=postgresql://username:password@localhost:5432/bestbuy_db
```
<i>NOTE: Please copy .env.example, rename the file and update database variables/ url with your credentials.</i>

#### Run Flask App
```
cd backend/api
flask run
```

## Frontend Setup
```
cd frontend
npm install
npm start
```
<i>NOTE: The app runs on http://localhost:3000 and connects to backend at http://localhost:5000.</i>

## Running Tests

#### Backend Tests (Pytest)
```
cd backend
pytest
```
<i>NOTE: Tests use a test database defined in .env.test and are cleaned up after each run. Please copy .env.test.example, rename the file and update database url with your credentials.</i>

#### Frontend Tests (Jest + React Testing Library)
```
cd frontend
npm test
```

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
- Web Scraping: BeautifulSoup, Requests

## Included Documents
- [Design Decisions.md](design-decisions.md) : Explains design choices and the time spent on each section.
- [Ai usage.md](ai_usage.md) : Includes AI tools used for development and list of prompts.