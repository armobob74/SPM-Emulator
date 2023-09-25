# SPM Emulator
## introduction 
It's nice to have an emulator for testing purposes!
The first thing to do is set up two virtual ports on Linux using socat.
This is all handled by running the script emulator\_setup.zsh
```zsh
zsh emulator_setup.zsh
```
The output is written to logfile.txt, which is parsed by the parseLogfile() function to determine:
1. whether simulated-ports exist
2. what the pty names are

If the simulated ports do not exist, emulate.py asks the user to first run the socat script.
Otherwise, python starts emulating!
