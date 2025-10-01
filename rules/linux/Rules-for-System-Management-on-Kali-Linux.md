# Rules for System Management on Kali Linux

**Generated on:** October 1, 2025 at 11:48 AM CDT

---

## **Installation & Setup**
*   **Kali Linux Download (64-bit):** Download the 64-bit full Kali version if your system is 64-bit (do not use Light, Lxde, or other alternatives).
*   **Kali Linux Download (32-bit):** Install the 32-bit Kali version if your system has a 32-bit CPU.
*   **Kali Linux Download (ARM):** Download and install the ARM architecture version of Kali for Raspberry Pi, tablets, or other mobile devices.
*   **Virtual Machine RAM Allocation:** Do not allocate more than 25% of total system RAM to a VM.
    *   **VM RAM (4GB Host):** Allocate 1GB RAM for the VM if the host has 4GB RAM.
    *   **VM RAM (16GB Host):** Allocate 4GB (4096MB) RAM for the VM if the host has 16GB RAM.
*   **Virtual Machine Hard Drive Allocation:** Allocate a minimum of 20GB to 25GB hard drive space for the VM.
*   **Virtualization Software (Windows):** Disable competing virtualization software (e.g., Hyper-V) on Windows systems before installing Kali in VirtualBox.
*   **GRUB Installation (Kali VM):** Select "Enter device manually" when prompted to install the GRUB bootloader during Kali VM installation to avoid blank screen issues.
*   **Kali Login:** Log in to Kali using username 'kali' and password 'kali' (or your chosen password).

### **Windows Subsystem for Linux (WSL)**
*   **WSL Installation:** Enable WSL by running `Enable_windowsOptionalFeature -Online -FeatureName Microsoft-Subsystem-Linux` in PowerShell.
*   **Kali Tools Installation (WSL):** Install all Kali tools by running `sudo apt update && sudo apt upgrade -y && sudo apt install kali-linux-everything -y`.
*   **Ping Utility (WSL Kali):** Enable the ping utility by running `sudo setcap cap_net_raw+p /bin/ping`.

### **General Linux Usage**
*   **Filesystem Case Sensitivity:** The Linux filesystem is case-sensitive.
*   **Root User for Routine Tasks:** Do not log in as the root user for routine tasks.
*   **Regular User Login:** Log in as a regular user for starting regular applications, browsing the web, and running tools like Wireshark.
*   **Command Root Privileges:** Precede commands requiring root privileges with `sudo` if logged in as a regular user.
*   **Process Actions:** Any action on a process generally requires specifying its Process ID (PID).
*   **Service Installation:** Install the `at` utility using `sudo apt install at` before use.

