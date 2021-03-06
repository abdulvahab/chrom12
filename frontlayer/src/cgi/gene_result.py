#!/usr/bin/env python3
"""*************************************************************************************************
* project: Genome browse for chromosome-12,Msc Bioinformatics & System Biology
* Module: Biocomuting-2 Taught By(Dr Andrew C. Martin)                                             *
* file:gene_result.py                                                                              *
* Date: 08/05/2018                                                                                 *
* version:v1.0 ,v2.0 (updated on 13/05/18)                                                         *
* Function : This python script generate result page according to user input in search
* Licence:See the LICENSE.txt for licensing information                                            *
* Author: Abdulvahab Kharadi                                                                       *
* ***********************************************************************************************"""
# Import required Modules
import cgi
import cgitb
from front_api import gene_query_acno,gene_query_gi
import json
cgitb.enable()
print ("Content-Type: text/html\n")

form = cgi.FieldStorage()
choice = form['choice'].value
query = form['query'].value

# This html function creates Result page for gene queryied by user 
def result():    
    if choice == 'gi':
    	gene_info = gene_query_gi(query)
    elif choice == 'gene_acc':
    	gene_info = gene_query_acno(query)
    return gene_info
    
    
    
def html():
    html ='<html lang="en">'
    html += '<head>'
    html += "<title>Chromosome-12 Information</title>"
    html += "<meta charset='utf-8'>"
    html += "<meta name='viewport' content='width=device-width,initial-scale=1.0'>"
    html += '<link rel ="stylesheet" type="text/css" href = "http://localhost/chrom12/frontlayer/src/html/main.css">'
    #html += '<link rel="stylesheet" href="https://localhost/chrom12/frontlayer/src/html/main.css">'
    html += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">'
    html += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>'
    html += '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>'
    html += "<style>"
    html += '''body{
    color:#660099;
    text-align: center;
    background-size:cover;
    background-color: rgba(255,255,255,0.7);
    background-blend-mode: lighten;
    background-image: url('chromo1.jpg');
    background-repeat: no-repeat;
    margin-bottom:50px;
    }'''
    html += "</style>"
    html += '</head>'
    html += "<body >"
    
    html += "<div class='main-container'>"
    html += "<header ><h1>Query Result</h1></header>"
    html += '<nav>'
    html += "<a href='http://student.cryst.bbk.ac.uk/~ka001/index.html'>Home  |</a>"
    html += "<a href='http://student.cryst.bbk.ac.uk/~ka001/gene_search.html'>Gene Search  |</a>"
    html += "<a href='http://student.cryst.bbk.ac.uk/~ka001/prot_search.html'>Protein Search  |</a>"
    html += "<a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/ka001/gene_summary.py'>Gene Summary  |</a>"
    html += "<a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/ka001/prot_summary.py'>Protein Summary  |</a>"
    html += "<a href='http://student.cryst.bbk.ac.uk/~ka001/contactus.html'>Contact us</a>"
    html += '</nav>'
    html += "<div class='footer'>&copy; 2018,Group Chromosome-12.</div>"
        
    html += "<div class='col-lg-6' style='text-align:left'>"
    html += '<h4><b>Accesion number:</b></h4>'
    html += '<code>'+ str(result()[0])+ '</code>'
    html += '<h4><b>Gene_Identifier:</b></h4>'
    html += '<code>'+ str(result()[1])+ '</code>'
    html += '<h4><b>Organism:</b></h4>'
    html += '<code>'+ str(result()[2])+ '</code>'
    html += '<h4><b>Chromosomal_Location:</b></h4>'
    html += '<code>'+ str(result()[3])+ '</code>'    
    html += '<h4><b>Sequence_Length:</b></h4>' 
    html += '<code>'+str(result()[4])+'</code>'
    html += '<h4><b>DNA Sequence:</b></h4>'  
    html += "<code>"
    html += "<textarea style='width:100%; height:200px; word-wrap:break-word;'>" +str(result()[5])+ "</textarea>"
    html += '</code>'
    html += '</div>'
    
    html += "<div class='col-lg-6' style='text-align:left'>"
    html += '<h4><b>CDS Start:</b></h4>'
    html += '<code>'+str(result()[6])+'</code>'
    html += '<h4><b>CDS End:</b></h4>'
    html += '<code>'+str(result()[7])+'</code>'
    html += '<h4><b>CDS Sequence:</b></h4>'
    html += '<code>'
    html += "<textarea style='width:100%; height:200px; word-wrap:break-word;'>" +str(result()[8])+ "</textarea>"
    html += '</code>'
    html += '<h4><b>Protein Information:</b></h4>'
    html += "<code><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/ka001/prot_result.py?query={}&choice=prot_acc'>Expand</a> </code>".format(result()[0])
    html += '</div>'
    
    html += '</div>'
    
    html += '</body>'
    html += '</html>'
    print(html)
if __name__=="__main__":
    html()
