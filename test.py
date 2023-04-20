"""
mi_matriz = []

mi_matriz.append([1, 2, 3])
mi_matriz.append([4, 5, 6])
mi_matriz.append([7, 8, 9])

for fila in mi_matriz:
    print(fila)
"""
import sys
import webbrowser
from datetime import date

import pdfrw
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtWidgets

Ui_MainWindow, QMainWindow = loadUiType('View/prueba.ui')


# uic.loadUi("View/prueba.ui")

class Test(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:

        super().__init__()
        self.setupUi(self)
        self.btn_cotizar.clicked.connect(self.realizarCotizacion)

    def write_pdf(self, template, output, data_dict):
        ANNOT_KEY = '/Annots'
        ANNOT_FIELD_KEY = '/T'
        ANNOT_VAL_KEY = '/V'
        ANNOT_RECT_KEY = '/Rect'
        SUBTYPE_KEY = '/Subtype'
        WIDGET_SUBTYPE_KEY = '/Widget'

        def fill_pdf(input_pdf_path, output_pdf_path, data_dict):
            template_pdf = pdfrw.PdfReader(input_pdf_path)

            for page in template_pdf.pages:
                annotations = page[ANNOT_KEY]

                for annotation in annotations:
                    if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                        if annotation[ANNOT_FIELD_KEY]:
                            key = annotation[ANNOT_FIELD_KEY][1:-1]

                            if key in data_dict.keys():
                                if type(data_dict[key]) == bool:
                                    if data_dict[key] == True:
                                        annotation.update(pdfrw.PdfDict(AS=pdfrw.PdfName('Yes')))

                                else:
                                    annotation.update(pdfrw.PdfDict(V='{}'.format(data_dict[key])))
                                    annotation.update(pdfrw.PdfDict(AP=''))

            template_pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
            pdfrw.PdfWriter().write(output_pdf_path, template_pdf)

        fill_pdf(template, output, data_dict)
        webbrowser.open_new(output)

    def realizarCotizacion(self):
        try:
            region = self.pedir2.text()
            print(region)
            finca = self.pedir3.text()
            estado = self.pedir4.text()
            tipo = self.pedir1.currentText()

            if region != '--Seleccionar--' and finca != '--Seleccionar--' and estado != '--Seleccionar--' and tipo != '--Seleccionar--':

                cantidad = int(self.cantidad_line.text())

                if cantidad > 0:
                    QMessageBox.about(self, 'Aviso', 'Se ha generado la cotización!')

                    data_dict = {
                        'Fecha': date.today(),
                        'Numero': '0',
                        'Cliente': '',
                        'Nit': 'C/F',
                        'Direccion': 'Ciudad',
                        'Telefono': '',
                        'Correo': '',
                        'Producto': f"Café de {region}, finca {finca}, {estado}, {tipo}",
                        'Producto1': '',
                        'Producto3': '',
                        'Producto4': '',
                        'Producto5': '',
                        'Producto2': '',
                        'Precio1': '',
                        'Precio2': '',
                        'Precio3': '',
                        'Precio4': '',
                        'Precio5': '',
                        'Unidades': cantidad,
                        'Unidades1': '',
                        'Unidades2': '',
                        'Unidades3': '',
                        'Unidades4': '',
                        'Unidades5': '',
                        'Precio': '',
                        'Preciot': '',
                        'Preciot1': '',
                        'Preciot2': '',
                        'Preciot3': '',
                        'Preciot4': '',
                        'Totalp': '',
                        'Descuento': '',
                        'Total': ''
                    }

                    self.write_pdf('cotizacion2.pdf', 'cotizacion_final.pdf', data_dict)

                    self.cantidad_line.clear()

                else:
                    raise Exception('Debe ser un valor mayor a 0')

            else:
                raise Exception('No se ha seleccionado uno de los parametros para la cotización.')

        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Test()
    ventana.show()
    sys.exit(app.exec_())
