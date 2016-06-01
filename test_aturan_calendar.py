import pytest

import aturan_calendar as cal
import arrow
import datetime


class TestConstants:
    def test_days_in_year(self):
        assert cal.ATURAN_DAYS_IN_YEAR == 359

    def test_days_in_month(self):
        assert cal.ATURAN_DAYS_IN_MONTH == 44

    def test_days_in_span(self):
        assert cal.ATURAN_DAYS_IN_SPAN == 11

    def test_first_holy_day(self):
        assert cal.ATURAN_FIRST_HOLY_DAY == 353

    def test_winters_solstice(self):
        assert cal.ATURAN_WINTERS_SOLSTICE_DAY == 359

    def test_origin(self):
        assert cal._ORIGIN == arrow.get(2006, 8, 11)

    def test_month_names(self):
        assert cal.ATURAN_MONTH_OF_YEAR_NAMES[1] == 'Thaw'
        assert cal.ATURAN_MONTH_OF_YEAR_NAMES[2] == 'Equis'
        assert cal.ATURAN_MONTH_OF_YEAR_NAMES[3] == 'Caitelyn'
        assert cal.ATURAN_MONTH_OF_YEAR_NAMES[4] == 'Solace'
        assert cal.ATURAN_MONTH_OF_YEAR_NAMES[5] == 'Lannis'
        assert cal.ATURAN_MONTH_OF_YEAR_NAMES[6] == 'Reaping'
        assert cal.ATURAN_MONTH_OF_YEAR_NAMES[7] == 'Fallow'
        assert cal.ATURAN_MONTH_OF_YEAR_NAMES[8] == 'Dearth'
        assert cal.ATURAN_MONTH_OF_YEAR_NAMES[9] == ''

    def test_day_names(self):
        assert cal.ATURAN_DAY_NAMES[1] == 'Luten'
        assert cal.ATURAN_DAY_NAMES[2] == 'Shuden'
        assert cal.ATURAN_DAY_NAMES[3] == 'Theden'
        assert cal.ATURAN_DAY_NAMES[4] == 'Feochen'
        assert cal.ATURAN_DAY_NAMES[5] == 'Orden'
        assert cal.ATURAN_DAY_NAMES[6] == 'Hepten'
        assert cal.ATURAN_DAY_NAMES[7] == 'Chaen'
        assert cal.ATURAN_DAY_NAMES[8] == 'Felling'
        assert cal.ATURAN_DAY_NAMES[9] == 'Reaving'
        assert cal.ATURAN_DAY_NAMES[10] == 'Cendling'
        assert cal.ATURAN_DAY_NAMES[11] == 'Mourning'


def test_month_of_year():
    data = [
        {
            'days': range(1, 45),
            'month': 1
        },
        {
            'days': range(45, 89),
            'month': 2
        },
        {
            'days': range(89, 133),
            'month': 3
        },
        {
            'days': range(133, 177),
            'month': 4
        },
        {
            'days': range(177, 221),
            'month': 5
        },
        {
            'days': range(221, 265),
            'month': 6
        },
        {
            'days': range(265, 309),
            'month': 7
        },
        {
            'days': range(309, 353),
            'month': 8
        },
        {
            'days': range(353, 360),
            'month': 9
        },
    ]

    for datum in data:
        for day in datum['days']:
            result = cal.month_of_year(day)
            assert result == datum['month'], "{} should be in month {}, not {}".format(day, datum['month'], result)

            day_plus_year = day + cal.ATURAN_DAYS_IN_YEAR
            result = cal.month_of_year(day_plus_year)
            assert result == datum['month'], "{} should be in month {}, not {}".format(day_plus_year, datum['month'], result)


