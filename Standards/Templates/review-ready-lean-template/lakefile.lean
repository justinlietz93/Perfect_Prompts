import Lake

open System Lake DSL

package ReviewReadyTemplate where
  version := v!"0.1.0"
  description := "Reviewer-grade Lean 4 package template with audit, docs, CI, and closure scaffolding."
  keywords := #["lean4", "formalization", "audit-ready", "reviewer-grade"]
  homepage := "https://example.com/review-ready-template"
  license := "MIT"
  readmeFile := "README.md"
  reservoir := true
  testDriver := "ReviewReadyTemplateTest"
  lintDriver := "reviewerLint"
  leanOptions := #[
    ⟨`autoImplicit, false⟩,
    ⟨`relaxedAutoImplicit, false⟩,
    ⟨`linter.missingDocs, true⟩
  ]

@[default_target]
lean_lib ReviewReadyTemplate where
  globs := #[.submodules `ReviewReadyTemplate]

lean_lib ReviewReadyTemplateTest where
  globs := #[.submodules `ReviewReadyTemplateTest]

private def requiredReviewerFiles : Array FilePath := #[
  "README.md",
  "REVIEW.md",
  "CLAIMS.md",
  "ARTIFACT_MANIFEST.md",
  "CLOSURE_CERTIFICATE.md",
  "Audit/flagship-theorems.txt",
  "docs/TheoremIndex.md"
]

/--
Run lightweight repository hygiene checks used by `lake lint`.

Checks:
* no `sorry` or `admit` in tracked Lean files
* required reviewer-facing files exist
-/
script reviewerLint (_args) do
  let mut ok := true

  for path in requiredReviewerFiles do
    if !(← path.pathExists) then
      IO.eprintln s!"missing required reviewer file: {path}"
      ok := false

  let grep := ← IO.Process.output {
    cmd := "git"
    args := #[("grep" : String), "-n", "-E", "\\b(sorry|admit)\\b", "--", "*.lean"]
  }

  if grep.exitCode == 0 then
    IO.eprintln "forbidden placeholders found in Lean sources:"
    if !grep.stdout.isEmpty then
      IO.eprintln grep.stdout
    if !grep.stderr.isEmpty then
      IO.eprintln grep.stderr
    ok := false
  else if grep.exitCode != 1 then
    IO.eprintln "git grep failed while checking placeholders:"
    if !grep.stdout.isEmpty then
      IO.eprintln grep.stdout
    if !grep.stderr.isEmpty then
      IO.eprintln grep.stderr
    return grep.exitCode

  return if ok then 0 else 1
