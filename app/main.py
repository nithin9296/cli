# import csv
# import sys
# import pdftotext
# import argparse
# # import datefinder
# import re
# import logging
# from loader import read_templates
# import invtemplate
# import argparse
# import shutil
# import os
# from os.path import join
# from flask import Flask, render_template, request, redirect, url_for, session
# from werkzeug.utils import secure_filename
# import json
# from flask import jsonify
# from app.forms import Dataentryform, Invoicetemplateform
# from urllib.parse import unquote
# from collections import namedtuple
# from bunch import bunchify
# from flask_sqlalchemy import SQLAlchemy
# from flask import render_template, flash, redirect, url_for, request
# from flask_login import login_user, logout_user, current_user, login_required
# from werkzeug.urls import url_parse
# from app import app, db
# from app.forms import LoginForm, RegistrationForm
# from app.models import User, Post
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_login import LoginManager
# from config import Config





# invoicefile = sys.argv

# input_mapping = {
#     'pdftotext': pdftotext,
    
#     }



# def allowed_file(filename):
#     return '.' in filename and \
#         filename.rsplit('.', 1)[1].lower()

# @app.route("/upload_invoice", methods=["GET", "POST"])
# def extract_data(templates=None, input_module=pdftotext):
#     if request.method == "POST":
#         file = request.files["file"]
        
#         if file and allowed_file(file.filename):
#             invoicefile = secure_filename(file.filename)


#         # invoicefile = request.files['file']
#             if templates is None:
#                 templates = read_templates()

#             # print(templates)
#             extracted_str = input_module.to_text(invoicefile).decode('utf-8')
#             print(extracted_str)
    

#     # myList = [item for item in extracted_str.split('\n')]

#             myList = [item for item in extracted_str.split()]
#             newString = ' '.join(myList)
#     # matches = datefinder.find_dates(newString)
#     # for match in matches:
#         # print (match)

#             logger.debug('START pdftotext result ===========================')
#             logger.debug(extracted_str)
#             logger.debug('END pdftotext result =============================')

    
#             logger.debug('Testing {} template files'.format(len(templates)))


#             for t in templates:
#                 optimized_str = t.prepare_input(extracted_str)
#                 print(optimized_str)
        

#                 if t.matches_input(optimized_str):
#                     ext =  t.extract(optimized_str)
#                     print(ext)


#             logger.error('No template for %s', invoicefile)
#             # data = {
#             #             'optimized_str': optimized_str
#             # }
#             # json_data=jsonify(ext)
#             session['ext'] = ext
#             # print(type(json_data))
            
#         return redirect(url_for('form_input', ext=ext))
#            # return jsonify(ext)
#             # return redirect_urlfor(", form=issuer)


#     return render_template("extract.html")

#     # matches = datefinder.find_dates(newString)

   
    

#     # for match in matches:
#         # print (match)

#     # return newString



# @app.route('/form_input', methods=["GET", "POST"])
# def form_input():
#     form  = Dataentryform()  
#     ext = session['ext']
#     form.issuer =  ext['issuer']
#     form.amount = ext['amount']
#     form.invoice_number = ext['invoice_number']
#     form.date = ext['date']
#     form.currency = ext['currency']
#     return render_template("inputdata.html",form=form)



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# import pickle
# from selenium.webdriver.support.select import Select

# # associateStr = 'Kariningufu sep-18'
# usernameStr = 'nithinpathak@velocityglobal.com'
# passwordStr = 'Motorokr240377#'
# # answerStr = 'sunil'
# # createdate = '9/6/2018'
# # duedate = '9/6/2018'
# # billno = 'PO#2718-Accrual'
# # amount = '68,185.33'



# @app.route('/selenium', methods = ["POST"])
# def selenium():
#     issuer = request.form['issuer']
#     Invoice_number = request.form['invoice_number']
#     Date = request.form['date']
#     Currency = request.form['currency']
#     Amount = request.form['amount']
    
