# Rules for Building a Linux From Scratch (LFS) System

These rules are distilled from various segments of the LFS documentation and cover critical aspects of system construction, from host requirements to final bootloader configuration and system management. Adherence to these guidelines is essential for a successful and stable LFS build.

**Generated on:** October 1, 2025 at 11:03 AM CDT

---

## I. General Process & Environment

* Understand each command before execution; do not blindly type commands.
* Capture terminal output using the `tee` utility for debugging purposes.
* Extract source code archives using `tar`; do not use `cp -R`, as it can destroy timestamps.
* Delete extracted source directories after a package build, unless otherwise instructed.
* Re-extract packages from their original tarball if installation correctness is in doubt, ensuring the previous extraction is removed first.
* The LFS system is designed to be built in a single session; avoid system shutdowns during the process.
* Run all commands for Chapters 7 and onwards within the `chroot` environment.
* Define and consistently verify the `$LFS` environment variable throughout the build process.
* Set the default `umask` to `022` to enforce appropriate file permissions and avoid security holes.
* Perform Chapters 5 and 6 tasks as the `lfs` user (`su - lfs`) to prevent installing packages to the host system.
* Ensure a clean environment for the `lfs` user by using `exec env -i ...` in `~/.bash_profile` to prevent host environment variable leakage.
* Set `LC_ALL=POSIX` (or `C`) for consistent behavior in the cross-compilation environment.
* Prepend `$LFS/tools/bin` to the `PATH` variable to ensure the cross-compiler is used immediately.
* Set `CONFIG_SITE=$LFS/usr/share/config.site` to prevent contamination from host-specific configuration items.
* Turn off Bash's hash function (`set +h`) in `~/.bashrc` to force the shell to search `PATH` for new tools.
* Set `MAKEFLAGS="-j$(nproc)"` for parallel compilation in Chapters 5 and 6 (or replace `$(nproc)` with a specific number of jobs).
* Never use `make -j` without specifying a number of jobs, or set `MAKEFLAGS=-j` without a value, as this can lead to infinite build jobs and system instability.
* Unset optimization-related environment variables (e.g., `CFLAGS`, `CPPFLAGS`, `CXXFLAGS`, `LDFLAGS`) before compiling GCC Pass 2.
* The `PATH` variable inside the `chroot` environment must not include `/tools/bin` as the cross toolchain is no longer used.
* Execute all commands within the `chroot` environment as the `root` user.
* The `$LFS` directory hierarchy must be owned by `root:root` before entering `chroot` to prevent malicious manipulation.
* The `bash` shell must be used for any user needing the `$LFS` variable, ensuring `.bash_profile` is loaded.
* Avoid including `/bin` or `/sbin` in the `PATH` variable (e.g., in `.bashrc`) as it may cause some BLFS packages to fail to build.

### II. Host System Requirements

* Build LFS from an existing Linux distribution.
* Ensure essential development tools are installed on the host system (e.g., by selecting the "development" option during host distribution installation).
* Meet or exceed the minimum specified host software versions; do not use versions outside recommended ranges (e.g., Binutils versions greater than 2.44 or GCC versions greater than 14.2.0 are not recommended).
* Ensure required host system symbolic links are correctly set:
  * `/bin/sh` must link to `bash`.
  * `/usr/bin/yacc` must link to `bison` (or a script executing `bison`).
  * `/usr/bin/awk` must link to `gawk`.
* Do not use symbolic links to unsupported host software (e.g., `dash`, `mawk`), as they are untested and may require deviations or additional patches.
* Ensure C and C++ standard libraries with headers are present on the host for compiler functionality.
* The host kernel must support UNIX 98 pseudo terminals (PTYs); confirm `CONFIG_UNIX98_PTYS` is set to `y` if building a custom host kernel.
* If the host kernel is older than 5.4, it must be replaced with a more up-to-date version.
* If `/etc/bash.bashrc` exists on the host, move it aside to prevent unwanted modification of the `lfs` user's environment; restore it later if desired.

### III. Filesystem & Storage

* All partitions must be formatted to contain a file system before use.
* The LFS root filesystem (/) is assumed to be of type `ext4`.
* Initialize new swap partitions using `mkswap /dev/<yyy>`.
* Enable swap partitions using `swapon -v /dev/<zzz>`.
* Do not mount the LFS partition with restrictive options such as `nosuid` or `nodev`; if set, remount the partition.
* If the system is shut down, remount the LFS partition or configure `/etc/fstab` on the host to auto-mount it upon reboot.
* The `/usr/lib64` directory must not exist in the LFS filesystem; verify its non-existence periodically.
* Mount virtual kernel file systems within the `$LFS` directory tree *before* entering `chroot`:
  * `/dev` must be bind-mounted from the host (`mount -v --bind /dev $LFS/dev`).
  * `/dev/pts` must be mounted with `gid=5,mode=0620`.
  * `/proc`, `/sys`, and `/run` must be mounted.
  * `/dev/shm` must be handled appropriately (created with `1777` permissions if symlinked from host, or explicitly mounted as `tmpfs`).
