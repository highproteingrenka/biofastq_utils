### Biofastq_utils
A small Python library for working with nucleotide sequences and FASTQ data.

It includes two main modules:

**filter_fastq** — filtering of reads by GC composition, length, and average quality (phred33).

**run_dna_rna_tools** is a convenient way to perform basic operations on DNA/RNA (reverse, complement, etc.).

Add **bio_files_processor.py** a set of utilities for preprocessing biofiles.
The **convert_multiline_fasta_to_oneline** function brings FASTA to the canonical form "1 record = 2 lines":
a line with the title (>), then one line with the full sequence without newlines inside.

The **parse_blast_output** function extracts the best description (best hit) for each query 
from the BLAST text report in a "paired" format (classic TXT) 
and saves the descriptions to a text file — one description per line. 
The list is sorted alphabetically.

### Requirements
Python 3.10+
External dependencies: none (standard Python)

### Installation
Copy the module files to your project and import them.

### Structure
biofastq_utils/

bio_files_processor.py contains parse_blast_output(), convert_multiline_fasta_to_oneline
main.py contains filter_fastq(), run_dna_rna_tools()
module.py contains calculate_gc, calculate_average_quality, filter_sequence, read_fastq, write_fastq
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
    input_fastq: str, output_fastq: str,
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

### bio_files_processor.py
A set of utilities for preprocessing bioinformatic files.

**convert_multiline_fasta_to_oneline(input_fasta, output_fasta=None)**
Turns FASTA with multi-line sequences into the canonical "2 lines per record" format 
(header > and one line with the whole sequence). Writes the result to a new file.

**parse_blast_output(input_txt, output_txt=None)**
BLAST (TXT) extracts one best hit for each query from a text report 
and saves a list of descriptions (one line per record) to a file.
### Usage example:
from bio_files_processor import convert_multiline_fasta_to_oneline, parse_blast_output

convert_multiline_fasta_to_oneline("multi.fasta")         # -> multi_oneline.fasta
parse_blast_output("blast_report.txt")                    # -> blast_report_oneline.txt
