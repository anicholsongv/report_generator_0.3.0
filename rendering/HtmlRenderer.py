import jinja2

class HTMLRenderer:
    templateLoader = jinja2.FileSystemLoader(searchpath="../templates/")
    templateEnv = jinja2.Environment(loader=templateLoader)

    def __init__(self, template_dict):
        self.template_dict = template_dict


    def main_renderer(self):
        template = self.templateEnv.get_template("sensitive_template.html")
        main_html = template.render(template_dict=self.template_dict)

        final_html = open("../data/dist/main_report.html", "w")
        final_html.write(main_html)
        final_html.close()

