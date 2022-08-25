from flask import Flask,url_for,render_template,request,send_file,redirect,request
from flask_uploads import UploadSet,configure_uploads,ALL,DATA
from spacy import blank
from werkzeug import secure_filename

from flask import Flask, make_response


# imporying lexnlp
from lexnlp_fun import lexnlp_entity

# Spacy work importing from spacy file

from spacy_fun import task_opt_org,task_opt_name,task_opt_place,task_opt_law,task_opt_quantity,task_opt_product
from spacy_fun import view_entity



# Other Packages
import os


# Summarization
from spacy_summarization import text_summarizer
from gensim.summarization import summarize
from nltk_summarization import nltk_summarizer

# Sumy Pkg
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

# summarization function
def sumy_summary(docx):
	parser = PlaintextParser.from_string(docx,Tokenizer("english"))
	lex_summarizer = LexRankSummarizer()
	summary = lex_summarizer(parser.document,3)
	summary_list = [str(sentence) for sentence in summary]
	result = ' '.join(summary_list)
	return result

# Initialize App
app = Flask(__name__)

# Configuration For Uploads
files = UploadSet('files',ALL)
app.config['UPLOADED_FILES_DEST'] = 'static/uploadedfiles'
configure_uploads(app,files)


@app.route('/')
def index():
	return render_template("index.html")


@app.route('/extract', methods=['GET', 'POST'])
def extract():
	if request.method == 'POST' and 'rawtext' in request.files:
		if request.form["submit"] == "Summary":
			file = request.files['rawtext']
			N = int(request.form["number"])

			filename = secure_filename(file.filename)
			file.save(os.path.join('static/uploadedfiles', filename))

			with open(os.path.join('static/uploadedfiles',filename), 'r+', encoding="utf-8") as f:
				c_text = f.read()
				# SpaCy
				fs_spacy = text_summarizer(c_text)
				# Gensim Summarizer
				fs_gensim = summarize(c_text,ratio=N/100)
				# NLTK
				fs_nltk = nltk_summarizer(c_text)
				# Sumy
				fs_sumy = sumy_summary(c_text)
			return render_template('summary.html',c_text=c_text,  fs_spacy=fs_spacy, fs_gensim=fs_gensim,fs_nltk=fs_nltk,fs_sumy=fs_sumy)
		elif request.form["submit"] == "Entity":
			file = request.files['rawtext']
			filename = secure_filename(file.filename)
			file.save(os.path.join('static/uploadedfiles', filename))

			with open(os.path.join('static/uploadedfiles',filename), 'r+', encoding="utf-8") as f:
				c_text = f.read()
				# From Spacy

				result_org,l_org = task_opt_org(c_text)
				result_places,l_place = task_opt_place(c_text)
				result_name,l_person = task_opt_name(c_text)
				result_law, l_law = task_opt_law(c_text)
				result_quantity, l_quntity = task_opt_quantity(c_text)
				result_product,l_product = task_opt_product(c_text)

				#From lexnlp 
				xy = lexnlp_entity(c_text)

				result_date = xy.date_time()
				result_acts = xy.acts()
				result_constraints= xy.constraints()
				result_condition = xy.conditioons()
				result_money = xy.get_money()
				result_trademark = xy.trademark()
				result_regulation = xy.regulation()
				result_copyright = xy.copyrights()
								
			return render_template('entity.html',c_text=c_text,
			result_org=result_org,l_org=l_org, result_places=result_places,l_place=l_place,result_name=result_name,
			l_person=l_person,result_law=result_law, l_law=l_law,result_quantity=result_quantity, l_quntity =l_quntity,
			result_product=result_product,l_product=l_product,
			result_acts=result_acts, l_acts= len(result_acts),l_dateTime=len(result_date),result_date=result_date,
			result_constraints=result_constraints,l_cons =len(result_constraints),
			result_condition=result_condition,l_cond=len(result_condition),result_money=result_money,l_money=len(result_money),
			result_trademark=result_trademark,l_trade= len(result_trademark),result_regulation=result_regulation,
			l_regu = len(result_regulation),result_copyright=result_copyright,l_copy =len(result_copyright)
			)
		elif request.form["submit"] == "View All Entity":
			file = request.files['rawtext']
			filename = secure_filename(file.filename)
			file.save(os.path.join('static/uploadedfiles', filename))

			with open(os.path.join('static/uploadedfiles',filename), 'r+', encoding="utf-8") as f:
				c_text = f.read()
				x =  view_entity(c_text)
			return render_template("all_entities.html",entity = x)




@app.route('/extract_typed', methods=['GET', 'POST'])
def extract_typed():
	if request.method == 'POST' and 'pasted' in request.form:
		if request.form['submit'] == "Summary":	
			pasted = request.form["pasted"]
			N = request.form["number"]
			# SpaCy
			fs_spacy = text_summarizer(pasted)
			# Gensim Summarizer
			fs_gensim = summarize(pasted,ratio=int(N)/100)
			# NLTK
			fs_nltk = nltk_summarizer(pasted)
			# Sumy
			fs_sumy = sumy_summary(pasted)
			return render_template('summary.html',c_text=pasted,  fs_spacy=fs_spacy, fs_gensim=fs_gensim,fs_nltk=fs_nltk,fs_sumy=fs_sumy)
		
		elif request.form["submit"]=="View All Entity" :
			# From Spacy
			c_text = str(request.form["pasted"])
			
			x =  view_entity(c_text)
			return render_template("all_entities.html",entity = x)
		elif request.form["submit"]=="Entity":
						# From Spacy
			c_text = str(request.form["pasted"])
			result_org,l_org = task_opt_org(c_text)
			result_places,l_place = task_opt_place(c_text)
			result_name,l_person = task_opt_name(c_text)
			result_law, l_law = task_opt_law(c_text)
			result_quantity, l_quntity = task_opt_quantity(c_text)
			result_product,l_product = task_opt_product(c_text)

			#From lexnlp 
			xy = lexnlp_entity(c_text)

			result_date = xy.date_time()
			result_acts = xy.acts()
			result_constraints= xy.constraints()
			result_condition = xy.conditioons()
			result_money = xy.get_money()
			result_trademark = xy.trademark()
			result_regulation = xy.regulation()
			result_copyright = xy.copyrights()
							
			return render_template('entity.html',c_text=c_text,
			result_org=result_org,l_org=l_org, result_places=result_places,l_place=l_place,result_name=result_name,
			l_person=l_person,result_law=result_law, l_law=l_law,result_quantity=result_quantity, l_quntity =l_quntity,
			result_product=result_product,l_product=l_product,
			result_acts=result_acts, l_acts= len(result_acts),l_dateTime=len(result_date),result_date=result_date,
			result_constraints=result_constraints,l_cons =len(result_constraints),
			result_condition=result_condition,l_cond=len(result_condition),result_money=result_money,l_money=len(result_money),
			result_trademark=result_trademark,l_trade= len(result_trademark),result_regulation=result_regulation,
			l_regu = len(result_regulation),result_copyright=result_copyright,l_copy =len(result_copyright)
			)

		



if __name__ == '__main__':
	app.run(debug=True)