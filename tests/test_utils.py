from utils import sort_data


def test_sort_data(test_data):
#    for v in test_data:
#        print(v['date'])
    sorted_data = sort_data(test_data)
    assert [x['date'] for x in sorted_data] == ['2019-08-26T10:50:58.294041', '2019-07-03T18:35:29.512364']





