# Booking data invariants

These invariants help prevent inconsistent booking records as the application evolves.

## Seat allocation
- A seat must not be confirmed for two bookings for the same show.
- Seat identifiers must belong to the selected show or screen.
- The final price must be calculated from trusted server-side data, not accepted directly from the client.
- A booking should not be marked confirmed until the seat allocation is committed successfully.

## Booking lifecycle
- Use explicit booking states such as pending, confirmed, and cancelled.
- A cancellation must release seats only when the cancellation is valid.
- Repeated submission should not create duplicate bookings when the same request is retried.
- Store timestamps consistently and document the timezone used for display.

## Database consistency
- Use transactions for operations that update multiple related records.
- Add appropriate uniqueness constraints for show-seat allocation.
- Handle database errors without leaving partial booking state.
- Test simultaneous booking attempts for the same seat using separate sessions.

These are design expectations; verify which constraints are currently implemented before describing them as existing application behavior.
