import asyncio

from asyncio_hello_world.hello import main


def test_main_prints_greeting(capsys):
    asyncio.run(main())
    captured = capsys.readouterr()
    assert captured.out == "Hello,\nWorld!\n"
