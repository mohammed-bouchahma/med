# med
MED Link Checker

MED is a simple command-line tool for checking the status of links in a given URL.
Installation

To install MED, simply clone the repository and install the required packages:

==== bash =====

=====> git clone https://github.com/mohammed-bouchahma/med.git
=====> cd med
=====> pip install -r requirements.txt

Usage

To check the status of links in a URL, use the following command:

mathematica:

====> python med.py <URL>

For example:

arduino

=====> python med.py https://www.example.com/

The tool will then check all links in the given URL and return their status codes. It will also indicate any broken links (status code >= 400).

By default, MED will follow redirects up to a maximum of 10 times. You can change this by passing the --max-redirects argument:

arduino

======> python med.py <URL> --max-redirects 5

You can also choose to output the results to a file using the --output argument:

css

=======> python med.py <URL> --output results.txt

License

This tool is released under the MIT License. Feel free to use, modify, and distribute it as you see fit.
