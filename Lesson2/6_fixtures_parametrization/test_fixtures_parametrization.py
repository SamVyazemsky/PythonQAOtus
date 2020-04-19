import pytest


# @pytest.mark.parametrize("test_input", [(1, 1), (2, 2), (3, 3)])
# def test_one_2(test_input):
#     assert test_input[0] - test_input[1] == 0
#     #print(test_input)

#
# @pytest.mark.parametrize("test_input", [1, 2, 3])
# class TestClassParametrized:
#
#     # Все функци должны использовать аргумент
#     def test_one(self, test_input):
#         pass
#
#     def test_two(self, test_input):
#         pass


# Parametrize with fixture

# def test_one_1(fixture_with_params):
#     print(fixture_with_params)

# Combine parametrization

# @pytest.mark.parametrize("test_input", [1, 2, 3])
def test_one_2(fixture_two, fixture_one):
    print(fixture_one, fixture_two)
