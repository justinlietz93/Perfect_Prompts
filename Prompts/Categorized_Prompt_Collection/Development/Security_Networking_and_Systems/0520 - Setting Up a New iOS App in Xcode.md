You are setting up a new iOS app project in Xcode.

Goal
Create a clean iPhone-only app with strict defaults.

Project settings
- Minimum iOS Deployment Target: 26.0
- Supported Platforms: iPhone only
- Mac support: Mac (Designed for iPhone) enabled
- iPad support: disabled

Orientation
- Default orientation: Portrait only
- Set “Supported interface orientations (iPhone)” to Portrait only
- Verify Build Settings or Info.plist includes only:
  - UISupportedInterfaceOrientations = UIInterfaceOrientationPortrait

Security and compliance
- Info.plist: App Uses Non-Exempt Encryption (ITSAppUsesNonExemptEncryption) = NO

Output
Confirm each item above and list where you set it in Xcode (Target, General, Build Settings, Info.plist).
