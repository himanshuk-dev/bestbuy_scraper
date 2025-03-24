# Design Decisions & Development Summary

## Project Overview

This project is a full-stack application that scrapes product data from BestBuy, stores it in a database, and exposes it via a REST API. A React frontend consumes this API to display products with pagination and category-based filtering.

---

## Backend (Flask API)

### Framework: Flask  
Chosen for its simplicity, extensibility, and suitability for building lightweight REST APIs.

### ORM: SQLAlchemy  
Used for database modeling and query abstraction. Ensures better readability and maintainability of database interactions.

### Structure

```
backend/
├── api/
│   ├── __init__.py       # App factory + DB init
│   ├── models.py         # Product & Category models
│   ├── routes.py         # API route definitions
│   ├── db.py             # SQLAlchemy instance
│   ├── test_api.py       # Unit tests with pytest
│   ├── test_config.py    # Setup/teardown for test DB
```

### Design Decisions
- **Blueprints** used for clean modular routing.
- **Pagination** handled at the DB query level using `query.paginate`.
- **Testing** with `pytest`, including test database setup using `.env.test`.

### Time Spent on API development
| Task                       | Time Spent |
|----------------------------|------------|
| Flask API Setup            | 1 hour     |
| Models + DB Integration    | 1 hour     |
| API Routes + Pagination    | 1.5 hours  |
| Testing & Fixtures         | 1 hour     |

---

## Frontend (React.js with Material UI)

### Framework: Create React App  
Chose CRA for quick setup, along with functional components and React Hooks.

### Component Structure

```
frontend/
└── src/
    ├── api/
    │   └── apiClient.js
    ├── components/
    │   ├── ProductList.jsx
    │   └── Filter.jsx
    ├── pages/
    │   └── Home.jsx
    └── __tests__/
        └── ProductList.test.js
```

### Design Decisions
- **Material UI**: Provided accessible, modern UI components with minimal styling effort.
- **Category Filter**: Dynamically fetched from the API.
- **Pagination Controls**: Integrated with current page state.
- **Error Handling + Loading Indicators** for better UX.

### Time Spent on Frontend development
| Task                           | Time Spent |
|--------------------------------|------------|
| Frontend Setup (CRA + Routing)| 30 mins    |
| ProductList + Pagination       | 1.5 hours  |
| Category Filter (API Integrated)| 1 hour     |
| Styling with MUI               | 1 hour     |
| Testing (Jest + React Testing Lib)| 1 hour |

---

## Integration & Deployment

### Environment Config
Used `.env` and `.env.test` for switching between dev/test configs easily.

### CORS Handling
Configured Flask-CORS to allow frontend (port 3000) to access backend (port 5000).

---

## Summary

| Section                            | Task                         | Time Spent |
|------------------------------------|------------------------------|------------|
| **Web Scraper (Backend) - Selenium** | Scraper development           | 2 hours    |
|                                    | Data parsing & formatting     | 1 hour     |
| **Database Storage**               | Models + DB Integration       | 1 hour     |
|                                    | Seeding & schema setup        | 0.5 hour   |
| **Bonus: REST API**                | Flask API Setup               | 1 hour     |
|                                    | API Routes + Pagination       | 1.5 hours  |
|                                    | Testing & Fixtures            | 1 hour     |
| **Bonus: Frontend UI**             | React app + API integration   | 2 hours    |
|                                    | MUI design + pagination       | 1.5 hours  |
|                                    | Filtering + error handling    | 1 hour     |

**Total Time**: ~11.5–12 hours

---

## Final Thoughts

The modular design, emphasis on testing, and Material UI integration help ensure the project is scalable and developer-friendly. The codebase follows clean separation of concerns and should be easy to extend with additional features like:
- Search by keyword
- User authentication
- Product details page