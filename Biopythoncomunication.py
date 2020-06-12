# call modules
from Bio.Seq import Seq
from Bio.Seq import transcribe
from Bio.Alphabet import IUPAC
from Bio.Blast import NCBIWWW

def validSequence():
    definition = ''
    seq = 'ACTG'
    validdna = 'ACTG'
    validprotein = 'MKLTYI'
    validrna = 'ACTU'
    for letter in seq:
        if letter in validdna:
            definition = 'DNA'

    if definition != 'DNA':
        for letter in seq:
            if letter in validrna:
                definition = 'RNA'


    if definition != 'DNA' or definition != 'RNA':
        pass
    else:
        for letter in seq:
            if letter in validprotein:
                definition = 'Protein'


    return definition

def translate():

    sequence = "ATGCCGATCGTATCA"
    dna_seq = Seq(sequence)
    transcription = dna_seq.transcribe().reverse_complement()

    rna_sequence = Seq(str(transcription))
    translation = rna_sequence.translate()

    return transcription,translation



def blasting(translation):
    closest_match = NCBIWWW.qblast("blastn","nr",translation)

    return closest_match

if __name__ == '__main__':
    # print(validSequence())
    print(translate())
    transcription,translation = translate()
    blasting(translation)
    print(blasting())
