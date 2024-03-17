from functools import cached_property


class AssertionsHelper:
    def __init__(self, logic_provider):
        from generic import LogicProvider

        self.logic_provider: LogicProvider = logic_provider

    @cached_property
    def post_v1_account(self):
        from generic.assertions.post_v1_account import AssertionsPostV1Account

        return AssertionsPostV1Account(logic_provider=self.logic_provider)
