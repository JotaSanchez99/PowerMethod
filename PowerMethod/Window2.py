import PySimpleGUI as sg
from Operation import Operation
import csv
from datetime import datetime


#sg.ChangeLookAndFeel('GreenTan')

# ------ Menu Definition ------ #
menu_def = [['&File', ['&Open', '&Save', 'E&xit', 'Properties']],
            ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Help', '&About...'], ]

tab1_layout = [[sg.Menu(menu_def, tearoff=True)],
    
    [sg.Text('Control Panel') ],

    [sg.Frame(layout=[
    
    [sg.Radio('Random Stochastic Matrix     ', "key1", default=True, size=(20,1)), sg.Radio('Comma-Separated Values (CSV) File ', "key1")]], title='Select the matrix source', relief=sg.RELIEF_SUNKEN)],
    [sg.Text('_' * 80)],

]