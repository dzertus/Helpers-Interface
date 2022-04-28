from PySide2 import QtWidgets, QtCore


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("dispatcher")  # titre de la fenêtre
        self.setup_ui()  # Fonction de l'UI
        self.set_default_values()

    def setup_ui(self):
        # Créer le layout (fenêtre):
        self.main_layout = QtWidgets.QVBoxLayout(self)  # layout vertical

        # Créer les widgets (boutons, textes, listes, etc):
        self.spn_blade_instance = QtWidgets.QDoubleSpinBox()  # line edit nb instance
        self.le_blade_title = QtWidgets.QLineEdit("Name of blade")  # line edit name
        self.spn_blade_thread = QtWidgets.QSpinBox()  # line edit threads
        self.spn_blade_ghz = QtWidgets.QSpinBox()  # line edit Ghz
        self.spn_blade_rendertime = QtWidgets.QSpinBox()  # line edit rendertime

        self.btn_addBlade = QtWidgets.QPushButton("Add blade")  # Bouton ajouter une machine
        self.lw_blades = QtWidgets.QListWidget()  # liste des blades
        self.lw_blades.setSelectionMode(
            QtWidgets.QListWidget.ExtendedSelection)  # Permet de faire une selection étendue
        self.btn_removeBlades = QtWidgets.QPushButton("Delete blade")  # Bouton delete

        # Ajouter les widgets dans le layout:
        self.main_layout.addWidget(self.spn_blade_instance)
        self.main_layout.addWidget(self.le_blade_title)
        self.main_layout.addWidget(self.spn_blade_thread)
        self.main_layout.addWidget(self.spn_blade_ghz)
        self.main_layout.addWidget(self.spn_blade_rendertime)

        self.main_layout.addWidget(self.btn_addBlade)
        self.main_layout.addWidget(self.lw_blades)
        self.main_layout.addWidget(self.btn_removeBlades)

    def set_default_values(self):
        self.spn_blade_instance.setValue(1)
        self.spn_blade_thread.setValue(6)
        self.spn_blade_ghz.setValue(2)
        self.spn_blade_rendertime.setValue(0)


# Lancer l'application:

app = QtWidgets.QApplication([])
win = App()  # Nom de la classe
win.show()
app.exec_()