* Ensure correct permissions for critical directories: `/root` must have `0750`, and `/tmp` and `/var/tmp` must have `1777` (sticky bit set).
* Specify all auto-mounted partitions in `/etc/fstab`.
* If using a separate `/usr` partition, an `initramfs` is required (this is an advanced topic not covered by LFS).
* The GRUB BIOS partition must be unformatted and reside on the boot drive if using GPT.
* For D-Bus and systemd compatibility, create a symlink from `/etc/machine-id` to `/var/lib/dbus`.
* When configuring `/etc/fstab`:
  * Replace placeholders like `<xxx>`, `<yyy>`, and `<fs_type>` with appropriate device nodes and filesystem types.
  * For MS-DOS or Windows origin filesystems (e.g., `vfat`, `ntfs`) with non-ASCII characters, the `utf8` option is required.
  * For non-UTF-8 locales, `iocharset` must be set to the kernel-understood character set (if compiled into the kernel or as a module).
  * For UTF-8 locales, use the `utf8` option instead of `iocharset=utf8` to prevent the filesystem from becoming case-sensitive.
  * The `codepage` option is required for `vfat` and `smbfs` filesystems, set to the MS-DOS codepage number for the country.
  * To make ext3 filesystems reliable across power failures on supported hard disk types, add the `barrier=1` mount option.
  * LVM-based partitions cannot use the `barrier` option.
  * Consider replacing device node paths (e.g., `/dev/sda1`) with `PARTUUID=<partition UUID>` in `/etc/fstab` to avoid boot failures if device names change.

### IV. Security & Permissions

* Do not use a package release known to be vulnerable; consult security advisories.
* Harden GCC features by default with `--enable-default-pie` and `--enable-default-ssp`.
* Configure Glibc to enable strong stack protection with `--enable-stack-protector=strong`.
* Configure Binutils to only generate GNU-style hash tables by default with `--enable-default-hash-style=gnu`.
* Prevent hardcoding library search paths (rpath) using `--disable-rpath` for Tcl and specific `sed` commands for Readline.
* Configure Libxcrypt to use strong and Glibc-compatible hash algorithms with `--enable-hashes=strong,glibc`.
* Libxcrypt must disable obsolete API functions and failure tokens using `--enable-obsolete-api=no` and `--disable-failure-tokens`.
* Configure Shadow to use the YESCRYPT method for password encryption.
* Ensure `/usr/bin/passwd` exists (e.g., `touch /usr/bin/passwd`) before installing Shadow.
* Configure Shadow with `group-name-max-length=32` and `--without-libbsd`.
* Override `systemd`'s default `udev` rule for `/dev/kvm` with `-D dev-kvm-mode=0660`.
* Ensure the `man` program (from Man-DB) is not `setuid` by using `--disable-setuid`.
* Unset build-affecting environment variables (`{C,CPP,CXX,LD}FLAGS`) for GRUB.
* Do not use custom compilation flags for GRUB, as aggressive optimization may break low-level bootloader operations.
* When using `pip3` for system-wide package installations as `root`, create `/etc/pip.conf` to suppress warnings about non-virtual environment installation and version checks.
* If retaining the kernel source tree, run `chown -R 0:0` on the kernel source directory (e.g., `linux-6.13.4`) for security.
* Before stripping binaries, create a backup of the LFS system.
* Do not allow the stripping process to affect currently running binaries or libraries; instead, copy them to `/tmp`, strip them there, and then reinstall.
* If package versions differ from the book, update library file names in `save_usrlib` or `online_usrlib` variables in the stripping script to prevent system instability.
* Remove all debug symbols and unneeded symbol table entries using `strip --strip-unneeded`.
* Compress and preserve debugging symbols for selected libraries in separate `.dbg` files using `objcopy --only-keep-debug --compress-debug-sections=zlib $LIB $LIB.dbg`.
* Add debuglink to stripped binaries/libraries using `objcopy --add-gnu-debuglink=$LIB.dbg /tmp/$LIB`.

### V. Package Management & Updates

