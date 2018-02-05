# coding=utf-8

import time
import yappi as profiler_yappi
import cProfile as cprofile_profiler
import line_profiler
import memory_profiler
from functools import partial
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
from subprocess import call


BLANK_LINES_COUNT = 3
BLANK_LINES = BLANK_LINES_COUNT * '\n'
DELIMETER_LENGTH = 80
DELIMETER_UNIT = '*'
DELIMETER = DELIMETER_LENGTH * DELIMETER_UNIT
PROF_FILENAME = 'cprofile.prof'
CALL_TREE_IMG_FILENAME = 'pycallgraph.png'


def _print_results(result_func_or_str, profiled_func, type):
    print BLANK_LINES
    print DELIMETER
    print '{}-PROFILING of {}.{}(*args, **kwargs)'.format(
        type,
        profiled_func.__module__,
        profiled_func.__name__
    )
    print DELIMETER
    if callable(result_func_or_str):
        result_func_or_str()
    else:
        print result_func_or_str
    print DELIMETER
    print BLANK_LINES


def simple_time(func):

    def _wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = (time.time() - start) * 1000  # ms

        _print_results('duration: {}'.format(duration), func, 'simpletime')

        return result

    return _wrapper


def yappi(func):

    def _wrapper(*args, **kwargs):
        profiler_yappi.start()
        result = func(*args, **kwargs)

        _print_results(profiler_yappi.get_func_stats().print_all, func, 'yappi')
        profiler_yappi.stop()

        return result

    return _wrapper


def cprofile(func):

    def _wrapper(*args, **kwargs):
        profiler = cprofile_profiler.Profile()
        result = profiler.runcall(func, *args, **kwargs)

        _print_results(partial(profiler.print_stats, sort="time"), func, 'cprofile')

        return result

    return _wrapper


def cprofile_dump(func):

    def _wrapper(*args, **kwargs):
        profiler = cprofile_profiler.Profile()
        result = profiler.runcall(func, *args, **kwargs)

        profiler.dump_stats(PROF_FILENAME)

        return result

    return _wrapper


def line(func):

    def _wrapper(*args, **kwargs):
        profiler = line_profiler.LineProfiler()
        result = profiler(func)(*args, **kwargs)

        _print_results(profiler.print_stats, func, 'line')

        return result

    return _wrapper


def memory(func):

    def _wrapper(*args, **kwargs):
        profiler = memory_profiler.LineProfiler()
        result = profiler(func)(*args, **kwargs)

        memory_profiler.show_results(profiler)

        return result

    return _wrapper


def timeit(func):
    n = 1000

    def _wrapper(*args, **kwargs):
        start = time.time()
        for i in range(0, n):
            result = func(*args, **kwargs)

        duration = (time.time() - start) * 1000  # ms

        _print_results('n: {}, all: {}ms, avg: {}ms'.format(
            n,
            duration,
            duration / n
        ), func, 'timeit')

        return result

    return _wrapper


def calltree(func):

    def _wrapper(*args, **kwargs):
        with PyCallGraph(output=GraphvizOutput()):
            result = func(*args, **kwargs)
            call(['open', CALL_TREE_IMG_FILENAME])
        return result

    return _wrapper


def grind(func):

    def _wrapper(*args, **kwargs):
        profiler = cprofile_profiler.Profile()
        result = profiler.runcall(func, *args, **kwargs)
        profiler.dump_stats(PROF_FILENAME)
        call(['pyprof2calltree', '-i', PROF_FILENAME, '-k'])

        return result

    return _wrapper
