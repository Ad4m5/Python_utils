from pypdf import PdfReader
import argparse
import os

def arguments():
    arg = argparse.ArgumentParser(
                    prog='PDF parser',
                    description='parse pdf file to find email address from a domain name')
    arg.add_argument('-d','--domain',required=True, help='email address domain name or domain name list (separate by comma)')
    arg.add_argument('--dir',required=True, help='directory containing pdf files to parse (absolute path)')
    return arg.parse_args()

def parser_pdfs(path,domain):
    keywords='@' + domain
    emails_list = []
    for files in os.listdir(path):
        full_path = path + "/" + files
        try:
            reader = PdfReader(full_path)
            for i in range(len(reader.pages)):
                page = reader.pages[i]
                content = page.extract_text()
                tab_to_parse = content.split("\n")
                for words in tab_to_parse:
                    word = words.split(" ")
                    for j in word:
                        if keywords in j:
                            email_format = j.split("@")[0] + keywords
                            if email_format not in emails_list:
                                emails_list.append(email_format)
        except KeyboardInterrupt:
            sys.exit()
        except:
            continue
    return emails_list


def main():
    argument = arguments()
    path = argument.dir
    domain = argument.domain.split(',')
    for dom in domain:
        tab_results = parser_pdfs(path,dom)
        print(f"Found {len(tab_results)} emails for domain {dom}")
        print("\n".join(tab_results))
        print("\n")


if __name__ == '__main__':
    main()
