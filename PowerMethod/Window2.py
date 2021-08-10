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
    [sg.Text('Number of Iterations: ', size=(15, 1)),  sg.Input(key='txt1', size=(3,1))],
    [sg.Text('Square Matrix Size: ', size=(15, 1)),  sg.Input(key='txt2', size=(3,1))],
    [sg.Button('Execute')],  


    [sg.Text('_' * 80)],
    [sg.Text('Choose A File', size=(25, 1))],
    [sg.Text('Your File: ', size=(10, 1), auto_size_text=False, justification='right'),
     sg.InputText(' ', size=(30, 1)), sg.FolderBrowse(), sg.Button('Export to CSV')],
    [sg.Text('_' * 80)], 

    ]
tab2_layout =  [[sg.T('This is inside tab 2')]]

layout = [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout), sg.Tab('Tab 2', tab2_layout)]])],
              ]

window = sg.Window('Power Method for Page Rank', layout)

event, values = window.read()
window.close()
