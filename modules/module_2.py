alphabet_rna = {"A", "G", "C", "U", "a", "g", "c", "u"}
alphabet_dna = {"A", "T", "G", "C", "a", "t", "g", "c"}
dict_complement_dna = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C",
    "a": "t",
    "t": "a",
    "g": "c",
    "c": "g",
}
dict_complement_rna = {
    "A": "U",
    "U": "A",
    "C": "G",
    "G": "C",
    "a": "u",
    "u": "a",
    "g": "c",
    "c": "g",
}


def is_dna(*sequences: str) -> str:
    """
    Check if all sequences contain only valid DNA nucleotides (A, T, G, C).
    *sequences: str
    Returns True if all characters are valid DNA nucleotides, False otherwise.
    """
    for seq in sequences:
        unique_chars = set(seq)
        valid_seq = unique_chars <= alphabet_dna
        return valid_seq


def is_rna(*sequences: str) -> str:
    """
    Check if all sequences contain only valid RNA nucleotides (A, U, G, C).
    *sequences: str
    Returns True if all characters are valid RNA nucleotides, False otherwise.
    """
    for seq in sequences:
        unique_chars = set(seq)
        valid_seq = unique_chars <= alphabet_rna
        return valid_seq


def is_nucleic_acid(*sequences: str) -> str:
    """
    Check if sequences contain valid nucleic acid characters (DNA or RNA).
    *sequences: str
    Returns True if all characters are valid DNA or RNA nucleotides, False otherwise.
    """
    for seq in sequences:
        unique_chars = set(seq)
        valid_seq = (unique_chars <= alphabet_rna) or (unique_chars <= alphabet_dna)
        return valid_seq


def transcribe(*sequences: str) -> str:
    """
    Transcribe DNA to RNA by replacing T with U.
    *sequences: str
    Returns transcribed sequence or None and WARNING for invalid input.
    """
    for seq in sequences:
        if is_nucleic_acid(seq):
            transcribed_seq = ""
            for char in seq:
                if char == "T":
                    transcribed_seq += "U"
                else:
                    transcribed_seq += char
        else:
            print("WARNING: недопустимые символы — верну None")
            return
        return transcribed_seq


def reverse(*sequences: str) -> str:
    """
    Reverse the nucleic acid sequence.
    *sequences: str
    Returns reversed sequence or None and WARNING for invalid input.
    """
    for seq in sequences:
        if is_nucleic_acid(seq):
            return seq[::-1]
        else:
            print("WARNING: недопустимые символы — верну None")
            return


def complement(*sequences: str) -> str:
    """
    Get complementary strand for DNA or RNA sequence.
    *sequences: str
    Returns complementary sequence or None and WARNING for invalid input.
    """
    for seq in sequences:
        if is_nucleic_acid(seq) and is_dna(seq):
            for nucleotide in seq:
                return "".join([dict_complement_dna[nucleotide] for nucleotide in seq])

        if is_nucleic_acid(seq) and is_rna(seq):
            for nucleotide in seq:
                return "".join([dict_complement_rna[nucleotide] for nucleotide in seq])
        else:
            print("WARNING: недопустимые символы — верну None")
            return


def reverse_complement(*sequences: str) -> str:
    """
    Get reverse complement of nucleic acid sequence.
    *sequences: str
    Returns reverse complement or None and WARNING for invalid input.
    """
    for seq in sequences:
        if is_nucleic_acid(seq):
            reversed_seq = reverse(seq)
            return complement(reversed_seq)
        else:
            print("WARNING: недопустимые символы — верну None")
            return
