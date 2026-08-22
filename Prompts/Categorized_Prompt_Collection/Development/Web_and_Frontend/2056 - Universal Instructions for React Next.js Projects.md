# Universal Instructions for React / Next.js Projects

> Purpose: General rules for developing various projects with React + TypeScript, Next.js + TypeScript, and Tailwind CSS.
> Usage: Place this file in the root of a new project as `AGENTS.md`, `CLAUDE.md`, or `PROJECT_RULES.md`, or use it as a base instruction set for an AI agent.
> Important: These instructions do not contain product-specific rules. Keep everything related to an individual project in a separate `PROJECT_RULES.md` file.

---

# 1. Core Principle

Build a production-ready application, not a collection of disconnected components.

Always follow this sequence:

1. Review the current project structure, `package.json`, routing, UI primitives, stores, hooks, schemas, and project rules.
2. Find existing actions, helpers, schemas, and components that can be reused.
3. Identify the smallest change required for the task.
4. Preserve existing behavior.
5. Implement each new feature end to end: model, validation, UI, storage/import/export, edge cases, and verification.
6. Run the relevant checks and report the results honestly.

Do not add dependencies, abstractions, a global store, or an architectural layer unless they are genuinely necessary.
Use `shadcn/ui` by default for UI work. Do not add another UI kit on top of it without a clear reason.

---

# 2. Choosing Between React and Next.js

Use Next.js when the project needs:

- routing;
- SEO;
- SSR / Server Components;
- Server Actions;
- Route Handlers / API routes;
- authentication;
- database access;
- private environment variables;
- content publishing.

Use React + Vite when:

- the application is entirely client-side;
- SEO is not required;
- it is a local tool, dashboard, editor, admin panel, or desktop-like UI;
- the server already exists as a separate service.

Do not choose Next.js simply because it is popular. Do not add Redux, Zustand, React Query, a form library, or another UI kit without a specific reason.

---

# 3. Default Stack and Checks

Use the following by default:

- React;
- TypeScript in strict mode;
- Tailwind CSS;
- `shadcn/ui` as the required UI approach for clean design and rapid interface development;
- Lucide React or the icon library used by the current shadcn configuration;
- ESLint;
- a shared `cn()` helper;
- runtime validation for external data;
- accessible HTML elements.

Use `shadcn/ui` as the primary source of UI primitives: buttons, inputs, selects, dialogs, sheets, dropdowns, tooltips, tabs, carousels, cards, badges, skeletons, scroll areas, and other required components. Create custom primitives only when shadcn does not provide a suitable component or when the project already has a stable local primitive.

For an MVP, begin with mock/JSON/localStorage data and validate local user flows first. Add the backend, database, payments, authentication, and external integrations last, once the UI, models, and flows are clear.

At a minimum, run these commands after code changes:

```bash
npm run typecheck
npm run lint
npm run build
```

Do not claim that the project works if these commands were not run or completed with errors.

---

# 4. Architecture

For Next.js projects expected to grow, keep source code inside `src/` by default: `src/app`, `src/components`, `src/lib`, `src/data`, `src/hooks`, and `src/features`. Keep root-level support folders and files (`public`, configuration files, lockfiles, and README) in the project root.

For small projects, the following structure is acceptable:

```text
src/
  app/ or pages/
  components/
  features/
  lib/
  shared/
```

For medium and large projects, use an FSD-like approach:

```text
src/
  app/       # bootstrap, providers, layouts, routes
  views/     # page-level composition
  widgets/   # large UI blocks
  features/  # user workflows
  entities/  # domain model
  shared/    # generic helpers, config, thin wrappers around shadcn/ui
```

Import direction:

```text
app/views -> widgets -> features -> entities -> shared
```

Do not:

- import `widgets` into `features`;
- place business logic in `shared`;
- turn `shared/lib` into a dumping ground for unrelated functions;
- duplicate mutation logic across multiple UI components;
- use deep imports into another module's internals when that module exposes a public API.

---

# 5. Public API

Every feature, entity, or shared UI folder should expose a clear public API through `index.ts` when the module is used externally. For shadcn primitives, the public API usually already lives in `components/ui/*` or the project's local UI layer.

