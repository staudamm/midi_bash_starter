import mido
import subprocess


def select_input():
    inputs = mido.get_input_names()
    select_string = ""
    for idx, inp in enumerate(inputs):
        select_string += str(idx) + ": " + inp + "\n"
    index = input("Select inputs by entering the corresponding number: \n" + select_string)
    return inputs[int(index)]


if __name__ == "__main__":
    inp = select_input()
    print("Selected: " + inp)
    subprocess.run(['/bin/bash', './default.sh'])
