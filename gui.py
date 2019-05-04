import sys  
import PySimpleGUI as sg  
import numpy as np
from sklearn.externals import joblib
from oxo_q import play_game, check_game



# model = joblib.load('model.joblib')


q_table = np.load('Q_table.npy')

layout = [[sg.Text('Your typed chars appear here:'), sg.Text('', key='_OUTPUT_') ],  
          [sg.Input(do_not_clear=True, key='_IN_')],  
          [sg.Button('Show'), sg.Button('Exit')]]  

layout_oxo = [[sg.Button('   ', key=0), sg.Button('   ', key=1), sg.Button('   ', key=2)],
[sg.Button('   ', key=3), sg.Button('   ', key=4), sg.Button('   ', key=5)],
[sg.Button('   ', key=6), sg.Button('   ', key=7), sg.Button('   ', key=8)], 
[sg.Text('Resultado', key='_OUTPUT_')]]


window = sg.Window('Window Title').Layout(layout_oxo)  

g = np.zeros(9).astype(int) #[0,0,0,0,0,0,0,0,0,0,0]

# game[-2] = 1
# game[-1] = 2

def message(msg):
    window.FindElement('_OUTPUT_').Update(msg)

a = play_game(g, 2)
g[a] = 2
window.FindElement(a).ButtonText = ' X '


while True:                 # Event Loop  
  event, values = window.Read()  
#   print(event, values)

  if event is None or event == 'Exit':  
      break  
  if event == 'Show':  
      # change the "output" element to be the value of "input" element  
      window.FindElement('_OUTPUT_').Update(values['_IN_'])
  if event != '':
      window.FindElement(event).Update(' O ')
      g[event] = 1

      if check_game(g) == 2:
        #   print('Você ganhou')
          message('Você ganhou')
      if check_game(g) == 1:
          message('Empate')
        #   print('Empate')
        #   window.FindElement('_OUTPUT_').Update(values['Empate'])


      if False: #np.sum(q_table[g[0], g[1], g[2], g[3], g[4], g[5], g[6], g[7], g[8], :]) == 0:
          a = play_game(g, 2)
        #   print('CHUTE')
          message('CHUTE')

        #   window.FindElement('_OUTPUT_').Update(values['CHUTE'])
      else:
          a = np.argmax(q_table[g[0], g[1], g[2], g[3], g[4], g[5], g[6], g[7], g[8], :]) 
          print(g, a)
          message('ACTION!!!')

      if check_game(g) == 2:
        #   print('Você ganhou')
          message('Você perdeu')
      if check_game(g) == 1:
          message('Empate')
        #   print('Empate')
        #   window.FindElement('_OUTPUT_').Update(values['Empate'])




      print(a)

      g[a] = 2

      window.FindElement(a).Update(' X ')


window.Close()