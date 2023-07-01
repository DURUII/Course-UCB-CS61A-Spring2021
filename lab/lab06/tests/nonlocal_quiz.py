test = {
  'name': 'nonlocal_quiz',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '55fd3e5f4f226790ab44943e3e633474',
          'choices': [
            '5',
            '2',
            '3',
            'This code will error'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          What is the value returned by the function call ba(3)?
          >>> def ba(by):
          ...     def yo(da):
          ...         by += 2
          ...         return by
          ...     return yo(2)
          ...
          >>> ba(3)
          """
        },
        {
          'answer': '73dc0de5202f020182ea500448cc846a',
          'choices': [
            '5',
            '2',
            '3',
            'This code will error'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          What is the value returned by the function call ba(3)?
          >>> def ba(by):
          ...     def yo(da):
          ...         nonlocal by
          ...         by += 2
          ...         return by
          ...     return yo(3)
          ...
          >>> ba(3)
          """
        },
        {
          'answer': 'a06dbad8160b15bdcd6c55fe942aa898',
          'choices': [
            '[1, 2, 3, 5]',
            '[1, 2, 3]',
            'None',
            'This code will error'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          What is the value returned by the function call ba([1, 2, 3])?
          >>> def ba(by):
          ...     def yo(da):
          ...         by.append(da)
          ...         return by
          ...     return yo(5)
          ...
          >>> ba([1, 2, 3])
          """
        },
        {
          'answer': 'f6b228b9600512664524ace9bb20487f',
          'choices': [
            '5',
            '10',
            '15',
            'This code will error'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          What is the value returned by the function call ba(5)?
          >>> def ba(by):
          ...     def yo(da):
          ...         yoda = by + da
          ...         return yoda
          ...     return yo(5)
          ...
          >>> ba(5)
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
