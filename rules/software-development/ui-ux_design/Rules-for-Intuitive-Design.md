# Rules for Intuitive Design

**Generated on:** November 7, 2025 at 6:19 PM CST

---

## General Usability Principles

* **Krug's First Law of Usability:** Do not make the user think.
* **Krug's Second Law of Usability:** Ensure each click is a mindless, unambiguous choice.
* **Krug's Third Law of Usability:** Get rid of half the words on each page, then get rid of half of what's left.
* Define usability as: A person of average (or even below average) ability and experience must be able to figure out how to use the thing to accomplish something without it being more trouble than it's worth.
* Ensure Web pages are self-evident; if not possible, they must be self-explanatory, requiring only a little thought.
* Aim for pages to work most of their magic at a glance.
* Design for scanning, not reading.
* Assume users do not make optimal choices; they satisfice (choose the first reasonable option).
* Assume users do not figure out how things work; they muddle through.

## Design Principles & Visual Hierarchy

* **Clarity Trumps Consistency:** If you can make something significantly clearer by making it slightly inconsistent, choose clarity.
* Leverage existing conventions (standardized design patterns) to make interfaces easier to grasp.
* If deviating from a convention, ensure the new design is either:
  * So clear and self-explanatory that there is no learning curve and it is as good as the convention.
  * Adds so much value that it justifies a small learning curve.
* Be creative and innovative, but always ensure the design remains usable.
* Create effective visual hierarchies:
  * Ensure more important elements are more prominent (larger, bolder, distinctive color, more white space, nearer the top).
  * Visually relate logically connected items (grouping, similar style, defined areas).
  * Visually nest items to show what belongs to what.
* Break pages into clearly defined areas.
* Make it obvious what is clickable.
* Do not use the same color for text links and non-clickable headings.
* Eliminate visual noise; everything not contributing to the solution must go.
* Use grids to align elements on a page and avoid disorganization.
* Prioritize elements to avoid "shouting" (all elements clamoring for attention).
* If a visual cue is sticking out like a sore thumb to a designer, make it twice as prominent for users.

## Content & Wording

* Avoid cute, clever, marketing-induced, company-specific, or unfamiliar technical names that require thought.
* When choosing names, skew towards "Obvious."
* Eliminate "happy talk" (content-free, self-congratulatory promotional text).
* Eliminate instructions entirely by making elements self-explanatory. If instructions are necessary, keep them to the bare minimum.
* Format text to support scanning:
  * Use plenty of well-written, thoughtful headings.
  * If using multiple heading levels, ensure obvious visual distinction between them (e.g., larger size, more space above).
  * Do not float headings between paragraphs; they must be closer to the text they introduce than the text they follow. (Repeated definitively later).
  * Keep paragraphs short; single-sentence paragraphs are acceptable.
  * Use bulleted lists for any series of items.
  * Ensure a small amount of additional space between bulleted list items for optimal readability.
  * Highlight key terms in bold where they first appear, but do not over-highlight.

## Form Design

* If a choice is difficult, provide brief, timely, and unavoidable guidance.
* Do not put labels inside form fields unless the form is exceptionally simple, labels disappear when typing, labels reappear if the field is empty, labels cannot be confused with answers, there is no possibility of submitting labels with user input, AND they are completely accessible.
* Do not punish users for not formatting data a specific way (e.g., dashes in SSN, spaces in credit card number).

## Home Page

* The Home page must convey site identity, mission, hierarchy, search, teases (content/feature promos), timely content, deals, shortcuts, and registration options.
* The Home page must quickly and clearly answer: "What is this?", "What can I do here?", "What do they have here?", and "Why should I be here—and not somewhere else?". Users must be able to answer these at a glance, correctly and unambiguously, with very little effort.
* Every page of the site should do its best to orient users, but the Home page is critical for this.
* Explicitly state what the site is about in the tagline, welcome blurb, or a "learn more" section.
* Use as much space as necessary to convey the main message, but no more; keep it short and focused on key features.
* Do not use a corporate mission statement as a welcome blurb.
* Make entry points (e.g., search box, category lists, sign-in) look like entry points and label them clearly.
* Preserve the Home page from promotional overload ("tragedy of the commons").
* **Taglines:**
  * Appear right below, above, or next to the Site ID.
  * Must be clear, informative, and explain what the site/organization does.
  * Should be 6-8 words long.
  * Must convey differentiation and a clear benefit (ideally, no one else could use it).
  * Avoid sounding generic.
  * Do not confuse a tagline with a motto.
  * Can be personable, lively, or clever, but cleverness must convey, not obscure, the benefit.

## Navigation

