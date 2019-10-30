from unittest import TestCase
from mock import Mock, patch
from python_examples.code import use_dependency_internally, use_injected_dependency, ExternalDependency


class CodeTest(TestCase):

    @patch("python_examples.code.ExternalDependency")
    def test_use_dependency_internally(self, patched_dependency_constructor):
        patched_dependency_constructor.return_value.get_number.return_value = 10

        result = use_dependency_internally(2)

        self.assertEqual(result, 20)

    def test_use_injected_dependency(self):
        mocked_dependency = Mock(spec=ExternalDependency)
        mocked_dependency.get_number.return_value = 10

        result = use_injected_dependency(mocked_dependency, 2)

        self.assertEqual(result, 20)