def test_day_of_span():
    data = [
        range(1, 12),
        range(12, 23),
        range(23, 34),
        range(34, 45),
        range(45, 56),
        range(56, 67),
        range(67, 78),
        range(78, 89),
        range(89, 100),
        range(100, 111),
        range(111, 122),
        range(122, 133),
        range(133, 144),
        range(144, 155),
        range(155, 166),
        range(166, 177),
        range(177, 188),
        range(188, 199),
        range(199, 210),
        range(210, 221),
        range(221, 232),
        range(232, 243),
        range(243, 254),
        range(254, 265),
        range(265, 276),
        range(276, 287),
        range(287, 298),
        range(298, 309),
        range(309, 320),
        range(320, 331),
        range(331, 342),
        range(342, 353),
        range(353, 360),
    ]

    for datum in data:
        expected = 0
        for day in datum:
            expected += 1

            result = cal.day_of_span(day)
            assert result == expected, "{} should be {}, not {}".format(day, expected, result)

            day_plus_year = day + cal.ATURAN_DAYS_IN_YEAR
            result = cal.day_of_span(day_plus_year)
            assert result == expected, "{} should be {}, not {}".format(day_plus_year, expected, result)


def test_day_of_month():
    data = [
        range(1, 45),
        range(45, 89),
        range(89, 133),
        range(133, 177),
        range(177, 221),
        range(221, 265),
        range(265, 309),
        range(309, 353),
        range(353, 360),
    ]

    for datum in data:
        expected = 0
        for day in datum:
            expected += 1

            result = cal.day_of_month(day)
            assert result == expected, "{} should be {}, not {}".format(day, expected, result)

            day_plus_year = day + cal.ATURAN_DAYS_IN_YEAR
            result = cal.day_of_month(day_plus_year)
            assert result == expected, "{} should be {}, not {}".format(day_plus_year, expected, result)


def test_span_of_month():
    data = [
        {
            'days': range(1, 12),
            'span': 1,
        },
        {
            'days': range(12, 23),
            'span': 2,
        },
        {
            'days': range(23, 34),
            'span': 3,
        },
        {
            'days': range(34, 45),
            'span': 4,
        },
        {
            'days': range(45, 56),
            'span': 1,
        },
        {
            'days': range(56, 67),
            'span': 2,
        },
        {
            'days': range(67, 78),
            'span': 3,
        },
        {
            'days': range(78, 89),
            'span': 4,
        },
        {
            'days': range(89, 100),
            'span': 1,
        },
        {
            'days': range(100, 111),
            'span': 2,
        },
        {
            'days': range(111, 122),
            'span': 3,
        },
        {
            'days': range(122, 133),
            'span': 4,
        },
        {
            'days': range(133, 144),
            'span': 1,
        },
        {
            'days': range(144, 155),
            'span': 2,
        },
        {
            'days': range(155, 166),
            'span': 3,
        },
        {
            'days': range(166, 177),
            'span': 4,
        },
        {
            'days': range(177, 188),
            'span': 1,
        },
        {
            'days': range(188, 199),
            'span': 2,
        },
        {
            'days': range(199, 210),
            'span': 3,
        },
        {
            'days': range(210, 221),
            'span': 4,
        },
        {
            'days': range(221, 232),
            'span': 1,
        },
        {
            'days': range(232, 243),
            'span': 2,
        },
        {
            'days': range(243, 254),
            'span': 3,
        },
        {
            'days': range(254, 265),
            'span': 4,
        },
        {
            'days': range(265, 276),
            'span': 1,
        },
        {
            'days': range(276, 287),
            'span': 2,
        },
        {
            'days': range(287, 298),
            'span': 3,
        },
        {
            'days': range(298, 309),
            'span': 4,
        },
        {
            'days': range(309, 320),
            'span': 1,
        },
        {
            'days': range(320, 331),
            'span': 2,
        },
        {
            'days': range(331, 342),
            'span': 3,
        },
        {
            'days': range(342, 353),
            'span': 4,
        },
        {
            'days': range(353, 360),
            'span': 1,
        },
    ]

    for datum in data:
        for day in datum['days']:
            result = cal.span_of_month(day)
            assert result == datum['span'], "{} should be {}, not {}".format(day, datum['span'], result)

            day_plus_year = day + cal.ATURAN_DAYS_IN_YEAR
            result = cal.span_of_month(day_plus_year)
            assert result == datum['span'], "{} should be {}, not {}".format(day_plus_year, datum['span'], result)


