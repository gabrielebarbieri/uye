from solutions import solutions
from note_checker import same_note
from subprocess import Popen
from random import shuffle
from datetime import datetime


def get_audio_file_path(i):
    return f"data/audio/Play_the_same_note_{i:02d}.mp3"


class Player:

    def __init__(self, audio_file):
        self.audio_file = audio_file
        self.process = None

    def stop(self):
        if self.process is not None:
            self.process.terminate()
            self.process = None

    def play(self):
        self.stop()
        self.process = Popen(['afplay', self.audio_file])


class Exercise:

    def __init__(self, exercise_id: int):
        self.exercise_id = exercise_id
        self.player = Player(get_audio_file_path(exercise_id))
        self.solution = solutions[self.exercise_id]
        self.answer = None

    def collect_answer(self):
        self.player.play()
        user_input = input()
        while not user_input:
            # Enter means replay the audio file
            self.player.play()
            user_input = input()
        self.player.stop()
        self.answer = user_input

    def playback(self):
        self.player.play()
        user_input = input()
        while user_input:
            # Here Enter means stop the audio file
            self.player.play()
            user_input = input()
        self.player.stop()

    @property
    def is_correct(self):
        return same_note(self.solution, self.answer)

    def check_answer(self):
        if self.is_correct:
            print(f'You are right, the solution is {self.solution}')
            return True
        print(f'You are wrong, the solution is {self.solution}')
        print(f'Compare {self.answer} versus {self.solution}')
        self.playback()
        return False

    def run(self):
        self.collect_answer()
        self.check_answer()
        return self.is_correct


def run_all_exercises():
    ids = list(range(1, 51))
    shuffle(ids)
    exercises = [Exercise(i) for i in ids]
    correct = 0
    total = 0
    t = datetime.now()
    for exercise in exercises:
        total += 1
        if exercise.run():
            correct += 1
        print('-' * 80)
        print(f'The actual score is {correct}/{total}')
        print(f'Elapsed time: {datetime.now() - t}')
        print('-' * 80)


if __name__ == '__main__':
    run_all_exercises()
