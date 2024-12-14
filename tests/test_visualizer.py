import unittest
from visualizer import get_dependencies

class TestDependencyVisualizer(unittest.TestCase):
    def test_get_dependencies(self):
        # Пример теста для пакета с известными зависимостями
        dependencies = get_dependencies('some_package')
        # Замените 'some_package' на реальный пакет и проверьте его зависимости
        self.assertIn('some_dependency', dependencies)

if __name__ == '__main__':
    unittest.main()
