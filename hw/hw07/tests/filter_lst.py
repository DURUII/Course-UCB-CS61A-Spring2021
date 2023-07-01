test = {
  'name': 'filter-lst',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (filter-lst even? '(1 2 3 4))
          f46f3fc2fe06f7581f4a8c09d2595608
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter-lst odd? '(1 3 5))
          550647f0ac22816b6186c318859689bf
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter-lst odd? '(2 4 6 1))
          c050f073ab2eb36093912b614f490656
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter-lst even? '(3))
          7b043779e02c43bdcd630251dbb3ebc9
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter-lst odd? nil)
          7b043779e02c43bdcd630251dbb3ebc9
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (filter-lst even? '(1 2 3 4)) ; checks you dont use builtin filter
          (2 4)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (define filter nil) 
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