Good:

```ts
import { createTask } from "@/features/create-task";
```

Bad:

```ts
import { createTask } from "@/features/create-task/model/createTask";
```

Exception: internal code within the same feature or entity.

---

# 6. TypeScript

Required:

- enable `strict: true`;
- do not use `any` except in isolated interoperability code;
- do not hide type errors with `as` assertions;
- use discriminated unions for complex state;
- validate runtime JSON with a schema;
- do not create multiple identical types without a meaningful reason.

Example state type:

```ts
type LoadState<T> =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: T }
  | { status: "error"; message: string };
```

---

# 7. React State and Effects

Store state where it actually belongs:

| State type   | Where to store it                                           |
| ------------ | ----------------------------------------------------------- |
| Local UI     | `useState`, `useReducer`                                    |
| URL state    | route/search parameters                                     |
| Server state | server rendering or a cache/query layer                     |
| Form state   | form hook/library                                           |
| Global UI    | a small store when necessary                                |
| Domain state | entity/store when the state is shared across multiple flows |

Do not put the following in a global store:

- hover state;
- the state of a single dropdown;
- the draft value of a single input;
- the state of a single modal;
- the temporary selected tab of one component.

Use `useEffect` to synchronize with external systems:

- browser APIs;
- timers;
- subscriptions;
- external stores;
- DOM integrations.

Do not use `useEffect` for derived values.

Bad:

```tsx
const [fullName, setFullName] = useState("");

useEffect(() => {
  setFullName(`${firstName} ${lastName}`);
}, [firstName, lastName]);
```

Good:

```tsx
const fullName = `${firstName} ${lastName}`;
```

---

# 8. Next.js Boundaries

In the App Router, components are Server Components by default.

Add `"use client"` only where you need:

- event handlers;
- local state;
- effects;
- `window`, `document`, or `localStorage`;
- drag and drop;
- `contenteditable`;
- client-only libraries.

Do not make an entire layout a Client Component without a clear need.

Server-only code includes:

- database access;
- authentication;
- private API clients;
- secret environment variables;
- webhooks;
- access checks.

Never import a server-only module into a Client Component.

---

# 9. Runtime Validation and Migrations

Validate all external data at the boundary:

- request bodies;
- form data;
- URL/search parameters;
- uploaded files;
- imported JSON;
- localStorage/IndexedDB data;
- responses from external APIs.

When adding a new model field, update the entire lifecycle:

1. TypeScript type.
2. Runtime schema.
3. Factory/default values.
4. Parser/migration for legacy data.
5. Normalization helpers.
6. Import/export.
7. Search/filter indexing, if the field should be searchable.
8. Undo/redo snapshots, if users can edit the field.
9. UI for creating, editing, and clearing the field.
10. Edge cases and checks.

Example:

```ts
return {
  ...item,
  status: item.status ?? "active",
  tags: normalizeTags(item.tags),
  dueDate: normalizeDate(item.dueDate),
};
```

Do not add a model field only in the UI.

---

# 10. Forms

Every form must include:

- a validation schema;
- field errors;
- a submitting/loading state;
- a disabled submit button while submitting;
- protection against duplicate submissions;
- an error state;
- success behavior;
- reset/draft behavior, when applicable.

A form is not complete if it works only when the request succeeds perfectly.

---

# 11. shadcn/ui and Shared UI

Use `shadcn/ui` by default to build clean, consistent interfaces quickly.

Rules:

- first check whether the required component exists in the shadcn registry;
- add shadcn components through the CLI or the project's established local method;
- do not create a custom Button, Input, Modal, Dropdown, Tooltip, Tabs, or Card if shadcn already covers the use case;
- adapt shadcn components through `className`, variants, and composition instead of copying similar components;
- keep business components separate from primitives: `components/marketplace`, `features/*/ui`, `widgets/*`, or `entities/*/ui`;
- keep only shadcn primitives and thin reusable wrappers in `components/ui` or `shared/ui`;
- do not place product-specific business components there;
- if shadcn does not provide a component, create a minimal local wrapper consistent with the current shadcn configuration.

Base set of shadcn components for productivity interfaces:

```text
button
input
select
textarea
checkbox
switch
dialog
sheet
dropdown-menu
popover
tooltip
tabs
card
badge
avatar
separator
scroll-area
skeleton
carousel
accordion
collapsible
hover-card
```

For marketplace, chat, and support flows, also plan for these newer shadcn components:

```text
message
message-scroller
attachment
marker
```

Always use `cn()`:

```ts
export function cn(...values: Array<string | false | null | undefined>) {
  return values.filter(Boolean).join(" ");
}
```

---

# 12. Choosing the Right UI Surface

Before adding a new tool, choose the right surface:

| Feature size                       | Placement                         | Example                             |
| ---------------------------------- | --------------------------------- | ----------------------------------- |
| 1-5 quick settings                 | context menu / dropdown / popover | status, due date, tags              |
| 5-12 grouped settings              | sectioned, scrollable popover      | entity properties, compact filters  |
| large data sets or bulk actions    | sidebar / drawer                  | filters, tools panel                |
| complex form or dangerous action   | modal                             | import/export, delete confirmation  |
| permanent workspace                | dedicated view/page/widget        | dashboard, calendar, editor         |

Rule:

> If a control is used occasionally, keep it in a menu.
> If a control is used constantly, keep it visible on the main surface.
> If a control is complex and lengthy, move it to a sidebar or modal.

Do not turn a small group of controls into a large card on the page. In productivity interfaces, this wastes valuable space.

---

# 13. Compact UI for Editors, Dashboards, and Workspaces

In productivity applications, the primary content must remain the focus.

Required:

- the title, body, board, or editor must not be pushed downward by secondary controls;
- entity properties should generally open from an icon button next to the title;
- settings buttons must have an `aria-label`;
- an important status can be shown as a small badge;
- create/add actions must appear in a clear context;
- sidebar-heavy flows must include a mobile-friendly menu or switcher;
- do not make a productivity tool look like a landing page.

Bad:

```tsx
${largepropertiescard}
  <Select>Status</Select>
  <Select>Task</Select>
  <Input>Date</Input>
  <Input>Tags</Input>
</LargePropertiesCard>
```

Good:

```tsx
${titlerow}
  <TitleInput />
  <PropertiesMenu />
</TitleRow>
```

---

# 14. Overlays, Dropdowns, Popovers, and Context Menus

Every menu must behave as a true overlay.

Rules:

- if a menu may extend beyond its container, render it through `createPortal(..., document.body)`;
- use `position: fixed` or a reliable positioning helper;
- set an explicit `z-index`;
- use an opaque `backgroundColor`;
- do not rely only on a translucent `bg-black/50` background or blur;
- add a border, ring, or shadow;
- set `max-height` and `overflow-y-auto`;
- close on `Escape`;
- close on outside click/tap;
- prevent page text from showing through or rendering over the menu;
- hover and active states must not change the item's dimensions.

Minimal overlay style:

```tsx
<div
  role="menu"
  className="rounded-2xl border p-2 shadow-2xl"
  style=${backgroundcolor:"#151a21",
    boxShadow: "0 24px 70px rgb(0 0 0 / 78%)",
    isolation: "isolate",
    zIndex: 1000,}
>
  ...
</div>
```

If the menu background does not render correctly or content appears above it, check:

- the portal;
- `position`;
- `z-index`;
- parent stacking contexts;
- `isolation`;
- opacity/background;
- parent overflow/clipping.

---

# 15. Option Lists in Menus

A list of tasks, projects, users, tags, or other options in a menu must not look like a dense wall of text.

For a two-line item:

- use a `min-height` of 40-44px;
- include a `gap` between the icon, text, and checkmark;
- use vertical padding such as `py-1.5`;
- give the title and metadata different line heights;
- add `mt-0.5` between the title and metadata;
- apply `min-w-0` to the parent containing the text;
- apply `truncate` to the title and metadata;
- apply `shrink-0` to checkmarks and icons.

Example:

```tsx
<button className="flex min-h-11 items-center gap-2.5 rounded-lg px-2.5 py-1.5">
  <span className="min-w-0 flex-1">
    <span className="block truncate font-medium leading-5">${title}</span>
    <span className="mt-0.5 block truncate text-xs leading-4 text-muted">
      {meta}
    </span>
  </span>
  {isActive ? <Check className="shrink-0" /> : null}
</button>
```

