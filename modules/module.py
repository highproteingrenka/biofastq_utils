def calculate_gc(sequence: str) -> float:
    """
    Calculates the GC composition of a sequence as a percentage.

    Arguments:
    sequence: str

    Returns float.
    Raises exception if len(sequence) is 0
    """
    if len(sequence) == 0:
        return 0.0
    gc_count = sequence.upper().count("G") + sequence.upper().count("C")
    return (gc_count / len(sequence)) * 100


def calculate_average_quality(quality: str) -> float:
    """
    Calculates the average quality for a sequence

    Arguments:
    quality: str

    Returns float.
    """
    quality_scores = [ord(char) - 33 for char in quality]
    return sum(quality_scores) / len(quality_scores)


def filter_sequence(
    sequence: str,
    quality: str,
    gc_bounds=(0, 100),
    length_bounds=(0, 2**32),
    quality_threshold=0,
) -> bool:
    """
    Checks whether the sequence passes all filters.

    sequence: str
    quality: str
    gc_bounds: tuple / float
    length_bounds tuple / float
    quality_threshold int / float

    Returns bool.
    """
    seq_length = len(sequence)
    if isinstance(length_bounds, (int, float)):
        if not (seq_length <= float(length_bounds)):
            return False
    else:
        if not (length_bounds[0] <= seq_length <= length_bounds[1]):
            return False

    gc_content = calculate_gc(sequence)
    if isinstance(gc_bounds, (int, float)):
        if not (gc_content <= float(gc_bounds)):
            return False
    else:
        if not (gc_bounds[0] <= gc_content <= gc_bounds[1]):
            return False

    avg_quality = calculate_average_quality(quality)
    if avg_quality < quality_threshold:
        return False

    return True
