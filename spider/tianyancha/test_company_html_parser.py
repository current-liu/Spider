from unittest import TestCase
import h_parser
import company_html


class TestCompany_html_parser(TestCase):
    def test_company_html_parser(self):
        doc = company_html.doc
        company_name, contact, company_human, details = h_parser.company_html_parser(doc)
        print company_name
        print contact
        print company_human
        print details
