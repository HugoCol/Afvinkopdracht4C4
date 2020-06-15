# Ontwikkel een webapplicatie die in staat is om van een gegeven
# sequentie te bepalen of het DNA, RNA, eiwit of geen van drieen is.
#
# Wanneer de applicatie in staat is om te detecteren dat het om
# DNA gaat, geeft het de corresponderende RNA en eiwit sequenties.
#
# Als het een eiwit is geeft het meest waaarschijnlijke gen
# waar het van afkomstig is.

from Biopythoncomunication import validSequence,translate,blasting,read_XML
from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')
# home page
@app.route('/protein', methods=["POST", "GET"])
def index():
    '''
    input: dna sequence string from user input textbox
    :return: translated protein sequence
    '''
    translation = ''
    transcription = ''
    if request.method == "POST":
        seq = request.form.get("sequence", "")
        definition = validSequence(seq)
        if definition == 'dna':
            transcription,translation = translate(seq)
        elif definition == 'protein':
            blasting(seq)

        return render_template('home.html', title='Home',
                               proteins=seq,
                               transcription=transcription,
                               translation=translation)
    else:
        return render_template('home.html', title='Home',
                               proteins='')


# run the app
if __name__ == '__main__':
    app.run()
