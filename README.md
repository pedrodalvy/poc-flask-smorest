# POC Flask-Smorest

A proof of concept (POC) developed to demonstrate the implementation of the **Flask-Smorest** library in a simple project. The goal is to explore and illustrate how to use this library to create structured RESTful APIs with OpenAPI documentation support.

## 🚀 Main Objectives

- Demonstrate the use of the Flask-Smorest library.
- Implement a simple and organized project illustrating best practices.
- Automatically generate and document the project's OpenAPI specification.

---

## 📁 Project Structure

```plaintext
.
├── openapi.json             # File where Swagger data is generated.
├── poetry.lock
├── pyproject.toml
├── README.md
└── src
    ├── app.py               # Main application file where routes are registered.
    ├── entities
    │   ├── author.py
    │   └── post.py
    ├── repositories
    │   ├── authors_repository.py
    │   └── posts_repository.py
    ├── routes               # API routes and views.
    │   ├── authors.py        # Author-related routes.
    │   ├── posts.py          # Post-related routes.
    │   └── dto               # Swagger DTOs for each endpoint.
    │       ├── authors
    │       │   ├── create_author_dto.py
    │       │   ├── delete_author_dto.py
    │       │   ├── get_author_dto.py
    │       │   ├── list_authors_dto.py
    │       │   └── update_author_dto.py
    │       └── posts
    │           ├── create_post_dto.py
    │           └── list_posts_dto.py
    └── services
        ├── authors_service.py
        └── posts_service.py
```

### Notes:

- All DTOs inside the `dto` folder define the data models used by Swagger for each endpoint.
- Each route file inside the `routes` folder must be registered in `app.py` to take effect.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.13 or higher.
- Poetry installed for dependency management.

### Steps to run the application

1. Clone the repository:

   ```bash
   git clone git@github.com:pedrodalvy/poc-flask-smorest.git
   cd poc-flask-smorest
   ```

2. Install dependencies:

   ```bash
   poetry install
   ```

3. Start the application:

    - Normal mode:
      ```bash
      poetry run start
      ```

    - Debug mode:
      ```bash
      DEBUG=true poetry run start
      ```

4. Generate the OpenAPI documentation (optional):

   ```bash
   poetry run flask --app src/app.py openapi write --format=json openapi.json
   ```

---

## 🔍 Example Usage

### Available Endpoints

| Method | Endpoint      | Description                |
|--------|---------------|----------------------------|
| GET    | /authors      | List all authors.          |
| POST   | /authors      | Create a new author.       |
| GET    | /authors/{id} | Get author details.        |
| PUT    | /authors/{id} | Update an existing author. |
| DELETE | /authors/{id} | Delete an author.          |
| GET    | /posts        | List all posts.            |
| POST   | /posts        | Create a new post.         |

### Example using cURL

<details>
  <summary>List all authors</summary>

  ```bash
  curl --request GET \
    --url http://localhost:5000/authors
  ```
</details>

<details>
  <summary>Create an author</summary>

  ```bash
  curl --request POST \
    --url http://localhost:5000/authors \
    --header 'content-type: application/json' \
    --data '{
      "name": "John Doe"
    }'
  ```
</details>

<details>
  <summary>Get author details</summary>

  ```bash
  curl --request GET \
    --url http://localhost:5000/authors/{id}
  ```
</details>

<details>
  <summary>Update an author</summary>

  ```bash
  curl --request PUT \
    --url http://localhost:5000/authors/{id} \
    --header 'content-type: application/json' \
    --data '{
      "name": "Jane Doe"
    }'
  ```
</details>

<details>
  <summary>Delete an author</summary>

  ```bash
  curl --request DELETE \
    --url http://localhost:5000/authors/{id}
  ```
</details>

<details>
  <summary>List all posts</summary>

  ```bash
  curl --request GET \
    --url 'http://localhost:5000/posts?author_id={author_id}'
  ```
</details>

<details>
  <summary>Create a post</summary>

  ```bash
  curl --request POST \
    --url http://localhost:5000/posts \
    --header 'content-type: application/json' \
    --data '{
      "title": "My first post",
      "content": "This is my first post",
      "author_id": 1
    }'
  ```
</details>

---

## 🛠️ Additional Notes

- **Flask-Smorest**: A library for building RESTful APIs in Flask, with support for data validation, OpenAPI documentation, and automatic documentation generation.
- **Future expansions**: The project can be extended with automated tests, database integration, and authentication.
- **Debugging**: Use the `DEBUG=true` environment variable to facilitate development and debugging.

---
