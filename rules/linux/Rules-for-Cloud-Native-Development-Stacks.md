# Rules for Cloud-Native Development Stacks

This document synthesizes the core technical rules, syntax requirements, and constraints for setting up and operating various cloud-native development tools, including LXD, Multipass, MicroK8s, and the Data Science Stack. Adherence to these rules ensures proper system functionality, security, and maintainability.

**Generated on:** October 1, 2025 at 9:24 AM CDT

---

## I. General System Operations & Prerequisites

1.  A system reboot is required for new drivers to become active after installation.
2.  MicroK8s must be installed and configured as a prerequisite for the Data Science Stack.

## II. Installation & Initial Setup

1.  Install necessary tools (LXD, Multipass, MicroK8s, Data Science Stack) using the `snap` package manager (e.g., `sudo snap install <package_name>`).
    *   For MicroK8s, install with the `--classic` flag (`sudo snap install microk8s --classic`).
2.  Add your user account to the respective tool's system group (e.g., `lxd`, `microk8s`) using `sudo usermod -aG <group_name> "$USER"`.
3.  Activate new group memberships using `newgrp <group_name>` immediately after adding your user.
4.  Initialize LXD with recommended settings using `lxd init --auto`.
5.  Verify MicroK8s cluster status and readiness using `microk8s status --wait-ready`.
6.  Configure `kubectl` to interact with MicroK8s by redirecting its configuration to `$HOME/.kube/config`.
7.  Initialize the Data Science Stack with the local MicroK8s configuration using `dss initialize --kubeconfig "$(sudo microk8s config)"`.

## III. Configuration & Customization

1.  Enable the LXD web-based UI feature using `sudo snap set lxd ui.enable=true` and restart the LXD service using `sudo snap restart lxd`.
2.  Configure LXD's core HTTPS address for UI access using `lxc config set core.https_address :8443`.
3.  Add the public key of the client certificate to the LXD server's trust store using `lxc config trust add <certificate-path>`.
4.  When launching an LXD container to map the host user's UID to the container's default Ubuntu user (UID 1000), use the configuration option `-c raw.idmap="both $UID 1000"`.
5.  Mount a host directory into an LXD container using `lxc config device add <container_name> <device_name> disk source=<host_path> path=<container_path>`.
6.  Use a cloud-init configuration file for automated Multipass instance setup using the `--cloud-init` option.
7.  Enable required MicroK8s add-ons, such as `hostpath-storage`, `dns`, `rbac`, and optionally `nvidia` for GPU support, using `sudo microk8s enable <addon_name>`.
8.  Modify LXD container configurations using `lxc config edit`.
9.  Utilize LXD profiles to encapsulate common configurations and devices, simplifying container creation and management.

## IV. Lifecycle Management

1.  Create new LXD containers from an image using `lxc launch <image_source> <container_name>`.
2.  Manage LXD container lifecycle (start, stop, restart) using `lxc start`, `lxc stop`, or `lxc restart`.
3.  Move LXD container instances within or between LXD servers using `lxc move`.
4.  Manage LXD container images (list, import, export) using `lxc image list`, `lxc image import`, or `lxc image export`.
5.  Deploy applications to MicroK8s using `microk8s kubectl apply -f <manifest_file_or_URL>`.
6.  Launch a Jupyter Notebook server for the Data Science Stack using `dss create <notebook_name> --image=<image_name>`.

## V. Interaction & Access

1.  Display running LXD containers using `lxc list`.
2.  Execute commands within LXD containers or Multipass instances using `lxc exec <container_name> <command>` or `multipass exec <instance_name> -- <command>`.
3.  Access an LXD container or Multipass instance shell using `lxc exec <container_name> bash` or `multipass shell <instance_name>`.
4.  Exit an LXD container shell using the `exit` command or `Ctrl + D`.
5.  Transfer files between the host and LXD containers or Multipass VMs using `lxc file push/pull` or `multipass transfer <source> <destination>`.
6.  Access MicroK8s services via port forwarding using `kubectl port-forward service/<service_name> <local_port>:<container_port>`.
7.  Get MicroK8s dashboard access information (URL, token) using `microk8s dashboard-proxy`.
8.  Check the current status of the Data Science Stack, including MLFlow URLs, using `dss status`.

## VI. Constraints & Resource Management

1.  The `lxc launch` command requires at least two arguments: the image source and a container name.
2.  Assign a specific name to a Multipass instance using the `--name` option during creation.
3.  Allocate CPU cores and memory to a Multipass instance using `--cpus` and `--mem` options during creation.
4.  Multipass VM instance resource settings (CPU, memory, disk size) can only be changed while the instance is stopped.

## VII. Best Practices & Guidelines

1.  Employ clear and descriptive names for LXD containers and images to improve organization and clarity.
2.  Use labels and tags to categorize and manage LXD containers effectively.
3.  Update LXD container images regularly to take advantage of the latest security patches, bug fixes, and performance improvements.
4.  Monitor LXD container resource usage (CPU, memory, disk I/O) to identify potential performance bottlenecks and optimize resource allocation.
5.  Implement robust backup and disaster recovery strategies for LXD development work, including regular backups of container images and data.
6.  Fine-tune LXD container settings to optimize performance for specific development needs.

## Key Highlights

* MicroK8s must be installed and configured as a prerequisite for the Data Science Stack, and a system reboot is required for new drivers to become active after installation.
* Install necessary cloud-native tools using the `snap` package manager and ensure your user is added to the relevant system groups (e.g., `lxd`, `microk8s`), activating group memberships immediately with `newgrp`.
* After installation, initialize LXD with `lxd init --auto`, verify MicroK8s cluster status with `microk8s status --wait-ready`, and configure `kubectl` to interact with MicroK8s.
* Enable essential MicroK8s add-ons like `hostpath-storage`, `dns`, `rbac`, and optionally `nvidia` for GPU support, while also enabling and configuring the LXD web-based UI for management.
* For data sharing, mount host directories into LXD containers, and for proper user permissions, map host user UIDs to container users using the `-c raw.idmap` configuration.
* Enhance automation using cloud-init for Multipass instance setup and leverage LXD profiles to encapsulate common configurations, streamlining container creation and management.
* Note that Multipass VM instance resource settings for CPU, memory, and disk size can only be changed when the instance is stopped.
* Prioritize regular updates for LXD container images to incorporate security patches and performance improvements, and implement robust backup and disaster recovery strategies for all development work.
* Interact with containers and VMs by executing commands via `lxc exec` or `multipass exec`, and transfer files between host and instances using `lxc file push/pull` or `multipass transfer`.

## Example Ideas

* Develop comprehensive automation scripts or templates for the entire stack's initial setup and configuration (LXD, Multipass, MicroK8s, Data Science Stack) to streamline developer onboarding and ensure consistent environments.
* Conduct a security audit and develop hardening guidelines for the integrated cloud-native stack, focusing on network isolation, access control, and secure configuration across LXD, Multipass, and MicroK8s.
* Establish performance baselines and define optimization strategies for common workloads running on the integrated LXD, Multipass, and MicroK8s components, including resource allocation, storage, and network tuning.
* Investigate and prototype advanced lifecycle management and orchestration approaches for complex applications spanning multiple LXD containers, Multipass VMs, and MicroK8s deployments, potentially leveraging CI/CD integration.
* Implement a centralized logging and monitoring solution to provide holistic visibility into the health, performance, and operational status of all components (LXD, Multipass, MicroK8s, Data Science Stack) and deployed applications.
