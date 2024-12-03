Here’s a comprehensive and well-structured `README.md` template for your anime recommendation system project:

```markdown
# Anime Recommendation System

A RESTful API that allows users to search for anime, set preferences based on their favorite genre, and get personalized anime recommendations based on those preferences.

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Running the Project](#running-the-project)
- [Endpoints](#endpoints)
  - [POST /preferences](#post-preferences)
  - [GET /search](#get-search)
  - [GET /recommendations](#get-recommendations)
- [Sample Requests and Responses](#sample-requests-and-responses)

## Project Overview

This project is designed to help users find anime recommendations based on their favorite genre. It leverages the AniList API to fetch anime data and provides personalized recommendations using a user’s preferences stored in a database. It uses Flask for the backend, SQLAlchemy for ORM, and JWT for authentication.

## Technologies Used

- **Backend**: Flask
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)
- **External API**: AniList GraphQL API
- **Containerization**: Docker
- **ORM**: SQLAlchemy

## Setup and Installation

To set up and run the project locally, follow these steps:

### Prerequisites

- Python 3.10 or higher
- PostgreSQL
- Docker (optional, for containerization)
- Virtualenv (optional, for creating a virtual environment)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/anime-recommendation-system.git
   cd anime-recommendation-system
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   - Make sure PostgreSQL is installed and running on your system.
   - Create a new database called `xtage` in PostgreSQL:
     ```sql
     CREATE DATABASE xtage;
     ```

5. **Configure environment variables**
   Create a `.env` file in the root directory and add the following variables:
   ```
   DATABASE_URI=postgresql://username:password@localhost/xtage
   SECRET_KEY=your-secret-key
   JWT_SECRET_KEY=your-jwt-secret-key
   ```

6. **Run database migrations** (if you're using migrations with SQLAlchemy)
   ```bash
   flask db upgrade
   ```

7. **Start the Flask development server**
   ```bash
   flask run
   ```

### Docker Setup (Optional)

If you prefer to run the application in a Docker container, follow these steps:

1. **Build the Docker image**
   ```bash
   docker-compose build
   ```

2. **Start the application with Docker**
   ```bash
   docker-compose up
   ```

This will start both the Flask application and the PostgreSQL database in Docker containers.

## Running the Project

Once the project is running, you can access the API via `http://localhost:5000`. Use Postman or any other API client to make requests to the available endpoints.

## Endpoints

### `POST /preferences`

Set or update the user’s preferences for the favorite anime genre. This endpoint requires JWT authentication.

**Request:**
- **Headers**: 
  - `Authorization: Bearer <jwt_token>`
- **Body** (JSON):
  ```json
  {
    "favorite_genre": "Action"
  }
  ```

**Response:**
- **Status Code**: 200 OK
- **Body** (JSON):
  ```json
  {
    "message": "Preferences updated successfully"
  }
  ```

### `GET /search`

Search for anime based on a name or genre. This endpoint does not require authentication.

**Request:**
- **Query Parameters**:
  - `name`: The name of the anime (optional)
  - `genre`: The genre of the anime (optional)

**Example:**
```
GET http://localhost:5000/search?name=Naruto
```

**Response:**
- **Status Code**: 200 OK
- **Body** (JSON):
  ```json
  {
    "data": {
      "Media": {
        "id": 1,
        "title": {
          "romaji": "Naruto",
          "english": "Naruto"
        },
        "genres": ["Action", "Adventure"]
      }
    }
  }
  ```

### `GET /recommendations`

Get personalized anime recommendations based on the user’s favorite genre. This endpoint requires JWT authentication.

**Request:**
- **Headers**: 
  - `Authorization: Bearer <jwt_token>`
- **Response** (Sample):
  ```json
  {
    "data": {
      "Page": {
        "media": [
          {
            "title": {
              "romaji": "Naruto",
              "english": "Naruto"
            }
          },
          {
            "title": {
              "romaji": "One Piece",
              "english": "One Piece"
            }
          }
        ]
      }
    }
  }
  ```

## Sample Requests and Responses

### Sample Request to Set Preferences
**Request:**
```http
POST /preferences HTTP/1.1
Host: localhost:5000
Authorization: Bearer <your-jwt-token>
Content-Type: application/json

{
  "favorite_genre": "Action"
}
```

**Response:**
```json
{
  "message": "Preferences updated successfully"
}
```

### Sample Request to Search Anime
**Request:**
```http
GET /search?name=Naruto HTTP/1.1
Host: localhost:5000
```

**Response:**
```json
{
  "data": {
    "Media": {
      "id": 1,
      "title": {
        "romaji": "Naruto",
        "english": "Naruto"
      },
      "genres": ["Action", "Adventure"]
    }
  }
}
```

### Sample Request to Get Recommendations
**Request:**
```http
GET /recommendations HTTP/1.1
Host: localhost:5000
Authorization: Bearer <your-jwt-token>
```

**Response:**
```json
{
  "data": {
    "Page": {
      "media": [
        {
          "title": {
            "romaji": "Naruto",
            "english": "Naruto"
          }
        },
        {
          "title": {
            "romaji": "One Piece",
            "english": "One Piece"
          }
        }
      ]
    }
  }
}
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

### Key Features of This README

- **Project Overview**: Provides a brief summary of the application and its core functionality.
- **Technologies Used**: Lists the main tools and technologies that the project uses.
- **Setup and Installation**: Detailed instructions to run the project locally, including setting up the virtual environment, installing dependencies, and configuring the database.
- **Docker Setup**: Instructions for running the project with Docker.
- **Endpoints**: Lists all available API endpoints with request and response formats.
- **Sample Requests and Responses**: Provides examples of how to interact with the API using Postman or other API tools.