* Use the exact package versions listed in the documentation unless specified otherwise by LFS errata or security advisories.
* Do not use repository snapshot tarballs; always use release tarballs.
* Store all downloaded packages and patches accessibly within the LFS partition (e.g., `$LFS/sources`).
* Verify downloaded files using `md5sum` (e.g., by placing `md5sums` in `$LFS/sources` and running `md5sum -c md5sums`).
* If downloaded as a non-root user, change ownership of downloaded files to `root:root` to avoid issues with unnamed UIDs in the final LFS system.
* Read security advisories *before* downloading packages to determine if newer versions are required to fix vulnerabilities.
* If the Linux kernel is upgraded, no other packages need to be rebuilt, but the system must be rebooted.
* Upgrading Glibc requires extra precautions to avoid breaking the system; upgrading prior to LFS 11.0 is not supported.
* Recompile dependent packages if a shared library name changes, and do not remove old libraries until their dependents are recompiled.
* Rebuild packages promptly if they link to both old and new revisions of an updated shared library.
* Remove old library files if their file version decreases to prevent `ldconfig` from symlinking to an older, seemingly newer, version.
* Restart all running programs linked to a security-fixed shared library after an update.
* Restart the `systemd` daemon with `systemctl daemon-reexec` if its libraries are updated.
* Avoid system-wide "install in separate directories" package management schemes.
* Use `DESTDIR` for symlink-style package management; do not use `--prefix=/usr/pkg/...`.
* `pip3 install` commands must be run as `root` (unless in a virtual environment) for modules to be accessible by all users.
* Use `pip3 --upgrade` for Python package upgrades.
* Use `pip3 --force-reinstall --no-deps` for downgrading or reinstalling the same version of a Python package.
* When installing Python documentation with `tar`, use `--no-same-owner --no-same-permissions`.
* If downloading sources directly onto the LFS system (in `chroot` or after booting), install `libtasn1`, `p11-kit`, `make-ca`, and `wget`.
* For working from the LFS command line, ensure `libtasn1`, `p11-kit`, `make-ca`, `wget`, `gpm`, and `links` (or `lynx`) are installed in `chroot` before rebooting into the new LFS system.

### VI. Toolchain & Package-Specific Configuration

