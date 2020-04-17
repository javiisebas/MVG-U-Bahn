
import mvg_api
from sty import fg, bg, ef, rs
from sty import Style, RgbFg
import os, sys
import inquirer

sys.path.append(os.path.realpath('.'))


def print_information(destinations):

    print('\n' + bg(255,255,255) + fg(0,0,0) + '  Line    Time     Destination ' + rs.bg + '\n')    

    for stop in destinations:
        if stop['product'] == 'UBAHN':
            destination = stop['destination']
            time = stop['departureTimeMinutes']

            color = {'U1':bg(70, 132, 71),
                     'U2':bg(221, 61, 77),
                     'U3':bg(239, 136, 36),
                     'U4':bg(4, 175, 144),
                     'U5':bg(183, 135, 48),
                     'U6':bg(4, 114, 179),
                     'U7':fg(255,255,255) + bg(70, 132, 71) + ' U' + bg(221, 61, 77) + '7 ' + rs.bg,
                     'U' :fg(255,255,255) + bg(0, 108, 178) + ' U ' + rs.bg}
            
            finalLine = color[stop['label']] + fg(255,255,255) + ' ' + stop['label'] + ' ' + rs.bg

            sep_time = {"1":7, "2":6, "3":5}
            tam_time = str(len(str(time)))
            print('  {}     {}{}{}'.format(finalLine,time," "*sep_time[tam_time],destination))

    print('\n')



def get_info(station):
    global print_information

    try:      

        Id = mvg_api.get_id_for_station(station)

        if Id:
            destinations = mvg_api.get_departures(Id)
            print_information(destinations)

        else:
            print('\n   ' + bg(255,0,0) + ' The station does not exists ' + rs.bg + '\n')

    except:
        print('\n   ' + bg(255,0,0) + ' Something wrong has happened ' + rs.bg + '\n')



def main_process():

    questions = [inquirer.Text("stop",message=fg(255,255,255) +"Stop")]
    station = inquirer.prompt(questions)['stop']

    while station != 'exit':    
        if station != 'exit':

            get_info(station)

            questions = [inquirer.Text("stop",message=fg(255,255,255) +"Stop")]
            station = inquirer.prompt(questions)['stop']
        
main_process()s