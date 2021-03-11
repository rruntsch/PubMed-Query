# PubMed-Query

What does this project do?

PubMed Query includes a Python class called e_utility that is used to search the NIH PubMed database for biomedical journal article abstracts. It downloads each found article as an XML file.

Why is this project useful?

As part of the U.S. National Library of Medicine, PubMed is a public and freely-available online database of over 32 million biomedical and life sciences journal article citations. Many citations are linked to full articles. The PubMed site features a powerful search engine. PubMed article citations can also be searched and downloaded programmatically with the Entrez programmin utilities (also called E-utilities).

How can users can get started with PubMed-Query?

1. Install Python.
2. In Windows, create a folder called c:\pubmed_xml_files to store XML files written by the program. In Linux or other operating systems, create a folder the program to write xml files to and modify the value of self.output_file_path in the __init__() function with the name of that folder.
3. Modify the search term in the util.search() function at the end of file pubmed_query.py as desired. For information about search term syntax, see the links to PubMed documentation in the next section for help. Since the program creates and submits a URL to the PubMed server, the URL cannot contain spaces. So, in your search term, remember to replace each space with a plus sign (+).
4. Run the program to search the PubMed database, to fetch matching citations, and to write them as XML files to the folder specified in  step 2.

Where users can get help with your project?

PubMed website: https://pubmed.ncbi.nlm.nih.gov/

PubMed FAQs and user guide: https://pubmed.ncbi.nlm.nih.gov/help/

Entrez programming utilities help: https://www.ncbi.nlm.nih.gov/books/NBK25499/

Who maintains and contributes to the project?

PubMed-Query was created by and is maintained by Randy Runtsch, a programmer and data analyst based in Rochester, Minnesota, USA.
