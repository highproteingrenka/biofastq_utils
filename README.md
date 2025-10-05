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

main.py contains filter_fastq(), run_dna_rna_tools()
module.py contains calculate_gc, calculate_average_quality, filter_sequence
module_2.py contains is_dna, is_rna, is_nucleic_acid, transcribe, reverse, complement, reverse_complement

README.md

### filter_fastq.py
Library for filtering FASTQ sequences by GC content, length and quality.
Main functions:

calculate_gc - calculate sequence GC content

calculate_average_quality - calculate average read quality

filter_sequence - check sequence against criteria

filter_fastq - filter dictionary of sequences

### Usage example:

Parameters:
gc_bounds: (low, high) as a percentage, inclusive.
You can pass a single number x. It will be considered the upper bound of [0, x].

length_bounds: (low, high) for the length, inclusive.

quality_threshold: minimum average quality (Phred+33).

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

### Usage example:

#### Type checking
run_dna_rna_tools("ATCG", "is_dna")

#### Transcription
run_dna_rna_tools("ATCG", "transcribe")

#### Reverse complement
run_dna_rna_tools("ATCG", "reverse_complement")
