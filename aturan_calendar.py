"""
aturan_calendar
~~~~~~~~~~~~~~~
Converts Western/Gregorian dates into Aturan dates. From the wonderful world of Patrick Rothfuss in The Kingkiller Chronicles.

:copyright: (c) 2016 Christian Erick Sauer.
:license: MIT, see LICENSE for more details.

All rights regarding The Kingkiller Chronicles are reserved by Patrick Rothfuss.

--

Things we know for sure:
    * 11 Days in a Span.
    * 4 Spans in a Month.
    * 44 Days in a Month.
    * 8 Months in a Year.
    * 7 Holy Days after the eight Month and before the first Month of the new Year.
    * The last Holy Day, and therefore the last Day of the Year, is Winter's Solstice.
    * The names of the Days of the Span.
    * The names of the Months of the Year.
    * The Name of the Wind's first sentence tells us it was Felling Night.
    * The Name of the Wind was published on 27-Mar-2007

Things we don't know but can make reasonable guesses:
    * The Month in which present day is taking place. But we know neighboring farms are harvesting, so that would suggest `Reaping`.

Things we don't know AT ALL.
    * The Span of the Month in which present day is taking place. Assumed it was the first Span of `Reaping`
    * The Year in which present day is taking place. We have NO SENSE of actual years, just relative mentions. Since this would be a totally wild guess, just made it the same as The Name of the Wind's published Year.

Given everything above, that would make 27-Mar-2007 line up with Felling Night in the first Span of Reaping 2007 which is the 228th day of the Aturan Year.  Walking backwards, the first Day of Aturan Year 2007 is 11-Aug-2006. We can use this `point of origin` to calculate any other date.

As mentioned above, some of this is just guesswork. If `Day 3` gives better insight, this will be updated.

"""

# Book published 27-Mar-2007, 85th day
# Felling Night, Reaping, 228th day
import datetime
import arrow

ATURAN_DAY_NAMES = {
    1: 'Luten',
    2: 'Shuden',
    3: 'Theden',
    4: 'Feochen',
    5: 'Orden',
    6: 'Hepten',
    7: 'Chaen',

    8: 'Felling',
    9: 'Reaving',
    10: 'Cendling',
    11: 'Mourning',  # eleventh day
}

ATURAN_MONTH_OF_YEAR_NAMES = {
    1: 'Thaw',
    2: 'Equis',
    3: 'Caitelyn',
    4: 'Solace',
    5: 'Lannis',
    6: 'Reaping',
    7: 'Fallow',
    8: 'Dearth',
    9: '',
}

ATURAN_DAYS_IN_YEAR = 359
ATURAN_DAYS_IN_MONTH = 44
ATURAN_DAYS_IN_SPAN = 11
ATURAN_FIRST_HOLY_DAY = 353
ATURAN_WINTERS_SOLSTICE_DAY = 359

_ORIGIN = arrow.get(2006, 8, 11)