* Binutils (Pass 1) must be the first package compiled.
* For GCC (Pass 1), unpack GMP, MPFR, and MPC into the GCC source directory and rename them appropriately.
* GCC (Pass 1) must be built in a dedicated build directory.
* Configure GCC (Pass 1) with `--target=$LFS_TGT`, `--prefix=$LFS/tools`, `--with-glibc-version=2.41`, `--with-sysroot=$LFS`, `--with-newlib`, `--without-headers`, `--enable-default-pie`, `--enable-default-ssp`, `--disable-nls`, `--disable-shared`, `--disable-multilib`, `--disable-threads`, `--disable-libatomic`, `--disable-libgomp`, `--disable-libquadmath`, `--disable-libssp`, `--disable-libvtv`, `--disable-libstdcxx`, and `--enable-languages=c,c++`.
* Create a full internal header for GCC Pass 1 after installation using the specified `cat` command.
* Glibc must be built in a dedicated build directory.
* Ensure `ldconfig` and `sln` are installed to `/usr/sbin` for Glibc by adding `echo "rootsbindir=/usr/sbin" > configparms` to the build process.
* Configure Glibc with `--prefix=/usr`, `--host=$LFS_TGT`, `--build=$(../scripts/config.guess)`, `--enable-kernel=5.4`, `--with-headers=$LFS/usr/include`, `--disable-nscd`, and `libc_cv_slibdir=/usr/lib`.
* Libstdc++ must be built from the GCC sources, in a dedicated build directory.
* Configure Libstdc++ with `--host=$LFS_TGT`, `--build=$(../config.guess)`, `--prefix=/usr`, `--disable-multilib`, `--disable-nls`, `--disable-libstdcxx-pch`, and `--with-gxx-include-dir=/tools/$LFS_TGT/include/c++/14.2.0`.
* Remove libtool archive files (`.la`) after Libstdc++ installation.
* For Binutils Pass 2, run `sed '6031s/$add_dir//' -i ltmain.sh` to work around a libtool inconsistency.
* Configure Binutils Pass 2 with `--enable-shared` and `--enable-64-bit-bfd`.
* For GCC Pass 2, unpack GMP, MPFR, and MPC into the GCC source directory and rename them appropriately.
* Configure GCC Pass 2 with `--build=$(../config.guess)`, `--host=$LFS_TGT`, `--target=$LFS_TGT`, `LDFLAGS_FOR_TARGET=-L$PWD/$LFS_TGT/libgcc`, `--prefix=/usr`, `--with-build-sysroot=$LFS`, `--enable-default-pie`, `--enable-default-ssp`, `--disable-nls`, `--disable-multilib`, `--disable-libatomic`, `--disable-libgomp`, `--disable-libquadmath`, `--disable-libsanitizer`, `--disable-libssp`, `--disable-libvtv`, and `--enable-languages=c,c++`.
* Create a `cc` symlink to `gcc` after GCC Pass 2 installation.
* Add the LTO compatibility symlink after GCC Pass 2 installation.
* Configure `Bash` (final build) with `--without-bash-malloc` and `--with-installed-readline`.
* Configure `Ncurses` (final build) with `--with-shared`, `--without-debug`, `--without-normal`, `--with-cxx-shared`, `--enable-pc-files`, and `--with-pkg-config-libdir=/usr/lib/pkgconfig`.
* For `Ncurses` (final build) installation, follow specific commands for shared library replacement and header modification to ensure correct wide-character ABI usage and avoid shell crashes, including creating symlinks from non-wide-character library names to wide-character versions (only safe if `curses.h` is edited).
* Configure `File` (Pass 1) with `--disable-bzlib`, `--disable-libseccomp`, `--disable-xzlib`, and `--disable-zlib`.
* Configure `Make` (Pass 1) with `--without-guile`.
* Configure `Xz` (Pass 1) with `--disable-static`.
* Configure `Bc` with `CC=gcc -G -O3 -r`.
* Configure `Flex` with `--disable-static`.
* Configure `Tcl` with `--disable-rpath`, remove references to the build directory from its configuration files, and run `make install-private-headers`.
* Rename the `Thread.3` man page for `Tcl` to avoid conflicts.
* Configure `Expect` with `--enable-shared`, `--disable-rpath`, `--with-tcl=/usr/lib`, and `--with-tclinclude=/usr/include`.
* Configure `Pkgconf` with `--disable-static`.
* Configure `GMP` with `--enable-cxx` and `--disable-static`.
* Configure `MPFR` with `--disable-static` and `--enable-thread-safe`.
* Configure `MPC` with `--disable-static`.
* Configure `Attr` with `--disable-static`.
* Configure `Acl` with `--disable-static`.
* For `Libcap` installation, prevent static libraries by running `sed -i '/install -m.*STA/d' libcap/Makefile`, and use `lib=lib` parameter during `make`.
* Configure `GDBM` with `--disable-static` and `--enable-libgdbm-compat`.
* Configure `Expat` with `--disable-static`.
* Configure `Inetutils` with `--disable-logger`, `--disable-whois`, `--disable-rcp`, `--disable-rexec`, `--disable-rlogin`, `--disable-rsh`, and `--disable-servers`.
* For `Perl`, set `export BUILD_ZLIB=False` and `export BUILD_BZIP2=0`.
* Configure `Perl` with `-D useshrplib`, `-D usethreads`, `-D man1dir=/usr/share/man/man1`, and `-D man3dir=/usr/share/man/man3`.
* For `Intltool`, apply `sed -i 's:\\\${:\\\$\\{:' intltool-update.in` to fix a warning with Perl 5.22+.
* Configure `OpenSSL` with `--prefix=/usr`, `--openssldir=/etc/ssl`, `--libdir=lib`, `shared`, and `zlib-dynamic`.
* For `OpenSSL` installation, run `sed -i '/INSTALL_LIBS/s/libcrypto.a libssl.a//' Makefile` before `make install`.
* Configure `Libelf` with `--disable-debuginfod` and `--enable-libdebuginfod=dummy`.
* Configure `Libffi` with `--disable-static` and `--with-gcc-arch=native` (or a specific architecture if copying to a less capable system).
* Configure `Python` with `--enable-shared`, `--with-system-expat`, and `--enable-optimizations`.
* Build and install `Flit-core`, `Wheel`, `Setuptools`, `MarkupSafe`, and `Jinja2` using `pip3 wheel` followed by `pip3 install --no-index --find-links dist --no-cache-dir --no-build-isolation --no-deps`.
* Build `Ninja` with `--bootstrap`.
* Configure `Meson` with `--buildtype=release` and `--wrap-mode=nofallback`.
* Configure `Kmod` with `-D manpages=false`.
* Configure `systemd` with `--prefix=/usr`, `--buildtype=release`, `-D default-dnssec=no`, `-D firstboot=false`, `-D install-tests=false`, `-D ldconfig=false`, `-D sysusers=false`, `-D rpmmacrosdir=no`, `-D homed=disabled`, `-D userdb=false`, `-D man=disabled`, `-D mode=release`, `-D pamconfdir=no`, `-D dev-kvm-mode=0660`, `-D nobody-group=nogroup`, `-D sysupdate=disabled`, `-D ukify=disabled`, and `-D docdir=/usr/share/doc/systemd-257.3`.
* Configure `Man-DB` with `--disable-setuid`, `--enable-cache-owner=bin`, and specific browser/formatter paths.
* Configure `Procps-ng` with `--prefix=/usr`, `--docdir=/usr/share/doc/procps-ng-4.0.5`, `--disable-static`, `--disable-kill`, `--enable-watch8bit`, and `--with-systemd`.
* Configure `Util-linux` with `--bindir=/usr/bin`, `--libdir=/usr/lib`, `--runstatedir=/run`, `--sbindir=/usr/sbin`, `--disable-chfn-chsh`, `--disable-login`, `--disable-nologin`, `--disable-su`, `--disable-setpriv`, `--disable-runuser`, `--disable-pylibmount`, `--disable-liblastlog2`, `--disable-static`, `--without-python`, `ADJTIME_PATH=/var/lib/hwclock/adjtime`, and `--docdir=/usr/share/doc/util-1linux-2.40.4`.
* For `Util-linux`, use `--disable-*` and `--without-*` options for unneeded components or those inconsistent with other installed programs.
* For `IPRoute2`, remove `ARPD` references from its `Makefile` and man page.
* For `Kbd`, apply `kbd-2.7.1-backspace-1.patch`, disable the `resizecons` program, and configure with `--disable-vlock`.
* For `Tar`, use `FORCE_UNSAFE_CONFIGURE=1` during configuration.
* For `Vim`, define `#define SYS_VIMRC_FILE "/etc/vimrc"` in `src/feature.h` and ensure `set nocompatible` is the first setting in its configuration file (`/etc/vimrc`).
* For D-Bus, configure with `--prefix=/usr --buildtype=release --wrap-mode=nofallback` and use `--wrap-mode=nofallback` to prevent Meson from downloading Glib packages for D-Bus tests.
* For E2fsprogs, build the package in a subdirectory of the source tree and configure with `--prefix=/usr --sysconfdir=/etc --enable-elf-shlibs --disable-libblkid --disable-libuuid --disable-uuidd --disable-fsck`.
* For E2fsprogs, do not build and install `libuuid`, `libblkid`, `uuidd` daemon, and `fsck` wrapper (`--disable-libblkid`, etc.) as `util-linux` provides more recent versions.
* After E2fsprogs installation, remove useless static libraries: `rm -fv /usr/lib/{libcom_err,libe2p,libext2fs,libss}.a`.
* If an utility cannot recognize an ext4 filesystem with the `metadata_csum_seed` feature enabled, remove the feature from `/etc/mke2fs.conf` using `sed 's/metadata_csum_seed,//' -i /etc/mke2fs.conf`.

