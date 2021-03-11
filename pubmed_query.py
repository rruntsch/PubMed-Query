""" 
    Name:           pubmed_query.py
    Author:         Randy Runtsch
    Date:           March 11, 2021
    Description:    Given a valid PubMed search term, call the esearch utility
                    to retrieve the list of resulting article abstracts. Then,
                    loop through the result set, and call the efetch utility to
                    fetch each article abstract and write it as an XML file.
    Prerequisites:  Create a folder called c:\pubmed_xml_files to write the XML
                    filed into.
"""

import json
import urllib.request
import time

class e_utility():

    def __init__(self):

        self.sleep_minutes = .2 
        self.base_url_esearch = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?'
        self.base_url_efetch = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?'
        self.output_file_path = r"c:\\pubmed_xml_files\\"
   
    def search(self, search_term):

        # Call the esearch utility with the search team. Return the result in JSON format. 
        # Loop through the result set and retrieve each article abstract.

        # Build Entrez database search URL.

        print("Searching PubMed")

        url = self.base_url_esearch + 'db=pubmed&term=' + \
            search_term + '&retmode=json&retmax=20&usehistory=y'
 
        # Search specified database with the text string. 
        # For each record found return the abstract.        

        result = urllib.request.urlopen(url)
        text = result.read().decode('utf-8')

        json_text = json.loads(text)

        #Call retrieve_abstract() for each UID.

        uid_cnt = 0
        webenv = json_text["esearchresult"]["webenv"]
        for uid in json_text["esearchresult"]["idlist"]:
            uid_cnt += 1 
            self.retrieve_abstract(uid, uid_cnt, webenv)

    def retrieve_abstract(self, uid, uid_cnt, webenv):

        # Retrieve the abstract and write it to a file with an extension of xml.

        print("Fetching PubMed abstract #" + str(uid_cnt) + ". UID: " + str(uid) + ".")

        url = self.base_url_efetch + 'db=pubmed&retmode=xml&id=' + \
            uid + '&webenv=' + webenv
    
        result = urllib.request.urlopen(url)
        xml_text = result.read().decode('utf-8')

        file_name = self.output_file_path + "pubmed_" + uid + ".xml"

        file_out = open(file_name, "w", encoding="utf-8")
        file_out.write(xml_text)
        file_out.close()

        # Sleep for a subsecond so that the PubMed server is not overloaded.
        time.sleep(self.sleep_minutes)

util = e_utility()
util.search("Johns+Hopkins[ad]+heart[ti]+2020/12/15:2020/12/31[dp]")
