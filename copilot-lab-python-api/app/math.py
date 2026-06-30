import math


def calculate_sine(angle_radians: float) -> float:
    """
    Calculate the sine of an angle given in radians.
    
    Args:
        angle_radians: The angle in radians
    
    Returns:
        The sine value of the angle
    
    Example:
        >>> calculate_sine(math.pi / 2)
        1.0
    """
    return math.sin(angle_radians)


def calculate_sine_degrees(angle_degrees: float) -> float:
    """
    Calculate the sine of an angle given in degrees.
    
    Args:
        angle_degrees: The angle in degrees
    
    Returns:
        The sine value of the angle
    
    Example:
        >>> calculate_sine_degrees(90)
        1.0
    """
    angle_radians = math.radians(angle_degrees)
    return math.sin(angle_radians)
