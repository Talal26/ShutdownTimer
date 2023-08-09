from subprocess import run
import time


def _shutdown(delay: int, tag: str):
    run(f'shutdown {tag} -t {delay}')


def shutdown(delay: int):
    _shutdown(delay, '-s')


def restart(delay: int):
    _shutdown(delay, '-r')


def sleep(delay: int):
    time.sleep(delay)
    run('rundll32.exe powrprof.dll, SetSuspendState Sleep')
