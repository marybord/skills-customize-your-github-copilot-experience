# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a RESTful API using the FastAPI framework. Students will create endpoints that return JSON, accept request data, and validate input with Pydantic models.

## 📝 Tasks

### 🛠️ Create the API Structure

#### Description
Create the FastAPI application and add a root endpoint that returns a welcome message as JSON.

#### Requirements
Completed program should:

- Import `FastAPI` and create an app instance.
- Add a GET endpoint at `/`.
- Return a JSON response such as `{ "message": "Welcome to the FastAPI assignment!" }`.


### 🛠️ Build CRUD Endpoints

#### Description
Add endpoints to list items, retrieve a single item by ID, and create a new item.

#### Requirements
Completed program should:

- Add a GET endpoint at `/items/` that returns a list of items.
- Add a GET endpoint at `/items/{item_id}` that returns one item by its ID.
- Add a POST endpoint at `/items/` that accepts item data and returns the created item.


### 🛠️ Add Validation and Documentation

#### Description
Use Pydantic models to validate request bodies and support optional query parameters.

#### Requirements
Completed program should:

- Define a Pydantic model for item input with fields: `name`, `description`, `price`, and `in_stock`.
- Validate that `price` is a positive number.
- Support an optional query parameter such as `q` or `limit` for the `/items/` endpoint.
- Confirm the API is usable with automatic FastAPI docs at `/docs`.
