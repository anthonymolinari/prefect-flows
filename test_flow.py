from prefect import flow, task


@task(log_prints=True)
def say_hello(name: str):
    print(f"Hello {name}!")


@task(log_prints=True)
def say_goodbye(name: str):
    print(f"Goodbye {name}!")


@flow
def hello_universe():
    names = ["Jim", "John", "Joe"]
    for name in names:
        say_hello(name)
        say_goodbye(name)
