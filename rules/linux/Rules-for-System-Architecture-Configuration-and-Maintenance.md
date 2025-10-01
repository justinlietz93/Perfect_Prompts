# Rules for System Architecture, Configuration, and Maintenance

These rules are distilled from various technical documentation segments to ensure proper design, installation, configuration, and troubleshooting of computing systems.

**Generated on:** October 1, 2025 at 12:10 PM CDT

---

## I. System Architecture & Design

* The CPU must perform mathematical calculations, logical comparisons, and data manipulation.
* Processor design must specify internal time requirements such that the maximum limit does not exceed the chip's rated speed.
* The CPU must support speculative execution, allowing it to jump to the next instruction when branches occur in the instruction flow.
* Program execution must prevent confusion when multiple executions occur (Register Renaming).
* Write buffers must be utilized to execute various instructions and prevent pipeline overloading or stalling.
* The Control Bus must allow data transfer only from the CPU to I/O and memory (unidirectional).
* The Data Bus must allow data transfer to and from the CPU, I/O, and memory (bidirectional).
* AGP must be exclusively used for connecting video cards to the computer.
* For advanced performance, AGP's full bandwidth must be utilized, and the bus must be queued by the target.
* Once the AGP Read Buffer Full signal (RBF#) is asserted, the arbiter must not initiate the request to take back low priority read data to the master.
* Once the AGP Write Buffer Full signal (WBF#) is asserted, the arbiter must not initiate the request to provide data.
* Memory must always be available to access and retrieve information when required.
* DRAM must be continuously refreshed using refresh circuitry to prevent data loss.
* Control lines are required for the operation of memory chips.
* RAM in modern motherboards must be added through DIMM/RIMM slots.
* The Northbridge is responsible for managing traffic for faster CPU-intensive components (e.g., video cards, RAM).
* The Southbridge is responsible for controlling slower traffic components (e.g., I/O devices, DMA controller, system clock).
* An SCSI system must include at least one initiator and one target.
* The PCI Lock (-LOCK) signal must prevent other initiators from modifying locked addresses or selected expansion devices.

## II. Hardware Compatibility & Selection

* The host computer's motherboard must support multiple processors.
* Processor selection must align with the requirements of the application being used.
* CPU sockets must be designed to serve specific types of CPUs; using incompatible sockets will limit system speed.
* Specific Pentium processor ranges require specific sockets: Pentium 60/66 processors require Socket 4; Pentium processors from 75 to 133 MHz require Socket 5 or Socket 7; Pentium 150s, 166s, and 200s processors require Socket 7.
* Overdrive processors are hard-wired to a specific clock multiplier; they must not set their multiplier based on motherboard jumpers like regular Pentiums.
* The Pentium Pro is optimized for running 32-bit code and supports quad processor configurations.
* A motherboard must have only one 1.5V AGP slot.
* AGP cards are not interchangeable if their signal layouts are similar but key locations differ.
* When upgrading memory, ensure proficient compatibility with existing memory.
* An extended memory card must not be used to utilize expanded memory, and vice-versa.
* Memory modules within a bank must have the same size, speed, and RAM technology; otherwise, the system will fail to recognize them.
* The system must have sufficient memory, with a minimum of 64MB required for modern processing.
* The motherboard's physical size must be suitable to accommodate internal drives, the power supply, expansion slots, and the new processor without crushing components.
* The computer case must accommodate the chosen motherboard, ensuring mounting holes correspond.
* The chosen SCSI host adapter must be compatible with the existing PC bus and support relevant SCSI standards.
* SCSI peripherals must be flexible enough to operate on any of the eight SCSI IDs (0-7).
* SCSI peripherals should support SCSI parity.
* If using an internal SCSI device, ensure sufficient physical space inside the PC case.
* Monitors must support the screen resolution and refresh rate configured in the display settings.
* USB cables are categorized by data transfer speeds; ensure the correct cable type is used for the specific USB plug-and-play device.
* If cross-OS driver compatibility is desired (e.g., Windows 2000/98), use WDM drivers only.
* The video card must be supported by the operating system (e.g., listed in the Hardware Compatibility List).

## III. System Configuration & Optimization

* Bus clock speed must be set so that all connected devices interact at the same speed.
* The host computer's operating system must support multiprocessing (e.g., Windows NT/2000, LINUX).
* For PCI, IRQs can be shared among devices; however, other system resources must generally not be shared.
* To fully utilize a faster CPU, a faster Front Side Bus (FSB) should also be employed.
* To access extended memory, protected mode must be used.
* Memory modules must be placed securely and tightly in the motherboard sockets.
* SIMM modules must be inserted at an angle of approximately 60 degrees, then moved upwards to a perpendicular position.
* DIMM modules must be inserted vertically and locked into position using their special plastic clips.
* For Pentium systems, Bank 0 must be filled first before other banks. For instance, if Bank 0 is filled with 8MB, another 8MB must be stored in Bank 1 for processing. Failure to fill Bank 0 will prevent the PC from identifying subsequently installed RAM.
* When using two DIMMs of different sizes, install the larger DIMM in Bank 0 and the smaller in Bank 1.
* When using two DIMMs of identical size but one is single-sided and the other double-sided, install single-sided DIMMs in Bank 0 and double-sided DIMMs in Bank 1.
* If a motherboard has unused ports (e.g., video ports), they must be disabled (e.g., by setting jumpers or switches) to prevent hardware conflicts, crashes, or interference.
* The system must always use correct CMOS settings for proper system confirmation.
* Installed components must have standard CMOS settings.
* All available Level-1 and Level-2 cache memory in the system must be enabled via CMOS settings.
* Main memory (RAM) must be set to minimum wait state values; however, setting values too low can cause the system to hang.
* ROM shadowing must be enabled to increase system performance.
* Power management features must be enabled in the system.
* Both the drive and drive controller must be mutually supported.
* Always use the fastest data transfer protocol for drive access.
* For the CTCHIPZ utility, the chipset type must be known to select the correct `.CFG` configuration file.
* Accurate system knowledge is required to configure the system; otherwise, the computer may not boot.
* To set video characteristics, shadow memory must be configured, and on-board video memory must be disabled.
* For legacy products that do not detect Plug and Play (PnP) details, settings must be entered on the PnP/PCI page in CMOS.
* For Hard Disk C, if WPre (Write Precompensation) has no value in newer computers, it must be set to a negative or maximum value to avoid calculations.
* For Hard Disk C, if LZ (Landing Zone) has no value in newer computers, it must be set to 0 or the maximum number of cylinders.
* To maintain boot speed, select the lowest time for HDD delay.
* To speed up booting time, Quick POST can be selected in BIOS to skip some checks (e.g., memory count).
* When installing a sound card, select IRQ numbers, base I/O addresses, or DMA channels that do not conflict with other devices.
* Each SCSI logical unit must have a unique ID number ranging from 0 to 7; duplicate SCSI IDs are not allowed unless Logical Unit Numbers (LUNs) are utilized.
* The SCSI adapter should generally be set to ID7.
* The primary SCSI hard drive should generally be set to ID0.
* The secondary SCSI hard drive should generally be set to ID1.
* If using devices that utilize LUNs (e.g., a CD jukebox), LUNs support must be enabled in the host adapter's BIOS or device drivers.
* There must be no resource conflicts (IRQs, BIOS addresses, or I/O) in the SCSI controller; ensure the PCI slot containing the SCSI host adapter is active and uses a unique IRQ.
* If SCSI hard drives are present in the system and IDE drives are not, set the drive entries under CMOS to "none".
* For USB, the BIOS must assign an Interrupt Request Line (IRQ) to the root USB controller, and this IRQ must be assigned through the CMOS setup.
* The hard drive jumper must be set to "Master" if it is the only hard disk, or "Slave" if a second hard disk is being added.
* A CD-ROM drive's jumper can be configured as 'Slave' (on the same IDE cable as the hard drive) or 'Master' (on a separate IDE cable).
* When using Windows 3.1 drivers with a sound card, ensure the mixer control program is used to adjust volume. Specifically, confirm that the "Mute All" and "Mute Wave" checkboxes are not selected, Balance sliders for Volume Control and Wave are centered, and Volume Control and Wave sliders are at least halfway to the top.

## IV. Installation & Physical Assembly

* Memory modules must be inserted gently into their motherboard sockets; excessive pressure or incorrect insertion angle (for SIMMs) or vertical alignment (for DIMMs) can cause breakage. The modules must snap securely into place.
* When replacing a damaged memory socket, the motherboard must be removed, the damaged socket detached, and a new socket soldered in.
* Memory and socket contacts must engage simultaneously to prevent contact corrosion.
* Before beginning any upgrade process, a thorough plan must be in place, including verifying existing component functionality and identifying upgrade needs.
* When upgrading the motherboard, carefully review specifications due to unique features.
* When upgrading to AMD or dual-core processors, the motherboard layout must be planned to easily accommodate a heat sink for extra heat dissipation.
* The new motherboard must be placed gently inside the system, ensuring slots and ports are properly aligned with the case openings; do not apply force.
* The mounting holes of the case must match the mounting holes of the motherboard.
* When fixing motherboard bolts, ensure the motherboard does not contact conductive materials and always use a nonconductive washer between the bolt and the motherboard.
* After installation, the system must complete POST successfully and boot.
* Hardware drivers for any newly installed components must be installed.
* When installing cards into PCI slots, ensure they point out through the slots at the back of the PC cabinet. Leave sufficient space between cards for cooling airflow, particularly next to potentially heat-generating AGP cards.
* All back-panel ports (LAN, USB, PS/2, parallel, etc.) must fit through their respective slots on the PC case.
* The standard 20-pin ATX power cable from the SMPS must be connected to the motherboard.
* Auxiliary 12V ATX power connections must be connected to modern motherboard/processor combinations if required.
* The hard disk must be placed in the case and fastened with 4 screws.
* A power supply cable must be connected to the hard drive.
* A power supply cable must be connected to the CD-ROM drive.
* The SCSI host adapter card must be inserted slowly and firmly into its slot and secured with a screw to tighten the bracket.
* The computer's drive activity LED cable must be connected to the suitable connector on the SCSI card.
* During SCSI adapter installation, ensure all other bus connections are proper if needed.
* When installing memory, ensure the two latches on the motherboard slot are apart before insertion and begin installation with the lowest-numbered slot (usually slot 0).
* When upgrading an add-on video card, remove the old card and its drivers before installing the new video card and its drivers.
* When upgrading to an AGP video card with integrated motherboard video, disable the on-board video in the BIOS before installing the AGP video card and its drivers.
* When inserting a graphics card into an AGP slot, ensure it is fully seated and not sitting up at either end.

## V. Resource Management & Allocation

* Interrupt 0 and Interrupt 1 are high priority and must not be available to the ISA Bus, as they handle the timer chip and keyboard respectively.
* Any card inserted in the eighth expansion slot of an 8-bit ISA PC must provide a special signal called "card selected" on pin labeled B8, due to tighter timing requirements for this slot.
* A +3.3V PCI connector must include a key at the 12th position to prevent insertion of a +5V board into a +3.3V bus.
* A +5V PCI connector must include a key at the 50th position to prevent insertion of a +3.3V board into a +5V slot.
* The Linux kernel will not accept addresses that conflict with other devices or ones that the hardware cannot natively support.

## VI. Cabling & Connectivity

* SCSI cables must be terminated with a terminating resistor, and proper terminations (preferably active) must be present at both ends of the SCSI cable.
* SCSI devices must use 50-pin or 68-pin cables.
* If using an external SCSI device, the adapter should have two SCSI connectors for chain connectivity.
* SCSI peripheral devices must offer built-in cable termination.
* Do not use high-speed USB cables with low-speed cables, as this can cause signal distortion over long distances.
* The maximum length of a standard USB cable is 5 meters for high-speed devices and 3 meters for low-speed devices; exceeding these lengths may significantly decrease signal quality and prevent proper device function.
* SCSI cable quality must be high, and cables must be securely attached to each device.
* Avoid using specialized SCSI cables that may not be universally supported by all devices.
* Keep SCSI cable lengths as short as possible to optimize signal integrity.

## VII. Power Management

* Ensure the AC power supply is in proper working order.
* If the PC's AC connection is shared with heavy loads (e.g., water motor, boiler), use another dedicated power supply connector for the PC.
* The computer's power supply must be sufficient to handle all installed devices, including SCSI devices, and should be at least 250W for a basic system with a monitor.
* The motherboard/processor combination must have an auxiliary power connection in addition to the standard ATX power supply if required.
* High-power USB devices (e.g., printers, scanners) must have their own power supplies and draw minimal power from the USB bus.
* If devices connected to a USB root hub do not work, verify the power requirements of the bus; devices drawing too much or too little power will not function.

## VIII. Software & Drivers

* Always ensure the correct drivers are being used for the video card.
* When upgrading system components (motherboard, processor, or operating system), uninstall old device drivers, download the latest suitable drivers, and then reinstall them.
* SCSI device drivers must be compatible with the standard protocol used by the adapters; both the SCSI host adapter and peripherals require compatible device drivers to operate properly.
* USB devices designed for UHCI host controllers may not be supported by OHCI controllers and may not function properly.
* PnP device drivers must not assign resources directly but only identify the requested resources.
* A PnP driver must fulfill specific criteria, including providing required PnP entry points, handling required PnP IRPs, and adhering to PnP guidelines.
* Every type of bus on a system must have a corresponding bus driver.
* One function driver must be loaded by the Plug and Play Manager for each device.
* Every device must have at least two (bus driver and function driver) or three (including an optional filter driver) driver layers.
* Specific USB devices require related drivers to be installed prior to their functioning on any computer.
* DOS drivers for SCSI host adapters and non-HDD devices must be properly installed in CONFIG.SYS and AUTOEXEC.BAT.
* Necessary protected mode drivers for SCSI host adapters and devices must be properly installed when working under Windows environments.

## IX. Maintenance & Safety Procedures

* A solid understanding of the physical and mechanical concepts of a PC and its components is essential before troubleshooting.
* Exercise extreme caution when using slots for different processors.
* Removing a fitted memory module is risky and must be performed with great care.
* If epoxy is used for socket breaks or cracks, ensure adequate ventilation.
* Circuit damage or a destroyed motherboard cannot typically be repaired.
* Always back up the entire system before initiating any upgrade process.
* Follow comprehensive precautionary measures to prevent electrostatic discharge (ESD) when handling motherboards and components. This includes:
  * Cabling an antistatic mat to the motherboard for proper grounding.
  * Having enough antistatic mats to cover the entire work area.
  * Avoiding placing the motherboard on an electrostatic area.
  * Using an antistatic strap with proper grounding while handling components.
  * Holding components from the edges, avoiding direct contact with circuit chips or pins.
  * Placing disassembled components in antistatic bags.
* Avoid performing upgrade processes in dry weather due to the increased possibility of electrostatic charge creation.
* After taking ESD precautions during a motherboard upgrade, load updated CMOS settings onto the new motherboard's CMOS.
* Exercise extreme caution when handling screwdriver blades to avoid damaging the motherboard.
* Always turn off the system and unplug it from the AC receptacle before opening the cabinet cover.
* Label internal components and cables to facilitate accurate reassembly.
* Remove screws gently when detaching the motherboard; do not apply force, as it may cause damage.
* Refer to the user manual for clarifications during installation procedures.
* Exercise extreme caution when reviewing and setting CMOS settings; initially set CMOS variables to their default state and reboot the system.
* Ensure device managers are free from errors after any installation or upgrade.
* Take proper safety measures to protect yourself from injury during any PC work.
* Avoid allowing screws, paper clips, or any conducting wires to come into contact with internal components, as they can cause short circuits or motherboard failure.
* Verify that the screws connecting the motherboard to the case lead to proper grounding.
* Ensure there is sufficient space between conductive materials and the motherboard.
* Do not overtighten screws, as this can lead to erratic connections on the motherboard.
* Replacing a motherboard should be considered a last resort solution for persistent failures or for defective integrated components like a parallel port.
* Exercise caution when clearing CMOS settings, as crucial settings, if lost, are difficult to retrieve.
* The CMOS chip and CMOS battery must be maintained separately.
* The CMOS battery needs to be changed frequently.
* When replacing the CMOS battery, ensure a CMOS backup is available on an external disk. The procedure requires shutting down the computer, unplugging the system, carefully removing and recycling the old battery, installing the new battery based on manufacturer instructions, securing it, restarting, going to CMOS setup to restore settings, and then booting from a disk containing setup routines.

## X. Troubleshooting & Diagnostics

* When inspecting a PC for repair or replacement, ensure all connectors and cables, including the motherboard's power cable, are properly connected and tight.
* Verify that CPU chips, ROM chip, CMOS, and RTC module are mounted properly in their respective sockets.
* If .wav files play improperly or are unplayable, the files may be damaged. Check the Audio Format box for missing information; if missing, the file is likely damaged. Confirm by playing other .wav files compressed using the same method.
* If experiencing video subsystem problems or system instability in Windows, verify that the issue is not due to faulty or incorrect drivers. Install the latest motherboard chipset drivers, uninstall any old display drivers, and then install the latest display drivers.
* Disable the sound system if troubleshooting video issues.
* Disable the AGP port if troubleshooting video issues.
* Perform physical checks, including testing the CPU and RAM, checking the power supply, verifying that a separate video card adapter is properly seated, examining the monitor cable for broken/bent pins, and ensuring the monitor cable to the VGA port is secure.
* Verify the correct jumper settings for video cards mounted to the motherboard by consulting documentation.
* If the display goes blank after the initial startup screen, suspect an incorrect video driver installation.
* To resolve an incompatible video driver in Windows XP, start the computer in Safe Mode (by pressing F8 during startup), select Safe Mode, and then install the correct video driver via Device Manager.
* If poor display persists after driver checks, adjust the resolution and refresh rate for the video adapter card. If unable to select the desired resolution or refresh rate, check that the operating system has correctly identified the card using Device Manager, and update the driver if necessary. If the listed monitor in display settings is incorrect, update the monitor driver.
* If videos and animations are not correctly displayed, use the DirectX Diagnostic Tool (DxDiag.exe) to determine if the video card adapter driver supports DirectDraw. If it does not pass DirectDraw tests, update the video adapter driver.
* If a USB device should be automatically detected but isn't, troubleshoot by checking for faulty devices, incorrectly configured hardware, mismatched cables, outdated firmware, or USB root hub problems.
* If a USB device is not recognized, download the latest Windows OS updates, including the latest Service Pack, after creating a system restore point.
* To fix a previously working USB device that stops, use System Restore to revert to an earlier restore point.
* To perform power cycle troubleshooting for USB devices: detach the USB device, turn off the computer, unplug the power supply, wait one minute, plug the power cord back in, turn on the computer, and reinsert the USB device once the Windows OS is fully loaded.
* If a USB device is not working, connect it directly to the computer (without extension cables) to rule out cable issues, and verify that the USB cable is compatible with your plug-and-play USB device.
* If a power cycle does not resolve a USB port issue, update the USB firmware and system BIOS.
* If a USB plug-and-play device still does not work after other checks, consider corrupted USB controllers or bad USB ports; if ports are confirmed bad, they must be replaced.
* To reinstall USB controllers: Open Device Manager, expand "Universal Serial Bus Controllers," right-click each controller, and select "Uninstall," ignoring system instability messages.
* An exclamation mark in a yellow circle or triangle next to a root hub in Device Manager indicates an error.
* If firmware malfunctions result in a second copy of a device loading in Device Manager or reappearing as a second instance after removal and reinsertion, verify you have the most up-to-date firmware for the device.
* During SCSI host adapter installation, verify that all bus connections are proper if needed.
* Verify the SCSI IDs of each SCSI device and properly check the termination end point.
* Verify successful SCSI installation by confirming the new SCSI host adapter is listed in System Properties (Device Manager).

## Key Highlights

* Always back up the entire system before initiating any upgrade process to prevent potential data loss.
* Follow comprehensive precautionary measures, such as proper grounding and handling components by their edges, to prevent electrostatic discharge (ESD) when working with PC hardware.
* Ensure memory modules within a bank have identical size, speed, and RAM technology, as mismatched modules will prevent the system from recognizing them.
* When upgrading system components, always uninstall old device drivers and then install the latest suitable drivers for optimal performance and compatibility.
* The computer's power supply must be sufficient for all installed devices, with a minimum of 250W recommended for a basic system with a monitor.
* SCSI cables require proper termination with a resistor at both ends, preferably active terminations, for correct device functionality.
* Exercise extreme caution when reviewing and setting CMOS (BIOS) options; it is advisable to initially set variables to their default state before making custom adjustments.
* During physical assembly, insert components gently and securely, ensuring proper alignment, and leave sufficient space between expansion cards for adequate cooling airflow.

## Example ideas

* Conduct a comprehensive review to identify which rules remain relevant for modern computing architectures (e.g., PCIe, NVMe, DDR5) and which are obsolete or specific to legacy systems.
* Perform a gap analysis to identify critical missing topics for contemporary system architecture, configuration, and maintenance, such as virtualization, cloud infrastructure, and advanced security practices.
* Investigate opportunities to automate manual configuration, installation, and troubleshooting processes described, utilizing modern tools for configuration management, scripting, and infrastructure as code.
* Develop a strategy for updating or archiving this documentation, considering its target audience (e.g., legacy support, foundational training) and integrating it with current technical standards and practices.
