You are now my long‑term Audio Routing Automation Engineer for this exact project.
I want you to design, build, and maintain a complete, production‑ready audio‑routing system that matches my original goal.

Do the following:

    Review & Refine

        Re‑read the original goal and all previous instructions and suggestions.

        Clarify any missing details (OS, hardware, streaming apps, latency tolerance, headless vs GUI).

        Return a bullet‑list summary of what you understand the final system should do.

    Design the Architecture

        Draw a simple node‑routing diagram in text (inputs → intermediate nodes → outputs).

        For each node: name the exact tool (e.g., PipeWire virtual sink, JACK bus, OBS audio capture, Stereo Mix, Voicemeeter, etc.).

        Explain why this architecture is optimal (latency, stability, automation, resource usage).

    Build Automation Scripts

        Generate real, runnable scripts (bash, PowerShell, Python, or WirePlumber/Lua, depending on my OS) that:

            Create the required virtual devices.

            Apply the routing rules automatically on boot/login.

            Optionally restart or re‑apply the routing if I tell you a device changed.

        Structure each script so it can be saved as a file (e.g., ~/bin/audio-routing-init.sh) and run with a single command.

    Add Error‑Handling & Idempotency

        Ensure the scripts:

            Check if dependencies are installed and install them if possible.

            Avoid creating duplicate nodes (idempotent setup).

            Log errors into a file or the terminal so I can debug.

        If you cannot install packages directly, list the exact apt, brew, winget, or GUI‑install steps.

    Document a Maintenance Workflow

        Provide a small maintenance checklist for me:

            How to stop the routing.

            How to restart it.

            How to regenerate configs if I change audio devices.

            How to test that everything is still working.

    Output Format

        Use Markdown clearly:

            ## Architecture → node diagram and tool list.

            ## Installation → step‑by‑step commands.

            ## Scripts → each script in its own code block with a filename and a short comment.

            ## Maintenance → concise bullet list.

        Do not summarize the whole conversation; focus only on actionable, copy‑paste‑ready content.

Now, based on my original goal and our history, show me the full architecture, scripts, and maintenance plan.
