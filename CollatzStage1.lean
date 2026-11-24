import Init.Omega

namespace DotProofs

def collatz (n : Nat) : Nat :=
  if n % 2 = 0 then n / 2 else 3 * n + 1

def orbit (k n : Nat) : Nat :=
  match k with
  | 0 => n
  | k + 1 => orbit k (collatz n)

def CollatzClaim : Prop :=
  ∀ n : Nat, 0 < n → ∃ k : Nat, orbit k n = 1

theorem oddOneModFourDescent (q : Nat) (hq : 0 < q) :
    orbit 3 (4 * q + 1) = 3 * q + 1 ∧ orbit 3 (4 * q + 1) < 4 * q + 1 := by
  have h₁ : (4 * q + 1) % 2 ≠ 0 := by omega
  have h₂ : 3 * (4 * q + 1) + 1 = 12 * q + 4 := by omega
  have h₃ : (12 * q + 4) % 2 = 0 := by omega
  have h₄ : (12 * q + 4) / 2 = 6 * q + 2 := by omega
  have h₅ : (6 * q + 2) % 2 = 0 := by omega
  have h₆ : (6 * q + 2) / 2 = 3 * q + 1 := by omega
  have h₇ : orbit 3 (4 * q + 1) = 3 * q + 1 := by
    simp only [orbit, collatz, h₁, if_false, h₂, h₃, if_true, h₄, h₅, h₆]
  exact ⟨h₇, by rw [h₇]; omega⟩

theorem twentyStepDescentFails :
    ∀ k : Nat, k ≤ 20 → 27 ≤ orbit k 27 := by
  intro k hk
  have casesK :
      k = 0 ∨ k = 1 ∨ k = 2 ∨ k = 3 ∨ k = 4 ∨ k = 5 ∨
      k = 6 ∨ k = 7 ∨ k = 8 ∨ k = 9 ∨ k = 10 ∨ k = 11 ∨
      k = 12 ∨ k = 13 ∨ k = 14 ∨ k = 15 ∨ k = 16 ∨ k = 17 ∨
      k = 18 ∨ k = 19 ∨ k = 20 := by omega
  rcases casesK with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl |
    rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;> decide

#print axioms oddOneModFourDescent
#print axioms twentyStepDescentFails

end DotProofs
