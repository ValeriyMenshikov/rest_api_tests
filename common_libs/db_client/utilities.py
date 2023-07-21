import allure


def allure_attach(fn):
    def wrapper(*args, **kwargs):
        query = kwargs.get('query')
        allure.attach(query, name='query', attachment_type=allure.attachment_type.TEXT)
        dataset = fn(*args, **kwargs)
        if dataset is not None:
            allure.attach(dataset, name='dataset', attachment_type=allure.attachment_type.TEXT)
        return dataset

    return wrapper
