import subprocess
from typing import Optional, Tuple, Union

def ping(ip: str, count: int = 1) -> Tuple[bool, Optional[Exception]]:
    """
    Executes a ping command to the specified IP with the given count.
    
    Args:
        ip: The IP address or hostname to ping
        count: The number of ping packets to send (default: 1)
        
    Returns:
        A tuple containing:
        - Boolean indicating success (True) or failure (False)
        - None if successful, Exception object if failed
    """
    try:
        # Execute the ping command and capture its output
        result = subprocess.run(
            ["ping", "-c", str(count), ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        print(result.stdout)  # Print the output as a string
        return True, None     # Return success with no error
    except subprocess.CalledProcessError as e:
        print(e.stderr)       # Print the error output
        return False, e       # Return failure with the error