# Testing checklist

Use this checklist when manually validating the movie ticket booking application.

## Core flow
- [ ] Launch the application with the expected Python dependencies installed.
- [ ] Confirm the movie list loads and empty results are handled clearly.
- [ ] Select a movie and verify the available show information.
- [ ] Select seats and confirm the displayed seat count and price are consistent.
- [ ] Complete a booking and verify that the saved booking can be retrieved.
- [ ] Attempt to book an already-reserved seat and confirm the application rejects it.

## Input and persistence checks
- [ ] Try blank values and whitespace-only values in every required field.
- [ ] Try unusually long text and unexpected numeric values.
- [ ] Restart the application and verify persisted records remain available.
- [ ] Confirm database errors are surfaced without exposing SQL statements or credentials.

## Regression notes
Record the operating system, Python version, test data, expected result, and actual result for every failure. Use a temporary database for tests so manual checks do not modify personal booking data.