---

# 16. Long Text and Overflow

Any user-provided text may contain a long word with no spaces.

For editors, `contenteditable` elements, Markdown, card titles, and comments:

- use `min-w-0` on flex/grid children;
- use the current Tailwind utilities for wrapping long words;
- in newer Tailwind versions, `break-words` may be written as `wrap-break-word`;
- check the documentation for the project's current Tailwind version before using wrapping, overflow, text-wrap, grid, spacing, or arbitrary-value classes;
- if an element is inside a flex container and long text breaks its width, check whether `wrap-anywhere` is appropriate;
- use `truncate` for short lines in cards;
- wrap body text instead of allowing horizontal overflow;
- text must not render over a menu, popover, or modal;
- test with a long string containing no spaces.

For an editable block:

```tsx
className = "min-w-0 wrap-break-word whitespace-pre-wrap";
```

If the project uses an older Tailwind version where `wrap-break-word` is unavailable, check the installed Tailwind version and the official documentation or version notes, then use a supported equivalent: `break-words`, an arbitrary value, or a CSS property.

For a badge:

```tsx
className = "inline-flex whitespace-nowrap";
```

A badge must not compress text vertically. If it does not fit, move it to a new line or use `truncate` with an explicit, understandable width.

---

# 17. Tailwind CSS: Verify Current Class Names

The AI agent must check the Tailwind version installed in the project before using new or potentially version-dependent classes.

Process:

1. Inspect `package.json` and the lockfile.
2. Determine the Tailwind major version.
3. If a class may differ between versions, check the official documentation for that exact version.
4. Do not replace classes mechanically without verification.
5. When using an arbitrary value, confirm that it is included in the build output.

Pay particular attention to:

- `break-words` / `wrap-break-word` / `wrap-anywhere`;
- `text-wrap`, `text-balance`, and `text-pretty`;
- `overflow-*`;
- `size-*`;
- arbitrary colors such as `bg-[#151a21]`;
- arbitrary shadows;
- arbitrary grid templates;
- dynamic class names.

Do not build dynamic Tailwind classes like this:

```tsx
const color = "red";
return <div className={`bg-${color}-500`} />;
```

Tailwind may not detect that class during the build. Use a map:

```tsx
const colorClassName = {
  danger: "bg-red-500",
  success: "bg-emerald-500",
}${variant};
```

If an important overlay background must not depend on Tailwind's build output, using an inline `style.backgroundColor` is acceptable.

---

# 18. Layout and Sidebar Collapse

Collapsing a sidebar or drawer must not change the page height or leave an empty block.

Rules:

- app shell: `h-dvh min-h-dvh overflow-hidden`;
- internal regions: `flex min-h-0 flex-1 overflow-hidden`;
- enable scrolling only on the appropriate region with `overflow-y-auto`;
- when collapsing, change width/flex-basis rather than height;
- a collapsed sidebar must have a stable width;
- provide a clear control for restoring the sidebar;
- destructive or creation actions must not remain as isolated buttons without context;
- preferences may be persisted in localStorage.

Example:

```tsx
<main className="flex h-dvh min-h-dvh flex-col overflow-hidden">
  <div className="flex min-h-0 flex-1 overflow-hidden">
    <Sidebar className="h-full min-h-0 shrink-0" />
    <section className="min-h-0 flex-1 overflow-y-auto" />
  </div>
</main>
```

---

# 19. Browser APIs and localStorage

In Next.js, browser APIs are available only in Client Components.

Rules:

- a file that uses `localStorage`, `window`, `document`, drag and drop, or `contenteditable` must include `"use client"`;
- do not read `localStorage` in a Server Component;
- do not cause hydration errors with different initial values;
- wrap storage operations in `try/catch`;
- storage failures must not break the UI;
- verify persisted UI preferences after a reload;
- the build must not fail with `window is not defined`.

Example:

