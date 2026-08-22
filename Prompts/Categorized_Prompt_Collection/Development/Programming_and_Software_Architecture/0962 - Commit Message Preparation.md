# Git Commit Guidelines for AI Language Models

## Core Principles

1. **Follow Conventional Commits** (https://www.conventionalcommits.org/)
2. **Be concise and precise** - No flowery language, superlatives, or unnecessary adjectives
3. **Focus on WHAT changed, not HOW it works** - Describe the change, not implementation details
4. **One logical change per commit** - Split related but independent changes into separate commits
5. **Write in imperative mood** - "Add feature" not "Added feature" or "Adds feature"
6. **Always include body text** - Never use subject-only commits

## Commit Message Structure

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Type (Required)

- `feat`: New feature
- `fix`: Bug fix
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `perf`: Performance improvement
- `style`: Code style changes (formatting, missing semicolons, etc.)
- `test`: Adding or updating tests
- `docs`: Documentation changes
- `build`: Build system or external dependencies (npm, gradle, Xcode, SPM)
- `ci`: CI/CD pipeline changes
- `chore`: Routine tasks (gitignore, config files, maintenance)
- `revert`: Revert a previous commit

### Scope (Optional but Recommended)

Indicates the area of change: `auth`, `ui`, `api`, `db`, `i18n`, `analytics`, etc.

### Subject (Required)

- **Max 50 characters**
- **Lowercase first letter** (unless it's a proper noun)
- **No period at the end**
- **Imperative mood**: "add" not "added" or "adds"
- **Be specific**: "add email validation" not "add validation"

### Body (Required)

- **Always include body text** - Minimum 1 sentence
- **Explain WHAT changed and WHY** - Provide context
- **Wrap at 72 characters**
- **Separate from subject with blank line**
- **Use bullet points for multiple changes** (use `-` or `*`)
- **Reference issue numbers** if applicable
- **Mention specific classes/functions/files when relevant**

### Footer (Optional)

- **Breaking changes**: `BREAKING CHANGE: <description>`
- **Issue references**: `Closes #123`, `Fixes #456`
- **Co-authors**: `Co-Authored-By: Name <email>`

## Banned Words & Phrases

**NEVER use these words** (they're vague, subjective, or exaggerated):

❌ Comprehensive
❌ Robust
❌ Enhanced
❌ Improved (unless you specify what metric improved)
❌ Optimized (unless you specify what metric improved)
❌ Better
❌ Awesome
❌ Great
❌ Amazing
❌ Powerful
❌ Seamless
❌ Elegant
❌ Clean
❌ Modern
❌ Advanced

## Good vs Bad Examples

### ❌ BAD (No body)
```
feat(auth): add email/password login
```

**Problems:**
- No body text
- Doesn't explain what was actually implemented

### ❌ BAD (Vague body)
```
feat: Add awesome new login feature

This commit adds a powerful new login system with robust authentication
and enhanced security features. The implementation is clean and modern.
```

**Problems:**
- Subjective adjectives (awesome, powerful, robust, enhanced, clean, modern)
- Doesn't specify what was added
- Body describes quality, not functionality

### ✅ GOOD
```
feat(auth): add email/password login with Firebase

Implement login flow using Firebase Authentication. Users can now sign in
with email and password. Includes client-side email validation and error
handling for network failures and invalid credentials.
```

**Why it's good:**
- Specific technology mentioned (Firebase)
- Clear scope (auth)
- Body describes what functionality was added
- Explains what error handling covers

---

### ❌ BAD (No body)
```
fix(auth): prevent login button double-tap
```

**Problems:**
- No body text explaining the fix

### ✅ GOOD
```
fix(auth): prevent login button double-tap

Disable login button after first tap to prevent duplicate authentication
requests when user taps multiple times quickly. Button re-enables after
authentication completes or fails.
```

**Why it's good:**
- Imperative mood
- Specific problem described
- Body explains both the issue and solution approach

---

### ❌ BAD
```
refactor(auth): extract helper functions

Make code better and more maintainable by extracting functions.
```

**Problems:**
- Subjective (better, maintainable)
- Not specific about which functions

### ✅ GOOD
```
refactor(auth): extract helper functions to static struct methods

Convert private functions randomNonceString and sha256 into static methods
of AppleSignInHelper struct for better code organization and namespacing.
```

**Why it's good:**
- Specific change described
- Mentions exact function names
- Body explains reasoning and new structure

---

### ❌ BAD
```
feat(i18n): add localization
```

**Problems:**
- No body
- Too vague

### ✅ GOOD
```
feat(i18n): add English and Turkish translations for login screen

Create String Catalog with translations for login UI elements, alerts,
and authentication errors in English and Turkish. Covers all user-facing
strings in LoginView, LoginViewController, and AuthService.
```

**Why it's good:**
- Specific languages mentioned
- Clear scope (i18n)
- Body lists what was translated and which files

---

## Multi-File Commit Guidelines

### When to Split Commits

Split changes into separate commits when:

1. **Different logical concerns**
   - ✅ Commit 1: Add function
   - ✅ Commit 2: Add tests for function

2. **Different scopes**
   - ✅ Commit 1: `feat(ui): add button component`
   - ✅ Commit 2: `feat(api): add endpoint for button action`

3. **Different types**
   - ✅ Commit 1: `feat(auth): add login form`
   - ✅ Commit 2: `refactor(auth): extract validation logic`

### When to Combine Commits

Combine changes in one commit when:

1. **Tightly coupled changes**
   - ✅ Adding a function and its usage in the same component

2. **Atomic change**
   - ✅ Refactoring function name across multiple files

3. **Breaking without each other**
   - ✅ Adding interface and its implementation together

## File-Level Commit Strategy

### Example: LoginView Changes

If LoginView has 2 independent changes:

**Change 1:** Refactor stack view structure
**Change 2:** Add loading indicator

**Split into 2 commits:**

```
refactor(ui): extract content stack view as property in login view

Change inline stack view initialization to property-based approach for
better code organization and reusability. Moves stack view definition
from setupUI method to lazy property.
```

```
feat(ui): add loading state with activity indicator to login view

Add loading indicator overlay and setLoading method to disable user
interaction and dim content during authentication. Content alpha reduces
to 0.5 when loading.
```

## Localization-Specific Guidelines

### ✅ GOOD
```
feat(i18n): add English and Turkish translations

Create String Catalog (Localizable.xcstrings) with English and Turkish
translations for all login screen strings, error messages, and alerts.
```

```
build(i18n): add Turkish localization support

Add Turkish language to project localizations and enable String Catalog
generation (SWIFT_EMIT_LOC_STRINGS) in build settings for Debug and
Release configurations.
```

```
feat(i18n): localize login view UI elements

Replace hardcoded strings with NSLocalizedString in LoginView for title,
subtitle, labels, placeholders, and button titles. All user-facing text
now supports localization.
```

### ❌ BAD
```
feat: Add comprehensive multi-language support

Add awesome localization system to the app.
```

```
feat: Add translations
```

## Breaking Changes

When introducing breaking changes:

```
feat(api): change authentication response structure

Authentication endpoint now returns user object in 'data' field instead
of root level. This allows for additional metadata in the response.

BREAKING CHANGE: Update all API consumers to access response.data.user
instead of response.user.

Migration guide:
- Before: const user = response.user
- After: const user = response.data.user
```

## Commit Ordering

When preparing multiple commits, order them logically:

1. **Dependencies first**: Add libraries/configs before usage
2. **Foundation before features**: Models before views
3. **Build before source**: Build configs before code changes
4. **Utilities before consumers**: Helpers before components that use them

### Example Order:

```
1. build(auth): add Sign in with Apple entitlement
   Add entitlements file with Sign in with Apple capability for enabling
   Apple ID authentication.

2. feat(auth): add Apple Sign-In cryptographic helpers
   Add utility functions for generating random nonce and SHA256 hashing
   required for Apple Sign-In authentication flow.

3. feat(auth): add Apple Sign-In authentication to AuthService
   Add signInWithApple method to AuthService protocol and implementation.
   Uses OAuthProvider credential with idToken and nonce for Firebase
   authentication.

4. feat(auth): add Apple Sign-In flow to login view model
   Implement loginWithApple method in LoginViewModel to handle Apple
   authentication with idToken, nonce, and fullName.

5. feat(auth): implement Apple Sign-In authorization flow
   Add ASAuthorizationController delegate methods to handle Apple Sign-In
   authorization, credential validation, and error handling.
```

## Special Cases

### Configuration Files

```
chore: ignore GoogleService-Info.plist from version control

Add GoogleService-Info.plist to .gitignore to prevent committing Firebase
configuration with API keys.
```

```
build: update iOS deployment target to 15.0

Change minimum iOS version from 14.0 to 15.0 to support async/await syntax
in authentication flows.
```

```
ci: add GitHub Actions workflow for testing

Add workflow to run unit tests on pull requests. Runs on macOS latest
with Xcode 15.
```

### Documentation

```
docs: add API authentication guide

Document Firebase Authentication setup process, including Google Sign-In
and Apple Sign-In configuration steps.
```

```
docs: update README with installation steps

Add SPM dependency installation instructions and Firebase setup guide.
```

### Refactoring

```
refactor(auth): convert helper functions to static struct methods

Wrap Apple Sign-In helper functions in AppleSignInHelper struct with
static methods for better code organization and namespacing. Converts
randomNonceString and sha256 from private functions to static methods.
```

```
refactor(ui): extract email validation to separate method

Move email validation regex logic from loginWithEmail to isValidEmail
method for reusability and testability.
```

### Performance

**Specify the improvement:**

❌ `perf: optimize login`

✅
```
perf(auth): reduce login request time from 2s to 500ms

Add request caching for Firebase configuration to avoid repeated network
calls. Configuration is now cached after first retrieval.
```

## Body Text Requirements

**Minimum requirements for body text:**

1. **At least 1-2 complete sentences**
2. **Describe WHAT was changed specifically**
3. **Explain WHY the change was needed (when not obvious)**
4. **Mention affected components/files when relevant**
5. **Include technical details that aren't obvious from subject**

### Good Body Examples:

```
Add loading indicator overlay and setLoading method to disable user
interaction and dim content during authentication.
```

```
Update signInWithApple method to accept fullName parameter and use
appleCredential for proper user profile creation in Firebase.
```

```
Replace hardcoded strings with NSLocalizedString in LoginView for title,
labels, placeholders, and buttons. All UI text now supports English and
Turkish translations.
```

### Bad Body Examples:

❌ `Add feature.` (too vague)
❌ `Updated files.` (doesn't explain what)
❌ `Bug fix.` (doesn't explain which bug)
❌ `Refactoring.` (doesn't explain what was refactored)

## Template for AI Models

When an AI model is asked to create commits:

```
1. Read git diff to understand ALL changes
2. Group changes by logical concern
3. Order commits by dependency
4. For each commit:
   - Choose appropriate type and scope
   - Write specific, concise subject (max 50 chars)
   - Write detailed body (minimum 1-2 sentences, required)
   - Use imperative mood
   - Avoid banned words
   - Focus on WHAT changed and WHY
5. Output format:
   ## Commit [N]

   **Title:**
   ```
   type(scope): subject
   ```

   **Description:**
   ```
   Body text explaining what changed and why. Mention specific
   components, classes, or methods affected. Provide context.
   ```

   **Files to add:**
   ```bash
   git add path/to/file
   ```
```

## Final Checklist

Before suggesting a commit, verify:

- [ ] Type is correct (feat/fix/refactor/etc.)
- [ ] Scope is specific and meaningful
- [ ] Subject is imperative mood
- [ ] Subject is ≤50 characters
- [ ] **Body text is present (required)**
- [ ] **Body has at least 1-2 complete sentences**
- [ ] Body explains WHAT and WHY
- [ ] No banned words used
- [ ] No subjective adjectives
- [ ] Specific about WHAT changed
- [ ] Mentions affected components/files
- [ ] One logical change per commit
- [ ] Files grouped correctly

---

## Example Commit Message (Complete)

```
feat(auth): add email validation to login form

Implement client-side email validation using regex pattern before sending
authentication request. Validates format matches standard email pattern
(user@domain.ext) and displays error message for invalid inputs. Prevents
unnecessary Firebase API calls for malformed emails.
```

**What makes this good:**
- Clear type and scope
- Specific subject
- Body explains what validation does
- Body explains why it's needed
- Mentions the benefit (prevents API calls)
- No banned words
- Imperative mood throughout

---

**Remember:** A good commit message should allow someone to understand the change without looking at the diff. Be specific, be concise, be objective, and always include meaningful body text.
