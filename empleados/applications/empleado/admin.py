from django.contrib import admin
from .models import Empleado,Trabajo, Pais
import csv
from django.http import HttpResponse
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
from applications.departamento.models import Departamento

# Register your models here.

admin.site.register(Empleado)
admin.site.register(Trabajo)
admin.site.register(Pais)


def export_selected_employees_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="empleados.csv"'

    writer = csv.writer(response)
    
    field_names = ['Nombre', 'Apellidos', 'Email', 'Departamento', 'Puesto de Trabajo']
    writer.writerow(field_names)

    
    for obj in queryset:
      
        departamento_nombre = obj.departamento.nombre if obj.departamento else 'N/A'
        trabajo_nombre = obj.trabajo.nombre if obj.trabajo else 'N/A'
        
        writer.writerow([
            obj.nombre,
            obj.apellidos,
            obj.email,
            departamento_nombre,
            trabajo_nombre
        ])
    return response
export_selected_employees_csv.short_description = "Exportar empleados seleccionados a CSV" # Text displayed in admin dropdown



def export_selected_employees_pdf(modeladmin, request, queryset):
   
    template_path = 'empleado/employees_pdf_template.html'
    context = {'empleados': queryset} 
    template = get_template(template_path)
    html = template.render(context) 

    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="empleados.pdf"'

    
    pisa_status = pisa.CreatePDF(
        html,
        dest=response 
    )
    if pisa_status.err:
        return HttpResponse('Tuvimos algunos errores al generar el PDF <pre>' + html + '</pre>')
    return response
export_selected_employees_pdf.short_description = "Exportar empleados seleccionados a PDF" 

class EmpleadoAdmin(admin.ModelAdmin):
    
    list_display = (
        'nombre_completo', 
        'email',
        'get_trabajo_nombre', 
        'get_departamento_nombre', 
        'pais',
    
        
    )
    search_fields = ('nombre', 'apellidos', 'email','Pais','fecha_nac')
    list_filter = ('trabajo', 'departamento') 

    def get_trabajo_nombre(self, obj):
        return obj.trabajo.nombre if obj.trabajo else '-'
    get_trabajo_nombre.short_description = 'Trabajo' 
    def get_departamento_nombre(self, obj):
        return obj.departamento.nombre if obj.departamento else '-'
    get_departamento_nombre.short_description = 'Departamento' 



class TrabajoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion',)
    search_fields = ('nombre',)

