# Rules for Ubuntu System Management, Development, and Operations

This document synthesizes technical rules, requirements, and constraints across various aspects of Ubuntu system management, development, and enterprise operations. Adherence to these guidelines ensures system stability, security, and effective collaboration.

**Generated on:** October 1, 2025 at 9:54 AM CDT

---

## I. General System Administration & Best Practices

* **Rule:** Properly configure and manage Ubuntu systems with attention to detail and repeatability.
* **Rule:** Implement effective system monitoring for all Ubuntu systems.
* **Rule:** Perform comprehensive software package management (installing, updating, removing) across all Ubuntu systems.
* **Rule:** Refresh the package cache using `sudo apt update` after adding a new APT repository.

## II. Community Engagement & Contribution

* **Rule:** Adhere to the Ubuntu Code of Conduct and general community guidelines and etiquette.
* **Rule:** Treat other contributors with kindness and respect.
* **Rule:** Communicate effectively using clear, concise, and unambiguous language when engaging with the community, reporting issues, or submitting contributions.
* **Rule:** When asking questions or reporting issues:
  * Provide clear, concise, and unambiguous problem statements.
  * Include essential details and context.
  * Share relevant system information, such as the Ubuntu version (from `/etc/os-release`), specific software and its version, error messages, and any recent system changes.
  * Provide detailed, step-by-step instructions to reproduce the issue.
  * Demonstrate prior attempts to solve the problem.
  * Include a courteous closing.
* **Rule:** Use `ubuntu-bug <packagename>` to report bugs when the Ubuntu package name is known, or `ubuntu-bug` (without arguments) for guided reporting.
* **Rule:** When contributing code to open source projects:
  * Fork the repository.
  * Clone your forked repository.
  * Create a dedicated branch for your changes.
  * Commit changes with clear and descriptive messages.
  * Push changes to your forked repository.
  * Submit a pull request to project maintainers for review.
  * Be patient for contributions to be reviewed and accepted.
  * Embrace feedback to improve your skills.
  * *Recommendation:* Mentor new contributors as your skills grow.
  * *Note:* Complex code is not required for open source contributions.

## III. System Security

### A. Updates & Vulnerability Management

* **Rule:** Routinely update your system with the latest security patches and essential security updates promptly.
* **Rule:** Enable automatic installation of security updates for non-Snap packages by setting "When there are security updates" to "Download and install automatically" in Software & Updates.
* **Note:** Snap packages automatically update without additional user steps.
* **Rule:** Carefully consider any software before installing it to protect against threats.

### B. Firewall Management

* **Rule:** Enable and keep the UFW (Uncomplicated Firewall) active to restrict network traffic and limit system exposure.
  * Use `sudo ufw enable` to enable UFW.
  * Use `sudo ufw status` to check UFW status.
* **Rule:** Understand that UFW's default policies deny incoming and allow outgoing connections.
* **Rule:** When creating custom firewall rules:
  * Choose a direction (Incoming or Outgoing).
  * Specify the protocol (TCP, UDP, or any).
  * Specify a specific port number or select an application from the predefined list.
  * Set the action (allow or deny).
  * *Example:* `sudo ufw allow <port>/<protocol>` or `sudo ufw deny <port>/<protocol>`.
  * *Example:* `sudo ufw allow from <IP_address> to any port <port_number>`.
* **Rule:** Test network connectivity after adding new firewall rules.
* **Rule:** Document all custom firewall rules.
* *Recommendation:* Start firewall configuration with a predefined profile and gradually add custom rules.
* *Recommendation:* Use `iptables` for advanced control (e.g., NAT, port forwarding) when UFW is insufficient.
  * *Example (Block IP):* `sudo iptables -A INPUT -s <IP_address> -j DROP`.
  * *Example (Port Forwarding):* `sudo iptables -t nat -A PREROUTING -p tcp --dport <external_port> -j DNAT --to-destination <internal_IP>:<internal_port>`.

### C. Data Encryption

* **Rule:** Prioritize safeguarding data by using encryption.
* **Rule:** Comply with industry and organizational data protection regulations and standards that require full disk encryption.
* **Rule:** Always back up data before performing encryption operations (e.g., full disk, USB, home directory).
* **Rule:** Be aware that forgetting an encryption passphrase (LUKS, ZFS, USB, eCryptfs) will result in irreversible data loss.
* *Recommendation:* Use LUKS (Linux Unified Key Setup) for full disk encryption due to its maturity and reliability if comprehensive system protection is needed.

