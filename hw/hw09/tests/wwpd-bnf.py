test = {
  'name': 'ebnf-pycombinator',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'ceb66eb925d7e8e2992dc909b43fe073',
          'choices': [
            'add(1, 2)',
            'sub(3, 4)',
            'add(sub(1, 2))',
            'add()'
          ],
          'hidden': False,
          'locked': True,
          'question': 'Which of the following expressions would NOT be parsable according to this BNF?'
        },
        {
          'answer': '79f9518fbc9a1791f267d64e63c6e293',
          'choices': [
            'add(a, b)',
            'add("a", "b")',
            'add(10, 20)',
            'All of these'
          ],
          'hidden': False,
          'locked': True,
          'question': 'Which of these expressions WOULD be parsable according to this BNF?'
        },
        {
          'answer': '2ee0d14b436fb92b3d0bf7c7bf76cb08',
          'choices': [
            'pycomb_call: func "(" arg ("," arg)* ")"',
            'arg: pycomb_call | NUMBER',
            'func: FUNCNAME',
            'FUNCNAME: "add" | "mul" | "sub"'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What line of the BNF should we modify to add support for a "div" operation?'
        },
        {
          'answer': '840de28c224a2b2126746de68288bdbb',
          'choices': [
            'pycomb_call',
            'arg',
            'func',
            'FUNCNAME',
            'NUMBER',
            'both FUNCNAME and NUMBER',
            'All of these'
          ],
          'hidden': False,
          'locked': True,
          'question': 'Which of the following are considered a terminal?'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
