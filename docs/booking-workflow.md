# Ticket Booking Workflow

## Typical flow
1. The customer selects a movie and a show.
2. The application displays the seats available for that show.
3. The customer selects seats and reviews the booking summary.
4. The server validates that the selected seats are still available.
5. The booking is recorded only after the availability check succeeds.
6. The customer receives a confirmation containing the booking reference.

## Consistency requirements
- A seat must not be confirmed for two bookings for the same show.
- Availability must be checked on the server, not trusted from the browser.
- A failed booking must not leave seats marked as permanently reserved.
- Booking and payment states should be distinguishable if payment is part of the workflow.

## Edge cases to test
- Two customers attempt to book the same seat at nearly the same time.
- A customer refreshes or resubmits the booking form.
- A selected seat becomes unavailable before confirmation.
- A request contains an invalid show or seat identifier.

## User feedback
Show a clear confirmation on success and a useful explanation when the requested seats cannot be booked.
