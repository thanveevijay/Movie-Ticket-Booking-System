# Booking transaction test scenarios

Use an isolated database to test consistency when booking operations fail or overlap.

## Scenarios
1. A normal booking creates one booking record and reserves the selected seats.
2. An attempt to reserve an already-booked seat is rejected.
3. A failure after creating a booking but before reserving seats rolls back all related changes.
4. Two sessions attempt to reserve the same seat; at most one succeeds.
5. A repeated request does not create duplicate confirmed bookings.
6. A valid cancellation changes booking state and releases the correct seats.
7. An invalid cancellation leaves the original booking and seat allocation unchanged.

## Assertions
- No seat is assigned to more than one confirmed booking for a show.
- Related writes either all succeed or all roll back.
- Error responses do not expose raw SQL or local database paths.
- Tests clean up their records and do not alter user data.

Document the database engine and concurrency assumptions used by the test environment.