def _get_aturan_year(_ORIGIN, days):
    return (_ORIGIN.year + 1) + ((days - 1) // ATURAN_DAYS_IN_YEAR)


def _normalize_date(dateish):
    if isinstance(dateish, datetime.date):
        return arrow.Arrow.fromdate(dateish)

    if isinstance(dateish, arrow.Arrow):
        return dateish.floor('day')

    raise TypeError


def _normalize_doy(days):
    return days - (((days - 1) // ATURAN_DAYS_IN_YEAR) * ATURAN_DAYS_IN_YEAR)


def _create_entry(ndoy):
    ndoy = _normalize_doy(ndoy)
    return {
        'day_of_year': ndoy,
        'month_of_year': month_of_year_name(ndoy),
        'span_of_month': span_of_month_num(ndoy),
        'day_of_span': day_of_span_name(ndoy),
    }


def month_of_year(doy):
    """
    Calculates the Aturan numerical month of the year for a given day of the year. You probably want to use
        `month_of_year_name` instead.

    :param doy: Integer, day of year to look up. If greater than ATURAN_DAYS_IN_YEAR, value is "normalized"
        i.e. 362 becomes 3.
    :return: :int: the numerical value of the month (1-9)
    """
    return ((_normalize_doy(doy) - 1) // ATURAN_DAYS_IN_MONTH) + 1


def day_of_span(doy):
    """
    Calculates the Aturan day of the week/span for a given day of the year. You probably want to use `day_of_span_name`
        instead.

    :param doy: Integer, day of the year to look up. If greater than ATURAN_DAYS_IN_YEAR, value is "normalized"
        i.e. 362 becomes 3
    :return: :int: The numerical value of the day of the week/span (1-11)
    """
    dos = _normalize_doy(doy) % ATURAN_DAYS_IN_SPAN
    return ATURAN_DAYS_IN_SPAN if dos == 0 else dos


def day_of_month(doy):
    """
    Calculates the Aturan day of the month for a given day of the year.

    :param doy: Integer, day of the year to look up. If greater than ATURAN_DAYS_IN_YEAR, value is "normalized"
        i.e. 362 becomes 3
    :return: :int: The numerical value of the day of the month (1-44)
    """
    ndoy = _normalize_doy(doy)
    return ndoy - (((ndoy - 1) // ATURAN_DAYS_IN_MONTH) * ATURAN_DAYS_IN_MONTH)


def span_of_month(doy):
    """
    Calculates the Aturan span of the month for a given day of the year. You probably want to use `span_of_month_num`
        instead.

    :param doy: Integer, day of the year to look up. If greater than ATURAN_DAYS_IN_YEAR, value is "normalized"
        i.e. 362 becomes 3
    :return: :int: The numerical value of the span of the month (1-4)
    """
    dom = day_of_month(doy)
    return ((dom - 1) // ATURAN_DAYS_IN_SPAN) + 1


def day_of_span_name(doy):
    """
    Calculates the Aturan day of the week/span for a given day of the year.

    :param doy: Integer, day of the year to look up. If greater than ATURAN_DAYS_IN_YEAR, value is "normalized"
        i.e. 362 becomes 3
    :return: :string: The name of the day of the week/span (i.e. 'Luten', 'Shuden', 'Theden', etc)
    """
    ndoy = _normalize_doy(doy)
    n = day_of_span(doy)
    if ndoy >= ATURAN_FIRST_HOLY_DAY:
        day = "High Mourning Day #{}".format(ndoy - (ATURAN_FIRST_HOLY_DAY - 1))
        if ndoy == ATURAN_WINTERS_SOLSTICE_DAY:
            day += ' (Winter\'s Solstice)'
        return day
    return ATURAN_DAY_NAMES[n]


def month_of_year_name(doy):
    """
    Calculates the Aturan month of the year for a given day of the year.
    :param doy: Integer, day of the year to look up. If greater than ATURAN_DAYS_IN_YEAR, value is "normalized"
        i.e. 362 becomes 3
    :return: :string: or None, The name of the month of the year (i.e. 'Thaw', 'Equis', , 'Caitelyn', etc).
        The High Mourning Holy Days are not part of a month and thus will be None.
    """
    ndoy = _normalize_doy(doy)
    n = month_of_year(doy)
    if ndoy >= ATURAN_FIRST_HOLY_DAY:
        return None
    return ATURAN_MONTH_OF_YEAR_NAMES[n]


def span_of_month_num(doy):
    """
    Calulates the Aturan span of the month for a given day of the year.

    :param doy: Integer, day of the year to look up. If greater than ATURAN_DAYS_IN_YEAR, value is "normalized"
        i.e. 362 becomes 3
    :return: :int: or None, The numerical value of the span of the month (1-4). The High Mourning Holy Days are not
        part of a month and thus will be None.
    """
    ndoy = _normalize_doy(doy)
    n = span_of_month(ndoy)
    if ndoy >= ATURAN_FIRST_HOLY_DAY:
        return None
    return n


def full_calendar():
    """
    Creates a 359 day representation of the Aturan calendar. There is no Year because the Aturan Calendar is consistent.
    :return: :dict: of :dict:, the outer key is the day of the year. Inner keys are 'day_of_year', 'month_of_year',
        'span_of_month', and 'day_of_span'.
    """
    rtn = []
    for i in range(1, 360):
        rtn.append(_create_entry(i))
        
    return rtn


def aturan_calendar_for_western_year(year):
    """
    Creates a 365 day list of Aturan days for the given Western/Gregorian year.  Aturan years are only 359 days long,
        so at some point the items will change year.

    :param year: Integer, the Western/Gregorian year for which you want the Aturan equivalent
    :return: :list: of :dict:, inner keys are 'day_of_year', 'month_of_year', 'span_of_month', 'day_of_span', and
        'year'.
    """
    year_begin = arrow.get(year, 1, 1)
    year_end = year_begin.replace(years=+1, days=-1)
    return [western_to_aturan(day) for day
            in arrow.Arrow.range('day', year_begin, year_end)]


def western_to_aturan(dateish):
    """
    Returns the Aturan date information for a given Western/Gregorian date.

    :param dateish: datetime.Date, datetime.DateTime, or Arrow. The date for which you want the Aturan equivalent.
    :return: :dict:, inner keys are 'day_of_year', 'month_of_year', 'span_of_month', 'day_of_span', 'year'.
    """
    days = (_normalize_date(dateish) - _ORIGIN).days
    entry = _create_entry(days)
    entry['year'] = _get_aturan_year(_ORIGIN, days)
    return entry