### **Command Syntax & Options**
*   **`ls` Hidden Files:** Use the `-a` switch with `ls` to show hidden files.
*   **`ls` Multiple Flags:** Combine multiple `ls` flags into one (e.g., `-la` instead of `-l -a`).
*   **Command Options (Word vs. Letter):** Use a double dash (`--`) before word options (e.g., `--help`) and a single dash (`-`) before single-letter options (e.g., `-h`).
*   **`locate` Database Update:** Update the `locate` command database by running `sudo updatedb`.
*   **Piping Output:** Use the `|` command to pipe the output of one command as input to another.
*   **`cat` Interactive Exit:** Press `CTRL-D` to exit interactive mode and return to the prompt when creating a file with `cat`.
*   **`rmdir` Limitations:** The `rmdir` command cannot remove non-empty directories.
*   **`rmdir` Pre-removal:** Remove all contents from a directory before attempting to remove it with `rmdir`.
*   **`rm -r` (Recursive Delete):** Use `rm -r` to remove a directory and its contents recursively.
*   **`ifconfig` Network Modification:** Commands that modify network information with `ifconfig` require root privileges (use `sudo`).
*   **MAC Spoofing Procedure:** To spoof a MAC address, first take down the interface (`ifconfig <interface> down`), then set the new MAC (`ifconfig <interface> hw ether <MAC address>`), and finally bring the interface back up (`ifconfig <interface> up`).
*   **`apt search`:** Use `sudo apt search <keyword>` to search for available packages.
*   **`apt install`:** Use `sudo apt install <packagename>` to install software from the repository.
*   **`apt remove`:** Use `sudo apt remove <packagename>` to remove software.
*   **`apt purge`:** Use `sudo apt purge <packagename>` to remove software and its configuration files.
*   **`apt update`:** Use `sudo apt update` to update the list of available packages from repositories.
*   **`apt upgrade` (Permissions):** You must be logged in as root (or use `sudo`) to run `apt upgrade`.
*   **`git clone`:** Use `git clone <GitHub URL>` to download software from GitHub.
*   **`chmod` (Octal Notation):** Use `chmod <octal_digits> <filename>` to change file permissions.
*   **`chmod` (Symbolic UGO):** Use `chmod <user><operator><permission> <filename>` (e.g., `u+x`, `g-w`, `o=r`) to change file permissions symbolically.
*   **`umask` Value:** Use `umask` to view the current user file-creation mask.
*   **`ps aux`:** Do not prefix `aux` with a dash and ensure it is lowercase when using `ps aux`.
*   **`top` Interaction:** Press `H` or `?` for interactive commands in `top`, and `Q` to quit.
*   **`nice` Values:** `nice` values range from -20 (highest priority) to +19 (lowest priority).
*   **`nice` vs. `renice`:** `nice` increments the priority value, while `renice` sets an absolute priority value.
*   **`renice` Values:** `renice` accepts absolute values between -20 and 19.
*   **`renice` Argument:** `renice` requires a Process ID (PID) as an argument, not a process name.
*   **`renice` Permissions (Root):** Only the root user can set a negative `renice` value (higher priority). Any user can reduce priority (increase `renice` value).
*   **`top renice`:** In `top`, press `R` to change a process's nice value, then supply the PID and new nice value.
*   **`kill` Command:** Use `kill -<signal> <PID>` to send a signal to a process.
*   **`killall` Command:** Use `killall -<signal> <processname>` to kill a process by name.
*   **`top kill`:** In `top`, press `K` to terminate a process, then enter the PID.
*   **Background Process (`&`):** Append an ampersand (`&`) to the end of a command to run a process in the background.
*   **Background Process (`bg`):** Use `bg <PID>` to move a process to the background.
*   **Foreground Process (`fg`):** Use `fg <processname>` to move a background process to the foreground.
*   **`tar` Content List:** Use `tar -tvf <tarball>` to display files from a tarball without extracting them.
*   **`tar` Extract:** Use `tar -xvf <tarball>` to extract files from a tarball.
*   **`bzip2` Uncompress:** Use `bunzip2` to uncompress files compressed with `bzip2`.
*   **`fsck` Auto-repair:** Use `fsck -p <device>` to automatically repair filesystem errors.
*   **`journalctl` Priority Filter:** Use `journalctl -p <priority>` to filter logs by priority.
*   **`journalctl` Unit Filter:** Use `journalctl -u <service_name>` to view logs for a specific service.
*   **`journalctl` Quiet Flag:** Use `-q` flag with `journalctl` to suppress noisy messages and reduce activity traces.
*   **`journalctl` UID Filter:** Use `journalctl UID=<ID>` to filter logs by user ID.
*   **`journalctl` Vacuum:** Use `sudo journalctl -u <service> --vacuum-time=<duration>` to delete archived logs older than a specified duration for a service.
*   **`shred` Options:** Use `shred -f` to force permission changes for overwriting and `shred -n <count>` to specify overwrite count.
*   **`shred` Command Example:** Use `shred -f -n <count> <filepath_with_wildcard>` to shred multiple files forcefully with a specified overwrite count.
*   **`systemctl start`:** Use `sudo systemctl start <servicename>` to start a service.
*   **`systemctl stop`:** Use `sudo systemctl stop <servicename>` to stop a service.
*   **`airmon-ng`:** Use `sudo airmon-ng start|stop|check <interface>` to manage wireless monitor mode.
*   **`airodump-ng`:** Use `sudo airodump-ng <monitor_interface_name>` to capture and display wireless traffic data.
*   **`airodump-ng` Capture:** Use `sudo airodump-ng -c <channel> --bssid <AP_MAC> -w <output_file> <monitor_interface>` to capture packets for cracking.
*   **`aireplay-ng` Deauthentication:** Use `sudo aireplay-ng --deauth <count> -a <AP_MAC> -c <Client_MAC> <monitor_interface>` to deauthenticate clients.
*   **`aircrack-ng` Crack:** Use `sudo aircrack-ng -w <wordlist> -b <AP_MAC> <capture_file>` to crack Wi-Fi passwords.
*   **`l2ping`:** Use `sudo l2ping <MAC_address> -c <NumberOfPackets>` to ping Bluetooth devices.
*   **`sysctl` IP Forwarding (Temporary):** Enable IP forwarding temporarily with `sudo sysctl -w net.ipv4.ip_forward=1`.
*   **`sysctl -p`:** Run `sudo sysctl -p` after modifying `/etc/sysctl.conf` to apply changes.
*   **`modprobe` Add:** Use `modprobe -a <module_name>` to add a kernel module.
*   **`modprobe` Remove:** Use `sudo modprobe -r <module_name>` to remove a kernel module.
*   **Crontab (Time Fields):** Crontab time fields are (in order): minute (0-59), hour (0-23), day of month (1-31), month (1-12), day of week (0-7).
*   **Crontab (Numerical Time):** All time elements in crontab must be represented numerically.
*   **Crontab (Day of Week):** Day of week in crontab uses 0 or 7 for Sunday.
*   **Crontab (Multiple Values):** Separate multiple non-contiguous time values in crontab fields with commas (`,`).
*   **Crontab (Wildcard):** Use `*` as a wildcard to indicate "any" or "all" for a time field.
*   **Crontab (Multiple Dates):** Specify multiple days of the month by separating with commas (e.g., `15,30`).
*   **Crontab Edit:** Use `crontab -e` to edit the cron table.
*   **`update-rc.d`:** Use `update-rc.d <script_or_service_name> <action>` to manage services in `rc.d` scripts.
*   **`rcconf` Installation:** Install `rcconf` using `sudo apt install rcconf`.
*   **`pip3 install`:** Use `pip3 install <package_name>` to download and install Python modules.
*   **`pip3 show`:** Use `pip3 show <package_name>` to view information about an installed Python package.
*   **Python Manual Package Install:** Manually install Python packages by running `python3 setup.py install` after unpacking.
*   **Python Shebang:** Start Python 3 scripts with `#!/usr/bin/python3` to specify the interpreter.
*   **Python Object Method Call:** Call object methods using `object.method()`.

