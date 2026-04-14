# GAP Template — General Software / Business Logic

Use this template when the constraints are design patterns, business logic, API
contracts, architectural boundaries, or system requirements. The vocabulary should
name specific, widely-recognized patterns to maximize attention anchoring.

---

## Template

```
I was thinking about why we keep running into issues with **[Current Bug/Feature]**,
and I want to get your thoughts on the architecture here.

Based on our rules for **[Insert Core Architecture/Design Pattern/Business Logic]**,
we know that **[State the hard technical or logical constraint]**.

If that is the case, wouldn't it make sense that **[The specific problematic
variable/function/component]** is actually a representation of **[Domain A]**,
while our standard baseline represents **[Domain B]**?

If you agree with this theoretical split, how should we architect the codebase
to ensure these two systems are processed independently, so we don't accidentally
violate **[Core Architecture Rule]**?
```

---

## Slot Definitions

| Slot | What goes here | Good example | Bad example |
|------|---------------|--------------|-------------|
| **Current Bug/Feature** | The specific symptom or friction | "the checkout flow drops cart state after redirect" | "it doesn't work" |
| **Core Architecture Rule** | Named pattern or principle | "Flux unidirectional data flow" | "our architecture" |
| **Hard constraint** | The specific rule being violated | "Components must not directly mutate global store" | "things should be clean" |
| **Problematic element** | The specific component/function | "`CartSummary.handleCheckout()` in `cart/index.tsx`" | "the cart page" |
| **Domain A / Domain B** | The two sides of the separation | "side-effect logic / pure render logic" | "frontend / backend" |

---

## Worked Examples

### Example 1: State Management Bug

```
I was thinking about why the cart keeps resetting after a successful payment
redirect, and I want to get your thoughts on the architecture here.

Based on our Flux/Redux architecture, we know that component state should
flow unidirectionally: actions → reducer → store → view. No component should
directly mutate the store or hold state that the store should own.

If that's the case, wouldn't it make sense that `CartSummary.handleCheckout()`
is violating this boundary by holding the cart items in local component state
instead of the Redux store, so when the redirect unmounts the component,
the state evaporates?

If you agree with this analysis, how should we architect the checkout flow
so that all cart state lives exclusively in the Redux store, and
`CartSummary` is a pure rendering component with no local state that could
conflict with the store?
```

### Example 2: Microservice Boundary Violation

```
I was looking at why the order service keeps timing out under load, and I
want to get your thoughts on the service architecture here.

Based on our microservice contract, the order service must be stateless —
every request should be self-contained, with all state persisted in the
database layer. No in-memory caches that could drift between instances.

If that's the case, wouldn't it make sense that the `orderCache` HashMap
in `OrderService.java` is actually creating a stateful bottleneck? Under
load, every instance builds its own divergent cache, and the cache
invalidation logic is serializing requests through a mutex.

If you agree that this cache violates the stateless contract, how should
we architect the caching layer so it's externalized (Redis, CDN, etc.)
and the order service itself remains truly stateless?
```

### Example 3: API Contract Mismatch

```
I was thinking about why the mobile client keeps showing stale data after
updates, and I want to get your thoughts on the API architecture.

Based on our REST API contract, we defined that `PUT /resources/:id` must
return the full updated resource in the response body — the client should
never need a follow-up `GET` to see its own changes.

If that's the case, wouldn't it make sense that the staleness bug is because
`updateResource()` in the API handler is returning a `204 No Content`
instead of `200` with the updated body? The mobile client is left holding
its stale local copy.

If you agree this is a contract violation, how should we architect the
response pipeline so that every mutating endpoint automatically returns
the full resource state, and we have a test that enforces this contract
across all resource handlers?
```

---

## Domain-Specific Tips

- **Name the pattern, not the preference.** "Flux unidirectional data flow" is
  a named pattern with well-defined rules. "Clean architecture" is vaguer.
  The more specific the name, the stronger the anchor.
- **Reference your own docs.** "Per our API spec v2.3, Section 4.1" is more
  powerful than "based on how we usually do things."
- **State violations as deductions, not accusations.** "Wouldn't it make sense
  that X is violating Y" is more effective than "X is violating Y." The
  question form activates the agent's analytical mode.
- **Keep the architectural question genuinely open.** If you already know exactly
  what code change you want, GAP isn't the right tool — just tell the agent.
  GAP works when you know the *constraints* but want the agent to find the
  *architecture*.
