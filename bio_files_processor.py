import os
def convert_multiline_fasta_to_oneline(input_fasta: str, output_fasta=None) -> str:
    """
    Convert a FASTA file where sequences may span multiple lines into a FASTA where
       each record is exactly two lines: a header (starting with '>') and a single
       concatenated sequence line.

    Args:
        input_fasta: Path to the input FASTA file with potentially multi-line sequences.
        output_fasta: Optional path for the output FASTA file. If None, an output
            filename will be generated next to the input as with suffix '_oneline.txt'.

    Returns:
        The path to the written output FASTA file.
    """
    if output_fasta is None:
        base_name = os.path.splitext(input_fasta)[0]
        output_fasta = f"{base_name}_oneline.fasta"

    with open(input_fasta) as fasta_file, open(output_fasta, 'w') as outfile:
        current_header=None
        current_sequence=[]
        for line in fasta_file:
            line = line.strip()
            if line.startswith('>'):
                if current_header is not None:
                    outfile.write(f"{current_header}\n{''.join(current_sequence )}\n")
                current_header = line
                current_sequence = []
            else:

                current_sequence.append(line)


        if current_header is not None:
            outfile.write(f"{current_header}\n{''.join(current_sequence)}\n")
    return output_fasta
