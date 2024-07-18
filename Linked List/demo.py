def checkOnesSegment(s: str) -> bool:
    # Split the string by '0's
    segments = s.split('0')
    print(segments)
    
    # Count the number of non-empty segments
    count_of_ones_segments = sum(1 for segment in segments if segment)
    print(count_of_ones_segments)
    
    # Return true if there is at most one non-empty segment
    return count_of_ones_segments <= 1

# Test the function with the example input
s = "110"
print(checkOnesSegment(s))  # Output: false
