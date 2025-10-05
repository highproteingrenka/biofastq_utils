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
    "c": "g"
}
dict_complement_rna = {
    "A": "U",
    "U": "A",
    "C": "G",
    "G": "C",
    "a": "u",
    "u": "a",
    "g": "c",
    "c": "g"
}
def is_dna(*sequences: str)->str:
    """
    Check if all sequences contain only valid DNA nucleotides (A, T, G, C).
    *sequences: str
    Returns True if all characters are valid DNA nucleotides, False otherwise.
    """
    for seq in sequences:
        unique_chars = set(seq)
        valid_seq = (unique_chars <= alphabet_dna)
        return valid_seq

def is_rna(*sequences:str)->str:
    """
    Check if all sequences contain only valid RNA nucleotides (A, U, G, C).
    *sequences: str
    Returns True if all characters are valid RNA nucleotides, False otherwise.
    """
    for seq in sequences:
        unique_chars = set(seq)
        valid_seq = (unique_chars <= alphabet_rna)
        return valid_seq

def is_nucleic_acid(*sequences:str)->str:
    """
    Check if sequences contain valid nucleic acid characters (DNA or RNA).
    *sequences: str
    Returns True if all characters are valid DNA or RNA nucleotides, False otherwise.
    """
    for seq in sequences:
            unique_chars = set(seq)
            valid_seq = (unique_chars <= alphabet_rna) or (unique_chars <= alphabet_dna)
            return valid_seq
