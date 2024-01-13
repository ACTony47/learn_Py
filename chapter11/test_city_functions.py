from city_functions import output
def test_city_country():
    ans = output('chongqing', 'china')
    assert ans == 'Chongqing, China'
