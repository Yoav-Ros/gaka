from mingus.extra import lilypond

def generate_start_tone_as_note(start_note):
    note = lilypond.from_note()
    my_note=start_note
    answer = note(my_note)
    return answer