### VII. Kernel Configuration & Modules

* Sanitize Linux kernel API headers to expose the kernel's API for `Glibc`.
* Run `make mrproper` before each kernel compilation or before installing Linux API Headers to ensure a clean source tree; do not rely on the source tree being clean after un-tarring.
* Do not use `make headers_install` for Linux API Headers, as it requires `rsync`, which may not be available.
* Install Linux API Headers using `make headers`, `find usr/include -type f ! -name '*.h' -delete`, and `cp -rv usr/include $LFS/usr`.
* For `make menuconfig` with a UTF-8 text console, set the `LANG` environment variable (e.g., `LANG=<host_LANG_value> LC_ALL=`).
* **Mandatory Kernel Features for LFS:**
  * Enable `CONFIG_PSI` (Pressure stall information tracking) and `CONFIG_PSI_DEFAULT_DISABLED`.
  * Enable `CONFIG_CGROUPS` (Control Group support), `CONFIG_MEMCG` (Memory controller), and `CONFIG_CGROUP_SCHED` (CPU controller).
  * Enable `CONFIG_RELOCATABLE` (Build a relocatable kernel) and `CONFIG_RANDOMIZE_BASE` (KASLR).
  * Enable `CONFIG_STACKPROTECTOR` and `CONFIG_STACKPROTECTOR_STRONG` (Stack Protector buffer overflow detection).
  * Enable `CONFIG_NET` (Networking support) and `CONFIG_INET` (TCP/IP networking); `CONFIG_IPV6` is strongly recommended.
  * Enable `CONFIG_DEVTMPFS` and `CONFIG_DEVTMPFS_MOUNT` (devtmpfs filesystem for `/dev`).
  * Enable `CONFIG_FW_LOADER` (Firmware loading facility).
  * Enable `CONFIG_DMIID` (Export DMI identification via sysfs).
  * Enable `CONFIG_SYSFB_SIMPLEFB` (Mark VGA/VBE/EFI FB as generic system framebuffer).
  * Enable `CONFIG_DRM` (Direct Rendering Manager), `CONFIG_DRM_PANIC`, `CONFIG_DRM_PANIC_SCREEN=kmsg`, `CONFIG_DRM_FBDEV_EMULATION`, and `CONFIG_DRM_SIMPLEDRM`.
  * Enable `CONFIG_FRAMEBUFFER_CONSOLE` (Framebuffer Console support).
  * Enable `CONFIG_INOTIFY_USER` (Inotify support for userspace).
  * Enable `CONFIG_TMPFS` and `CONFIG_TMPFS_POSIX_ACL` (Tmpfs virtual memory file system support).
* **Conditional Kernel Features:**
  * For 64-bit systems, enable `CONFIG_X86_X2APIC`, `CONFIG_PCI`, `CONFIG_PCI_MSI`, `CONFIG_IOMMU_SUPPORT`, and `CONFIG_IRQ_REMAP` in the specified order (`X2APIC` first, then `IRQ_REMAP`, then re-select `X2APIC`).
  * For 32-bit systems with more than 4GB RAM, set `CONFIG_HIGHMEM64G` to `64GB`.
  * If the LFS system partition is on an NVME SSD, enable `CONFIG_BLK_DEV_NVME`.
  * If host hardware uses UEFI and LFS will boot with it, adjust kernel configuration as per the BLFS page.
* **Prohibited Kernel Features:**
  * Do not enable `CONFIG_RT_GROUP_SCHED` (Group scheduling for SCHED_RR/FIFO) if `systemd` features are needed, as it may cause malfunctions.
  * Do not enable `CONFIG_UEVENT_HELPER` (Support for uevent helper) as it may interfere with device management when using Udev.
  * Do not enable `CONFIG_FW_LOADER_USER_HELPER` (Enable the firmware sysfs fallback mechanism).
