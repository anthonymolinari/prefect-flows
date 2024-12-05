from prefect import task


@task(log_prints=True)
def say_hello(name: str):
    print(f"Hello {name}!")


@task(log_prints=True)
def say_goodbye(name: str):
    print(f"Hello {name}!")