#     print (issuer)
#     print (Invoice_number)
#     print (Date)
#     print (Currency)
#     print (Amount)
#     browser = webdriver.Chrome(executable_path='/Users/nithinpathak/Downloads/chromedriver')
#     browser.get(('https://system.na2.netsuite.com'))
#     username = browser.find_element_by_id('userName')
#     username.send_keys(usernameStr)
#     password = WebDriverWait(browser, 10).until(
#     EC.presence_of_element_located((By.ID, 'password')))
#     password.send_keys(passwordStr)
#     loginButton = browser.find_element_by_id('submitButton')
#     loginButton.click()
#     answer = browser.find_element_by_name("answer")
#     answer.send_keys(answerStr)
#     submitButton = browser.find_element_by_name("submitter")
#     submitButton.click()
#     associate_search = WebDriverWait(browser, 30).until(
#     EC.presence_of_element_located((By.ID, '_searchstring')))
#     associate_search.send_keys(associateStr)
#     associate_search.send_keys(Keys.RETURN)

#     return 'OK'
# #     browser = webdriver.Chrome(executable_path='/Users/nithinpathak/Downloads/chromedriver')
# #     browser.get(('https://system.na2.netsuite.com'))
# #     username = browser.find_element_by_id('userName')
# #     username.send_keys(usernameStr)
# #     password = WebDriverWait(browser, 10).until(
# #     EC.presence_of_element_located((By.ID, 'password')))
# #     password.send_keys(passwordStr)
# #     loginButton = browser.find_element_by_id('submitButton')
# #     loginButton.click()
# #     answer = browser.find_element_by_name("answer")
# #     answer.send_keys(answerStr)
# #     submitButton = browser.find_element_by_name("submitter")
# #     submitButton.click()
# #     associate_search = WebDriverWait(browser, 30).until(
# #      EC.presence_of_element_located((By.ID, '_searchstring')))
# #     associate_search.send_keys(associateStr)
# #     associate_search.send_keys(Keys.RETURN)

# #     browser.find_element_by_link_text("Edit").click()
# #     billnumber = WebDriverWait(browser, 30).until(
# #      EC.presence_of_element_located((By.ID, 'tranid')))
# #     billnumber.send_keys(billno)

# #     totalamount = WebDriverWait(browser, 30).until(
# #      EC.presence_of_element_located((By.ID, 'usertotal_formattedValue')))
# #     totalamount.send_keys(amount)













# app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# app.run()

# # def write_to_file(data, path):
# #     """Export extracted fields to csv
# #     Appends .csv to path if missing and generates csv file in specified directory, if not then in root
# #     Parameters
# #     ----------
# #     data : dict
# #         Dictionary of extracted fields
# #     path : str
# #         directory to save generated csv file
# #     Notes
# #     ----
# #     Do give file name to the function parameter path.
# #     Examples
# #     --------
# #         >>> from invoice2data.output import to_csv
# #         >>> to_csv.write_to_file(data, "/exported_csv/invoice.csv")
# #         >>> to_csv.write_to_file(data, "invoice.csv")
# #     """
    

# #     if path.endswith('.csv'):
# #         filename = path
# #     else:
# #         filename = path + '.csv'

# #     if sys.version_info[0] < 3:
# #         openfile = open(filename, "wb")
# #     else:
# #         openfile = open(filename, "w", newline='')

# #     with openfile as csv_file:
# #         writer = csv.writer(csv_file)

# #         # for line in data:
# #         #     first_row = []
# #         #     for k, v in line.items():
# #         #         first_row.append(k)

# #         # writer.writerow(first_row)
# #         # for line in data:
# #         #     csv_items = []
# #         #     for k, v in line.items():
# #         #         # first_row.append(k)
# #         #         if k == 'date':
# #         #             v = v.strftime('%d/%m/%Y')
# #         #         csv_items.append(v)
        

# #         #delimiter=',', quotechar=" ", quoting=csv.QUOTE_MINIMAL
         
        
# #         writer.writerow([data])




# # def ext_data(invoicefile, input_module=pdftotext):