### **Configuration & System Management**
*   **File Permissions (General):** Every file must have a defined permission level.
*   **Permission Changes (Ownership):** Only the root user or a file's owner can change its permissions.
*   **New File Permissions:** Newly created files (e.g., bash scripts) are not executable by default.
*   **Bash Script Permissions:** Grant execute permissions (`chmod`) to Bash scripts before running them.
*   **SUID Bit Setting:** Set the SUID bit by adding a `4` prefix to the octal permissions (e.g., `chmod 4644 <filename>`).
*   **SGID Bit Setting:** Set the SGID bit by adding a `2` prefix to the octal permissions (e.g., `chmod 2644 <filename>`).
*   **`umask` Mechanism:** The `umask` value is subtracted from default file (666) or directory (777) permissions to determine final permissions.
*   **`umask` Change (Permanent):** Edit `/home/<username>/.profile` to permanently change a user's `umask` value.
*   **Environment Variable Scope:** Environment variable changes made without `export` are only valid for the current session.
*   **Permanent Variable Changes:** Use the `export` command to make environment variable changes permanent across sessions.
*   **`PS1` Export:** Export `PS1` variable to make shell prompt changes permanent across sessions.
*   **`PATH` Variable Constraint:** Commands outside directories listed in the `PATH` variable will not be found unless explicitly invoked with their full path.
*   **`PATH` Variable Separator:** Directories in the `PATH` variable must be separated by colons (`:`).
*   **`PATH` Variable Content Symbol:** Precede a variable name with `$` to access its content.
*   **`PATH` Assignment:** Do not directly assign a single directory to `PATH` as it will overwrite existing paths.
*   **`PATH` Modification:** Append to the `PATH` variable, do not replace it entirely.
*   **User-Defined Variables (Persistence):** Export user-defined variables to make them persist across new sessions.
*   **`unset` Variable Deletion:** Use `unset <variable_name>` to delete a variable.
*   **Crontab (Hour Format):** The crontab hour field uses a 24-hour clock.
*   **`update-rc.d` Changes (Reboot):** Reboot the system for `update-rc.d` changes to take effect.

