from asyncio_hello_world import cli


def test_cli_runs_greeting_in_subprocess(capsys):
    cli.main()
    captured = capsys.readouterr()
    assert captured.out == "Hello,\nWorld!\n"