# #     """Extracts structured data from PDF/image invoices.
# #     This function uses the text extracted from a PDF file or image and
# #     pre-defined regex templates to find structured data.
# #     Reads template if no template assigned
# #     Required fields are matches from templates
# #     Parameters
# #     ----------
# #     invoicefile : str
# #         path of electronic invoice file in PDF,JPEG,PNG (example: "/home/duskybomb/pdf/invoice.pdf")
# #     templates : list of instances of class `InvoiceTemplate`, optional
# #         Templates are loaded using `read_template` function in `loader.py`
# #     input_module : {'pdftotext', 'pdfminer', 'tesseract'}, optional
# #         library to be used to extract text from given `invoicefile`,
# #     Returns
# #     -------
# #     dict or False
# #         extracted and matched fields or False if no template matches
# #     Notes
# #     -----
# #     Import required `input_module` when using invoice2data as a library
# #     See Also
# #     --------
# #     read_template : Function where templates are loaded
# #     InvoiceTemplate : Class representing single template files that live as .yml files on the disk
# #     Examples
# #     --------
# #     When using `invoice2data` as an library
# #     >>> from invoice2data.input import pdftotext
# #     >>> extract_data("invoice2data/test/pdfs/oyo.pdf", None, pdftotext)
# #     {'issuer': 'OYO', 'amount': 1939.0, 'date': datetime.datetime(2017, 12, 31, 0, 0), 'invoice_number': 'IBZY2087',
# #      'currency': 'INR', 'desc': 'Invoice IBZY2087 from OYO'}
# #     """

# # def create_parser():
# #     """Returns argument parser """

# #     parser = argparse.ArgumentParser(description='Extract structured data from PDF files and save to CSV or JSON.')

# #     parser.add_argument('--input-reader', choices=input_mapping.keys(),
# #                         default='pdftotext', help='Choose text extraction function. Default: pdftotext')

# #     parser.add_argument('--output-format', choices=output_mapping.keys(),
# #                         default='none', help='Choose output format. Default: none')

# #     parser.add_argument('--output-name', '-o', dest='output_name', default='invoices-output',
# #                         help='Custom name for output file. Extension is added based on chosen format.')

# #     parser.add_argument('--debug', dest='debug', action='store_true',
# #                         help='Enable debug information.')

# #     parser.add_argument('--copy', '-c', dest='copy',
# #                         help='Copy renamed PDFs to specified folder.')

# #     parser.add_argument('--template-folder', '-t', dest='template_folder',
# #                         help='Folder containing invoice templates in yml file. Always adds built-in templates.')
    
# #     parser.add_argument('--exclude-built-in-templates', dest='exclude_built_in_templates',
# #                         default=False, help='Ignore built-in templates.', action="store_true")

# #     parser.add_argument('input_files', type=argparse.FileType('r'), nargs='+',
# #                         help='File or directory to analyze.')

# #     return parser


# # def main(args=None):
# #     """Take folder or single file and analyze each."""
# #     if args is None:
# #         parser = create_parser()
# #         args = parser.parse_args()

# #     if args.debug:
# #         logging.basicConfig(level=logging.DEBUG)
# #     else:
# #         logging.basicConfig(level=logging.INFO)

# #     input_module = input_mapping[args.input_reader]
# #     output_module = output_mapping[args.output_format]

# #     templates = []
    
# #     # Load templates from external folder if set.
# #     if args.template_folder:
# #         templates += read_templates(os.path.abspath(args.template_folder))

# #     # Load internal templates, if not disabled.
# #     if not args.exclude_built_in_templates:
# #         templates += read_templates()
    
# #     output = []
# #     for f in args.input_files:
# #         res = extract_data(f.name, templates=templates, input_module=input_module)
# #         if res:
# #             logger.info(res)
# #             output.append(res)
# #             if args.copy:
# #                 filename = FILENAME.format(
# #                     date=res['date'].strftime('%Y-%m-%d'),
# #                     desc=res['desc'])
# #                 shutil.copyfile(f.name, join(args.copy, filename))

# #     if output_module is not None:
# #         output_module.write_to_file(output, args.output_name)


# # if __name__ == '__main__':
# #     main()























































       
        