#### LUKS Full Disk Encryption

* **Rule:** Select the "Use LVM and encryption" option during Ubuntu installation for LUKS full disk encryption.
* **Rule:** Choose a strong and unique passphrase for disk encryption.
* **Rule:** Store your LUKS passphrase in a secure location.
* **Rule:** The correct LUKS passphrase must be provided during system startup to access encrypted data.

#### TPM-backed Full Disk Encryption (Experimental)

* **Rule:** Exercise caution and ensure data backups when using experimental TPM-backed encryption.
* **Rule:** To use TPM-backed encryption, your computer must have a compatible TPM chip enabled in BIOS settings, and Secure Boot must be enabled.
* **Rule:** Select the "Enable hardware-backed full disk encryption" option during installation.
* **Rule:** Back up the TPM recovery key using `sudo snap recovery --show-keys` after installation.
* *Recommendation:* Clear the TPM in BIOS if the TPM-backed encryption option is unavailable despite meeting requirements.

#### ZFS with Full Disk Encryption (Experimental)

* **Rule:** Be aware that ZFS with full disk encryption is an experimental feature and may contain bugs.
* **Rule:** Ensure sufficient RAM and CPU power when using ZFS due to its resource intensiveness.
* **Rule:** Store your ZFS passphrase securely.

#### eCryptfs Home Directory Encryption

* **Rule:** Remember that eCryptfs only encrypts the home directory, leaving other system parts unencrypted.
* **Rule:** Home directory data cannot be migrated for a user account with an active logged-in session; create a temporary administrative user account to perform the migration.
  * Use `sudo apt install ecryptfs-utils cryptsetup` to install utilities.
  * Use `sudo ecryptfs-migrate-home -u USERNAME` to encrypt a home directory.
* **Rule:** The eCryptfs passphrase is required at each login to access the encrypted home directory.
* **Rule:** Reboot the computer to complete the eCryptfs home directory encryption process.
* **Note:** eCryptfs may cause a slight performance decrease, especially with large or frequently accessed files.

#### USB Device Encryption (LUKS)

* **Rule:** Identify the correct USB stick in the Disks utility before proceeding.
* **Rule:** Unmount the USB stick before formatting or encrypting it.
* **Rule:** Choose "Internal disk For use with Linux systems only (Ext4)" and check "Password protect volume (LUKS)" when formatting a USB stick for encryption.
* **Rule:** Enter and confirm a strong and unique passphrase for USB stick encryption.
* **Rule:** Wait for the formatting and encryption process to complete.

### D. Password & Physical Security

* **Rule:** Choose strong, unique, and complex passwords for all accounts, including the Ubuntu system's user account.
* **Rule:** Passwords must be at least 12 characters and include a mix of uppercase and lowercase letters, numbers, and symbols.
* **Rule:** Avoid reusing passwords across different accounts.
* **Rule:** Change passwords periodically.
* *Recommendation:* Consider using a password manager for all passphrases.
* **Rule:** Ensure your screen is locked when unattended.
* **Rule:** Require a password to unlock after suspend or when the screen blanks due to inactivity (e.g., "Automatic Screen Lock," "Lock Screen on Suspend" settings).

### E. SSH Security

* **Rule:** Disable password authentication for SSH.
  * To disable, add `PasswordAuthentication no` to a configuration file (e.g., `/etc/ssh/sshd_config.d/disable-passwd.conf`) using `echo "PasswordAuthentication no" | sudo tee -a /etc/ssh/sshd_config.d/disable-passwd.conf`.
* **Rule:** Use public key authentication for SSH.
* **Rule:** Restart the SSH service (`sudo systemctl restart ssh`) after making configuration changes.
* **Rule:** If password authentication *must* be enabled, use strong and unique passphrases.
* **Note:** After disabling password authentication, remote SSH login is only possible with SSH key-based authentication.
* **Rule:** Install the `openssh-server` package to enable the SSH server on Ubuntu Desktop.

### F. Network Monitoring & Malware Detection

* **Rule:** Regularly monitor system network connections using the `ss` command.
* **Rule:** Investigate any unfamiliar or unexpected listening ports.
* **Rule:** Pay attention to connections from unknown or suspicious IP addresses identified by `ss`.
* **Rule:** Regularly scan systems with `chkrootkit` as a proactive security measure.
  * Install using `sudo apt install chkrootkit`.
  * Initiate a default scan using `sudo chkrootkit`.
