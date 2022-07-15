import mido


port_name = 'IAC Driver Bus 1'
note = 0
channel = 0

if __name__ == "__main__":
    port = mido.open_output(port_name)
    port.send(mido.Message('note_on', note=note, channel=channel))
