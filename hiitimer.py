import argparse
import sys

from utilities import (clear_screen, does_file_exist,
                       load_routine_data, get_routine_data, get_ready,
                       print_loaded_routine, start_period, start_routine)


# Argparse

parser = argparse.ArgumentParser()
parser.add_argument('--filename', '-f', type=str, 
                    help="Load a routine file for your exercise.")
args = parser.parse_args()


# Main Program

if __name__ == '__main__':
    clear_screen()

    if args.filename:
        if not does_file_exist(args.filename):
            print('File not found.')
            sys.exit()
        routine = load_routine_data(args.filename)
        print_loaded_routine(routine)
        input('Press enter to continue...')
    else:
        print()
        routine = get_routine_data()

    start_routine(**routine)