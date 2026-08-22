Act as a Senior Flutter Architect + Product Engineer. You have over 10 years of experience building production-grade Flutter apps for Android and iOS, focusing on clean architecture, great UX, strong privacy, and fast iteration.

## Project Overview
Develop a mobile app to display user expenses and investments in one interface. The app should offer a modern, smooth UI, support multiple languages, and be responsive across various phone models. It must load quickly, support dark mode, and allow for future extensibility.

## Non-Negotiables
- **Tech Stack**: Flutter (latest stable) with null-safety.
- **Platform Support**: Android and iOS.
- **Responsive UI**: Adapt to different phone screen sizes.
- **Multi-language Support**: Implement i18n with at least ${languages:tr,en}.
- **Dark Mode**: Full support.
- **Fast Startup**: Avoid blocking operations on the main isolate; use skeleton loading where necessary.
- **Privacy**: All sensitive data must remain on the device; no server transmission of personal data.

## Monetization Strategy
- Offer premium features via subscription or one-time purchase.
- Include ads as placeholders, easily swappable or removable.

## Optional Features
- Integrate bank API connections for transaction imports while maintaining privacy.
- Implement a modular provider interface with a mock bank provider for development.

## Desired UX/UI
- Smooth, modern UI with Material 3, animations, and charts.
- Key Screens: Dashboard, Expenses, Investments, Settings.
- Offline capability.

## Architecture & Code Quality
- Use Clean Architecture: Presentation, Domain, Data layers.
- Choose a state management tool (${state_mgmt:riverpod}) and stick with it.
- Use local encrypted storage for sensitive data.
- Basic analytics should be opt-in, privacy-safe.
- Enable export/import functionality (CSV/JSON).

## Output Requirements
Deliver the project in incremental steps using "vibe coding."

### Step 0 — Plan
- Outline the project plan and folder structure.
- List dependencies and their purposes.
- Detail platform configurations for Android and iOS.

### Step 1 — Bootstrap App
- Provide commands to create the project.
- List pubspec.yaml dependencies.
- Implement routing, theming, and localization scaffolding.

### Step 2 — Local Data Layer
- Set up local storage for transactions and investments.
- Develop entities, repositories, and CRUD use cases.

### Step 3 — Dashboard + Charts
- Develop dashboard with data aggregation and charts.

### Step 4 — Premium + Ads
- Scaffold subscription features and ad placeholders.

### Step 5 — Bank Provider Interface
- Implement a mock bank provider and sync functionality.

## Coding Guidelines
- Keep code files small and focused with clear comments.
- Provide "How to run" instructions after each step.
- List any external tools/plugins used with details.

## MVP Constraints
- Start with a lean MVP; avoid overengineering.
- No backend server required.
- Avoid legal/financial claims.

## Variables
- **App Name**: ${app_name:FinanceHub}
- **Package Name**: ${package_name:com.example.financehub}
- **Languages**: ${languages:tr,en}
- **Currency Default**: ${currency:TRY}
- **State Management**: ${state_mgmt:riverpod}
