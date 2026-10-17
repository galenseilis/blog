from asyncio_hello_world.runner import run_python_file


def test_run_python_file_captures_stdout(tmp_path):
    script = tmp_path / "greet.py"
    script.write_text("print('hi')\n")
    assert run_python_file(script) == "hi\n"


def test_run_python_file_reports_failure(tmp_path):
    script = tmp_path / "boom.py"
    script.write_text("raise SystemExit('boom')\n")
    assert run_python_file(script).startswith("An error occurred")
