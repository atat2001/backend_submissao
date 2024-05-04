from subprocess import Popen, PIPE, DEVNULL


def test_process(command: list[str], input: str) -> tuple:
    """
    Spawns a process given by command using Popen, passes the desired input
    trough stdin, and returns the code and output given by stdout.

    In case stdout is empty, return the stderr instead.

    All reads and writes are encoded to UTF8.

    Before returning the output, we wait for the process to conclude.
    """
    child = Popen(
        command,
        stdin=PIPE,
        stdout=PIPE,
        stderr=PIPE,
        encoding="utf8"
    )
    child.stdin.write(input)
    child.stdin.close()
    output = child.stdout.read().rstrip()
    # An exception? Return stderr content instead.
    if not output:
        output = child.stderr.read().rstrip()
    child.wait()
    return child.poll(), output


def py_runner(file, input_str):
    """
    Runs a python file with the given the input returning the output code and
    the stdout output.
    """
    a = test_process(["python", file], input_str)
    #print("pyrunner")
    #print(a)
    return a


def js_runner(file, input_str):
    """
    Runs a js file with the given the input returning the output code and
    the stdout output.
    """
    #Install node
    child = Popen(
        ["apk", "add", "nodejs"],
        stdin=DEVNULL,
        stdout=DEVNULL,
        stderr=DEVNULL
    )
    child.wait()
    return test_process(["node", file], input_str)


def c_runner(file, input_str):
    """
    Compiles a c file and runs it with the given the input returning the
    output code and the stdout output.
    """
    # Install gcc
    child = Popen(
        ["apk", "add", "build-base"],
        stdin=DEVNULL,
        stdout=DEVNULL,
        stderr=DEVNULL
    )
    child.wait()
    # Compile the file
    child = Popen(
        ["gcc", file, "-o", "./output.o"],
        stdin=DEVNULL,
        stdout=DEVNULL,
        stderr=DEVNULL
    )
    child.wait()
    # Run it
    return test_process(["./output.o"], input_str)


def cpp_runner(file, input_str):
    """
    Compiles a cpp file and runs it with the given the input returning the
    output code and the stdout output.
    """
    # Install g++
    child = Popen(
        ["apk", "add", "build-base"],
        stdin=DEVNULL,
        stdout=DEVNULL,
        stderr=DEVNULL
    )
    child.wait()
    # Compile the file
    child = Popen(
        ["g++", file, "-o", "./output.o"],
        stdin=DEVNULL,
        stdout=DEVNULL,
        stderr=DEVNULL
    )
    child.wait()
    # Run it
    return test_process(["./output.o"], input_str)


def java_runner(file, input_str):
    """
    Compiles a java file and runs it with the given the input returning the
    output code and the stdout output.
    """
    # Install java
    child = Popen(
        ["apk", "add", "openjdk17"],
        stdin=DEVNULL,
        stdout=DEVNULL,
        stderr=DEVNULL
    )
    child.wait()
    # Compile the file
    child = Popen(
        ["javac", file],
        stdin=DEVNULL,
        stdout=DEVNULL,
        stderr=DEVNULL
    )
    child.wait()
    # Get the file name by removing ".java"
    file_name = file[:-5]
    # Run it
    return test_process(["java", file_name], input_str)


"""Dictionary with items (extension: runner)"""
RUNNERS = {
    "py": py_runner,
    "js": js_runner,
    "c": c_runner,
    "cpp": cpp_runner,
    "java": java_runner
}
