import mido
import subprocess
import asyncio

midi_port = None
channel = 0
note_id = 0
script_name = './default.sh'


def select_input():
    inputs = mido.get_input_names()
    select_string = ""
    for idx, inp in enumerate(inputs):
        select_string += str(idx) + ": " + inp + "\n"
    index = input("Select inputs by entering the corresponding number: \n" + select_string)
    return inputs[int(index)]


def handle_input(message):
    if message.channel == channel and message.note == note_id:
        subprocess.run(['/bin/bash', script_name])
    else:
        print("received message", message)


def connect_midi(port_name):
    mido.open_input(port_name, False, handle_input)


async def loop():
    while True:
        await asyncio.sleep(0.001)


def select_channel():
    user_input = input('Enter midi-channel (default: 0)')
    return 0 if user_input == "" else int(user_input)


def select_note():
    user_input = input('Enter midi-note from 0 (default) to 127')
    return 0 if user_input == "" else int(user_input)


def select_script():
    user_input = input('Enter absolute path to the bash-script')
    if user_input != "":
        return user_input
    else:
        return script_name


if __name__ == "__main__":
    port_name = select_input()
    channel = select_channel()
    note_id = select_note()
    script_name = select_script()
    print("Selected parameter: \n\tInput: {}\n\tChannel: {}\n\tNote: {}\n\tScript: {}".format(
        port_name, channel, note_id, script_name))
    connect_midi(port_name)
    asyncio.run(loop())
