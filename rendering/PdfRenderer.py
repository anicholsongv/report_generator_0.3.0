"""
    Takes a list of html file paths and renders them into a pdf in the order they were given


"""

from weasyprint import HTML

class PdfRenderer:

    def __init__(self, list_of_html):
        self.list_of_html = list_of_html

    def pdf_writer(self):
        list_of_html = self.list_of_html
        object_list = []
        combined_list = []
        for i in list_of_html:
            html_object = HTML(i)
            html_object = html_object.render()
            object_list.append(html_object)

        for obj in object_list:
            for p in obj.pages:
                combined_list.append(p)

        object_list[0].copy(combined_list).write_pdf(f'../data/dist/report_test.pdf')



