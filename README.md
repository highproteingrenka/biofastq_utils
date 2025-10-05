# Biofastq_utils
A small Python library for working with nucleotide sequences and FASTQ data.

It includes two main modules:

filter_fastq — filtering of reads by GC composition, length, and average quality (phred33).

run_dna_rna_tools is a convenient way to perform basic operations on DNA/RNA (reverse, complement, etc.).

### Requirements
Python 3.10+
External dependencies: none (standard Python)

### Installation
Copy the module files to your project and import them.

### Structure
biofastq_utils/

filter_fastq.py # calculate_gc, calculate_average_quality, filter_sequence
module.py # is_dna, is_rna, is_nucleic_acid, transcribe, reverse, complement, reverse_complement
run_dna_rna_tools.py # module operation
README.md

### filter_fastq.py
Library for filtering FASTQ sequences by GC content, length and quality.
Main functions:

calculate_gc - calculate sequence GC content

calculate_average_quality - calculate average read quality

filter_sequence - check sequence against criteria

filter_fastq - filter dictionary of sequences

Usage example:
filtered = filter_fastq(
    sequences,
    gc_bounds=(20, 80),
    length_bounds=(50, 150),
    quality_threshold=30
)

### run_dna_rna_tools
Library for DNA and RNA sequence manipulation.
Main functions:

is_dna / is_rna / is_nucleic_acid - check sequence type

transcribe - DNA → RNA transcription

reverse - reverse sequence

complement - complementary strand

reverse_complement - reverse complementary strand

run_dna_rna_tools - universal function for all operations

Usage example:

#### Type checking
run_dna_rna_tools("ATCG", "is_dna")

#### Transcription
run_dna_rna_tools("ATCG", "transcribe")

#### Reverse complement
run_dna_rna_tools("ATCG", "reverse_complement")
