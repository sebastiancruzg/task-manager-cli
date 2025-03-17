import argparse
from scr.task import Task
FILE_PATH = 'db.json'

def get_function(action, _input, **args):
    task = Task(file_path=FILE_PATH)

    ACTIONS_SWITCHER = {
        "add": task.create(_input),
        "update": task.update(_input, args)
    }

    return ACTIONS_SWITCHER[action]

def main():
    parser = argparse.ArgumentParser()
    subparser = parser.add
    parser.add_argument("action", help="Choose an option")
    parser.add_argument("input", help="extra input")

    args = parser.parse_args()
    get_function(args.action, args.input)

if __name__=='__main__':
    main()
