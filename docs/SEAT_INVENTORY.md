# Seat Inventory Invariants

A seat can be held or booked by at most one active booking for a given show. Expired holds must be released safely. Availability should be derived from authoritative database state, not from stale client-side seat maps.