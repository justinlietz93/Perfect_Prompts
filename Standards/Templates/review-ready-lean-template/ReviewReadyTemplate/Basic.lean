/-
Copyright (c) 2026 ReviewReadyTemplate contributors. All rights reserved.
Released under MIT license as described in the file LICENSE.
Authors: ReviewReadyTemplate contributors
-/

import Std

/-!
# ReviewReadyTemplate.Basic

A minimal theorem-bearing module that demonstrates reviewer-grade structure.

## Main declarations

- `IsZero`
- `isZero_zero`
- `add_zero_right`
- `add_zero_left`

## Notes

Replace these sample declarations with your real mathematical content, but preserve the same
reviewer-facing discipline: module docs, declaration docs, stable theorem names, and a clear
claim-to-theorem mapping.
-/

namespace ReviewReadyTemplate

/-- A tiny sample predicate used to demonstrate declaration documentation. -/
def IsZero (n : Nat) : Prop := n = 0

/-- The canonical witness that `0` satisfies `IsZero`. -/
theorem isZero_zero : IsZero 0 := by
  rfl

/-- Right-addition by zero leaves a natural number unchanged. -/
theorem add_zero_right (n : Nat) : n + 0 = n := by
  simpa using Nat.add_zero n

/-- Left-addition by zero leaves a natural number unchanged. -/
theorem add_zero_left (n : Nat) : 0 + n = n := by
  simpa using Nat.zero_add n

end ReviewReadyTemplate
