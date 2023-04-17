from utils import sort_data, filter_data, format_data


def test_sort_data(test_data):
#    for v in test_data:
#        print(v['date'])
    sorted_data = sort_data(test_data)
    assert [x['date'] for x in sorted_data] == ['2019-08-26T10:50:58.294041', '2019-07-03T18:35:29.512364']

def test_filter_data(test_data):
    dated = filter_data(test_data)
    assert [x['state'] for x in dated] == ['EXECUTED', 'EXECUTED']

def test_format_data(test_data):
    formated = format_data(test_data)
    assert  [x[1:11] for x in formated] == ['26.08.2019', '03.07.2019']
    assert [x[32:39] for x in formated] == ['Maestro', 'MasterC']
