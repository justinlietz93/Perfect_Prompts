/-
Copyright (c) 2026 ReviewReadyTemplate contributors. All rights reserved.
Released under MIT license as described in the file LICENSE.
Authors: ReviewReadyTemplate contributors
-/

import ReviewReadyTemplate

/-!
# ReviewReadyTemplateTest.Smoke

Smoke tests that mirror the public source tree.
-/

open ReviewReadyTemplate

example : IsZero 0 :=
  isZero_zero

example (n : Nat) : n + 0 = n :=
  add_zero_right n

example (n : Nat) : 0 + n = n :=
  add_zero_left n
