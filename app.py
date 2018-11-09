""" Controller for model AmazonScraper class """

from flask import Flask, request, render_template, redirect, url_for
from amazonscraper import AmazonScraper


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
	""" renders Amazon Android app title, version, change log, and release date
	parameters from AmazonScraper class to be rendered to results.html template """

	# get url input from user in index.html template form
	url_input = request.form['url_input']
	try:
	    amazon_scraper = AmazonScraper(url_input)

	    return render_template('results.html',
	                           title=amazon_scraper.get_title(),
	                           version=amazon_scraper.get_version(),
	                           change_log=amazon_scraper.get_change_log(),
	                           release_date=amazon_scraper.get_release_date())
	except:
	    return (render_template('404_not_found.html'), 404)


if __name__ == '__main__':
    app.run()
