# from solutions import solutions
# from subprocess import Popen
#
#
# def get_audio_file_path(i):
#     return f"data/audio/Play_the_same_note_{i:02d}.mp3"
#
#
# if __name__ == '__main__':
#     audio_path = get_audio_file_path(1)
#     process = Popen(['afplay', audio_path])
#     # process.wait()
#     input('play a key to stop')
#     process.terminate()
#

import eel

# Set web files folder and optionally specify which file types to check for eel.expose()
#   *Default allowed_extensions are: ['.js', '.html', '.txt', '.htm', '.xhtml']
eel.init('web', allowed_extensions=['.js', '.html'])


@eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)


say_hello_py('Python World!')
eel.say_hello_js('Python World!')   # Call a Javascript function

eel.start('hello.html')             # Start (this blocks and enters loop)
