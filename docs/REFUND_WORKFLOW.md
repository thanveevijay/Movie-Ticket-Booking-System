# Refund Workflow

Track refund requests separately from booking cancellation. Store provider reference, amount, currency, request time, completion time, and status. Process callbacks idempotently and reconcile pending refunds with the payment provider. Do not mark a refund complete solely because the user closed the payment page.