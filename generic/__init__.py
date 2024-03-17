from functools import cached_property


class LogicProvider:
    @cached_property
    def provider(self):
        from modules import modules_provider

        return modules_provider()

    @cached_property
    def account_helper(self):
        from generic.helpers.account import Account

        return Account(self)

    @cached_property
    def login_helper(self):
        from generic.helpers.login import Login

        return Login(self)

    @cached_property
    def search_helper(self):
        from generic.helpers.search import Search

        return Search(self)

    @cached_property
    def mailhog_helper(self):
        from generic.helpers.mailhog import MailHog

        return MailHog(self)

    @cached_property
    def assertions_helper(self):
        from generic.assertions import AssertionsHelper

        return AssertionsHelper(self)
