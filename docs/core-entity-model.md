# Core Booking Entities

This note describes a suggested conceptual model for a movie ticket booking application. Adapt field names to the implementation already present in the repository.

## Movie
Represents a film shown by the application. Typical attributes include a unique identifier, title, duration, language, and release information.

## Show
Represents a scheduled screening of a movie. It references one movie and contains the screening date, start time, and screen identifier.

## Seat
Represents a physical seat within a screen. A seat identifier should be unique within its screen and have a stable row and seat number.

## Booking
Represents a customer's booking request for a particular show. It should retain a unique booking reference, customer reference, booking status, and creation timestamp.

## Booked seat
Associates a booking with one or more seats for the selected show. Enforce a uniqueness rule that prevents the same seat from being confirmed twice for one show.

## Relationship checks
- A movie can have multiple shows.
- A show belongs to one movie and one screen.
- A booking belongs to one customer and one show.
- A booking can contain multiple booked seats.
- Seat availability must be evaluated in the context of a show.

Use database constraints in addition to application-level checks to protect booking consistency.
