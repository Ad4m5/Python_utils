# Usage
```shell
python3 pdf_parser.py -h  
usage: PDF parser [-h] -d DOMAIN --dir DIR

parse pdf file to find email address from a domain name

options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        email address domain name
  --dir DIR             directory containing pdf files to parse (absolute path)
```
# Use case
You can combine this script with metagoofil : 
```shell
mkdir pdf_extract
metagoofil -d YOURTARGET.com -t pdf -w -o ./pdf_extract
cd pdf_extract
python3 pdf_parser.py -d YOURTARGET.com --dir $(pwd)
```
