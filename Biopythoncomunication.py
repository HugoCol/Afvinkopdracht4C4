# call modules
from Bio.Seq import Seq
from Bio.Seq import transcribe
from Bio.Alphabet import IUPAC
from Bio.Blast import NCBIWWW
import re
from xml.etree import ElementTree

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
    # else re.search(validprotein, seq) and definition != 'dna' and \
    #         definition != 'rna':
    else:   definition = 'protein'
    # if definition != 'dna' and definition != 'rna' and definition != \
    #         'protein':
    #     definition = 'This is not a organic sequence'
    print(definition)
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
    print(transcription,translation)
    return transcription,translation



def blasting(translation):
    print('Blast start')
    closest_match = NCBIWWW.qblast("blastn","nr",translation,
                                   format_type="XML", hitlist_size=1)

    # for line in blast_data:

    # XMLFile = 'testdata.xml'
    XMLFile = closest_match.read()

    # Door bestand heen gaan
    dom = ElementTree.parse(XMLFile)
    # Alle hits eruit zoeken
    hits = dom.findall(
        'BlastOutput_iterations/Iteration/Iteration_hits/Hit')
    # Voor elke hit

    datadic = {}

    for c in hits:

        # Haal de data uit de hit en zet deze in een zelfbeschrijvende variabele
        Hit_id = c.find('Hit_id').text
        discript = c.find('Hit_def').text
        totaallengte = c.find('Hit_len').text
        querybegin = c.find('Hit_hsps/Hsp/Hsp_query-from').text
        queryeind = c.find('Hit_hsps/Hsp/Hsp_query-to').text
        querycoverage = (int(queryeind) - int(querybegin)) / int(
            totaallengte)
        organis = discript.split('[')
        organism = organis[1].split(']')
        description = organis[0]
        organisme = organism[0]
        acessiecode = c.find('Hit_accession').text
        print(acessiecode)
        score = c.find('Hit_hsps/Hsp/Hsp_bit-score').text
        tscore = c.find('Hit_hsps/Hsp/Hsp_score').text
        evalue = c.find('Hit_hsps/Hsp/Hsp_evalue').text
        percidentity = c.find('Hit_hsps/Hsp/Hsp_identity').text
        queryseq = c.find('Hit_hsps/Hsp/Hsp_qseq').text


        # lineage = seqio_read[0]["GBSeq_taxonomy"].split(";")

        # Print alle data om te zien of het gewerkt heeft
        datalist = [Hit_id, description, organisme, acessiecode,
                    score,
                    tscore, evalue, percidentity, queryseq,
                    querycoverage]
    print(datalist)

    return datalist
