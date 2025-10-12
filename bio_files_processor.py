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

import re

def parse_blast_output(input_txt: str, output_txt=None) -> str:
    """
        Parse a BLAST TXT report, collect the best-hit
        and write them to a text file,
        one description per line.

        Args:
            input_txt: Path to the BLAST TXT report.
            output_txt: Optional path to the output file. If None, the output file
                will be created next to the input with suffix '_oneline.txt'


        Returns:
            The path to the written output file.
    """
    if output_txt is None:
        base_name = os.path.splitext(input_txt)[0]
        output_txt = f"{base_name}_oneline.txt"

    best_titles = parse_blast_not_sorted(input_txt)
    sorted_best_titles = sorted(best_titles, key=str.lower)
    with open(output_txt, 'w') as outfile:
        for title in sorted_best_titles:
            string = str(title).strip()
            if string:
                outfile.write(string + "\n")
    return output_txt

def parse_blast_not_sorted(input_txt: str) -> list[str]:
    """
    Extract the most appropriate description (leftmost column) for each query from the BLAST TXT report.

    The function scans the header line
    of the "Sequences leading to significant alignment:" section for each query,
    then writes the first line of the description column.
    its description column. Column borders are defined by two or more spaces
    between the columns, this is how BLAST formats the table with pairwise output.

    Args:
    input_txt: Path to the BLAST TXT report.

    Returns:
    list: best-hit Description strings (one per query).

    """
    re_desc = re.compile(r"^\s*(?P<desc>\S.*?)(?:\s{2,}.*)?$")
    header_start_words = {
        "description", "scientific", "common", "taxid", "max", "total",
        "query", "e", "per.", "ident", "len", "accession", "name"
    }
    best_titles = []
    in_table = False


    with open(input_txt) as blast_file:
        for raw in blast_file:
            line = raw.rstrip("\r\n")
            if line.strip().lower().startswith("sequences producing significant alignments"):
                in_table = True
                continue
            if not in_table:
                continue

            stripped = line.strip()
            low = stripped.lower()
            if not stripped:
                continue

            if (
                    line.startswith(">")
                    or line.startswith("Query=")
                    or low.startswith("sequence id:")
                    or low.startswith("range ")
                    or low.startswith("score:")
                    or low.startswith("method:")
                    or low == "query"
                    or low == "sbjct"
                    or "no significant similarity found" in low
            ):
                in_table = False
                continue
            first_word = stripped.split(None, 1)[0].lower()
            if first_word in header_start_words:
                continue

            match_row = re_desc.match(line)
            if match_row:
                desc = match_row.group("desc").rstrip()
                best_titles.append(desc)
                in_table = False

        return best_titles
