ENHARMONICS = {
    'c#': 'db', 'd#': 'eb', 'f#': 'gb', 'g#': 'ab', 'a#': 'bb',
    'db': 'c#', 'eb': 'd#', 'gb': 'f#', 'ab': 'g#', 'bb': 'a#',
}


def same_note(note1: str, note2: str):
    if note1.lower() == note2.lower():
        # Exactly the same note => good
        return True
    if note1[-1] != note2[-1]:
        # Different height => no good
        return False
    pitch1 = note1[:-1].lower()
    pitch2 = note2[:-1].lower()

    if ENHARMONICS.get(pitch1) == pitch2:
        return True

    return False
