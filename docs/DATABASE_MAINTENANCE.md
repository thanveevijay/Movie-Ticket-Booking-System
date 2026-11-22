# SQLite database maintenance notes

These notes apply to local development and demonstration use of the SQLite database.

## Backups
- Stop writes or use SQLite's backup mechanism before copying a live database file.
- Store backups outside the repository and restrict access if they contain personal information.
- Test restoration periodically using a separate database path.
- Define a retention policy and remove obsolete backups securely.

## Integrity checks
Run SQLite's integrity check against a copy or during a maintenance window. Investigate failures before continuing to use the database.

## Schema changes
- Back up the database before applying schema changes.
- Prefer explicit, versioned migrations over ad hoc manual edits.
- Test migrations against a copy of representative data.
- Keep application code compatible with the schema version it expects.

## Data handling
Use synthetic records in screenshots, tests, and demonstrations. Avoid committing database files containing real user or booking information.
