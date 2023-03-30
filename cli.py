import sys


def get_input():
    parser = InputParser()
    parser.print()
    filepath = parser[1]
    if "-s" in parser.args():
        parser.set_manual_size()
    return filepath


class InputParser:
    def __init__(self):
        self.inputs = sys.argv
        self.size = None

    def set_manual_size(self):
        try:
            arg_idx = self.inputs.index("-s")
            value = self.inputs[arg_idx+1]
            dims = value.split('x')

            self.size = [dims[0], dims[2]]
            print(f"Size argument: {self.inputs[arg_idx]}")
            print(f"Size arg value: {value}")
        except IndexError:
            print("")

    def print(self):
        print(f"Command line arguments: {self.inputs}")

    def args(self):
        return self.inputs
