import allure


def allure_attach(fn):
    def wrapper(*args, **kwargs):
        query = kwargs.get("query")
        query = query.compile(compile_kwargs={"literal_binds": True})
        allure.attach(
            str(query),
            name="query",
            attachment_type=allure.attachment_type.TEXT,
        )
        dataset = fn(*args, **kwargs)
        if dataset is not None:
            allure.attach(
                str(dataset),
                name="dataset",
                attachment_type=allure.attachment_type.TEXT,
            )
        return dataset

    return wrapper
