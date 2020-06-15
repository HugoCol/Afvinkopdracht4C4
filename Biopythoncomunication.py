# call modules
from Bio.Seq import Seq
from Bio.Seq import transcribe
from Bio.Alphabet import IUPAC
from Bio.Blast import NCBIWWW
import re

def validSequence(seq):
    """
    Use RE to check if a sequence contains DNA, RNA or protein
    characters
    :param seq: from user input
    :return: definition of the sequence
    """
    definition = ''

    validdna = '^[ATCG]+$'
    validprotein = '^[GPAVLIMCFYWHKRQNEDST\\*]+$'
    validrna = '^[AUCG]+$'
    if re.search(validdna, seq):
        definition = 'dna'
    if re.search(validrna, seq) and definition != 'dna':
        definition = 'rna'
    if re.search(validprotein, seq) and definition != 'dna' and \
            definition != 'rna':
        definition = 'protein'
    if definition != 'dna' and definition != 'rna' and definition != \
            'protein':
        definition = 'This is not a organic sequence'

    return definition

def translate(dna_sequence):
    """

    :param dna_sequence: string of ACTG characters
    :return: transcription and translation of the string to AUCG and
    protein characters
    """
    # Turn the sequence in a Seq object, reverse complement and \
                                              # transcrbe it to RNA
    transcription = Seq(dna_sequence).transcribe().reverse_complement()

    # Get the transcription and translate is to a protein sequence
    translation = Seq(str(transcription)).translate()
    return transcription,translation



def blasting(translation):
    closest_match = NCBIWWW.qblast("blastn","nr",translation)

    return closest_match

