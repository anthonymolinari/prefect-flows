from prefect import flow


SOURCE_REPO = "https://github.com/anthonymolinari/prefect-flows.git"


if __name__ == "__main__":
    flow.from_source(
        source=SOURCE_REPO,
        entrypoint="flows/test_flow.py:hello_universe",
    ).deploy(
        name="my-first-deployment",
        work_pool_name="my-work-pool",
        cron="* * * * *",
    )

    flow.from_source(
        source=SOURCE_REPO,
        entrypoint="test_flow.py:goodbye_universe",
    ).deploy(
        name="my-second-deployment",
        work_pool_name="my-work-pool",
        cron="* * * * *",
    )
