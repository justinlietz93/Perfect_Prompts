# Rules for Systemd, Network, and Security Configuration

This document synthesizes core technical rules for configuring and managing systemd services, network resolution, and firewall settings. Adherence to these rules ensures stability, security, and maintainability across system deployments.

**Generated on:** October 1, 2025 at 10:49 AM CDT

---

## Systemd Unit File Structure and Syntax

* Comments in unit files must start with a pound sign (`#`).
* Section names in unit files must be enclosed in square brackets (e.g., `[Unit]`).
* The `[Service]` section must define the service type and the fully qualified path to the program.
* The `[Install]` section must specify the target unit that will trigger the service unit.
* To display service output on both the journal and console, include `StandardOutput=journal+console` in the `[Service]` section.
* Service unit files must not be executable.
* Service unit files must have user and group ownership by `root`.
* Service unit files must have `754` permissions.
* Most `systemd` unit files reside in `/usr/lib/systemd/system/`.
* Custom `systemd` unit files must be placed in `/usr/local/lib/systemd/system/` for FHS compliance.
* Modify `systemd` unit files using local changes, typically via `systemctl edit <unit>` to create an override file in `/etc/systemd/system/<unit>.d/override.conf`.

## Systemd Service Unit Types

* **Type=simple**: Systemd must consider the unit started immediately after the program begins execution.
* **Type=exec**: Systemd must consider the unit started immediately after the main service binary has been executed. The service manager must delay starting of follow-up units until the main service binary has been executed. `systemctl start` commands for `exec` services must report failure if the service's binary cannot be invoked successfully.
* **Type=forking**: Do not use `Type=forking`. Consider `Type=notify`, `Type=notify-reload`, or `Type=dbus` instead. If `Type=forking` is used, Systemd must consider the unit started immediately after the binary forked by the manager exits.
* **Type=oneshot**: Systemd must consider the unit up after the main process exits. The service manager must start follow-up units only after the main process exits.
* **Type=dbus**: The unit file must specify the `BusName=`. Systemd must consider the unit up when the specified bus name has been acquired.
* **Type=notify**: The service must send a "READY=1" notification message via `sd_notify(3)` or an equivalent call when it has finished starting up. Systemd must proceed with starting follow-up units only after the "READY=1" notification message has been sent.
* **Type=notify-reload**: The `SIGHUP` UNIX process signal must be sent to the service's main process when the service is asked to reload. The manager must wait for a notification about the reload finishing.
* **Type=idle**: Actual execution of the service program must be delayed until all active jobs are dispatched. Do not use `Type=idle` as a general unit ordering tool.

## Systemd Service Management and Startup Ordering

* All software that runs as a daemon should be managed by `systemd`.
* Execute `systemctl daemon-reload` after changing a unit file or creating a new one.
* To enable a service to start at boot, use `systemctl enable <unit>`.
* To enable a service at boot and start it immediately for the current session, add the `--now` option to `systemctl enable`.
* To ensure a unit starts in a specific order, configure the new unit with both `Wants=` and `After=` directives for its dependencies.
* To ensure a service starts after the network is online, add `After=network-online.target` and `Wants=network-online.target` to its `[Unit]` section.
* Do not rely solely on `WantedBy=multi-user.target` or `WantedBy=graphical.target` to define a unit's specific place in the startup sequence; these directives only determine if a unit starts as part of that target.
* Do not use `network.target` for sequencing services during startup, as it is used during shutdown.
* For a fully operational network, ensure `network-online.target` is reached.
* To replace `rc.local` functionality, create a single `systemd` service unit that launches a Bash script containing the required commands.

## Systemd Journal and Analysis

* `journalctl.conf` can specify journal entry retention based on age or maximum storage space.
* When configuring `journald.conf`, the default time unit is seconds, but it can be overridden using suffixes like "year," "month," "week," "day," "h," or "m."
* When using `journalctl --vacuum-time=`, `journalctl --vacuum-files=`, or `journalctl --vacuum-size=`, only complete archive files are deleted; active files are not truncated.
* Use `journalctl` options to narrow searches, as listing all journal entries is usually unnecessary.
* The `journalctl --list-boots` command lists boot sessions with an index and UUID. Boot index numbers change after each boot, but UUIDs do not.
* A lack of output messages from `systemd-analyze verify` indicates no errors in the scanned file.
* By default, `systemd-analyze` without a subcommand implies `systemd-analyze time`.
* Commands using `systemd-analyze` can generally be executed by a non-root user unless otherwise specified.
* Units causing startup delays are highlighted in red in `systemd-analyze critical-chain` output on color-supporting terminals.
* In `systemd-analyze critical-chain` output, "@" precedes the absolute time (seconds since startup) a unit became active.
* In `systemd-analyze critical-chain` output, "+" precedes the time taken for a unit to start.
* `systemd-analyze security` only works on service units.