* **Rule:** Keep `chkrootkit` updated to ensure it has the latest signatures.
* **Rule:** Always investigate `chkrootkit` findings further before taking action, due to potential false positives.
* **Note:** `chkrootkit` requires root privileges for effective scanning.

## IV. Enterprise Management & Tooling

### A. General Enterprise Environment

* **Rule:** When adding an operating system to an enterprise environment, ensure identity management, provisioning, and security are comprehensively addressed.
* **Rule:** Properly configure and manage Ubuntu systems with attention to detail and repeatability.
* **Rule:** Regularly audit Ubuntu systems.
* **Rule:** Generate compliance reports for Ubuntu systems as required.

### B. Landscape Management

* **Rule:** A device must be attached to an Ubuntu Pro subscription to enable Landscape support.
  * Enable using `sudo pro enable landscape`.
  * Install the client using `sudo apt install landscape-client`.
* **Rule:** Assign roles and permissions to users within Landscape using Role-Based Access Control (RBAC).
* **Rule:** Configure `/etc/landscape/client.conf` with the correct `url`, `ping_url`, `computer_title`, `account_name`, `include_manager_plugins`, and `script_users` for your Landscape instance.
* **Rule:** Restart the `landscape-client` service using `sudo service landscape-client restart` after modifying `/etc/landscape/client.conf` to enroll with new settings.
* **Rule:** Register with Landscape using `sudo landscape-config` if not already registered, and verify registration status with `sudo landscape-config --is-registered`.
* **Note:** Landscape scripts will run on selected systems when they are online.

### C. `authd` Identity Integration

* **Rule:** For Ubuntu 24.04, enable the `ppa:ubuntu-enterprise-desktop/authd` APT repository for `authd` packages. This repository is not required for Ubuntu 26.04 and beyond.
  * Add repository: `sudo add-apt-repository ppa:ubuntu-enterprise-desktop/authd`.
  * Install: `sudo apt install authd gnome-shell yaru-theme-gnome-shell`.
* **Rule:** Install the appropriate identity broker:
  * For Microsoft Entra ID: `sudo snap install authd-msentraid`.
  * For Google IAM: `sudo snap install authd-google`.
* **Rule:** Create the broker configuration directory using `sudo mkdir -p /etc/authd/brokers.d/`.
* **Rule:** Copy the broker configuration file to the `/etc/authd/brokers.d/` directory.
  * For Microsoft Entra ID: `sudo cp /snap/authd-msentraid/current/conf/authd/msentraid.conf /etc/authd/brokers.d/`.
  * For Google IAM: `sudo cp /snap/authd-google/current/conf/authd/google.conf /etc/authd/brokers.d/`.
* **Rule:** Configure the `issuer` ID, `client_id`, and `client_secret` in the respective `broker.conf` files (`/var/snap/authd-msentraid/current/broker.conf` for Microsoft Entra ID; `/var/snap/authd-google/current/broker.conf` for Google IAM).
* **Rule:** Set `allowed_users` in `broker.conf`.
* **Rule:** Optionally set `owner` in `broker.conf`; if not explicitly set, the first successful login user becomes the owner.
* **Rule:** Replace `YOUR_CLIENT_ID`, `YOUR_ISSUER_ID`, and `YOUR_CLIENT_SECRET` placeholders with actual values in configuration scripts.
* **Rule:** Reboot the system after completing `authd` configuration, including ensuring a `reboot` command is present at the end of `authd` configuration scripts deployed via Landscape.

## V. Software Development Environment

### A. Core Setup & Practices

* **Rule:** Install `build-essential` as a first step for development on Ubuntu using `sudo apt install build-essential`.
* **Rule:** Install Git for version control using `sudo apt install git`.
* **Rule:** Configure Git user name and email globally:
  * `git config --global user.name "Your Name"`
  * `git config --global user.email "your.email@example.com"`
* **Rule:** Use `venv` to create isolated Python virtual environments to prevent dependency conflicts and ensure organization.
  * Create: `python3 -m venv <environment_name>`.
  * Activate: `source <environment_name>/bin/activate`.
* **Rule:** Use static code analysis tools (e.g., `cppcheck` via `sudo apt install cppcheck`, `pylint` via `sudo apt install pylint`) to identify potential code issues before runtime.
* **Rule:** Consider using debugging and profiling tools (e.g., GDB via `sudo apt install gdb`, Valgrind via `sudo apt install valgrind`).

### B. Open Source Contributions

