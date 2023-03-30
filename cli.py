import sys


class InputBuilder:
    def __init__(self):
        self.inputs = sys.argv
        self.size = None
        self.path = None

    def set_size(self):
        try:
            arg_idx = self.inputs.index("-s")
            value = self.inputs[arg_idx+1]
            [width, height] = value.split('x')
            self.size = [int(width), int(height)]

            print(f"Size argument: {self.inputs[arg_idx]}")
            print(f"Size arg value: {value}")

            return self
        except IndexError:
            print("Index error while parsing args size!")

    def get_path(self):
        return self.path

    def set_path(self):
        self.path = self.inputs[1]
        return self

    def print(self):
        print(f"Command line arguments: {self.inputs}")
        print(f"Size: {self.size}")
        print(f"Path: {self.path}")

    def build(self):
        self.set_size()
        self.set_path()
        return self

    def args(self):
        return self.inputs