## Firewall Configuration and Management

* XML zone files must begin with `<?xml version="1.0" encoding="utf-8"?>`.
* All statements within a zone file must be enclosed by `<zone>` and `</zone>` tags.
* Do not access or change `nftables` rules directly; manipulate them only by using `firewall-cmd` (for `firewalld`) or `nft` (for `nftables`) command-line tools.
* `firewall-cmd` actions persist only until the firewall or the computer restarts; permanent actions must be accompanied by the `--permanent` flag.
* To make permanent changes active immediately, use the `--permanent` flag with the action, and then run `firewall-cmd --reload`.
* Run `firewall-cmd --reload` immediately after creating a new zone, or when first starting the `firewalld.service` after migrating from another firewall tool.
* When using `firewalld`, consistently add new rules using the service name rather than the port number, if the service is predefined.
* The `timeout=` option for adding services is incompatible with the `--permanent` option.
* Typically use the `masquerade` entry only on the firewall for outbound packets to the external network.
* Do not modify existing `firewalld` zone files; instead, copy an existing zone file and modify the copy.
* Do not use the `firewall-cmd --new-zone` command when creating a new zone file by copying an existing one.
* Do not make a newly created firewall zone the default zone; ensure the default firewall zone is the `public` zone.
* Explicitly assign a network interface to a new firewall zone.
* Ensure a new firewall zone does not have forwarding or masquerading enabled if they are not required.
* After testing a new zone, disable any temporary services (e.g., Telnet) and remove the zone from the network interface.
* Ensure that a network interface reverts to the `public` zone default after a custom zone is removed.
* When `firewalld` is in use, the `nftables` service is disabled.

## Firewall Security Best Practices

* When configuring a wireless interface in a public area, strongly recommend assigning it to the `drop` zone.
* The `drop` zone should be considered safer than the `block` zone because it does not send a rejection message back to the source.
* When configuring a new zone to block all external access except for specific services (e.g., SSH and Telnet), ensure only those services are allowed.
* Configure the firewall such that email allowed to pass through to the Internet can only originate from a known and trusted internal email server.

## Firewall Panic Mode

* Panic mode blocks all inbound and outbound packets, creating logical isolation.
* You must have physical or direct access to a host to turn panic mode off if activated remotely.
* Panic mode is not persistent and does not survive a reboot.
* Do not activate panic mode remotely without having direct access to the host, as remote access will be lost immediately.
* Do not configure panic mode to turn off after a specified period, as the problem resolution time is unpredictable.

## Fail2Ban Configuration

* Do not use the `jail.conf` file for most Fail2Ban configuration changes, as it might be overwritten during updates.
* Create a `jail.local` file in the same directory as `jail.conf` for local Fail2Ban configurations.
* Settings defined in `jail.local` will override those in `jail.conf`.
* Ensure the `enabled = true` line is added to the `[sshd]` section of `jail.local` to enable the sshd jail.
* Do not enable the Fail2Ban service to start on boot immediately after installation; start it manually for initial testing.
* `f2b-sshd` chain entries appear in the `nftables` rule set only after the first ban is triggered.
* Only IP-specific rejection lines are removed when Fail2Ban IP blocking rules time out; the first and last lines of an `f2b-sshd` chain are not deleted.
* For cleanup, revert `ignoreself` to `true`, `bantime` to `10m`, and `maxretry` to `5`.
* Stop Fail2Ban after cleanup if it was not enabled to start on boot.

## Name Resolution Configuration

