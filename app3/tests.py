from django.test import TestCase

# Create your tests here.
from app3.management.commands.my_manage import Command


class TestMyManage(TestCase):
    def setUp(self):
        pass

    def test_run(self) -> None:
        command = Command()
        import pdb
        pdb.set_trace()
        kwargs = {'a':1, 'b':2}
        res = command.handle(self, **kwargs)  # type: ignore
        self.assertEqual(res,0)