* **Kernel Installation:**
  * Install kernel modules using `make modules_install` unless module support is disabled in the kernel configuration.
  * If using a separate `/boot` partition, mount it before copying kernel files.
  * The kernel image filename (e.g., `vmlinuz-6.13.4-lfs-12.3-systemd`) should have a `vmlinuz` stem.
  * Copy the kernel image: `cp -iv arch/x86/boot/bzImage /boot/vmlinuz-<kernel-version>-lfs-<lfs-version>`.
  * Copy the `System.map` file: `cp -iv System.map /boot/System.map-<kernel-version>`.
  * Copy the kernel configuration file: `cp -iv .config /boot/config-<kernel-version>`.
  * Install kernel documentation: `cp -r Documentation -T /usr/share/doc/linux-<kernel-version>`.
  * If GCC has been upgraded, run `make clean` before rebuilding the kernel, or the new build may fail.
  * Do not create a symlink from `/usr/src/linux` pointing to the kernel source directory on an LFS system.
* **Linux Module Management:**
  * Create `/etc/modprobe.d/usb.conf` to ensure USB drivers (`ehci_hcd`, `ohci_hcd`, `uhci_hcd`) are loaded in the correct order (e.g., `ehci_hcd` before `ohci_hcd` and `uhci_hcd`).
  * Add `softdep` lines to `/etc/modprobe.d/<filename>.conf` to configure wrapper modules (e.g., `softdep snd-pcm post: snd-pcm-oss`).
  * To prevent unwanted modules from loading, either do not build them or blacklist them in `/etc/modprobe.d/blacklist.conf` (e.g., `blacklist forte`).
  * Do not rely on kernel device names being stable; create udev rules with persistent symlinks based on stable device attributes.
  * Do not use `/dev/video0` or `/dev/video1` directly for duplicate devices (e.g., webcam and TV tuner); use persistent symlinks (e.g., `/dev/webcam`, `/dev/tvtuner`) created by udev rules.
  * If a kernel driver does not export data to `sysfs` and `udev` cannot create a device node, create a static device node in `/usr/lib/udev/devices` with appropriate major/minor numbers.

### VIII. Boot Loader Configuration

* If your system uses UEFI and you plan to boot LFS with UEFI, skip the GRUB instructions for MBR systems and follow BLFS instructions, but still learn `grub.cfg` syntax and partition specification methods.
* Ensure an emergency boot disk is ready before configuring GRUB.
* Understand GRUB's `(hdn,m)` naming convention: hard drive numbers start from 0, normal partition numbers from 1, and extended partitions from 5. GRUB does not consider CD-ROM drives as hard drives.
* Install GRUB files and set up the boot track using `grub-install /dev/sda`; do not run `grub-install` if you do not want to overwrite an existing boot loader.
* If the system was booted using UEFI, add `--target i386-pc` to `grub-install` if `x86_64-efi` target files are not installed.
* Generate `/boot/grub/grub.cfg` using a `cat > /boot/grub/grub.cfg << "EOF" ... EOF` block.
* Set the framebuffer resolution and color depth for the kernel's SimpleDRM driver using `set gfxpayload=1024x768x32` (adjust values as needed) in `grub.cfg`.
* If a separate `/boot` partition is used, remove `/boot` from the `linux` line and update the `set root` line to point to the boot partition in `grub.cfg`.
* To avoid boot failures due to changing GRUB partition designators, use partition UUIDs (`PARTUUID`) or filesystem UUIDs (`fs-uuid`) instead of `(hdn,m)` or `/dev/sdX` paths. When using UUIDs, replace `set root=(hdx,y)` with `search --set=root --fs-uuid <filesystem UUID>` and `root=PARTUUID=<partition UUID>`.
* Do not use `root=UUID=<filesystem UUID>` in `grub.cfg` without an `initramfs`.
* Do not use `grub-mkconfig`, as it will destroy custom `grub.cfg` settings and is not recommended for LFS.
* Always back up your `grub.cfg` file.

### IX. Post-Installation & System Management

* Install any necessary firmware if kernel drivers require them.
* Before rebooting, exit the `chroot` environment and unmount all virtual filesystems in the correct order: `/dev/pts`, `/dev/shm` (if mounted), `/dev`, `/run`, `/proc`, `/sys`.
* Unmount any multiple partitions created before unmounting the main LFS partition.
* Unmount the LFS filesystem: `umount -v $LFS`.
* Set a password for the root user before rebooting into the new LFS system.
* After rebooting, to properly build packages in the new LFS system, ensure virtual filesystems (`/dev`, `/dev/pts`, `/proc`, `/sys`, `/run`, `/dev/shm`) are mounted.
* Do not mix BLFS sources and LFS sources in the `/sources` directory from the `chroot` environment.
* Ensure all necessary packages are accessible inside the `chroot` environment for further build steps.
* Create `/etc/hostname` and enter the computer's name (hostname only, not FQDN).
* For system clock configuration:
  * If the hardware clock is set to local time, create `/etc/adjtime` with `0.0 0.0\n0\nLOCAL\n`.
  * To set the hardware clock to local time using `timedatectl` (after LFS is booted): `timedatectl set-local-rtc 1`.
  * To change the system time (after LFS is booted): `timedatectl set-time YYYY-MM-DD HH:MM:SS`.
  * To change the time zone (after LFS is booted): `timedatectl set-timezone TIMEZONE`.
  * Do not use `timedatectl` in the `chroot` environment.
  * If the system clock is set to Local Time, `systemd-timesyncd` will not update the hardware clock; to disable `systemd-timesyncd`: `systemctl disable systemd-timesyncd`.
