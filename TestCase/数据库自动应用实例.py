import pytest


class DB:
    def __init__(self):
        self.intransaction = []

    def begin(self, name):
        self.intransaction.append(name)

    def rollback(self):
        # pop删除最后一个元素并返回改列表
        self.intransaction.pop()


@pytest.fixture(scope="module")
def db():
    return DB()


class TestClass:
    @pytest.fixture(autouse=True)
    def transact(self, request, db):
        db.begin(request.name)
        yield
        db.rollback()

    def test_method1(self, db):
        assert db.intransaction == ["test_method1"]

    def test_method2(self, db):
        assert db.intransaction == ["test_method2"]