* Users must be able to find their way around the site.
* Navigation reveals content and implicitly instructs users on how to use the site.
* Navigation conventions (appearance and location) should be followed.
* Use persistent (global) navigation elements on most pages.
* Persistent navigation must appear in the same place with a consistent look.
* Persistent navigation must include Site ID, Utilities, Sections (primary navigation), and Search.
* **Exception:** For forms, use a minimal persistent navigation (Site ID, Home link, relevant Utilities).
* **Site ID/Logo:**
  * Must appear on every page.
  * Expected at the top, usually near the upper-left corner (for L-to-R languages).
  * Must look like a Site ID (distinctive typeface, recognizable graphic).
  * Expected to be a clickable link to the Home page.
* Persistent navigation should accommodate only four or five utilities; less frequently used utilities belong in the footer.
* A link or button to the Home page is a crucial item in persistent navigation.
* Unless a site is very small or well-organized, every page must have a search box or link to a search page; preferably a search box.
* **Search Box:**
  * Must follow the simple formula: a box, a button, and "Search" or a magnifying glass icon.
  * Use "Search" as the label, not fancy wording like "Find" or "Quick Search."
  * If "Search" is the label, use "Go" as the button name.
  * Do not add instructions (e.g., "Type a keyword").
  * If search scope is ambiguous, spell it out.
  * Think carefully before adding options to limit search scope in the persistent search box; provide them on the search results page if needed.
* Design navigation for all potential levels of the site from the beginning.
* **Page Names:**
  * Every page must have a name.
  * The page name must be positioned to frame the unique content of that page.
  * The page name must be prominent (combination of position, size, color, typeface, often the largest text).
  * The page name must match the words of the link clicked to reach it. If not an exact match, they must be as close as possible and the reason for the difference obvious.
* Show current location ("You are here" indicators) by highlighting it in navigation.
* "You are here" indicators must stand out and use multiple visual distinctions (e.g., color and bold text).
* **Breadcrumbs:**
  * Position at the top of the page.
  * Use ">" as the separator between levels.
  * Boldface the last item (current page name), which should not be a link.
* **Tabs:**
  * Graphics must create the visual illusion that the active tab is in front of other tabs.
  * The active tab needs a different color or contrasting shade and must physically connect with the space below it.

## Mobile Design

* Mobile design principles are fundamentally the same as for Web usability, but users move faster and read less on small screens.
* Design decisions for mobile involve trade-offs, which should prioritize a good user experience.
* Do not sacrifice usability when managing real estate challenges on small screens.
* Mobile sites must be usable on any size screen.
* Allow zooming on mobile sites; do not resist efforts to view content on mobile devices.
* Do not redirect deep links to the mobile Home page; take users directly to the intended content.
* Always provide a link to the "full" (non-mobile) Web site, typically a "Mobile Site/Full Site toggle" at the bottom of every page.
* Affordances must be noticeable and should not be hidden.
* Compensate for the absence of hover effects on touch screens.
* If using Flat design, ensure all remaining visual dimensions are used to compensate for lost affordances and maintain clear distinctions.
* Prioritize speed and performance on mobile devices.
* Ensure responsive design solutions do not load pages with excessive code or images larger than necessary for the user's screen.
* Do not focus so much on making apps delightful that you forget to make them usable.
* For apps with more than a few features, ensure they are easy to learn, potentially through effective in-app training or help.
* Ensure apps are memorable; if easy to learn initially, they should be easy to relearn.

## Accessibility

* A site cannot be considered usable unless it is accessible.
* Prioritize fixing usability problems that confuse *everyone* first, as this is the most effective way to improve accessibility.
* Add appropriate `alt` text to every image:
  * Use an empty (`alt=""`) or "null" alt attribute for images screen readers should ignore.
  * Add helpful, descriptive text for all other images.
* Use HTML heading elements (`<h1>`, `<h2>`, `<h3>`, etc.) correctly to convey logical content organization. Define visual appearance using CSS.
* Make forms work with screen readers by using the HTML `<label>` element to associate fields with their text labels.
* Include a "Skip to Main Content" link at the beginning of each page.
* Ensure all content is accessible by keyboard.
* Create significant contrast between text and background colors; never use small, low-contrast type.
* Use accessible templates (e.g., WordPress themes designed for accessibility).

## Usability Testing

