# Booking Workflow Test Cases

| ID | Test | Expected outcome |
|---|---|---|
| BK-01 | Open a valid movie listing | Movie details and available shows are displayed |
| BK-02 | Select a valid show | Seat selection is associated with that show |
| BK-03 | Select an available seat | Seat is added to the booking summary |
| BK-04 | Submit without selecting a seat | Validation prevents an empty booking |
| BK-05 | Submit an invalid seat identifier | Server rejects the request safely |
| BK-06 | Attempt to book an already reserved seat | Booking is rejected and availability is refreshed |
| BK-07 | Refresh after successful booking | Confirmed booking remains recorded |
| BK-08 | Resubmit the same request | Duplicate booking is prevented or handled idempotently |

## Test notes
Run tests with a clean dataset and record the initial seat state. For concurrency scenarios, use two independent sessions and verify the final persisted booking records.

## Exit criteria
All critical validation, availability, and persistence scenarios should pass before a release.
