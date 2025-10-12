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

def as_interval(bounds: tuple[float, float] | int | float, *, default_lo: float, default_hi: float) -> tuple[float, float]:
    """
    Turns a single number (as an upper bound) or a tuple into an interval [lo, hi].
    """
    if isinstance(bounds, (int, float)):
        return float(default_lo), float(bounds)
    lo, hi = bounds
    return float(lo), float(hi)

def passes_length(sequence: str, length_bounds=(0, 2**32)) -> bool:
    lo, hi = as_interval(length_bounds, default_lo=0, default_hi=2**32)
    n = len(sequence)
    return lo <= n <= hi


def passes_gc(sequence: str, gc_bounds=(0, 100)) -> bool:
    lo, hi = as_interval(gc_bounds, default_lo=0, default_hi=100)
    gc = calculate_gc(sequence)
    return lo <= gc <= hi


def passes_quality(quality: str, threshold=0) -> bool:
    avg_q = calculate_average_quality(quality)
    return avg_q >= float(threshold)

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
        if len(sequence)!= len(quality):
        return False
    return (
            passes_length(sequence, length_bounds)
            and passes_gc(sequence, gc_bounds)
            and passes_quality(quality, quality_threshold)
    )

from pathlib import Path
def read_fastq(path: str) -> dict:
    path_to_file = Path(path)
    seqs={}
    with path_to_file.open("r") as file_fastq:
        while True:
            name = file_fastq.readline()
            if not name:
                break  
            seq = file_fastq.readline()
            plus = file_fastq.readline()
            qual= file_fastq.readline()

            if not (seq and plus and qual):
                break

            name = name.rstrip("\n\r")
            seq = seq.rstrip("\n\r")
            plus = plus.rstrip("\n\r")
            qual = qual.rstrip("\n\r")

            seqs[name] = (seq, qual)
    return seqs

def write_fastq(seqs: dict, output_fastq: str) -> Path:
    out_dir = Path("filtered")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / Path(output_fastq).name  
    with out_path.open("w") as out:
        for header, (seq, qual) in seqs.items():
            out.write(f"{header}\n{seq}\n+\n{qual}\n")
    return out_path
