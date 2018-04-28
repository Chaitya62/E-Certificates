from django.test import TestCase
from weasyprint import HTML
from weasyprint.fonts import FontConfiguration
from jinja2 import Environment, FileSystemLoader

# load template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('./templates/creator/certificate.html')

# render template
rendered = template.render(messages=['Hello','World'])

# write to PDF
HTML(string=rendered).write_pdf('weasyprint_jinja2_spike_output.pdf')


# Create your tests here.
