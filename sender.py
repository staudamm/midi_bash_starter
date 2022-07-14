import mido


if __name__ == "__main__":
    port_name = 'IAC Driver Bus 1'
    port = mido.open_output(port_name)
    port.send(mido.Message('note_on', note=50, channel=2))
