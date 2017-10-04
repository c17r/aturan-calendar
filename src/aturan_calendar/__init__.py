"""
aturan_calendar
~~~~~~~~~~~~~~~
Converts Western/Gregorian dates into Aturan dates. From the wonderful world of Patrick Rothfuss in The Kingkiller Chronicles.

:copyright: 2016-2017 Christian Erick Sauer.
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

"""  # noqa

from .core import *  # noqa
from .core import _ORIGIN  # noqa