* For Linux Console configuration:
  * The `/etc/vconsole.conf` file must contain lines in `VARIABLE=value` format.
  * If `KEYMAP` is unset, it defaults to `us`.
  * Set the default console font (e.g., `Lat2-Terminusl6.psfu.gz`) in `/etc/vconsole.conf` (`echo FONT=Lat2-Terminusl6 > /etc/vconsole.conf`).
  * To change the console keymap at runtime (after LFS is booted): `localectl set-keymap MAP`.
  * Do not use `localectl` for console changes in the `chroot` environment.
  * To use `localectl` parameters for X11 keyboard layout, the `XKeyboard-Config` package from BLFS is required.
* For System Locale configuration:
  * Environment variables for native language support are necessary, using two-letter language codes (`<ll>`), two-letter country codes (`<cc>`), and canonical charmaps (`<charmap>`).
  * If `locale` commands fail, install the desired locale with `localedef` or choose a supported locale.
  * Create `/etc/locale.conf` with `LANG=<ll>_<CC>.<charmap><@modifiers>`.
  * Configure `/etc/profile` to read locale settings from `/etc/locale.conf`.
  * If running in the Linux console (`$TERM = linux`), set `LANG=C.UTF-8` in `/etc/profile` to prevent rendering issues.
  * Do not use `localectl` for locale changes in the `chroot` environment.
  * Use the `C` locale only if you are certain you will never need 8-bit characters.
* For Readline configuration (`/etc/inputrc`):
  * Comments in `/etc/inputrc` cannot be on the same line as commands.
  * Create a global `/etc/inputrc` with desired readline settings.
* For Login Shells configuration (`/etc/shells`):
  * `/etc/shells` must contain one login shell path per line, relative to the root (`/`).
  * If a shell command name is not listed in `/etc/shells`, users will be denied the ability to change to that shell.
  * Applications like GDM and FTP daemons require `/etc/shells` to function correctly.
  * Create `/etc/shells` listing `/bin/sh` and `/bin/bash`.
* For Systemd Basic Configuration:
  * Configuration options are in `/etc/systemd/system.conf`.
  * To disable screen clearing at boot: `mkdir -pv /etc/systemd/system/getty@tty1.service.d; echo "[Service]\nTTYVTDisallocate=no" > /etc/systemd/system/getty@tty1.service.d/noclear.conf`.
  * If a separate partition is used for `/tmp`, do not create the symlink `/etc/systemd/system/tmp.mount` to `/dev/null`.
  * If a separate partition for `/tmp` is desired, specify it in `/etc/fstab`.
  * Local configuration files in `/etc/tmpfiles.d` override files with the same name in `/usr/lib/tmpfiles.d`; to modify, copy the relevant `.conf` file and edit it.
  * Unit parameters can be overridden by creating a directory (`/etc/systemd/system/foobar.service.d`) and a configuration file (`foobar.conf`) within it. After modification, run `systemctl daemon-reload` and `systemctl restart <service>`.
  * To limit disk space used by core dumps, create a configuration file in `/etc/systemd/coredump.conf.d` (e.g., `MaxUse=5G`).
* For Systemd Long Running Processes (systemd-230+):
  * Be aware that systemd kills all user processes when a user session ends, even with `nohup` or `daemon()/setsid()`.
  * Users can enable process lingering for their own user with `loginctl enable-linger <username>`.
  * System administrators can enable process lingering for any user with `loginctl enable-linger <username>`.
  * To start long-running processes for a lingering user, use `systemd-run --scope --user <command>`.
  * To globally disable killing user processes, set `killUserProcesses=no` in `/etc/systemd/logind.conf`.
  * To disable lingering by default during systemd build, add `-o default-kill-user-processes=false` to the `meson` command.
* Ensure to customize `DISTRIB_CODENAME` and `VERSION_CODENAME` fields in `/etc/lsb-release` and `/etc/os-release` files.
* Perform system cleanup:
  * Remove extra files from `/tmp`: `rm -xf /tmp/{*,.*}`.
  * Remove libtool archive files (`.la`): `find /usr/lib /usr/libexec -name \*.la -delete`.
  * Remove the partially installed compiler: `find /usr -depth -name $(uname -m)-lfs-linux-gnu\* | xargs rm -rf`.
  * Remove the temporary `tester` user account: `userdel -r tester`.
