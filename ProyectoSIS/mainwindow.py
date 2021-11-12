from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import Slot


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Tabacos Ornelas")
        self.ui.pushButton_ver_inventario.clicked.connect(self.click_ver_inventario)
        self.ui.pushButton_buscar_inventario.clicked.connect(self.click_buscar_inventario)
        self.ui.pushButton_eliminar_inventario.clicked.connect(self.click_eliminar_inventario)
        self.ui.pushButton_modificar_inventario.clicked.connect(self.click_modificar_inventario)
        self.ui.pushButton_agregar_inventario.clicked.connect(self.click_agregar_inventario)
        self.ui.pushButton_ver_pedidos.clicked.connect(self.click_ver_pedido)
        self.ui.pushButton_buscar_pedidos.clicked.connect(self.click_buscar_pedido)
        self.ui.pushButton_eliminar_pedidos.clicked.connect(self.click_eliminar_pedido)
        self.ui.pushButton_modificar_pedidos.clicked.connect(self.click_modificar_pedido)
        self.ui.pushButton_agregar_pedidos.clicked.connect(self.click_agregar_pedido)
        self.ui.pushButton_ver_ventas.clicked.connect(self.click_ver_venta)
        self.ui.pushButton_buscar_ventas.clicked.connect(self.click_buscar_venta)
        self.ui.pushButton_eliminar_ventas.clicked.connect(self.click_eliminar_venta)
        self.ui.pushButton_modificar_ventas.clicked.connect(self.click_modificar_venta)
        self.ui.pushButton_agregar_ventas.clicked.connect(self.click_agregar_venta)
        self.ui.pushButton_ver_total_ventas.clicked.connect(self.click_ver_total_venta)
        
    @Slot()
    def click_ver_inventario(self):
        print("ver inventario")
    
    @Slot()
    def click_buscar_inventario(self):
        print("buscar inventario")
    
    @Slot()
    def click_eliminar_inventario(self):
        print("eliminar inventario")
    
    @Slot()
    def click_modificar_inventario(self):
        print("modificar inventario")
    
    @Slot()
    def click_agregar_inventario(self):
        print("agregar inventario")
    
    
    
    @Slot()
    def click_ver_pedido(self):
        print("ver pedido")
    
    @Slot()
    def click_buscar_pedido(self):
        print("buscar pedido")
    
    @Slot()
    def click_eliminar_pedido(self):
        print("eliminar pedido")
    
    @Slot()
    def click_modificar_pedido(self):
        print("modificar pedido")
    
    @Slot()
    def click_agregar_pedido(self):
        print("agregar pedido")
    
    
    
    @Slot()
    def click_ver_venta(self):
        print("ver venta")
    
    @Slot()
    def click_buscar_venta(self):
        print("buscar venta")
    
    @Slot()
    def click_eliminar_venta(self):
        print("eliminar venta")
    
    @Slot()
    def click_modificar_venta(self):
        print("modificar venta")
    
    @Slot()
    def click_agregar_venta(self):
        print("agregar venta")
        
    @Slot()
    def click_ver_total_venta(self):
        print("ver total venta")