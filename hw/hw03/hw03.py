HW_SOURCE_FILE = __file__


def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    if x < 10:
        return 1 if x == 8 else 0

    return num_eights(x // 10) + num_eights(x % 10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """

    def start_from(index, value, direction):
        """
        Keep status of value and direction at the current index,
        Return the value of Nth sequence STARTING FROM a given index, along with its value and direction
        """
        # take parameter N from the parent environment
        if index == n:
            print("DEBUG:", index, value, direction)
            return value

        # n.b. do not miss the `return` in the statement,
        # otherwise this will return None in Python
        return start_from(index + 1,
                          value + direction,
                          direction * -1  # the direction of [index+1]
                          if num_eights(index + 1) > 0 or (index + 1) % 8 == 0
                          else direction)

    return start_from(1, 1, 1)


def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """

    # guard
    if n < 10:
        return 0

    # base case: 2-digit number
    # e.g. 58 -> number(6, 7) -> 8 - 5 - 1
    # e.g. 11 -> 0
    if 10 <= n <= 99:
        # do not miss the `No Missing` case
        return max(n % 10 - n // 10 - 1, 0)

    # e.g. f(16789) -> f(1678) + f(89)
    return missing_digits(n // 10) + missing_digits(n % 100)


def get_next_coin(coin):
    """Return the next coin. 
    >>> get_next_coin(1)
    5
    >>> get_next_coin(5)
    10
    >>> get_next_coin(10)
    25
    >>> get_next_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])                                          
    True
    """

    # e.g. of a bad thought
    # change(1) -> {1} = 1
    # change(2) -> change(1) u {1} = change(1) = 1
    # change(3) -> change(2) u {1} = change(1) = 1
    # change(4) -> change(3) u {1} = change(1) = 1
    # change(5) -> change(4) u {1} + change(0) u {5} = 2
    # change(6) -> change(5) u {1} + change(1) u {5} = 3 ({1,1,1,1,1,1}, {5, 1}, {1, 5})
    #
    # e.g. of a better thought (specify the ORDER of different coins)
    # change(6) -> change(6)from(1) + change(6)from(1, 5) = 2

    def change_from(money, note):
        """
        Return counts of ways to change MONEY using [note ~ max_note]
        which is derived from the thought on count_partitions (slightly different in m)
        """
        # guard
        if money < 0 or note is None:
            return 0

        # base case
        if money == 0:
            return 1

        # 不重不漏！！！
        return change_from(money - note, note) + change_from(money, get_next_coin(note))

    return change_from(change, 1)


from operator import sub, mul


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """

    # ref source: https://stackoverflow.com/a/8703135
    return (lambda myself: lambda args: myself(myself, args))(
        lambda f, n: 1 if n == 1 else mul(n, f(f, sub(n, 1)))
    )


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"

    if n == 1:
        print_move(start, end)
        return

    spare = 6 - start - end
    move_stack(n - 1, start, spare)
    move_stack(1, start, end)
    move_stack(n - 1, spare, end)
