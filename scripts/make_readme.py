
def write_doc(module, filename):
    with open(filename, 'w') as f:
        f.write(""".. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - |coveralls|
    * - package
      - |travis|

.. |travis| image:: https://travis-ci.org/c17r/aturan-calendar.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/c17r/aturan-calendar

.. |coveralls| image:: https://coveralls.io/repos/github/c17r/aturan-calendar/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://coveralls.io/github/c17r/aturan-calendar

.. end-badges
""")
        f.write(module.__doc__)
