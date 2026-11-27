# Architecture notes (mock)

orders depends on payments via contracts/payment_api.json.
contracts/* is a public contract consumed by the finance reporting service.
Any change to contracts/* requires a version bump and consumer sign-off.