* Unzip and update info directory files (e.g., `libext2fs.info.gz`): `gunzip -v /usr/share/info/libext2fs.info.gz` and `install-info --dir-file=/usr/share/info/dir /usr/share/info/libext2fs.info`.
* Do not expect manual pages in languages not listed in "Table 8.1. Expected character encoding of legacy 8-bit manual pages" to be supported by Man-DB.

### X. Testing Procedures

* Do not run test suites in Chapters 5 and 6, as programs are cross-compiled.
* Address PTY issues (e.g., running out of PTYs) before running `binutils` and `GCC` tests to prevent failures.
* Run the Glibc, GMP, and MPFR test suites as they are considered critical and must not be skipped.
* Attr tests must be run on a filesystem that supports extended attributes.
* Acl tests must be run on a filesystem that supports access controls.
* Run `Gperf` tests with `-j1` as they are known to fail with multiple simultaneous jobs.
* Run the `Bash` test suite as a non-root user in a new pseudo terminal (PTY).
* For `Coreutils`, run root tests with `make NON_ROOT_USERNAME=tester check-root` and non-root tests as user `tester` with standard input redirected from `/dev/null` (a temporary group must be added to `tester`).
* The `Meson` and `Kmod` test suites are outside the scope of LFS.
* The `GRUB` test suite is not recommended as most tests depend on packages not available in LFS.
* Run `Python` tests with `TESTOPTS="--timeout 120"` as some tests are known to hang.
* `Ninja` package tests cannot run in the `chroot` environment.
* Before running `systemd` tests, create a basic `/etc/os-release` file.
* Running the `Util-linux` test suite as `root` can be harmful; if done, `CONFIG_SCSI_DEBUG` must be built as a kernel module.
* When running `Procps-ng` or `Util-linux` tests as a non-root user (e.g., `tester`):
  * Change ownership of the current directory to `tester` (`chown -R tester .`).
  * Execute `make check` (or `make -k check`) as the `tester` user (e.g., `su tester --c "PATH=$PATH make check"`).
* For `Procps-ng` tests, ensure the host kernel is built with `CONFIG_SSP_PROCESS_ACCT` enabled, or the `ps` test will fail.
* For `Util-linux` tests, create a dummy `/etc/fstab` file and ensure the host kernel has `CONFIG_CRYPTO_USER_API_HASH` (or SHA256 implementation) and `CONFIG_NETLINK_DIAG` enabled to prevent test failures.
* If the LFS system's filesystem is not `ext4`, expect the `m_rootdir_acl` test from E2fsprogs to fail.
* The Binutils (final build) test suite is considered critical; do not skip it.
* The GCC (final build) test suite is considered important; first-time builders are encouraged to run it.

### XI. Syntax & Documentation

* Type commands exactly as seen in fixed-width font unless otherwise noted.
* Follow backslashes (`\`) with an immediate return; other whitespace characters after a backslash will cause incorrect results.
* Do not type `<REPLACED TEXT>`; this format indicates text for replacement or copy-and-paste.
* `[OPTIONAL TEXT]` indicates optional content.
* Reference man pages with section numbers (e.g., `passwd(5)` means `man 5 passwd`).
* Type `cat > file << "EOF"` sections exactly as seen, including the `EOF` markers.
* Configure your browser for a monospace font to distinguish similar glyphs like `1l1` or `oO0`.

## Key Highlights

* Crucially, understand each command before execution and never blindly type commands, as this is fundamental to a successful and stable LFS build.
* Ensure host system compatibility by meeting or exceeding specified software versions and confirming required symbolic links, such as `/bin/sh` to `bash`, are correctly set.
* To prevent host system contamination and ensure correct installation, perform Chapters 5 and 6 tasks as the `lfs` user, and all subsequent commands within the `chroot` environment after mounting virtual kernel filesystems like `/dev`, `/proc`, and `/sys`.
* Avoid mounting the LFS partition with restrictive options like `nosuid` or `nodev`, and verify that the `/usr/lib64` directory does not exist in the LFS filesystem to ensure full functionality.
* Always use the exact package versions specified in the documentation, consult security advisories, and verify downloaded files with `md5sum` to ensure build consistency and security.
* For kernel configuration, run `make mrproper` for a clean source tree, enable mandatory features like `CONFIG_PSI` and `CONFIG_CGROUPS`, and avoid prohibited features such as `CONFIG_RT_GROUP_SCHED` to prevent system malfunctions.
* Prioritize system security by hardening GCC with PIE/SSP, Glibc with strong stack protection, and never allow stripping processes to affect currently running binaries; copy them to `/tmp` first.
* Before the final reboot, ensure a clean shutdown by correctly unmounting all virtual and LFS filesystems, and crucially, set a password for the root user.
* Always have an emergency boot disk ready, use partition UUIDs for reliable GRUB configuration, and never use `grub-mkconfig` as it can overwrite essential custom settings.