### **Networking & Security**
*   **DHCP IP for Internet:** A DHCP-assigned IP is usually required to connect to the internet from a LAN.
*   **DNS Server Change (File):** Edit the `/etc/resolv.conf` plaintext file to change the DNS server.
*   **DNS Server Change (Permissions):** Editing `/etc/resolv.conf` requires root privileges (use `sudo`).
*   **DNS Server Change (via `echo`):** Use `sudo echo "nameserver <IP>" > /etc/resolv.conf` to change the DNS server from the command line.
*   **DNS Query Order:** The OS queries DNS servers in the order they appear in `/etc/resolv.conf`.
*   **DHCP DNS Override:** DHCP server settings will override manual `/etc/resolv.conf` entries upon DHCP address renewal.
*   **`/etc/hosts` Format:** Use a TAB character (not spacebar) to separate the IP address and domain name in `/etc/hosts`.
*   **Repository Usage:** Do not use testing, experimental, or unstable repositories in `/etc/apt/sources.list`.
*   **Repository Compatibility:** Ensure a repository is compatible with your system before adding it (e.g., Debian-based repos for Kali).
*   **Add Repository (File):** Add new repositories by editing the `/etc/apt/sources.list` file.
*   **Disable Logging (Journald):** Disable all logging by editing `/etc/system/journald.conf` and setting `Storage=null`.
*   **Disable Logging Procedure:** Uncomment `Storage=auto` in `/etc/system/journald.conf`, change it to `Storage=null`, save, and then restart `system-journald` using `sudo systemctl restart system-journald`.
*   **Apache Installation:** Install Apache using `sudo apt install apache2`.
*   **Apache Default Web Page Location:** Apache's default web page is located at `/var/www/html/index.html`.
*   **Customize Apache Default:** Overwrite the existing `/var/www/html/index.html` to customize the default web page.
*   **Service Restart (Config Changes):** Restart a service using `sudo systemctl restart <servicename>` after modifying its configuration file.
*   **Raspberry Pi SSH:** Enable SSH on Raspberry Pi OS according to its documentation (it's often off by default).
*   **Raspberry Pi Camera:** Attach the camera module to the dedicated camera port only when the Pi is off; never connect it to GPIO pins.
*   **Raspberry Pi Remote Control:** The Raspberry Pi must be connected to the local area network (LAN) for remote SSH control.
*   **Raspberry Pi Reboot (Camera):** Reboot the Raspberry Pi after configuring the camera for changes to take effect.
*   **MySQL Root Password:** Set a password for the MySQL/MariaDB root user immediately after the first login.
*   **MySQL Command Termination:** Terminate all MySQL commands with a semicolon (`;`).
*   **`SELECT` Command Requirements:** The `SELECT` command requires specifying the target table and columns.
*   **Wi-Fi Channels (US):** In the United States, Wi-Fi is limited to channels 1 to 11.
*   **Wi-Fi AP Power (US):** A Wi-Fi AP in the US must legally broadcast at an upper limit of 0.5 watts.
*   **Kali VM Wi-Fi:** An external USB Wi-Fi adapter is required for Wi-Fi functionality when running Kali in a VM.
*   **Wireless Monitor Mode:** Put the wireless network card into monitor mode before using `aircrack-ng` tools effectively.
*   **Wireless Interface Renaming:** Note the new name of the wireless interface after running `airmon-ng` as it will be renamed to `wlanXmon` (or similar).
*   **Wi-Fi Cracking Prerequisites:** Wi-Fi cracking requires the client MAC address, AP MAC address, operating channel, and a password list.
*   **Bluetooth Pairing:** Bluetooth devices can only pair if both are in discoverable mode.
*   **Bluetooth Adapter Verification:** Verify Bluetooth adapter recognition and enablement using `hciconfig` before scanning.
*   **`sysctl` Changes (Temporary):** `sysctl` changes are temporary and lost upon system reboot.
*   **`sysctl` Changes (Permanent):** Edit `/etc/sysctl.conf` to make `sysctl` changes permanent.
*   **`sysctl` Permanent IP Forwarding:** Uncomment `net.ipv4.ip_forward=1` in `/etc/sysctl.conf` to enable IP forwarding permanently.
*   **`insmod`/`rmmod` Caution:** Using `insmod` or `rmmod` without considering dependencies can leave the kernel unstable or unusable.

### **File & Storage Management**
*   **Mount Point:** A device's mount point must be an empty directory.
*   **`umount` Busy Device:** Cannot unmount a device that is currently in use.
*   **`fsck` Unmount Requirement:** Unmount a drive before running a filesystem check (`fsck`).
*   **`dd` for Daily Copying:** Do not use `dd` for typical day-to-day file copying due to its slow speed.
*   **`tar` Overwrite Behavior:** `tar -x` will overwrite existing files by default during extraction.

### **Programming & Scripting**
*   **Python Formatting:** Python code requires consistent indentation to define code blocks.
*   **Python Indentation Consistency:** Maintain consistent indentation levels within a code block for Python to recognize it.
*   **Python String Syntax:** Enclose string values in quotation marks in Python.
*   **Python Numbers in Strings:** Numbers within Python strings are treated as text and cannot be used in numerical calculations.
*   **Python Script Permissions:** Grant execute permissions (`chmod 755`) to Python scripts before running them.
*   **Execute Python Script:** Precede Python script names with `./` to execute them from the current directory if it's not in the PATH.
*   **Python Single-Line Comment:** Use the `#` symbol to designate single-line comments in Python.
*   **Python Multi-Line Comment:** Use three double quotation marks (`"""`) at the start and end for multi-line comments.
*   **Python List Indexing:** Python lists use 0-based indexing.
*   **Python Dictionary Syntax:** Create dictionaries using curly brackets `{}` with `key:value` pairs separated by commas.
*   **Python Control Block Syntax:** Control blocks must end with a colon (`:`) and be consistently indented.
*   **Python `while True` Loop:** Use `while True:` to run indented code indefinitely until the program is stopped.
*   **Python Exception Handling:** Use the `try/except` structure to handle errors or exceptions.
*   **Python String Strip:** Use the `strip()` function to remove leading/trailing newline characters (`\r\n`) from strings when iterating through file lines to avoid false negatives.
*   **TCP Client Target:** Create a target system (e.g., Metasploitable-2) on your network for TCP client scripts.

### **Artificial Intelligence (AI)**
*   **Cybersecurity & AI:** Cybersecurity professionals must adapt to and embrace AI technology.

## Key Highlights

* When installing Kali Linux in a VM, allocate no more than 25% of total system RAM and at least 20-25GB of hard drive space; during GRUB installation, select "Enter device manually" to prevent blank screen issues.
* Always log in as a regular user for routine tasks, using `sudo` for root privileges, and remember that the Linux filesystem is case-sensitive; newly created scripts require explicit execute permissions via `chmod`.
* Utilize `sudo apt update` to refresh package lists, `sudo apt install` to add software, and `sudo apt remove` or `sudo apt purge` to uninstall packages from your system.
* An external USB Wi-Fi adapter is crucial for Wi-Fi functionality in a Kali VM, and the wireless card must be put into monitor mode before using `aircrack-ng` tools effectively.
* Ensure permanent system changes for environment variables (e.g., `PATH`), `sysctl` settings, or `umask` values by editing relevant configuration files and applying them, as command-line changes are often temporary.
* After modifying a service's configuration file, always restart the service using `sudo systemctl restart <servicename>` for the changes to take effect.
* Manage process priority using `nice` or `renice <PID>` (with values from -20 to +19, where only root can set negative values), and terminate processes with `kill -<signal> <PID>` or `killall -<signal> <processname>`.
* Python scripts demand consistent indentation for code blocks, require execute permissions (`chmod 755`) to run, and should implement `try/except` for robust error handling.

## Example ideas

* Consolidate and formalize all security-related rules (e.g., root usage, permissions, MySQL password, repository safety) into a mandatory 'Kali Linux Security Best Practices' guide for all users.
* Develop practical guidelines for virtual machine resource allocation and system process management (nice/renice, journalctl vacuum) to optimize performance and prevent resource exhaustion.
* Create hands-on lab exercises or simulated scenarios that require users to apply multiple technical rules and commands from the summary for common tasks like network scanning, file manipulation, and service management.
* Investigate specific AI/ML tools or methodologies that can automate or enhance the effectiveness of the cybersecurity tasks mentioned (e.g., intelligent log analysis, predictive anomaly detection, advanced penetration testing).
