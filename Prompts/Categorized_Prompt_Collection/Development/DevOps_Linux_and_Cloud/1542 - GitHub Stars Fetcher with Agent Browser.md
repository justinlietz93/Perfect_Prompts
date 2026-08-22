# Using Agent Browser to Fetch GitHub Starred Projects

## Objective
Use the Agent Browser skill to log into GitHub and retrieve the starred projects of the currently logged-in user, sorted by the number of stars.

## Execution Steps (Follow in Order)

1. **Launch Browser and Open GitHub Homepage**
   ```bash
   agent-browser --headed --profile "%HOMEPATH%\.agent-browser\chrome-win64\chrome-profiles\github" open https://github.com && agent-browser wait --load networkidle
   ```

2. **Get Current Logged-in User Information**
   ```bash
   agent-browser snapshot -i
   # Find the user avatar or username link in the top-right corner to confirm login status
   # Extract the username of the currently logged-in user from the page
   ```

3. **Navigate to Current User's Stars Tab**
   ```bash
   # Construct URL: https://github.com/{username}?tab=stars
   agent-browser open https://github.com/{username}?tab=stars && agent-browser wait --load networkidle
   ```

4. **Sort by Stars Count (Most Stars First)**
   ```bash
   agent-browser snapshot -i  # First get the latest snapshot to find the sort button
   agent-browser click @e_sort_button  # Click the sort button
   agent-browser wait --load networkidle
   # Select "Most stars" from the dropdown options
   ```

5. **Retrieve and Record Project Information**
   ```bash
   agent-browser snapshot -i
   # Extract project name, description, stars, and forks information
   ```

## Critical Notes

### 1. Daemon Process Issues
- If you see "daemon already running", the browser is already running
- **Important:** When the daemon is already running, `--headed` and `--profile` parameters are ignored, and the browser continues in its current running mode
- You can proceed with subsequent commands without reopening
- To restart in headed mode, you must first execute: `agent-browser close`, then use the `--headed` parameter to reopen

### 2. Dynamic Nature of References
- Element references (@e1, @e2, etc.) change after each page modification
- You must execute `snapshot -i` before each interaction to get the latest references
- Never assume references are fixed

### 3. Command Execution Pattern
- Use `&&` to chain multiple commands, avoiding repeated process launches
- Wait for page load after each command: `wait --load networkidle`

### 4. Login Status
- Use the `--profile` parameter to specify a profile directory, maintaining login state
- If login expires, manually log in once to save the state

### 5. Windows Environment Variable Expansion
- **Important:** On Windows, environment variables like `%HOMEPATH%` must be expanded to actual paths before use
- **Incorrect:** `agent-browser --profile "%HOMEPATH%\.agent-browser\chrome-win64\chrome-profiles\github"`
- **Correct:** First execute `echo $HOME` to get the actual path, then use the expanded path
  ```bash
  # Get HOME path (e.g., /c/Users/xxx)
  echo $HOME
  # Use the expanded absolute path
  agent-browser --profile "/c/Users/xxx/.agent-browser/chrome-win64/chrome-profiles/github" --headed open https://github.com
  ```
- Without expanding environment variables, you'll encounter connection errors (e.g., `os error 10060`)

### 6. Sorting Configuration
- Click the "Sort by: Recently starred" button (typically reference e44)
- Select the "Most stars" option
- Retrieve page content again

## Troubleshooting Common Issues

| Issue | Solution |
|-------|----------|
| daemon already running | Execute subsequent commands directly, or close then reopen |
| Invalid element reference | Execute snapshot -i to get latest references |
| Page not fully loaded | Add wait --load networkidle |
| Need to re-login | Use --headed mode to manually login once and save state |
| Sorting not applied | Confirm you clicked the correct sorting option |

## Result Output Format
- Project name and link
- Stars count (sorted in descending order)
- Forks count
- Project description (if available)
