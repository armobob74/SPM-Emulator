from re import findall

def parseLogfile(filename='./logfile.txt'):
    """
    This function tells the emulator what ports are available to it
    input: path to the logfile where socat output is stored
    output:
        if socat is running, return [pty1, pty2]
        if socat is not running, return -1
    """
    with open(filename) as f:
        log_str = f.read()
    if 'exit' in log_str: 
        raise RuntimeError('Stale logfile: is socat running?')
    ports = findall('(/dev/pts/\d+)', log_str)
    if len(set(ports)) != 2:
        raise RuntimeError('Didn\'t get 2 distinct ports from logfile: is socat running?')
    return ports

if __name__ == "__main__": 
    port_a, port_b = parseLogfile()
