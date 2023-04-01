import sys
from errors import SingletonError


class InputBuilder:
    instantiations = 0

    def __init__(self):
        self.inputs = sys.argv
        self.size = None
        self.path = None

    def set_size(self):
        if len(self.inputs) > 3:
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
                sys.exit(1)
        else:
            return

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
        if self.instantiations > 0:
            raise SingletonError()

        self.set_size()
        self.set_path()

        self.instantiations += 1
        return self

    def args(self):
        return self.inputs
