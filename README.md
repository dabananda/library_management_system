# 📚 [Library Management System – API Design Documentation](https://library-management-system-zeta-ten.vercel.app/)

## Documentation

-    [Swagger](https://library-management-system-zeta-ten.vercel.app/swagger/)
-    [Redoc](https://library-management-system-zeta-ten.vercel.app/redoc/)

## 1. **Project Description**

The **Library Management System (LMS)** is a RESTful API designed to manage a library's collection of books, its members, and the borrowing process. The API allows CRUD operations for books and members, tracks borrowing records, and manages book availability in real-time.

### ✨ Functionalities:

-   Add, update, retrieve, and delete books
    
-   Manage authors and their books
    
-   Register and manage library members
    
-   Handle book borrowing and return processes
    
-   Maintain borrowing history for each member
    

----------

## 2. **Database Schema (Models Definition)**

### 📘 Book

-   **title** (string): Title of the book
    
-   **author** (ForeignKey to Author): Author of the book
    
-   **ISBN** (string): Unique identifier
    
-   **category** (string): Genre or category of the book
    
-   **availability_status** (boolean): True if available, False if borrowed
    

### ✍️ Author

-   **name** (string): Full name of the author
    
-   **biography** (text): Brief biography
    

### 🧑‍💼 Member

-   **name** (string): Member's full name
    
-   **email** (string): Contact email
    
-   **membership_date** (date): Date of registration
    

### 🔄 BorrowRecord

-   **book** (ForeignKey to Book): Borrowed book
    
-   **member** (ForeignKey to Member): Who borrowed the book
    
-   **borrow_date** (date): Date of borrowing
    
-   **return_date** (date or null): Date of return
    

----------

## 3. **API Endpoints Definition**

### 🔹 Books

-   `GET /books/` → List all books
    
-   `GET /books/{id}/` → Get details of a specific book
    
-   `POST /books/` → Add a new book
    
-   `PUT /books/{id}/` → Update details of a book
    
-   `DELETE /books/{id}/` → Remove a book
    

### 🔹 Authors

-   `GET /authors/` → List all authors
    
-   `POST /authors/` → Add a new author
    

### 🔹 Members

-   `GET /members/` → List all members
    
-   `POST /members/` → Register a new member
    
-   `PUT /members/{id}/` → Update member info
    
-   `DELETE /members/{id}/` → Remove a member
    

### 🔹 Borrowing

-   `POST /borrow/` → Member borrows a book
    
-   `POST /return/` → Member returns a book
    
-   `GET /borrow-records/` → View all borrow records
    

----------

## 4. **Request & Response Examples**

### ✅ POST `/books/`

#### Request:

```json
{
  "title": "The Pragmatic Programmer",
  "author": 2,
  "ISBN": "9780201616224",
  "category": "Software Engineering",
  "availability_status": true
}
```

#### Response:

```json
{
  "id": 1,
  "title": "The Pragmatic Programmer",
  "author": 2,
  "ISBN": "9780201616224",
  "category": "Software Engineering",
  "availability_status": true
}
```
