from jinja2 import Template
import pdfkit


def generate_pdf(data, output_path):
    with open("template.html") as f:
        template = Template(f.read())

    html_content = template.render(**data)

    pdfkit.from_string(
        html_content,
        output_path,
        options={"encoding": "UTF-8"}
    )