* Testing is essential for a great site; the only way to confirm a site works is to observe users.
* Testing one user is 100% better than testing none.
* Testing one user early in a project is more valuable than testing many users late in the process.
* Usability tests should be used throughout the entire development process.
* Do-it-yourself (DIY) usability testing is a viable and recommended approach.
* For DIY testing, spend one morning a month on testing, debriefing, and deciding what to fix.
* Conduct testing continually throughout the development process.
* Test with three participants per round for DIY testing.
* Recruit participants loosely; prioritize frequent testing over testing "actual" users perfectly.
* If a site requires specific domain knowledge, recruit some participants with that knowledge.
* When a participant encounters a problem, analyze if typical users would also experience it or if it's due to the participant's unique knowledge/lack thereof.
* Provide incentives for participants.
* Conduct tests in a quiet space with necessary equipment (computer, internet, mouse, keyboard, microphone).
* Use screen sharing software to allow observers to watch from another room.
* Use screen recording software to capture the session.
* The facilitator's main job is to encourage participants to "think out loud."
* Do not ask leading questions or provide clues/assistance during tasks, unless the participant is hopelessly stuck or extremely frustrated.
* If a participant asks for help, ask, "What would you do if I wasn’t here?"
* Encourage as many team members, stakeholders, and executives as possible to observe tests live.
* Observers must write down the three most serious usability problems they noticed after each session.
* Start testing as early as possible (e.g., competitive sites, existing site redesigns) and continue through sketches, wireframes, prototypes, and actual pages.
* For each round, define tasks carefully, ensuring participants understand what to do and providing any necessary information (e.g., login).
* During tasks, let participants work independently until they finish, get extremely frustrated, or new learning ceases.
* Save probing questions for the end of the task portion.
* Do not get overly excited by individual reactions to site aesthetics.
* Focus ruthlessly on fixing the most serious problems first.
* When debriefing, collectively list observed problems (no discussion yet).
* Only list observed problems that actually occurred during test sessions.
* Prioritize the most serious problems (e.g., top 10).
* Create an action plan for fixing the top problems within the next month, assigning owners and resources.
* Do not aim for perfect or complete fixes; aim to resolve the "serious problem" category.
* Stop allocating resources for fixes when the monthly capacity is reached.
* Keep a separate list of "low-hanging fruit" (problems one person can fix in under an hour without external permission).
* Resist adding new features or explanations when fixing problems; often, removing distractions is the better solution.
* Take new feature requests from participants with a grain of salt.
* Ignore "kayak" problems (minor issues where users quickly recover without help).
* For mobile testing:
  * The process is generally the same as desktop testing.
  * Use a camera pointed at the screen/device (rather than mirroring) to capture gestures.
  * Attach the camera to the device so the user can hold it naturally.
  * Avoid using a camera pointed at the participant's face.

## Ethical & Professional Conduct

* If asked to manipulate users (e.g., tricking them into signing up for newsletters, installing toolbars, phishing), understand that this is not part of a usability professional's job.
* Usability is fundamentally a user advocacy role.

## Copyright & Legal

* No part of the book may be reproduced or transmitted without prior written permission from the publisher.
* Contact <permissions@peachpit.com> for reprint/excerpt permission.
* The book is distributed "As Is" and without warranty.
* The author and publisher disclaim liability for any loss or damage caused by the book's instructions or described products.
* Trademarks are used as requested by owners or in editorial fashion without infringement intent.
* No use of product names/trade names is intended to convey endorsement or affiliation with the book.

## Key Highlights

* Krug's First Law of Usability dictates: Do not make the user think.
* A site cannot be considered usable unless it is accessible; prioritize fixing usability problems that confuse everyone first.
* Clarity trumps consistency; if something can be made significantly clearer by being slightly inconsistent, choose clarity.
* Design for scanning, not reading, assuming users will satisfice by choosing the first reasonable option and muddle through.
* Usability testing is essential and should be conducted continually throughout the development process, with DIY testing viable even with just three participants per round.
* Create effective visual hierarchies by making more important elements prominent, visually relating logically connected items, and nesting items to show belonging.
* Eliminate all visual noise; everything that does not contribute to the solution must be removed.
* The Home page must quickly and unambiguously answer 'What is this?', 'What can I do here?', 'What do they have here?', and 'Why should I be here?' at a glance.
* Usability is fundamentally a user advocacy role, and professionals should not engage in manipulating users or tricking them.

## Example ideas

* Establish a continuous, DIY usability testing program, conducting monthly rounds with 3 participants to identify and prioritize critical user experience issues early and iteratively.
* Conduct a comprehensive heuristic evaluation of existing key user flows and critical pages, cross-referencing against Krug's Laws and the defined design principles to pinpoint areas of unnecessary user thought or ambiguity.
* Initiate a detailed accessibility audit across primary digital products, specifically focusing on correct HTML semantics (headings, labels, alt text), keyboard navigation, and color contrast to ensure foundational accessibility.
* Implement a content audit and revision initiative for critical pages and user instructions, aiming to drastically reduce word count, eliminate 'happy talk,' and optimize content for scannability and self-evidence as per Krug's Third Law.
