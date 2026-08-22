---
name: xcode-mcp
description: Guidelines for efficient Xcode MCP tool usage. This skill should be used to understand when to use Xcode MCP tools vs standard tools. Xcode MCP consumes many tokens - use only for build, test, simulator, preview, and SourceKit diagnostics. Never use for file read/write/grep operations.
---

# Xcode MCP Usage Guidelines

Xcode MCP tools consume significant tokens. This skill defines when to use Xcode MCP and when to prefer standard tools.

## Complete Xcode MCP Tools Reference

### Window & Project Management
| Tool | Description | Token Cost |
|------|-------------|------------|
| `mcp__xcode__XcodeListWindows` | List open Xcode windows (get tabIdentifier) | Low ✓ |

### Build Operations
| Tool | Description | Token Cost |
|------|-------------|------------|
| `mcp__xcode__BuildProject` | Build the Xcode project | Medium ✓ |
| `mcp__xcode__GetBuildLog` | Get build log with errors/warnings | Medium ✓ |
| `mcp__xcode__XcodeListNavigatorIssues` | List issues in Issue Navigator | Low ✓ |

### Testing
| Tool | Description | Token Cost |
|------|-------------|------------|
| `mcp__xcode__GetTestList` | Get available tests from test plan | Low ✓ |
| `mcp__xcode__RunAllTests` | Run all tests | Medium |
| `mcp__xcode__RunSomeTests` | Run specific tests (preferred) | Medium ✓ |

### Preview & Execution
| Tool | Description | Token Cost |
|------|-------------|------------|
| `mcp__xcode__RenderPreview` | Render SwiftUI Preview snapshot | Medium ✓ |
| `mcp__xcode__ExecuteSnippet` | Execute code snippet in file context | Medium ✓ |

### Diagnostics
| Tool | Description | Token Cost |
|------|-------------|------------|
| `mcp__xcode__XcodeRefreshCodeIssuesInFile` | Get compiler diagnostics for specific file | Low ✓ |
| `mcp__ide__getDiagnostics` | Get SourceKit diagnostics (all open files) | Low ✓ |

### Documentation
| Tool | Description | Token Cost |
|------|-------------|------------|
| `mcp__xcode__DocumentationSearch` | Search Apple Developer Documentation | Low ✓ |

### File Operations (HIGH TOKEN - NEVER USE)
| Tool | Alternative | Why |
|------|-------------|-----|
| `mcp__xcode__XcodeRead` | `Read` tool | High token consumption |
| `mcp__xcode__XcodeWrite` | `Write` tool | High token consumption |
| `mcp__xcode__XcodeUpdate` | `Edit` tool | High token consumption |
| `mcp__xcode__XcodeGrep` | `rg` / `Grep` tool | High token consumption |
| `mcp__xcode__XcodeGlob` | `Glob` tool | High token consumption |
| `mcp__xcode__XcodeLS` | `ls` command | High token consumption |
| `mcp__xcode__XcodeRM` | `rm` command | High token consumption |
| `mcp__xcode__XcodeMakeDir` | `mkdir` command | High token consumption |
| `mcp__xcode__XcodeMV` | `mv` command | High token consumption |

---

## Recommended Workflows

### 1. Code Change & Build Flow
```
1. Search code      → rg "pattern" --type swift
2. Read file        → Read tool
3. Edit file        → Edit tool
4. Syntax check     → mcp__ide__getDiagnostics
5. Build            → mcp__xcode__BuildProject
6. Check errors     → mcp__xcode__GetBuildLog (if build fails)
```

### 2. Test Writing & Running Flow
```
1. Read test file   → Read tool
2. Write/edit test  → Edit tool
3. Get test list    → mcp__xcode__GetTestList
4. Run tests        → mcp__xcode__RunSomeTests (specific tests)
5. Check results    → Review test output
```

### 3. SwiftUI Preview Flow
```
1. Edit view        → Edit tool
2. Render preview   → mcp__xcode__RenderPreview
3. Iterate          → Repeat as needed
```

