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


def is_dna(sequence: str)->bool:
    """
    Check if all sequences contain only valid DNA nucleotides (A, T, G, C).
    sequence: bool
    Returns True if all characters are valid DNA nucleotides, False otherwise.
    """
    if not sequence:
        return False
    unique_chars = set(sequence)
    valid_seq = (unique_chars <= alphabet_dna)
    return valid_seq

def is_rna(sequence:str)->bool:
    """
    Check if all sequences contain only valid RNA nucleotides (A, U, G, C).
    sequence: bool
    Returns True if all characters are valid RNA nucleotides, False otherwise.
    """
    if not sequence:
        return False
    unique_chars = set(sequence)
    valid_seq = (unique_chars <= alphabet_rna)
    return valid_seq

def is_nucleic_acid(sequence:str)->bool:
    """
    Check if sequences contain valid nucleic acid characters (DNA or RNA).
    sequence: bool
    Returns True if all characters are valid DNA or RNA nucleotides, False otherwise.
    """
    if not sequence:
        return False
    unique_chars = set(sequence)
    valid_seq = (unique_chars <= alphabet_rna) or (unique_chars <= alphabet_dna)
    return valid_seq

def transcribe(sequence: str)->str:
    """
    Transcribe DNA to RNA by replacing T with U.
    sequence: str
    Returns transcribed sequence or None and WARNING for invalid input.
    """
    if is_nucleic_acid(sequence):
        transcribed_seq = ""
        for char in sequence:
            if char == "T":
                transcribed_seq += "U"
            elif char == "t":
                transcribed_seq += "u"
            else:
                transcribed_seq += char
    else:
        print("WARNING: invalid characters — return None")
        return
    return transcribed_seq

def reverse(sequence: str)->str:
    """
    Reverse the nucleic acid sequence.
    sequence: str
    Returns reversed sequence or None and WARNING for invalid input.
    """
    #for seq in sequences:
    if is_nucleic_acid(sequence):
        return sequence[::-1]
    else:
        print("WARNING: invalid characters — return None")
        return

def complement(sequence: str)->str:
    """
    Get complementary strand for DNA or RNA sequence.
    sequence: str
    Returns complementary sequence or None and WARNING for invalid input.
    """
    #for seq in sequences:
    if is_nucleic_acid(sequence) and is_dna(sequence):
            #for nucleotide in sequences:
        return "".join([dict_complement_dna[nucleotide] for nucleotide in sequence])
    elif is_nucleic_acid(sequence) and is_rna(sequence):
            #for nucleotide in sequences:
        return "".join([dict_complement_rna[nucleotide] for nucleotide in sequence])
    else:
        print("WARNING: invalid characters — return None")
        return
def reverse_complement(sequence: str)->str:
    """
    Get reverse complement of nucleic acid sequence.
    sequence: str
    Returns reverse complement or None and WARNING for invalid input.
    """
    #for seq in sequence:
    if is_nucleic_acid(sequence):
        reversed_seq = reverse(sequence)
        return complement(reversed_seq)
    else:
        print("WARNING: invalid characters — return None")
        return

def run_dna_rna_tools(*sequences: str)->str:
    """
    Universal function that applies DNA/RNA operations (transcription, complement, reverse, etc.) to one or multiple sequences.

    *sequences: str
                Last argument: operation name (str)
                All previous arguments: sequences to process (str)
    Returns single result if one sequence provided, list of results otherwise.
    """
    *seqs, operation = sequences
    operations = { "is_nucleic_acid": is_nucleic_acid, "transcribe": transcribe, "reverse": reverse,  "complement": complement, "reverse_complement": reverse_complement }
    if operation in operations:
        func = operations[operation]
        results = [func(seq) for seq in seqs]
        return results[0] if len(results) == 1 else results