*This section refers back to II. Community Engagement & Contribution for detailed rules on code contributions.*

## VI. Virtualization & Containerization

### A. LXD Container Management

* **Rule:** Install LXD using `sudo snap install lxd`.
* **Rule:** Add your user account to the `lxd` group using `sudo usermod -aG lxd "$USER"`.
* **Rule:** Activate `lxd` group membership in the current session using `newgrp lxd`.
* **Rule:** Initialize LXD. Consider interactive initialization to configure storage backend, network, and image remotes, or use `lxd init --auto` for recommended settings.
* **Rule:** Ensure robust isolation through kernel namespaces and advanced security features when using LXD for development.
* **Rule:** The `lxc launch` command **must** include an image source and a container name as arguments.
  * **Syntax:** `lxc launch <image-source> <container-name>`
* **Rule:** Map your host UID to the container's default `ubuntu` user UID (1000) for host file access when running as an ordinary user in LXD.
  * **Syntax for UID mapping:** `lxc launch <image-source> <container-name> -c raw.idmap="both $UID <container-user-uid>"`
* **Rule:** Manage LXD containers using `lxc` commands:
  * List containers: `lxc list`.
  * Start/Stop/Restart containers: `lxc start/stop/restart <container_name>`.
  * Execute commands inside a container: `lxc exec <container_name> -- <command>`.
    * **Syntax (shell):** `lxc exec <container-name> -- <shell-command>`
    * **Syntax (specific user):** `lxc exec <container-name> -- su -l <username>`
  * Transfer files: `lxc file push/pull`.
  * Manage images: `lxc image list/import/export`.
  * Modify container configurations: `lxc config edit <container-name>`.
  * Move container instances: `lxc move`.
  * Mount host directories: `lxc config device add <container-name> homedir disk source=$HOME path=/home/<container-user>`.
* **Rule:** Use `exit` or `Ctrl + D` to exit an LXD container shell.
* **Rule:** Use LXD snapshots to capture and revert development environment states.
* **Rule:** Employ clear and descriptive names for LXD containers and images.
* **Rule:** Use labels and tags to categorize and manage LXD containers effectively.
* **Rule:** Update LXD container images regularly.
* **Rule:** Utilize LXD profiles to encapsulate common configurations and devices.
* **Rule:** Monitor LXD container resource usage (CPU, memory, disk I/O).
* **Rule:** Implement robust backup and disaster recovery strategies for LXD, including regular backups of container images and data.
* **Rule:** Fine-tune LXD container settings to optimize performance for specific development needs.
* **Rule:** Use unprivileged containers and secure image management for sensitive LXD development projects.
* **Rule:** To enable LXD web UI:
  * Enable the UI: `sudo snap set lxd ui.enable=true`.
  * Restart service: `sudo snap restart lxd`.
  * Configure HTTPS address: `lxc config set core.https_address :8443`.
  * Add client certificate's public key to trust store: `lxc config trust add <certificate-path>`.
* **Rule:** Configure a proxy device for secure LXD connections, especially over untrusted networks.

### B. Multipass VM Management

* **Rule:** Install Multipass on Ubuntu using `sudo snap install multipass`.
* **Rule:** Launch an Ubuntu instance, optionally specifying the latest LTS release using `multipass launch`.
* **Rule:** Assign a specific name to a Multipass instance using the `--name` option.
* **Rule:** Allocate CPU cores and memory to a Multipass instance using `--cpus` and `--mem` options respectively.
* **Rule:** Use a cloud-init configuration file for automated setup with the `--cloud-init` option.
* **Rule:** Multipass instance resource settings (CPU, memory, disk size) **must** only be changed while the instance is stopped.
* **Rule:** Interact with Multipass VMs using `multipass` commands:
  * Open a shell session: `multipass shell <instance-name>`.
  * Execute a command: `multipass exec <instance-name> -- <command>`.
  * Copy files: `multipass transfer <instance-name>:<remote-path> <local-path>` or `multipass transfer <local-path> <instance-name>:<remote-path>`.

## VII. Orchestration & Data Science

### A. MicroK8s Configuration & Usage

