from ProjetoFinalController import ProjetoFinalController
from ProjetoFinalView import ProjetoFinalView

controller = ProjetoFinalController()
view = ProjetoFinalView(controller.root)
controller.inicializa(view)
controller.executa()