# Instantiation Guide

## 1. Start from the capability, not from the folder tree

Write one sentence answering: **what reusable job does this skill perform?**

If the answer is actually a persona, methodology, ruleset, one-off project procedure, or prompt template, stop and classify the artifact correctly before building a skill.

## 2. Define activation boundaries

Write concrete `use_when` and `do_not_use_when` conditions. The narrowest valid skill should win during routing.

## 3. Design the minimum package

Keep only support layers that are genuinely load-bearing:

- references when the procedure depends on durable explanatory material;
- schemas when machine-readable structure matters;
- scripts when repeatable execution or validation should be executable;
- assets when visual/media resources are required;
- runtime bindings when the environment needs metadata;
- tests when failure modes can be meaningfully exercised.

Delete unused directories.

## 4. Write the procedure

The procedure is skill-specific. Do not copy another skill's stages just because they exist.

## 5. Define outputs and completion

Name what gets produced and how success is verified.

## 6. Validate

Run:

```bash
python tools/validate_skill.py .
```

Then test at least:

- one representative successful invocation;
- one out-of-scope invocation;
- one missing-input or dependency failure if applicable.

## 7. Promote deliberately

Remain `DRAFT` until boundaries and behavior have been exercised. Use `CANDIDATE` for reviewable reusable skills and `CANONICAL` only after adoption.
