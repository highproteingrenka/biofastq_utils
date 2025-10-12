from modules.module import (
    calculate_gc,
    calculate_average_quality,
    filter_sequence,
    read_fastq,
    write_fastq,
)


from modules.module_2 import (
    is_dna,
    is_rna,
    is_nucleic_acid,
    transcribe,
    reverse,
    complement,
    reverse_complement,
)


def run_dna_rna_tools(*sequences: str) -> str:
    """
    Universal function that applies DNA/RNA operations (transcription, complement, reverse, etc.) to one or multiple sequences.

    *sequences: str
                Last argument: operation name (str)
                All previous arguments: sequences to process (str)
    Returns single result if one sequence provided, list of results otherwise.
    """
    *seqs, operation = sequences
    operations = {
        "is_nucleic_acid": is_nucleic_acid,
        "transcribe": transcribe,
        "reverse": reverse,
        "complement": complement,
        "reverse_complement": reverse_complement,
    }
    if operation in operations:
        func = operations[operation]
        results = [func(seq) for seq in seqs]
        return results[0] if len(results) == 1 else results


def filter_fastq(
    input_fastq: str, output_fastq: str, *, gc_bounds=(0, 100), length_bounds=(0, 2**32), quality_threshold=0
) -> dict:
    """
    Filters FASTQ sequences according to the specified criteria.

    input_fastq: str (path)
    output_fastq: str (path)
    gc_bounds: tuple / float
    length_bounds tuple / float
    quality_threshold int / float

    Returns dict.
    """
    seqs = read_fastq(input_fastq)
    filtered = {
        name: (seq, qual)
        for name, (seq, qual) in seqs.items()
        if filter_sequence(
            seq,
            qual,
            gc_bounds=gc_bounds,
            length_bounds=length_bounds,
            quality_threshold=quality_threshold,
        )
    }
    write_fastq(filtered, output_fastq)
    return filtered
