from botXsrc.botXexport import botXexport

"""
botXexport is a dictionary containing all the reusable components you
developed for the project, and you will use them in the main program.
"""
def main():
    print('starting app ...')
    manipulation_api = botXexport['manipulation_api']['module']()
    manipulation_api.setup()
"""
This is the only script that should be running from terminal so that the
program can gather modules correctly, so we need to specify main as entry point.
"""
if __name__ == '__main__':
    main()