* **Rule:** Install MicroK8s on Ubuntu using `sudo snap install microk8s --classic`.
* **Rule:** Add the current user to the `microk8s` group using `sudo usermod -a -G microk8s $USER`.
* **Rule:** Activate the new `microk8s` group membership using `newgrp microk8s`.
* **Rule:** Check MicroK8s cluster status and wait for it to be ready using `microk8s status --wait-ready`.
* **Rule:** Configure `kubectl` to interact with MicroK8s by setting its config file: `microk8s kubectl config view --raw > $HOME/.kube/config`.
* **Rule:** Deploy an application to MicroK8s using `microk8s kubectl apply -f <yaml-file-or-URL>`.
* **Rule:** Use `kubectl port-forward <service-type>/<service-name> <local-port>:<container-port>` for port forwarding to MicroK8s services.
* **Rule:** Enable MicroK8s add-ons as needed:
  * DNS: `microk8s enable dns`.
  * Hostpath-storage: `sudo microk8s enable hostpath-storage`.
  * Rook storage: `microk8s enable rook`.
  * Ingress controller: `microk8s enable ingress`.
  * Istio: `microk8s enable istio`.
  * Knative: `microk8s enable knative`.
  * Private container registry: `microk8s enable registry`.
  * Metrics server: `microk8s enable metrics-server`.
  * Dashboard: `microk8s enable dashboard` (access info with `microk8s dashboard-proxy`).

### B. Data Science Stack (DSS)

* **Rule:** Install MicroK8s as part of DSS using `sudo snap install --classic microk8s`.
* **Rule:** Enable essential MicroK8s add-ons for DSS: `hostpath-storage`, `dns`, and `rbac`.
  * `sudo microk8s enable hostpath-storage`
  * `sudo microk8s enable dns`
  * `sudo microk8s enable rbac`
* **Rule:** Install the Data Science Stack using `sudo snap install data-science-stack`.
* **Rule:** Enable the NVIDIA GPU operator for MicroK8s using `sudo microk8s enable nvidia` if GPU acceleration is required.
* **Rule:** Initialize DSS with the local MicroK8s configuration using `dss initialize --kubeconfig "$(sudo microk8s config)"`.
* **Rule:** Launch a Jupyter Notebook container with DSS using `dss create <notebook-name> --image=<image-name>`.
* **Rule:** Check the current status of DSS, including MLFlow URL and GPU acceleration, using `dss status`.

## VIII. Constraints & Notes

* **Constraint:** Prior experience with Kubernetes concepts is assumed for MicroK8s usage.
* **Constraint:** Prior experience with standard data science tools is assumed for Data Science Stack (DSS) usage.
* **Note:** The `ppa:ubuntu-enterprise-desktop/authd` APT repository is specifically for Ubuntu 24.04 and will not be required for `authd` packages on Ubuntu 26.04 and beyond.
* **Note:** `Landscape scripts` will run on selected systems when they are online.
* **Note:** `Complex code is not required for open source contributions`.

## Key Highlights

* Adherence to these guidelines ensures system stability, security, and effective collaboration across Ubuntu system management, development, and enterprise operations.
* Routinely update your system with the latest security patches and enable the Uncomplicated Firewall (UFW) to restrict network traffic, which are fundamental practices for system security.
* Prioritize safeguarding data by using encryption methods like LUKS for full disk or eCryptfs for home directories, always backing up data before encryption operations.
* Implement strong, unique passwords for all accounts and disable password authentication for SSH in favor of public key authentication to enhance system access security.
* For effective community engagement and issue reporting, provide clear, concise problem statements, include essential system details, and detailed reproduction steps.
* Developers should use `venv` for isolated Python virtual environments to manage dependencies and install `build-essential` and Git for core setup and version control.
* For enterprise environments, ensure comprehensive identity management, provisioning, and security, utilizing tools like Landscape for system management and `authd` for identity integration.
* Leverage virtualization and containerization tools like LXD and Multipass to create robust, isolated development environments and manage virtual machines efficiently.
* Install and configure MicroK8s to deploy and manage applications in a local Kubernetes cluster, enabling scalable orchestration for development and data science needs.

## Example Ideas

* Standardize configuration management practices for Ubuntu systems across the enterprise to ensure repeatability, automate provisioning, and facilitate consistent compliance auditing.
* Develop a formal evaluation process and readiness criteria for deploying experimental security features, specifically TPM-backed and ZFS full disk encryption, into production environments.
* Design and implement an integrated, automated security monitoring and alerting solution to proactively detect network anomalies, manage firewall rules, and efficiently handle findings from tools like chkrootkit, minimizing false positives.
* Create a strategic roadmap for the `authd` identity integration, focusing on secure credential management for `client_id` and `client_secret`, and planning for seamless migration to future Ubuntu releases (26.04+) where the dedicated PPA may no longer be required.
