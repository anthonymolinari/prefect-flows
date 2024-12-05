from prefect import flow
from tasks.test_task import say_hello, say_goodbye


@flow
def hello_universe():
    names = ["Jim", "John", "Joe"]
    for name in names:
        say_hello(name)


@flow
def goodbye_universe():
    names = ["Sam", "Sal", "Steve"]
    for name in names:
        say_goodbye(name)
