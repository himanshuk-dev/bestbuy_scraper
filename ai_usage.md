
# AI Usage Documentation

## Overview
While developing this project, I used AI tools like ChatGPT primarily as a debugging assistant and to accelerate minor development tasks. I intentionally avoided using AI for core logic or full code generation, ensuring that the project reflects my skills and problem-solving abilities.

---

## Where AI Was Used

### 1. Debugging & Error Fixes
- **Example**: Encountered a `NameError: name 'current_app' is not defined` while writing Flask route tests.
- **Prompt**:  
  ```
  I am getting `NameError: name 'current_app' is not defined` when testing a DELETE API in Flask.
  ```
- **Decision**: Instead of importing `current_app`, I refactored the test structure and ensured context usage was correct. ChatGPT helped me locate the actual mistake.

### 2. CORS Error Resolution
- **Prompt**:  
  ```
  My React frontend at localhost:3000 is being blocked by CORS when trying to call my Flask API at localhost:5000. What should I do?
  ```
- **Decision**: I manually added Flask-CORS to allow cross-origin requests during development.

### 3. UI Styling Suggestions
- **Prompt**:  
  ```
  Suggest Material UI layout to display paginated product data and category filter.
  ```
- **Decision**: While I used the suggestions, I restructured and customized the layout based on my preferences and design vision.

### 4. Markdown & Documentation
- I used AI to assist in structuring markdown documents (like the README, PR doc, and this AI Usage file) for clarity and professionalism.

---

## Where AI Was Not Used

- Writing the **Selenium scraper logic**
- Structuring the **database schema**
- Implementing **Flask API routes**
- Designing the **React component logic**
- Writing and maintaining **unit tests**
- Handling **pagination**, **filtering**, and **deployment flow**

---

## Why AI Was Used This Way
As a developer, I believe in leveraging tools like AI for:
- **Time-saving** on repetitive research or known error resolution
- **Learning faster** without relying solely on Stack Overflow or documentation
- **Reducing friction** while still owning the core code and architecture

I consciously avoided letting AI generate large code blocks to ensure the work remains original, maintainable, and showcases my strengths as a full-stack developer.

---

## Final Thoughts
This approach allowed me to maintain high code quality while being efficient.