* Every computer requires a resolver service to locate hosts on local and external networks.
* The operating system first checks the `/etc/hosts` file for hostname resolution.
* If a hostname is not found in `/etc/hosts`, the request is sent to the first name server specified in `/etc/resolv.conf`.
* Local name resolution depends on the sequence of entries in the `nsswitch.conf` file's `hosts` line.
* External name resolution follows a fixed process regardless of the local resolver configuration.
* `/etc/resolv.conf` can still be used as an ASCII plain-text file listing up to three name servers, but this bypasses `systemd-resolved`.
* `/etc/resolv.conf` must contain the domain name to search for hostnames if an FQDN is not provided.
* By default, `/etc/resolv.conf` is a symbolic link to `/run/systemd/resolve/stub-resolv.conf` or `/run/systemd/resolve/resolv.conf`.
* The target file of the `/etc/resolv.conf` symlink determines how `systemd-resolved` handles name resolution requests.
* To enable `systemd-resolved` by default, ensure `/etc/resolv.conf` links to `/run/systemd/resolve/stub-resolv.conf`, and `systemd-resolved.service` is running.
* The `nameserver` line in `/run/systemd/resolve/stub-resolv.conf` points to `127.0.0.53`.
* `/etc/hosts` is an ASCII plain-text file used to list IP addresses and hostnames.
* A default `/etc/hosts` file must contain entries to translate `localhost` to `127.0.0.1` (IPv4) and `::1` (IPv6).
* Only one host can be assigned a specific IP address in `/etc/hosts`; additional hostnames for that IP are aliases.
* Third-party programs should typically access name resolution through the `/etc/resolv.conf` symlink, not directly to stub files.
* To manage `resolv.conf` in a custom way, replace its symlink with a static file or a different symlink.
* `systemd-resolved.service` must be running for `mDNS` protocols to function.
* The `nsswitch.conf` file defines the database sources and order for name-service information, with earlier entries taking precedence.
* All hosts on a local network must run `avahi-daemon.service` to participate in `mDNS`.
* If `systemd-resolved` is unavailable, the historical `nss-DNS` service should be used for name resolution (as per `[!UNAVAIL=return] dns` in `nsswitch.conf`).
* To use traditional NSS resolver and prevent `authselect` from managing `/etc/nsswitch.conf`, you must `authselect opt-out`.
* The `NetworkManager` service creates `/etc/resolv.conf` at boot time if it doesn't exist.
* If `systemd-resolved` is running, `NetworkManager` creates the default symlink to `stub-resolv.conf`.
* For networks with DHCP or static configurations, `nss-DNS` name resolution services are generally better suited than `systemd-resolved` in its default configuration.

## Permissions, Ownership, and File System Hierarchy

* Shell programs used for systemd startup configurations must be executable.
* Shell programs used for systemd startup configurations must have user and group ownership by `root`.
* Shell programs used for systemd startup configurations must have `700` permissions.
* Place local executable files for startup scripts in `/usr/local/bin` to comply with the Linux FHS.
* Use the correct path for Bash in the shebang line of shell scripts (e.g., `#!/usr/bin/bash` for Red Hat/Fedora, `#!/bin/bash` for Debian).

## System Administration and Operational Procedures

* To reliably activate a new display manager, reboot the host.
* Use the `timedatectl set-local-rtc 0` command to configure the RTC to use UTC, avoiding time zone and daylight saving issues.
* The `hwclock --systohc --localtime` command can be used to set the RTC to the system time, with the `--localtime` option ensuring local time.

## Deprecated Features

* The `rc.local` file is deprecated and its use should be avoided.
* Migrate all `rc.local` contents to `systemd` services, as temporary support for `rc.local` will eventually be removed.

## Key Highlights

* All software running as a daemon should be managed by `systemd`. For custom unit files, place them in `/usr/local/lib/systemd/system/`, and modify existing ones via `systemctl edit <unit>` to create override files in `/etc/systemd/system/<unit>.d/override.conf`. Always execute `systemctl daemon-reload` after making changes.
* Avoid using `Type=forking` for `systemd` services; instead, prefer `Type=notify`, `Type=notify-reload`, or `Type=dbus` for more robust and reliable service state management.
* To ensure a `systemd` service starts only after the network is fully operational, add both `After=network-online.target` and `Wants=network-online.target` to its `[Unit]` section.
* For `firewalld` changes to persist across reboots and become active immediately, always use the `--permanent` flag with the action, and then run `firewall-cmd --reload`.
* Do not modify existing `firewalld` zone files; instead, copy and modify a duplicate. For enhanced security, assign wireless interfaces in public areas to the `drop` zone, as it offers better protection than `block` by not sending rejection messages.
* Create a `jail.local` file in the same directory as `jail.conf` for local Fail2Ban configurations to prevent custom settings from being overwritten during package updates.
* The operating system prioritizes hostname resolution by first checking the `/etc/hosts` file before sending requests to name servers specified in `/etc/resolv.conf`.
* Configure the Real-Time Clock (RTC) to use UTC with the `timedatectl set-local-rtc 0` command to prevent time zone and daylight saving issues, ensuring consistent system timekeeping.

## Example ideas

* Conduct a comprehensive audit of all custom systemd unit files: Verify compliance with FHS paths, root ownership, 754 permissions, proper [Service] types (avoiding Type=forking), and the use of systemctl edit for overrides.
* Evaluate and standardize the name resolution strategy across deployments: Determine the preferred approach between systemd-resolved and traditional nss-DNS, ensuring consistent /etc/resolv.conf symlinking and nsswitch.conf configuration.
* Perform a thorough review of firewalld configurations: Check for adherence to best practices, including correct zone assignments, use of service names over port numbers, proper application of --permanent and --reload, and security considerations like drop vs block zones.
* Identify and migrate all deprecated system initialization configurations: Specifically, replace any remaining rc.local scripts with dedicated systemd service units to improve maintainability and future compatibility.
