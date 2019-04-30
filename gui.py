import sys  
import PySimpleGUI as sg  


layout = [[sg.Text('Your typed chars appear here:'), sg.Text('', key='_OUTPUT_') ],  
          [sg.Input(do_not_clear=True, key='_IN_')],  
          [sg.Button('Show'), sg.Button('Exit')]]  

layout_oxo = [[sg.Button('   ', key='0'), sg.Button('   ', key='1'), sg.Button('   ', key='2')],
[sg.Button('   ', key='3'), sg.Button('   ', key='4'), sg.Button('   ', key='5')],
[sg.Button('   ', key='6'), sg.Button('   ', key='7'), sg.Button('   ', key='8')], 
[sg.Text('Resultado', key='_OUTPUT_')]]


window = sg.Window('Window Title').Layout(layout_oxo)  

while True:                 # Event Loop  
  event, values = window.Read()  
  print(event, values)
  if event is None or event == 'Exit':  
      break  
  if event == 'Show':  
      # change the "output" element to be the value of "input" element  
      window.FindElement('_OUTPUT_').Update(values['_IN_'])
  if event != '':
      window.FindElement(event).Update(' X ')


window.Close()