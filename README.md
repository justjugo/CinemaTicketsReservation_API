# Django REST Framework Tutorial: Movie Ticket Reservation API

This project serves as a comprehensive tutorial on using Django REST Framework (DRF) to build a **movie ticket reservation API**. It covers various types of views and provides practical examples of building RESTful APIs.

## Project Overview

The project demonstrates the following core concepts of DRF:

- **Models**: Representation of the core entities involved in the ticket reservation process, including movies, guests, and reservations.
- **Views**: Implementation of different view types in DRF such as Function-Based Views (FBVs), Class-Based Views (CBVs), Mixins, Generics, and ViewSets.
- **Authentication**: Use of token-based authentication to secure API endpoints.
- **CRUD Operations**: Creating, retrieving, updating, and deleting records for Movies, Guests, and Reservations.

## Models

### Movie
Represents movie screenings with the following fields:
- `hall`: The hall where the movie is screened.
- `movie`: The name of the movie.
- `date`: The date of the screening.
- `time`: The time of the screening.

### Guest
Represents guests booking the tickets with these fields:
- `name`: The name of the guest.
- `mobile`: The guest's mobile number.

### Reservation
Links a guest to a movie reservation with the following relationships:
- `guest`: A foreign key to the Guest model.
- `movie`: A foreign key to the Movie model.

## Features

- **Various View Types**: The API showcases multiple view types for handling requests, including:
  - Function-Based Views (FBV)
  - Class-Based Views (CBV)
  - Mixins
  - Generic Views
  - ViewSets with routers

- **Token Authentication**: The project implements token authentication to ensure secure access to the API endpoints.

- **CRUD Operations**: Endpoints for managing Movies, Guests, and Reservations using different view types.
