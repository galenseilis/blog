# How-to guides

## Run a Python file and capture its output

```python
from asyncio_hello_world.runner import run_python_file

output = run_python_file("path/to/script.py")
print(output, end="")
```

`run_python_file` returns the child's standard output as a string. If the child
exits unsuccessfully, it returns a message containing the child's standard error
instead of raising.

## Choose a specific interpreter

```python
run_python_file("script.py", interpreter="/usr/bin/python3.12")
```

The default is the interpreter running the current process (`sys.executable`),
which is usually what you want.

## Embed the greeting in a document

Run the console script and paste its output, or shell out from the document:

````markdown
```python
from asyncio_hello_world import runner
print(runner.run_python_file("greet.py"), end="")
```
````

## Handle errors from a failed child process

Because the failure is returned as a string, check for the prefix:

```python
output = run_python_file("maybe_broken.py")
if output.startswith("An error occurred"):
    raise RuntimeError(output)
```