```tsx
const toggle = useCallback(() => {
  setIsCollapsed((current) => {
    const next = !current;

    try {
      window.localStorage.setItem(KEY, next ? "true" : "false");
    } catch {
      // UI still works without browser storage.
    }

    return next;
  });
}, []);
```

Verify that:

- the default state works with empty storage;
- a reload preserves the state;
- private mode or storage errors do not break the screen;
- the build does not fail with `window is not defined`.

---

# 20. Relationships Between Tools

If one entity is linked to another, the relationship must be real:

- store it in the model;
- show it in the UI;
- clicking it opens the linked entity;
- when creating the related entity, save the relationship immediately;
- preserve the relationship during import/export;
- include the relationship in search/filter behavior when useful;
- if the related entity is deleted, show a fallback in the UI.

Do not create a decorative "Link" button if the relationship is not persisted.

---

# 21. Unified Domain Operations

Each user operation must have a single source of truth.

Do not:

- create an entity one way from the slash menu;
- create it another way from the toolbar;
- bypass validation from the command palette;
- duplicate mutation logic in the context menu.

Instead:

- keep the domain operation in one place;
- have UI components call that operation;
- use the same validation and constraints for every entry point.

---

# 23. Accessibility

Required:

- use `<button>` for actions;
- use `<a>` for navigation;
- add `aria-label` to icon-only buttons;
- provide labels for inputs;
- show a visible focus state;
- support keyboard navigation;
- close modals and popovers on `Escape`;
- close popovers on outside click;
- use a focus trap in modals;
- do not use color as the only way to communicate meaning;
- do not replace `<button>` with `${div_onclick}`.

---

# 24. Loading, Empty, and Error States

Data-driven screens must account for:

- loading;
- success;
- empty state;
- permission denied;
- network error;
- server error;
- retry.

A blank screen with no explanation is a bug.

---

# 25. Security

Required:

- keep secrets on the server only;
- use runtime validation;
- enforce access control on the server;
- validate file MIME types and sizes;
- sanitize user-provided HTML;
- do not use `dangerouslySetInnerHTML` without a sanitizer;
- do not log tokens or personal data;
- do not trust `role` or `userId` values supplied by the browser.

---

# 26. Performance

Measure first, then optimize.

Use:

- dynamic imports for heavy editor, chart, map, and PDF modules;
- image optimization;
- virtualization for large lists;
- abort/stale-request protection for search;
- selectors to reduce rerenders.

Do not add memoization without a reason.

---

# 27. Test the Design with Realistic Content

For additional guidance on interface quality, you may refer to:

- https://jakub.kr/skills/make-interfaces-feel-better

This resource is useful when polishing typography, hover states, shadows, borders, spacing, optical alignment, micro-interactions, and the overall feel of the interface.

Before completing a UI task, test it with:

- a long word with no spaces;
- a long Russian title;
- a short title;
- an empty title;
- multiple tags;
- a long list/category name;
- multiple options in a dropdown;
- active and inactive statuses;
- a date and a missing date.

Verify that:

- nothing overlaps;
- overlays cover the underlying content;
- text does not show through menus;
- badges do not compress text vertically;
- elements do not crowd each other;
- scrollbars do not cover important text;
- hover and focus states are easy to read;
- desktop and mobile widths both look correct.

---

# 28. Checks After Changes

After code changes, run:

```bash
npm run typecheck
npm run lint
npm run build
```

If the UI was changed:

- open the page in a browser;
- complete the primary user flow;
- test keyboard and mouse interaction;
- test `Escape` and outside-click behavior;
- test reloading;
- test long text;
- test a mobile viewport width;
- take a screenshot if the visual layer changed.

If browser verification is impossible, say so explicitly. Do not present `typecheck` as visual verification.

---

# 29. Git and the Working Tree

Before making changes, inspect the current state:

```bash
git status --short
```

Rules:

- do not revert someone else's changes without an explicit request;
- do not use destructive commands without explicit permission;
- do not perform unrelated refactoring;
- do not commit automatically unless the user asks you to;
- do not change line endings or reformat the entire project unnecessarily.

---

# 30. Final Report

In the final response, state:

- what changed;
- which files are important;
- which checks were run;
- what could not be verified;
- which risks remain.

Keep the report concise and honest.
