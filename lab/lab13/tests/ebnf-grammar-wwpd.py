test = {
  'name': 'ebnf-grammar',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '4a5a83c12cc8221930562b0949bf46d9',
          'choices': [
            'The subtraction operator requires at least one argument.',
            'The division operator requires at least two arguments.',
            'Each of the operands can itself be a Calculator expression.',
            'Variables can be defined and used as operands.'
          ],
          'hidden': False,
          'locked': True,
          'question': 'Which aspects of the Calculator language are supported by this grammar?'
        },
        {
          'answer': '19c7b940eaa810893d4bb9c0a8983ddd',
          'choices': [
            '(+ 1 2)',
            '(+)',
            '(+ 1 2 3)',
            '(+ 1)',
            '(1 + 2)',
            '(+ 1 (+ 2 3))'
          ],
          'hidden': False,
          'locked': True,
          'question': 'Which of the following expressions would NOT be parsable according to that BNF?'
        },
        {
          'answer': '583f56b71fee43ae58ff6b4151cf7613',
          'choices': [
            'start: calc_expr',
            '?calc_expr: NUMBER | calc_op',
            'calc_op: "(" OPERATOR calc_expr* ")"',
            'OPERATOR: "+" | "-" | "*" | "/"'
          ],
          'hidden': False,
          'locked': True,
          'question': 'Which line of the BNF should we modify to add support for calculations using a modulus operator, like (% 15 5)?'
        },
        {
          'answer': 'db083c522290b645c2746d2b46913df0',
          'choices': [
            'Yes, if we feed this grammar into a program that understands EBNF grammars, it will be able to parse Calculator expressions and output the result.',
            'Yes, but only if we feed this grammar into a program that was written in the Calculator language itself.',
            'No, this grammar gives enough information for parsing a Calculator expression, but it does not provide enough information to evaluate it.',
            'No, this grammar does not provide enough information for the parsing or evaluation step, it is useful mostly as documentation.'
          ],
          'hidden': False,
          'locked': True,
          'question': 'Does the EBNF grammar provide enough information to create a working interpreter for this version of the Calculator language?'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
