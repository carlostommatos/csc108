"""CSC108H1: Fall 2026 -- Assignment 2

This code is provided solely for the personal and private use of students
taking the CSC108 course at the University of Toronto. Copying for purposes
other than this use is expressly prohibited. All forms of distribution of
this code, whether as given or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2026 CSC108H1 Teaching Team
"""

import ast
import os
import sys
import runpy
import doctest
import threading
import subprocess
import importlib.util
from copy import deepcopy

PYTHON_TA_VERSION = '2.13.1'

CHECKER_DIR = os.path.dirname(os.path.abspath(__file__))

# Seconds a single call may take before we assume the loop never ends.
CALL_TIMEOUT = 5

TYPE_ERROR_MSG = '{} should return a {}, but returned {!r}, which is a {}.'


# The code you were given in a2-task6.py and a2-task7.py, above and below
# your own work. Only the lines with ? placeholders should change.
TASK6_PROLOGUE = """\
TARGET = 5

my_list = ['rode', 'biked', 'ran', 'walked']
"""

TASK6_EPILOGUE = """\
print(my_list)
"""

TASK7_PROLOGUE = """\
values = [7, 5, 9]
items = values
nums = values[:]
"""

TASK7_EPILOGUE = """\
print(values)
print(items)
print(nums)
print(removed)
"""

# Task label -> (file to check, code above your work, code below your work)
MEMORY_MODEL_TASKS = {
    'Task 6': ('a2-task6.py', TASK6_PROLOGUE, TASK6_EPILOGUE),
    'Task 7': ('a2-task7.py', TASK7_PROLOGUE, TASK7_EPILOGUE),
}


