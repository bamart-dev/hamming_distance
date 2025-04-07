def hamming_distance(strand1: str, strand2: str) -> int:
    """Returns number of differences between two DNA strands."""
    max_length = (
        len(strand2) if len(strand2) < len(strand1) else len(strand1)
        )
    difference = 0

    if not strand1 or not strand2:
        err = "An empty DNA strand has been provided."
        raise ValueError(err)

    if strand1.upper() == strand2.upper():
        return difference

    for i in range(max_length):
        if strand1[i].upper() == "U" or strand2[i].upper() == "U":
            return "A RNA strand has been passed in."

        if strand1[i].upper() != strand2[i].upper():
            difference += 1

    if len(strand1) > len(strand2):
        for base in strand1[max_length:]:
            difference += 1
    elif len(strand2) > len(strand1):
        for base in strand2[max_length:]:
            difference += 1

    return difference
