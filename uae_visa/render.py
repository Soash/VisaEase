from django.template.loader import get_template
from io import BytesIO
# from xhtml2pdf import pisa
# import arabic_reshaper
# from bidi.algorithm import get_display
from django.http import HttpResponse
import xhtml2pdf.pisa as pisa 
import arabic_reshaper
from bidi.algorithm import get_display
import win_unicode_console
# win_unicode_console.enable()

# class Render:
#     @staticmethod
#     def render(path:str,params:dict):
#         template=get_template(path)
#         html=template.render(params)
#         response=BytesIO()
#         # pdf=pisa.pisaDocument(BytesIO(html.encode('UTF-8')),response)
#         pdf = pisa.pisaDocument(BytesIO(html.encode("cp1252")), result)
#         if not pdf.err:
#             return HttpResponse(response.getvalue(),content_type='application/pdf')
#         else:
#             return HttpResponse('error rendering pdf', status=400)
        

class Render:
    @staticmethod
    def render(path:str,params:dict):
        template=get_template(path)
        html=template.render(params)
        response=BytesIO()
        reshaped_text = arabic_reshaper.reshape('your desired text in arabic')
        bidi_text = get_display(reshaped_text)
        pdf=pisa.pisaDocument(BytesIO(html.encode('UTF-8')),response)
        # pdf = pisa.pisaDocument(BytesIO(html.encode("cp1252")), response)
        if not pdf.err:
            return HttpResponse(response.getvalue(),content_type='application/pdf')
        else:
            return HttpResponse('error rendering pdf', status=400)

