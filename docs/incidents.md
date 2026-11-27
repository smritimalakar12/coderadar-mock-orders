# Incident history (mock)

INC-1042 (2026-08-14) payments: retry loop without backoff hammered the DB, 47 min outage.
Hotfix: added exponential backoff. Module owner: payments team.

INC-1101 (2026-09-30) orders: CSV export broke after an upstream field change.
