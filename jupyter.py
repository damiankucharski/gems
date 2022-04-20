from IPython import get_ipython


def launch_autoreload():
    ipython = get_ipython()

    ipython.magic("load_ext autoreload")
    ipython.magic("autoreload 2")


def launch_inline():
    ipython = get_ipython()
    ipython.magic('matplotlib inline')


def standard_setup():
    launch_autoreload()
    launch_inline()
