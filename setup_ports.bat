cd C:\Program Files (x86)\com0com
setupc install 50 PortName=COM55 PortName=COM56
echo "Ports are open. They will be closed on next keypress."
pause
setupc remove 50