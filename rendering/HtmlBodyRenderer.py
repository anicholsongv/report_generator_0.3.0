"""
    Writes html that will be used in the report body.
    These html pages will have separate styling from the front pages or appendices.
"""

import jinja2

class HtmlBodyRenderer:
    templateLoader = jinja2.FileSystemLoader(searchpath="../templates/")
    templateEnv = jinja2.Environment(loader=templateLoader)

    def __init__(self, template_dict):
        self.template_dict = template_dict


    def main_renderer(self):
        template = self.templateEnv.get_template("sensitive_template.html")
        main_html = template.render(template_dict=self.template_dict)
        file_path = "../data/dist/main_report.html"
        with open(file_path, "w") as final_html:
            final_html.write(main_html)
        return file_path




