import networkx as nx
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.widgets import *
from PyQt5.QtWidgets import QMessageBox
import sys
from bfs import Graph_bfs
from dfs import Graph_dfs
from astar import Graph_astar
from uni import Graph_ucs
from ids import Graph_ids
from bidirectional import Graph_bi
from bestf import Graph_best_first_search
from SIMULATED import SimulatedAnnealing
from ALPHABETA import AlphaBetaPruning
DG = nx.DiGraph()
G = nx.Graph()

Goal_list = []


class Ui_AISearchingTechniquesMainWindow(object):


    counter = 0
    counterG = 0
    EdgeWeight_arr = [1] * 30
    HeuristicDict = dict()
    H = {}
    graphastar1=Graph_astar(G,"Undirectd Graph")
    graphastar2=Graph_astar(DG,"directed Graph")

    graphfirst = Graph_best_first_search(G,"Undirectd Graph")
    graphfirst2 = Graph_best_first_search(DG, "directed Graph")

    def GeneratePathClicked(self):
        original_stdout = sys.stdout  # Save a reference to the original standard output

        with open('test.txt', 'w') as f:
            sys.stdout = f  # Change the standard output to the file we created.
            searchType = str(self.SearchTypecomboBox.currentText())
            graphType = str(self.GraphTypecomboBox.currentText())
            if (graphType == "Undirectd Graph"):
                if searchType == "BFS":
                    graphbfs = Graph_bfs(G,graphType)


                    start = self.StartNode_input.text()
                    goals = Goal_list
                    traced_path1 = graphbfs.bfs(start, goals)
                    if (traced_path1):
                        print('Path:', end=' ')
                        graphbfs.print_path(traced_path1)
                        print()
                        Goal_list.clear()
                    else :
                        print('Path Does not Exist')

                elif searchType == "DFS":
                    graphdfs = Graph_dfs(G,graphType)

                    start = self.StartNode_input.text()
                    goals = Goal_list
                    traced_path2 = graphdfs.dfs(start, goals)
                    if (traced_path2):
                        print('Path:', end=' ')
                        graphdfs.print_path(traced_path2)
                        print()
                        Goal_list.clear()
                    else:
                        print('Path Does not Exist')

                elif searchType == "A*":
                    self.graphastar1.graph = G
                    start = self.StartNode_input.text()
                    goals = Goal_list
                    trace_path = self.graphastar1.astar_search(start, goals)
                    if trace_path:
                        print('Path:', end=' ')
                        self.graphastar1.print_path(trace_path)
                        print()
                        Goal_list.clear()
                    else:
                        print('Path Does not Exist')

                elif searchType == "UCS":
                    graphuni = Graph_ucs(DG,graphType);

                    start = self.StartNode_input.text()
                    goals = Goal_list
                    traced_path2,current_cost = graphuni.uniform_cost_search(start, goals)
                    if (traced_path2):
                        print('Path:', end=' ')
                        graphuni.print_path(traced_path2)
                        print('COST: ',current_cost)
                        print()
                        Goal_list.clear()
                    else:
                        print('Path Does not Exist')
                elif searchType == "IDS":
                    graphids = Graph_ids(G, graphType);

                    start = self.StartNode_input.text()
                    goals = Goal_list
                    traced_path2 = graphids.ids(start, goals)
                    if (traced_path2):
                        print('Path:', end=' ')
                        graphids.print_path(traced_path2)
                        print()
                        Goal_list.clear()
                    else:
                        print('Path Does not Exist')
                elif searchType =="Bidirect":
                    graphbi = Graph_bi(G, graphType);

                    start = self.StartNode_input.text()
                    goals = Goal_list
                    traced_path2 = graphbi.bidirectional(start, goals)
                    if (traced_path2):
                        print('Path:', end=' ')
                        graphbi.print_path(traced_path2)
                        print()
                        Goal_list.clear()
                    else:
                        print('Path Does not Exist')

                elif searchType =="BESTF":
                    start = self.StartNode_input.text()
                    goals = Goal_list
                    trace_path=  self.graphfirst.best_first_search(start,goals)
                    if trace_path:
                     print('Path:', end=' ')
                     self.graphfirst.print_path(trace_path)
                     print()
                     Goal_list.clear()
                    else:
                        print('Path Does not Exist')
                elif searchType == "SIMULATED":
                  graph=  SimulatedAnnealing(G,graphType);
                  start = self.StartNode_input.text()
                  goals = Goal_list
                  trace_path = graph.simulated_annealing(start, goals,100,0.95)
                  if trace_path:
                      print('Path:', end=' ')
                      graph.print_path(trace_path)
                      print()
                      Goal_list.clear()
                  else:
                      print('Path Does not Exist')
                elif searchType == "ALPHABETA":
                  graph=  AlphaBetaPruning(G,graphType);
                  start = self.StartNode_input.text()
                  goals = Goal_list
                  trace_path = graph.alpha_beta_pruning(start, goals,10)
                  if trace_path:
                      print('Path:', end=' ')
                      graph.print_path(trace_path)
                      print()
                      Goal_list.clear()
                  else:
                      print('Path Does not Exist')








            else:
                if searchType == "BFS":
                    graphbfs = Graph_bfs(DG,graphType)

                    start = self.StartNode_input.text()
                    goals = Goal_list
                    traced_path1 = graphbfs.bfs(start, goals)
                    if (traced_path1):
                        print('Path:', end=' ')
                        graphbfs.print_path(traced_path1)
                        print()
                        Goal_list.clear()
                    else:
                        print('Path Does not Exist')

                elif searchType == "DFS":
                    graphdfs = Graph_dfs(DG,graphType)
                    start = self.StartNode_input.text()
                    goals = Goal_list
                    traced_path2 = graphdfs.dfs(start, goals)
                    if (traced_path2):
                        print('Path:', end=' ')
                        graphdfs.print_path(traced_path2)
                        print()
                        Goal_list.clear()
                    else:
                        print('Path Does not Exist')

                elif searchType == "A*":

                    self.graphastar2.graph = DG
                    start = self.StartNode_input.text()
                    goals = Goal_list
                    trace_path = self.graphastar2.astar_search(start, goals)
                    if trace_path:
                        print('Path:', end=' ')
                        self.graphastar2.print_path(trace_path)
                        print()
                        Goal_list.clear()
                    else:
                        print('Path Does not Exist')
                elif searchType == "UCS":
                    graphuni = Graph_ucs(DG, graphType);

                    start = self.StartNode_input.text()
                    goals = Goal_list
                    traced_path2, current_cost = graphuni.uniform_cost_search(start, goals)
                    if (traced_path2):
                        print('Path:', end=' ')
                        graphuni.print_path(traced_path2)
                        print('COST: ', current_cost)
                        print()
                        Goal_list.clear()
                    else:
                        print('Path Does not Exist')
                elif searchType == "IDS":
                    graphids = Graph_ids(DG, graphType);

                    start = self.StartNode_input.text()
                    goals = Goal_list
                    traced_path2 = graphids.ids(start, goals)
                    if (traced_path2):
                        print('Path:', end=' ')
                        graphids.print_path(traced_path2)
                        print()
                        Goal_list.clear()
                    else:
                        print('Path Does not Exist')
                elif searchType =="Bidirect":
                    graphbi = Graph_bi(DG, graphType);

                    start = self.StartNode_input.text()
                    goals = Goal_list
                    traced_path2 = graphbi.bidirectional(start, goals)
                    if (traced_path2):
                        print('Path:', end=' ')
                        graphbi.print_path(traced_path2)
                        print()
                        Goal_list.clear()
                    else:
                        print('Path Does not Exist')
                elif searchType == "BESTF":
                    self.graphfirst2.graph=DG
                    start = self.StartNode_input.text()
                    goals = Goal_list
                    trace_path = self.graphfirst2.best_first_search(start, goals)
                    if trace_path:
                        print('Path:', end=' ')
                        self.graphfirst2.print_path(trace_path)
                        print()
                        Goal_list.clear()
                    else:
                        print('Path Does not Exist')
                elif searchType == "SIMULATED":
                  graph=  SimulatedAnnealing(G,graphType);
                  start = self.StartNode_input.text()
                  goals = Goal_list
                  trace_path = graph.simulated_annealing(start, goals,100,0.95)
                  if trace_path:
                      print('Path:', end=' ')
                      graph.print_path(trace_path)
                      print()
                      Goal_list.clear()
                  else:
                      print('Path Does not Exist')



        sys.stdout = original_stdout  # Reset the standard output to its original value

        with open("test.txt") as f:
            contents = f.read()

        self.TheResult_Label.setText(contents)

    def GenerateGraphClicked(self):

        if self.SearchTypecomboBox.currentText()=="BESTF":
            if self.GraphTypecomboBox.currentText() == "Undirectd Graph":
                pos = nx.spring_layout(self.graphfirst.graph)
                nx.draw(self.graphfirst.graph, pos, with_labels=True, node_size=1500)

                # Draw heuristic values over nodes
                labels = {node: str(self.HeuristicDict[node]) for node in self.graphfirst.graph}
                pos_labels = {k: (v[0], v[1] + 0.15) for k, v in pos.items()}  # Shift label positions up slightly
                nx.draw_networkx_labels(self.graphfirst.graph, pos_labels, labels, font_size=26)

                nx.draw_networkx_edge_labels(self.graphfirst.graph, pos, font_size=26,
                                             edge_labels=nx.get_edge_attributes(self.graphfirst.graph, 'weight'))
                plt.show()
            elif self.GraphTypecomboBox.currentText() == "Directed Graph":
                pos = nx.spring_layout(self.graphfirst2.graph)
                nx.draw(self.graphfirst2.graph, pos, with_labels=True, node_size=1500)

                # Draw heuristic values over nodes
                labels = {node: str(self.HeuristicDict[node]) for node in self.graphfirst2.graph}
                pos_labels = {k: (v[0], v[1] + 0.15) for k, v in pos.items()}  # Shift label positions up slightly
                nx.draw_networkx_labels(self.graphfirst2.graph, pos_labels, labels, font_size=26)

                nx.draw_networkx_edge_labels(self.graphfirst2.graph, pos, font_size=26,
                                             edge_labels=nx.get_edge_attributes(self.graphfirst2.graph, 'weight'))
                plt.show()

        elif self.SearchTypecomboBox.currentText()=="A*":
            if self.GraphTypecomboBox.currentText() == "Undirectd Graph":
                pos = nx.spring_layout(self.graphastar1.graph)
                nx.draw(self.graphastar1.graph, pos, with_labels=True, node_size=1500)

                # Draw heuristic values over nodes
                labels = {node: str(self.HeuristicDict[node]) for node in self.graphastar1.graph}
                pos_labels = {k: (v[0], v[1] + 0.15) for k, v in pos.items()}  # Shift label positions up slightly
                nx.draw_networkx_labels(self.graphastar1.graph, pos_labels, labels, font_size=26)

                nx.draw_networkx_edge_labels(self.graphastar1.graph, pos, font_size=26,
                                             edge_labels=nx.get_edge_attributes(self.graphastar1.graph, 'weight'))
                plt.show()
            elif self.GraphTypecomboBox.currentText() == "Directed Graph":
                pos = nx.spring_layout(self.graphastar2.graph)
                nx.draw(self.graphastar2.graph, pos, with_labels=True, node_size=1500)

                # Draw heuristic values over nodes
                labels = {node: str(self.HeuristicDict[node]) for node in self.graphastar2.graph}
                pos_labels = {k: (v[0], v[1] + 0.15) for k, v in pos.items()}  # Shift label positions up slightly
                nx.draw_networkx_labels(self.graphastar2.graph, pos_labels, labels, font_size=26)

                nx.draw_networkx_edge_labels(self.graphastar2.graph, pos, font_size=26,
                                             edge_labels=nx.get_edge_attributes(self.graphastar2.graph, 'weight'))
                plt.show()

        elif self.GraphTypecomboBox.currentText() == "Undirectd Graph":
            pos = nx.spring_layout(G)
            nx.draw(G, pos, with_labels=True, node_size=1500)
            nx.draw_networkx_edge_labels(G, pos, font_size=26, edge_labels=nx.get_edge_attributes(G, 'weight'))
            plt.show()


        elif self.GraphTypecomboBox.currentText() == "Directed Graph":
            pos = nx.spring_layout(DG)
            nx.draw(DG, pos, with_labels=True, node_size=1500)
            nx.draw_networkx_edge_labels(DG, pos, font_size=26, edge_labels=nx.get_edge_attributes(DG, 'weight'))
            plt.show()

    def AddNodeClicked(self):
        N1 = self.Node1_input.text()
        N2 = self.Node2_input.text()
        W = self.EdgeWieght_input.text()
        G.add_edge(N1, N2, weight=W)
        DG.add_edge(N1, N2, weight=W)

        self.EdgeWeight_arr[self.counter] = W
        self.counter = self.counter + 1
        self.Node1_input.clear()
        self.Node2_input.clear()
        self.EdgeWieght_input.clear()

    def HeuristicPushed(self):
        InputHeuristic = int(self.NodeHeuristic_input.text())
        InputNodeH = self.Node_Input.text()
        self.H[self.Node_Input.text()] = self.NodeHeuristic_input.text()
        self.HeuristicDict.update({InputNodeH: InputHeuristic})
        self.graphfirst.set_heuristics(self.HeuristicDict)
        self.graphfirst2.set_heuristics(self.HeuristicDict)
        self.graphastar1.set_heuristics(self.HeuristicDict)
        self.graphastar2.set_heuristics(self.HeuristicDict)
        self.Node_Input.clear()
        self.NodeHeuristic_input.clear()

    def SubmitClicked(self):
        G = self.GoalNode_input.text()

        Goal_list.append(G)
        self.GoalNode_input.clear()

    def setupUi(self, AISearchingTechniquesMainWindow):
        AISearchingTechniquesMainWindow.setObjectName("AISearchingTechniquesMainWindow")
        AISearchingTechniquesMainWindow.resize(779, 790)
        self.centralwidget = QtWidgets.QWidget(AISearchingTechniquesMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SearchTypecomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.SearchTypecomboBox.setGeometry(QtCore.QRect(630, 50, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.SearchTypecomboBox.setFont(font)
        self.SearchTypecomboBox.setObjectName("SearchTypecomboBox")
        self.SearchTypecomboBox.addItem("")
        self.SearchTypecomboBox.addItem("")
        self.SearchTypecomboBox.addItem("")
        self.SearchTypecomboBox.addItem("")
        self.SearchTypecomboBox.addItem("")
        self.SearchTypecomboBox.addItem("")
        self.SearchTypecomboBox.addItem("")
        self.SearchTypecomboBox.addItem("")
        self.SearchTypecomboBox.addItem("")
        self.GenerateGraphButton = QtWidgets.QPushButton(self.centralwidget)
        self.GenerateGraphButton.setGeometry(QtCore.QRect(630, 240, 131, 31))
        self.GenerateGraphButton.setObjectName("GenerateGraphButton")
        self.GenerateGraphButton.clicked.connect(self.GenerateGraphClicked)
        self.Node1_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Node1_input.setGeometry(QtCore.QRect(26, 48, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node1_input.setFont(font)
        self.Node1_input.setText("")
        self.Node1_input.setObjectName("Node1_input")
        self.Node2_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Node2_input.setGeometry(QtCore.QRect(26, 101, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node2_input.setFont(font)
        self.Node2_input.setObjectName("Node2_input")
        self.Node1Label = QtWidgets.QLabel(self.centralwidget)
        self.Node1Label.setGeometry(QtCore.QRect(26, 25, 40, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node1Label.setFont(font)
        self.Node1Label.setObjectName("Node1Label")
        self.Node2Label = QtWidgets.QLabel(self.centralwidget)
        self.Node2Label.setGeometry(QtCore.QRect(26, 78, 40, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node2Label.setFont(font)
        self.Node2Label.setObjectName("Node2Label")
        self.EdgeWieghtLabel = QtWidgets.QLabel(self.centralwidget)
        self.EdgeWieghtLabel.setGeometry(QtCore.QRect(26, 131, 72, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.EdgeWieghtLabel.setFont(font)
        self.EdgeWieghtLabel.setObjectName("EdgeWieghtLabel")
        self.EdgeWieght_input = QtWidgets.QLineEdit(self.centralwidget)
        self.EdgeWieght_input.setGeometry(QtCore.QRect(26, 157, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.EdgeWieght_input.setFont(font)
        self.EdgeWieght_input.setObjectName("EdgeWieght_input")
        self.AddNodesButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddNodesButton.setGeometry(QtCore.QRect(26, 189, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.AddNodesButton.setFont(font)
        self.AddNodesButton.setObjectName("AddNodesButton")
        self.AddNodesButton.clicked.connect(self.AddNodeClicked)
        self.TheResult_Label = QtWidgets.QLabel(self.centralwidget)
        self.TheResult_Label.setGeometry(QtCore.QRect(10, 280, 751, 481))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TheResult_Label.setFont(font)
        self.TheResult_Label.setFrameShape(QtWidgets.QFrame.Box)
        self.TheResult_Label.setLineWidth(2)
        self.TheResult_Label.setText("")
        self.TheResult_Label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.TheResult_Label.setObjectName("TheResult_Label")
        self.GeneratePathButton = QtWidgets.QPushButton(self.centralwidget)
        self.GeneratePathButton.setGeometry(QtCore.QRect(460, 240, 131, 31))
        self.GeneratePathButton.setObjectName("GeneratePathButton")
        self.GeneratePathButton.clicked.connect(self.GeneratePathClicked)
        self.TheResultLabel = QtWidgets.QLabel(self.centralwidget)
        self.TheResultLabel.setGeometry(QtCore.QRect(10, 230, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.TheResultLabel.setFont(font)
        self.TheResultLabel.setObjectName("TheResultLabel")
        self.Node_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.Node_Input.setGeometry(QtCore.QRect(227, 49, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node_Input.setFont(font)
        self.Node_Input.setText("")
        self.Node_Input.setObjectName("Node_Input")
        self.NodeLabel = QtWidgets.QLabel(self.centralwidget)
        self.NodeLabel.setGeometry(QtCore.QRect(227, 26, 33, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.NodeLabel.setFont(font)
        self.NodeLabel.setObjectName("NodeLabel")
        self.NodeHeuristicLabel = QtWidgets.QLabel(self.centralwidget)
        self.NodeHeuristicLabel.setGeometry(QtCore.QRect(227, 78, 82, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.NodeHeuristicLabel.setFont(font)
        self.NodeHeuristicLabel.setObjectName("NodeHeuristicLabel")
        self.NodeHeuristic_input = QtWidgets.QLineEdit(self.centralwidget)
        self.NodeHeuristic_input.setGeometry(QtCore.QRect(227, 101, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.NodeHeuristic_input.setFont(font)
        self.NodeHeuristic_input.setObjectName("NodeHeuristic_input")
        self.AddNodeHeuristicButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddNodeHeuristicButton.setGeometry(QtCore.QRect(227, 130, 117, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.AddNodeHeuristicButton.setFont(font)
        self.AddNodeHeuristicButton.setObjectName("AddNodeHeuristicButton")
        self.AddNodeHeuristicButton.clicked.connect(self.HeuristicPushed)
        self.StartNode_input = QtWidgets.QLineEdit(self.centralwidget)
        self.StartNode_input.setGeometry(QtCore.QRect(430, 49, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.StartNode_input.setFont(font)
        self.StartNode_input.setText("")
        self.StartNode_input.setObjectName("StartNode_input")
        self.StartNodeLabel = QtWidgets.QLabel(self.centralwidget)
        self.StartNodeLabel.setGeometry(QtCore.QRect(430, 26, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.StartNodeLabel.setFont(font)
        self.StartNodeLabel.setObjectName("StartNodeLabel")
        self.GoalNodeLabel = QtWidgets.QLabel(self.centralwidget)
        self.GoalNodeLabel.setGeometry(QtCore.QRect(430, 77, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.GoalNodeLabel.setFont(font)
        self.GoalNodeLabel.setObjectName("GoalNodeLabel")
        self.GoalNode_input = QtWidgets.QLineEdit(self.centralwidget)
        self.GoalNode_input.setGeometry(QtCore.QRect(430, 100, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.GoalNode_input.setFont(font)
        self.GoalNode_input.setObjectName("GoalNode_input")
        self.GraphTypecomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.GraphTypecomboBox.setGeometry(QtCore.QRect(630, 100, 122, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.GraphTypecomboBox.setFont(font)
        self.GraphTypecomboBox.setObjectName("GraphTypecomboBox")
        self.GraphTypecomboBox.addItem("")
        self.GraphTypecomboBox.addItem("")
        self.SubmitButton = QtWidgets.QPushButton(self.centralwidget)
        self.SubmitButton.setGeometry(QtCore.QRect(430, 150, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.SubmitButton.setFont(font)
        self.SubmitButton.setObjectName("SubmitButton")
        self.SubmitButton.clicked.connect(self.SubmitClicked)
        AISearchingTechniquesMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AISearchingTechniquesMainWindow)
        self.statusbar.setObjectName("statusbar")

        self.TheResult_Label.setStyleSheet("background-color: lightGray;")

        # Set the button colors
        self.GenerateGraphButton.setStyleSheet("background-color: pink;")
        self.AddNodesButton.setStyleSheet("background-color: pink;")
        self.GeneratePathButton.setStyleSheet("background-color: pink;")
        self.AddNodeHeuristicButton.setStyleSheet("background-color: pink;")
        self.SubmitButton.setStyleSheet("background-color: pink;")

        # Set the label colors
        self.TheResultLabel.setStyleSheet("color: green;")
        self.Node1Label.setStyleSheet("color: black;")
        self.Node2Label.setStyleSheet("color: black;")
        self.EdgeWieghtLabel.setStyleSheet("color: black;")
        self.NodeLabel.setStyleSheet("color: black;")
        self.NodeHeuristicLabel.setStyleSheet("color: black;")
        self.StartNodeLabel.setStyleSheet("color: black;")
        self.GoalNodeLabel.setStyleSheet("color: black;")

        # Set the combobox colors
        self.SearchTypecomboBox.setStyleSheet("background-color: white;")
        self.GraphTypecomboBox.setStyleSheet("background-color: white;")

        # Set the line edit colors
        self.Node1_input.setStyleSheet("background-color: lightYellow;")
        self.Node2_input.setStyleSheet("background-color: lightYellow;")
        self.EdgeWieght_input.setStyleSheet("background-color: lightYellow;")
        self.Node_Input.setStyleSheet("background-color: lightYellow;")
        self.NodeHeuristic_input.setStyleSheet("background-color: lightYellow;")
        self.StartNode_input.setStyleSheet("background-color: lightYellow;")
        self.GoalNode_input.setStyleSheet("background-color: lightYellow;")

        # Set the status bar color
        self.statusbar.setStyleSheet("background-color: gray;")






        self.retranslateUi(AISearchingTechniquesMainWindow)
        QtCore.QMetaObject.connectSlotsByName(AISearchingTechniquesMainWindow)
        AISearchingTechniquesMainWindow.setStatusBar(self.statusbar)

    def retranslateUi(self, AISearchingTechniquesMainWindow):
        _translate = QtCore.QCoreApplication.translate
        AISearchingTechniquesMainWindow.setWindowTitle(
            _translate("AISearchingTechniquesMainWindow", "AI Searching Techniques"))
        self.SearchTypecomboBox.setCurrentText(_translate("AISearchingTechniquesMainWindow", "BFS"))
        self.SearchTypecomboBox.setItemText(0, _translate("AISearchingTechniquesMainWindow", "BFS"))
        self.SearchTypecomboBox.setItemText(1, _translate("AISearchingTechniquesMainWindow", "DFS"))
        self.SearchTypecomboBox.setItemText(2, _translate("AISearchingTechniquesMainWindow", "A*"))
        self.SearchTypecomboBox.setItemText(3, _translate("AISearchingTechniquesMainWindow", "UCS"))
        self.SearchTypecomboBox.setItemText(4, _translate("AISearchingTechniquesMainWindow", "IDS"))
        self.SearchTypecomboBox.setItemText(5, _translate("AISearchingTechniquesMainWindow", "Bidirect"))
        self.SearchTypecomboBox.setItemText(6, _translate("AISearchingTechniquesMainWindow", "BESTF"))
        self.SearchTypecomboBox.setItemText(7, _translate("AISearchingTechniquesMainWindow", "SIMULATED"))
        self.SearchTypecomboBox.setItemText(8, _translate("AISearchingTechniquesMainWindow", "ALPHABETA"))
        self.GenerateGraphButton.setText(_translate("AISearchingTechniquesMainWindow", "Generate Graph"))
        self.Node1Label.setText(_translate("AISearchingTechniquesMainWindow", "Node 1"))
        self.Node2Label.setText(_translate("AISearchingTechniquesMainWindow", "Node 2"))
        self.EdgeWieghtLabel.setText(_translate("AISearchingTechniquesMainWindow", "Edge Wieght"))
        self.AddNodesButton.setText(_translate("AISearchingTechniquesMainWindow", "Add Nodes"))
        self.TheResult_Label.setWhatsThis(_translate("AISearchingTechniquesMainWindow",
                                                     "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.GeneratePathButton.setText(_translate("AISearchingTechniquesMainWindow", "Generate Path"))
        self.TheResultLabel.setText(_translate("AISearchingTechniquesMainWindow", "The Result"))
        self.NodeLabel.setText(_translate("AISearchingTechniquesMainWindow", "Node "))
        self.NodeHeuristicLabel.setText(_translate("AISearchingTechniquesMainWindow", "Node Heuristic"))
        self.AddNodeHeuristicButton.setText(_translate("AISearchingTechniquesMainWindow", "Add Node Heuristic"))
        self.StartNodeLabel.setText(_translate("AISearchingTechniquesMainWindow", "Start Node"))
        self.GoalNodeLabel.setText(_translate("AISearchingTechniquesMainWindow", "Goal Nodes"))
        self.GraphTypecomboBox.setCurrentText(_translate("AISearchingTechniquesMainWindow", "Undirectd Graph"))
        self.GraphTypecomboBox.setItemText(0, _translate("AISearchingTechniquesMainWindow", "Undirectd Graph"))
        self.GraphTypecomboBox.setItemText(1, _translate("AISearchingTechniquesMainWindow", "Directed Graph"))
        self.SubmitButton.setText(_translate("AISearchingTechniquesMainWindow", "Submit"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AISearchingTechniquesMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())