### 4. Debug Flow
```
1. Check diagnostics → mcp__ide__getDiagnostics (quick syntax check)
2. Build project     → mcp__xcode__BuildProject
3. Get build log     → mcp__xcode__GetBuildLog (severity: error)
4. Fix issues        → Edit tool
5. Rebuild           → mcp__xcode__BuildProject
```

### 5. Documentation Search
```
1. Search docs       → mcp__xcode__DocumentationSearch
2. Review results    → Use information in implementation
```

---

## Fallback Commands (When MCP Unavailable)

If Xcode MCP is disconnected or unavailable, use these xcodebuild commands:

### Build Commands
```bash
# Debug build (simulator) - replace <SchemeName> with your project's scheme
xcodebuild -scheme <SchemeName> -configuration Debug -sdk iphonesimulator build

# Release build (device)
xcodebuild -scheme <SchemeName> -configuration Release -sdk iphoneos build

# Build with workspace (for CocoaPods projects)
xcodebuild -workspace <ProjectName>.xcworkspace -scheme <SchemeName> -configuration Debug -sdk iphonesimulator build

# Build with project file
xcodebuild -project <ProjectName>.xcodeproj -scheme <SchemeName> -configuration Debug -sdk iphonesimulator build

# List available schemes
xcodebuild -list
```

### Test Commands
```bash
# Run all tests
xcodebuild test -scheme <SchemeName> -sdk iphonesimulator \
  -destination "platform=iOS Simulator,name=iPhone 16" \
  -configuration Debug

# Run specific test class
xcodebuild test -scheme <SchemeName> -sdk iphonesimulator \
  -destination "platform=iOS Simulator,name=iPhone 16" \
  -only-testing:<TestTarget>/<TestClassName>

# Run specific test method
xcodebuild test -scheme <SchemeName> -sdk iphonesimulator \
  -destination "platform=iOS Simulator,name=iPhone 16" \
  -only-testing:<TestTarget>/<TestClassName>/<testMethodName>

# Run with code coverage
xcodebuild test -scheme <SchemeName> -sdk iphonesimulator \
  -configuration Debug -enableCodeCoverage YES

# List available simulators
xcrun simctl list devices available
```

### Clean Build
```bash
xcodebuild clean -scheme <SchemeName>

```

---

## Quick Reference

### USE Xcode MCP For:
- ✅ `BuildProject` - Building
- ✅ `GetBuildLog` - Build errors
- ✅ `RunSomeTests` - Running specific tests
- ✅ `GetTestList` - Listing tests
- ✅ `RenderPreview` - SwiftUI previews
- ✅ `ExecuteSnippet` - Code execution
- ✅ `DocumentationSearch` - Apple docs
- ✅ `XcodeListWindows` - Get tabIdentifier
- ✅ `mcp__ide__getDiagnostics` - SourceKit errors

### NEVER USE Xcode MCP For:
- ❌ `XcodeRead` → Use `Read` tool
- ❌ `XcodeWrite` → Use `Write` tool
- ❌ `XcodeUpdate` → Use `Edit` tool
- ❌ `XcodeGrep` → Use `rg` or `Grep` tool
- ❌ `XcodeGlob` → Use `Glob` tool
- ❌ `XcodeLS` → Use `ls` command
- ❌ File operations → Use standard tools

---

## Token Efficiency Summary

| Operation | Best Choice | Token Impact |
|-----------|-------------|--------------|
| Quick syntax check | `mcp__ide__getDiagnostics` | 🟢 Low |
| Full build | `mcp__xcode__BuildProject` | 🟡 Medium |
| Run specific tests | `mcp__xcode__RunSomeTests` | 🟡 Medium |
| Run all tests | `mcp__xcode__RunAllTests` | 🟠 High |
| Read file | `Read` tool | 🟠 High |
| Edit file | `Edit` tool | 🟠 High|
| Search code | `rg` / `Grep` | 🟢 Low |
| List files | `ls` / `Glob` | 🟢 Low |
