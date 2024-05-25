# Lesson 2: Tuples
# 1. Tuple Mastery in Python

def format_itineraries(itineraries):
    """
    Formats flight itineraries from a list of tuples.
    Each tuple contains (traveler_name, origin, destination).
    Returns a formatted string.
    """
    formatted_string = ""
    for i, (traveler, origin, destination) in enumerate(itineraries, start=1):
        formatted_string += f"Itinerary {i}: {traveler} - From {origin} to {destination}\n"
    return formatted_string.strip()  # Remove trailing newline

# Example usage
flight_data = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
formatted_itineraries = format_itineraries(flight_data)
print(formatted_itineraries)
