from prefect import flow


SOURCE_REPO = "https://github.com/anthonymolinari/prefect-flows.git"


if __name__ == "__main__":
    flow.from_source(
        source=SOURCE_REPO,
        entrypoint="",
    ).deploy(
        name="",
        work_pool_name="my-work-pool",
        cron="* * * * *",
    )
