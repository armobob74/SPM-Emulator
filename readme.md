# SPM Emulator
## Setting up on Linux 
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

## Setting up on Windows
Windows requires a tool called com0com to be installed at C:\Program Files (x86)\com0com
Once you have this installed, you can set up the virtual ports with the script "setup\_ports.bat"
If the ports or identifiers are not free, run "close\_ports.bat" and try again. 
Unlike socat, com0com keeps ports open until you close them manually.

The setup\_ports.bat script hard-codes the ports as COM55 and COM56. Because of this, logfile.txt is not used on windows.