def attempt_python_ta_installation(version: int) -> int:
    """Attempt installation of PythonTA.
    Returns the next version to attempt if there is one, or -1 if there
    are no other versions after version.
    """
    executables = ['python3.13', sys.executable]
    attempts = [f'-m pip install python-ta=={PYTHON_TA_VERSION}',
                # Turn off SSL verification (certificate errors)
                f'-m pip install python-ta=={PYTHON_TA_VERSION} '
                f'config --global http.sslVerify false',
                # Set pypi as a trusted host
                f'-m pip install python_ta=={PYTHON_TA_VERSION} '
                f'--trusted-host pypi.python.org'
                ]

    try:
        executable = executables[version % 2]
        attempt = attempts[version // 2]

        if executable == 'python3.13':
            subprocess.Popen(executable + ' ' + attempt,
                             shell=True,
                             stdout=subprocess.DEVNULL,
                             stderr=subprocess.DEVNULL)
        else:
            subprocess.check_call([executable] + attempt.split(),
                                  stderr=subprocess.DEVNULL,
                                  stdout=subprocess.DEVNULL)
    except:
        pass

    if version < len(attempts) * 2:
        return version + 1

    return -1


def python_ta_installed() -> bool:
    """Return True if PythonTA is installed."""
    try:
        if 'python_ta' in sys.modules:
            del sys.modules['python_ta']

        import python_ta
        importlib.reload(python_ta)
        installed_version = python_ta.__version__
        return installed_version == PYTHON_TA_VERSION
    except:
        return False


def install_python_ta():
    """Tries to install PythonTA."""
    if not python_ta_installed():
        print("Installing / Updating the style checker", end='')

    i = 0
    while not python_ta_installed() and i != -1:
        print(".", end='')
        i = attempt_python_ta_installation(i)

    print("")


def resolve(filename: str) -> str:
    """Return the path to filename, looking in the folder this checker is in
    before falling back to the current working directory.
    """

    beside_checker = os.path.join(CHECKER_DIR, filename)
    if os.path.exists(beside_checker):
        return beside_checker
    return filename


def run_pyta(filename: str, config_file: str) -> None:
    """Run PYTA with configuration config_file on the file named filename.
    """
    import json
    install_python_ta()

    error_message = '\nCould not install or run the style checker correctly.\n' \
                    'Please try to re-run the checker once.\n' \
                    'If you have already tried to re-run it, please go to office hours\n' \
                    'in order to resolve this. ' \
                    'For now, you may upload your code to MarkUs and run the self-test\n' \
                    'to see the style checker results.'

    try:
        import python_ta
        with open(resolve(config_file)) as cf:
            config_dict = json.loads(cf.read())
            config_dict['output-format'] = 'pyta-plain'

        # the shortest name that still points at the file, so that the
        # report header reads a2.py rather than a full path
        path = resolve(filename)
        try:
            path = os.path.relpath(path)
        except ValueError:
            pass

        python_ta.check_all(path, config=config_dict)
    except:
        print(error_message)


def find_file(filename: str, task: str) -> str:
    """Return the path to filename, one of the files you submit.

    Raises AssertionError if it cannot be found.
    """

    path = resolve(filename)
    if not os.path.exists(path):
        raise AssertionError(
            '{} could not be found. Make sure it is in the same folder as '
            'a2_checker.py and named exactly {} ({})'.format(
                filename, filename, task))
    return path


def get_submission(filename: str, task: str):
    """Return the module in filename, which is one of the files you submit.

    Imported here rather than at the top of the checker so that a syntax
    error in your file is reported as a checker result, after the style
    report that points at it, instead of crashing before anything runs.
    """

    find_file(filename, task)
    module_name = filename[:-len('.py')]
    try:
        return importlib.import_module(module_name)
    except SyntaxError as exn:
        raise AssertionError(
            '{} has a syntax error on line {}: {}. Fix that first; the '
            'style report above points at it ({})'.format(
                filename, exn.lineno, exn.msg, task)) from None
    except Exception as exn:
        raise AssertionError(
            '{} could not be imported: {}: {} ({})'.format(
                filename, type(exn).__name__, exn, task)) from None


def get_function(filename: str, name: str, task: str):
    """Return the function called name from filename.

    Raises AssertionError rather than asserting, so that the report shows
    the message on its own instead of following it with the expression that
    failed ("assert None is not None"), which means nothing to a student.
    """

    func = getattr(get_submission(filename, task), name, None)
    if func is None:
        raise AssertionError(
            '{} not found in {}. Make sure you have defined it following '
            'the Function Design Recipe ({})'.format(name, filename, task))
    if not callable(func):
        raise AssertionError(
            '{} in {} is not a function ({})'.format(name, filename, task))
    return func


def get_function_from_file(filename: str, name: str, task: str):
    """Return the function called name from filename.

    Used for the files whose names contain a hyphen, which means they cannot
    be imported by name the way get_function does it, so they are loaded from
    the file directly instead.
    """

    path = find_file(filename, task)
    spec = importlib.util.spec_from_file_location(name + '_module', path)
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except SyntaxError as exn:
        raise AssertionError(
            '{} has a syntax error on line {}: {}. Make sure you have '
            'replaced every ? with code ({})'.format(
                filename, exn.lineno, exn.msg, task)) from None
    except Exception as exn:
        raise AssertionError(
            'running {} caused an error: {} ({})'.format(
                filename, exn, task)) from None

    func = getattr(module, name, None)
    if func is None:
        raise AssertionError(
            '{} not found in {}. Make sure you did not rename or delete it '
            '({})'.format(name, filename, task))
    return func


def call_with_timeout(func: callable, args: list):
    """Call func(*args) and return its result.

    Raises TimeoutError if the call does not finish within CALL_TIMEOUT.
    Uses a daemon thread rather than signal.alarm so this works on Windows
    as well; the runaway thread cannot be stopped, but it will not keep the
    checker from exiting.
    """

    result = {}

    def run():
        try:
            result['value'] = func(*args)
        except BaseException as exn:     # re-raised on the calling thread
            result['error'] = exn

    thread = threading.Thread(target=run, daemon=True)
    thread.start()
    thread.join(CALL_TIMEOUT)

    if thread.is_alive():
        raise TimeoutError(
            'did not finish within {} seconds. Check that every loop '
            'eventually ends.'.format(CALL_TIMEOUT))
    if 'error' in result:
        raise result['error']
    return result.get('value')


def type_check_simple(func: callable, args: list,
                      expected: type) -> tuple[bool, object]:
    """Check if func(args) returns a result of type expected.

    Return (True, result-of-call) if the check succeeds.
    Return (False, error-or-failure-message) if anything goes wrong.
    """

    try:
        args_copy = deepcopy(args)
        returned = call_with_timeout(func, args_copy)
    except TimeoutError as exn:
        return (False, '{} {}'.format(func.__name__, exn))
    except Exception as exn:
        return (False, error_message(func, args, exn))

    if isinstance(returned, expected):
        return (True, returned)

    return (False, TYPE_ERROR_MSG.format(
        func.__name__, expected.__name__, returned, type(returned).__name__))


def error_message(func: callable, args: list,
                  error: Exception) -> str:
    """Return an error message: func(args) raised an error."""

    return 'The call {}({}) caused an error: {}'.format(
        func.__name__, ','.join(map(repr, args)), error)


def check_type(func: callable, args: list, ret_type: type) -> None:
    """Check that func called with args returns a value of type ret_type.
    Assert on failure.
    """

    result = type_check_simple(func, args, ret_type)
    assert result[0] is True, result[1]


def check_docstring_calls(func: callable, min_calls: int, task: str) -> None:
    """Check that func's docstring calls func at least min_calls times.

    For a function that changes its argument instead of returning a value,
    where the call itself has no output line.
    """

    name = func.__name__
    try:
        examples = doctest.DocTestParser().get_examples(func.__doc__ or '')
    except ValueError:
        raise AssertionError(
            '{} docstring examples could not be parsed. Make sure each '
            'example line starts with ">>> " (>>> followed by a space) '
            '({})'.format(name, task)) from None

    calls = [ex for ex in examples if '{}('.format(name) in ex.source]
    assert len(calls) >= min_calls, (
        '{}\'s docstring calls {} {} time(s), but it needs at least {}. '
        'Make sure you have added your example ({})'.format(
            name, name, len(calls), min_calls, task)
    )


def _statement_dumps(body: list) -> list:
    """Return a representation of each statement in body that ignores
    comments, blank lines, and indentation width.
    """

    return [ast.dump(node) for node in body]


def _find_block(body: list, block: str) -> int:
    """Return the index in body where the statements of block appear
    together, or -1 if they do not appear.
    """

    student = _statement_dumps(body)
    target = _statement_dumps(ast.parse(block).body)
    for start in range(len(student) - len(target) + 1):
        if student[start:start + len(target)] == target:
            return start

    return -1


def _without_docstring(body: list) -> list:
    """Return body without a leading module docstring."""

    if (body and isinstance(body[0], ast.Expr)
            and isinstance(body[0].value, ast.Constant)
            and isinstance(body[0].value.value, str)):
        return body[1:]

    return body


def check_memory_model_file(task: str) -> None:
    """Check the memory model file for task, a key of MEMORY_MODEL_TASKS.

    The file must keep the code you were given at the top and bottom, have
    your own code in between, and run. Comments and blank lines are ignored.
    Does not check whether your memory model is correct.
    """

    filename, prologue, epilogue = MEMORY_MODEL_TASKS[task]
    path = find_file(filename, task)

    with open(path, encoding='utf-8') as f:
        source = f.read()

    try:
        body = _without_docstring(ast.parse(source, filename=filename).body)
    except SyntaxError as exn:
        raise AssertionError(
            '{} has a syntax error on line {} and could not be run: {}. '
            'Make sure you have replaced every ? with code ({})'.format(
                filename, exn.lineno, exn.msg, task)) from None

    start = _find_block(body, prologue)
    assert start == 0, (
        'the code you were given at the top of {} was changed or moved. '
        'Restore it exactly as it was given to you ({})'.format(
            filename, task)
    )

    end = _find_block(body, epilogue)
    assert end != -1, (
        'the code you were given at the bottom of {} was changed or removed '
        '-- restore it exactly as it was given to you ({})'.format(
            filename, task)
    )

    n_prologue = len(ast.parse(prologue).body)
    n_epilogue = len(ast.parse(epilogue).body)

    after = body[end + n_epilogue:]
    assert not after, (
        '{} has {} extra statement(s) after the code you were given, '
        'starting on line {} ({})'.format(
            filename, len(after), after[0].lineno, task)
    )

    assert end > n_prologue, (
        'you have not added any code to {}. Replace each ? with the code '
        'needed to produce the required memory model ({})'.format(
            filename, task)
    )

    try:
        runpy.run_path(path)
    except Exception as exn:
        raise AssertionError(
            'running {} caused an error: {}. Check the code you wrote '
            '({})'.format(filename, exn, task)) from None