def test_day_of_span_name():
    data = [
        range(1, 12),
        range(12, 23),
        range(23, 34),
        range(34, 45),
        range(45, 56),
        range(56, 67),
        range(67, 78),
        range(78, 89),
        range(89, 100),
        range(100, 111),
        range(111, 122),
        range(122, 133),
        range(133, 144),
        range(144, 155),
        range(155, 166),
        range(166, 177),
        range(177, 188),
        range(188, 199),
        range(199, 210),
        range(210, 221),
        range(221, 232),
        range(232, 243),
        range(243, 254),
        range(254, 265),
        range(265, 276),
        range(276, 287),
        range(287, 298),
        range(298, 309),
        range(309, 320),
        range(320, 331),
        range(331, 342),
        range(342, 353),
        range(353, 360),
    ]
    names_regular = [
        'Luten',
        'Shuden',
        'Theden',
        'Feochen',
        'Orden',
        'Hepten',
        'Chaen',
        'Felling',
        'Reaving',
        'Cendling',
        'Mourning',
    ]
    names_special = [
        'High Mourning Day #1',
        'High Mourning Day #2',
        'High Mourning Day #3',
        'High Mourning Day #4',
        'High Mourning Day #5',
        'High Mourning Day #6',
        'High Mourning Day #7 (Winter\'s Solstice)',
    ]

    for datum in data:
        expected_idx = -1
        for day in datum:
            expected_idx += 1
            expected = names_regular[expected_idx]
            if day >= cal.ATURAN_FIRST_HOLY_DAY:
                expected = names_special[expected_idx]

            result = cal.day_of_span_name(day)
            assert result == expected, "{} should be {}, not {}".format(day, expected, result)

            day_plus_year = day + cal.ATURAN_DAYS_IN_YEAR
            result = cal.day_of_span_name(day_plus_year)
            assert result == expected, "{} should be {}, not {}".format(day_plus_year, expected, result)


def test_month_of_year_name():
    data = [
        {
            'days': range(1, 45),
            'month': 'Thaw'
        },
        {
            'days': range(45, 89),
            'month': 'Equis'
        },
        {
            'days': range(89, 133),
            'month': 'Caitelyn'
        },
        {
            'days': range(133, 177),
            'month': 'Solace'
        },
        {
            'days': range(177, 221),
            'month': 'Lannis'
        },
        {
            'days': range(221, 265),
            'month': 'Reaping'
        },
        {
            'days': range(265, 309),
            'month': 'Fallow'
        },
        {
            'days': range(309, 353),
            'month': 'Dearth'
        },
        {
            'days': range(353, 360),
            'month': ''
        },
    ]

    for datum in data:
        for day in datum['days']:
            result = cal.month_of_year_name(day)
            assert result == datum['month'], "{} should be in month {}, not {}".format(day, datum['month'], result)

            day_plus_year = day + cal.ATURAN_DAYS_IN_YEAR
            result = cal.month_of_year_name(day_plus_year)
            assert result == datum['month'], "{} should be in month {}, not {}".format(day_plus_year, datum['month'],
                                                                                       result)


def test_span_of_month_num():
    data = [
        {
            'days': range(1, 12),
            'span': 1,
        },
        {
            'days': range(12, 23),
            'span': 2,
        },
        {
            'days': range(23, 34),
            'span': 3,
        },
        {
            'days': range(34, 45),
            'span': 4,
        },
        {
            'days': range(45, 56),
            'span': 1,
        },
        {
            'days': range(56, 67),
            'span': 2,
        },
        {
            'days': range(67, 78),
            'span': 3,
        },
        {
            'days': range(78, 89),
            'span': 4,
        },
        {
            'days': range(89, 100),
            'span': 1,
        },
        {
            'days': range(100, 111),
            'span': 2,
        },
        {
            'days': range(111, 122),
            'span': 3,
        },
        {
            'days': range(122, 133),
            'span': 4,
        },
        {
            'days': range(133, 144),
            'span': 1,
        },
        {
            'days': range(144, 155),
            'span': 2,
        },
        {
            'days': range(155, 166),
            'span': 3,
        },
        {
            'days': range(166, 177),
            'span': 4,
        },
        {
            'days': range(177, 188),
            'span': 1,
        },
        {
            'days': range(188, 199),
            'span': 2,
        },
        {
            'days': range(199, 210),
            'span': 3,
        },
        {
            'days': range(210, 221),
            'span': 4,
        },
        {
            'days': range(221, 232),
            'span': 1,
        },
        {
            'days': range(232, 243),
            'span': 2,
        },
        {
            'days': range(243, 254),
            'span': 3,
        },
        {
            'days': range(254, 265),
            'span': 4,
        },
        {
            'days': range(265, 276),
            'span': 1,
        },
        {
            'days': range(276, 287),
            'span': 2,
        },
        {
            'days': range(287, 298),
            'span': 3,
        },
        {
            'days': range(298, 309),
            'span': 4,
        },
        {
            'days': range(309, 320),
            'span': 1,
        },
        {
            'days': range(320, 331),
            'span': 2,
        },
        {
            'days': range(331, 342),
            'span': 3,
        },
        {
            'days': range(342, 353),
            'span': 4,
        },
        {
            'days': range(353, 360),
            'span': None,
        },
    ]

    for datum in data:
        for day in datum['days']:
            result = cal.span_of_month_num(day)
            assert result == datum['span'], "{} should be {}, not {}".format(day, datum['span'], result)

            day_plus_year = day + cal.ATURAN_DAYS_IN_YEAR
            result = cal.span_of_month_num(day_plus_year)
            assert result == datum['span'], "{} should be {}, not {}".format(day_plus_year, datum['span'], result)


class TestWesternToAturan:

    PUBLISHED = {
        'day_of_year': 228,
        'month_of_year': 'Reaping',
        'span_of_month': 1,
        'day_of_span': 'Felling',
        'year': 2007
    }
    BIRTHDAY = {
        'day_of_year': 303,
        'month_of_year': 'Fallow',
        'span_of_month': 4,
        'day_of_span': 'Hepten',
        'year': 2016
    }

    def test_with_date(self):
        result = cal.western_to_aturan(datetime.date(2007, 3, 27))
        assert result == self.PUBLISHED

        result = cal.western_to_aturan(datetime.date(2016, 4, 14))
        assert result == self.BIRTHDAY

    def test_with_datetime(self):
        result = cal.western_to_aturan(datetime.datetime(2007, 3, 27, 0, 0, 0, 0))
        assert result == self.PUBLISHED

        result = cal.western_to_aturan(datetime.datetime(2016, 4, 14, 0, 0, 0, 0))
        assert result == self.BIRTHDAY

    def test_with_arrow(self):
        result = cal.western_to_aturan(arrow.get(2007, 3, 27))
        assert result == self.PUBLISHED

        result = cal.western_to_aturan(arrow.get(2016, 4, 14))
        assert result == self.BIRTHDAY

    def test_with_bad_type(self):
        with pytest.raises(TypeError):
            result = cal.western_to_aturan(1)


def test_full_calendar():
    expected = [
        {
            'day_of_year': 1,
            'month_of_year': 'Thaw',
            'span_of_month': 1,
            'day_of_span': 'Luten',
        },
        {
            'day_of_year': 160,
            'month_of_year': 'Solace',
            'span_of_month': 3,
            'day_of_span': 'Hepten',
        },
        {
            'day_of_year': 352,
            'month_of_year': 'Dearth',
            'span_of_month': 4,
            'day_of_span': 'Mourning',
        },
        {
            'day_of_year': 359,
            'month_of_year': '',
            'span_of_month': None,
            'day_of_span': 'High Mourning Day #7 (Winter\'s Solstice)',
        }
    ]

    result = cal.full_calendar()

    assert len(result) == cal.ATURAN_DAYS_IN_YEAR
    assert result[0] == expected[0]
    assert result[159] == expected[1]
    assert result[351] == expected[2]
    assert result[-1] == expected[-1]
