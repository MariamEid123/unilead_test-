"""Code-lab content for CSE014 — Structured Programming.

Each challenge is a plain dict (same spirit as ``curriculum/content_*.py``):
server-side source of truth, served to the UI through the lab API. Solutions,
test inputs and MCQ answers stay server-side — the manifest view never ships
them; grading runs the *student's* code against the public tests for real.

Challenge types:
  * complete_code      — fill in the blanks; graded by running the result.
  * debug              — fix a deliberately broken program.
  * output_prediction  — predict what a program prints (MCQ).
  * challenge          — write a full program, easy/medium/hard.
"""

from __future__ import annotations

COURSE_CODE = "CSE014"
COURSE_TITLE = "Structured Programming"
RUNTIME = "python"

LESSONS = [
    ("CS1", "Introduction & first programs"),
    ("CS2", "Variables & main memory"),
    ("CS3", "Input, operators & expressions"),
    ("CS4", "Operators, casting & Boolean logic"),
    ("CS5", "Selection statements"),
    ("CS6", "For loops & cumulative algorithms"),
    ("CS7", "While loops, nested loops & arrays"),
    ("CS8", "Strings & palindrome detection"),
    ("CS9", "Array operations"),
    ("CS10", "Functions & parameters"),
    ("CS11", "Recursion"),
]


def _cc(chid, lesson_code, topic, difficulty, title, prompt, starter, tests, hints):
    return {
        "id": chid,
        "lesson_code": lesson_code,
        "type": "complete_code",
        "topic": topic,
        "difficulty": difficulty,
        "title": title,
        "prompt": prompt,
        "starter_code": starter,
        "public_tests": tests,
        "hints": hints,
    }


def _dbg(chid, lesson_code, topic, difficulty, title, prompt, starter, tests, hints):
    return {
        "id": chid,
        "lesson_code": lesson_code,
        "type": "debug",
        "topic": topic,
        "difficulty": difficulty,
        "title": title,
        "prompt": prompt,
        "starter_code": starter,
        "public_tests": tests,
        "hints": hints,
    }


def _out(chid, lesson_code, topic, title, code_text, options, correct_index, explanation):
    return {
        "id": chid,
        "lesson_code": lesson_code,
        "type": "output_prediction",
        "topic": topic,
        "difficulty": "easy",
        "title": title,
        "prompt": "Read the program and predict exactly what it prints when you press Run.",
        "code_text": code_text,
        "options": options,
        "correct_index": correct_index,
        "explanation": explanation,
        "hints": {
            "general": "Trace the program line by line, keeping a little table of every variable and its value.",
            "specific": "Write out each assignment on paper before answering — the value of a variable is whatever was assigned most recently.",
            "solution": explanation,
        },
    }


def _chal(chid, lesson_code, topic, difficulty, title, prompt, starter, tests, hints):
    return {
        "id": chid,
        "lesson_code": lesson_code,
        "type": "challenge",
        "topic": topic,
        "difficulty": difficulty,
        "title": title,
        "prompt": prompt,
        "starter_code": starter,
        "public_tests": tests,
        "hints": hints,
    }


def _hint(general, specific, solution):
    return {"general": general, "specific": specific, "solution": solution}


CHALLENGES: list[dict] = [
    # ---------------------------------------------------------------- CS1
    _cc(
        "csc1-cc-print",
        "CS1", "input_output", "easy",
        "Complete the greeting program",
        "Fill in the blanks. The program should read a name and an age, then say hello "
        "and print how old the person will be next year.",
        'name = ____()\nage = int(____())\n'
        'print("Hello, " + name + "!")\n'
        'print("Next year you will be", age + ____)',
        [
            {"input": "Ahmed\n19\n", "expected": "Hello, Ahmed!\nNext year you will be 20"},
            {"input": "Sara\n20\n", "expected": "Hello, Sara!\nNext year you will be 21"},
        ],
        _hint(
            "The two blanks on the input lines are the same function: it reads a whole "
            "line of typing from the keyboard.",
            "For reading text use input(). Convert that text to a whole number with int(...) — "
            "the age blank adds 1 to this year's age.",
            "name = input() / age = int(input()) / print(\"Next year you will be\", age + 1)",
        ),
    ),
    _out(
        "csc1-out-stringplus",
        "CS1", "input_output",
        "Predict what happens — text + number",
        'print("2 + 3 is " + 5)',
        ["2 + 3 is 5", "2 + 3 is 55", 'TypeError: can only concatenate str (not "int") to str', "2 + 3 is  5"],
        2,
        "You cannot join a string and an int with +. Convert the number first: "
        'print("2 + 3 is " + str(5)) or use an f-string: print(f"2 + 3 is {5}").',
    ),
    _chal(
        "csc1-chal-hello",
        "CS1", "input_output", "easy",
        "Write the 'introduce yourself' program",
        "Read a name, then an age. Print exactly:\n\n    <name>, you are <age> years old.",
        'name = input()\nage = int(input())\nprint(name + ", you are " + str(age) + " years old.")',
        [
            {"input": "Sara\n20\n", "expected": "Sara, you are 20 years old."},
            {"input": "Omar\n18\n", "expected": "Omar, you are 18 years old."},
        ],
        _hint(
            "Think about the two pieces of information you must collect, and the order they arrive in.",
            "Print one line. The name is a string, the age came from int(...) — convert it back with str() "
            "before joining with +, or use an f-string.",
            'print(f"{name}, you are {age} years old.")',
        ),
    ),
    # ---------------------------------------------------------------- CS2
    _dbg(
        "csc2-dbg-swap",
        "CS2", "variables", "easy",
        "Fix the swap",
        "This program should read two numbers a and b and then print them in the "
        "opposite order (b, then a). Instead it prints something wrong. Debug it.",
        'a = int(input())\nb = int(input())\na = b\nb = a\nprint(a, b)',
        [
            {"input": "3\n5\n", "expected": "5 3"},
            {"input": "7\n1\n", "expected": "1 7"},
        ],
        _hint(
            "After the two assignments, what are the values of a and b? Write them down before you run it.",
            "Assigning a = b destroys the original value of a before you can move it into b. "
            "Save it somewhere first.",
            "temp = a\na = b\nb = temp",
        ),
    ),
    _out(
        "csc2-out-update",
        "CS2", "variables",
        "Predict the final value",
        "x = 5\nx = x + 3\nx += 2\nprint(x)",
        ["10", "8", "35", "5"],
        0,
        "The variable is updated twice: 5 + 3 = 8, then 8 + 2 = 10. The last line printed is "
        "whatever x holds at that moment.",
    ),
    _chal(
        "csc2-chal-rectangle",
        "CS2", "operators", "easy",
        "Rectangle area",
        "Read two integers — width and height — and print their product (the area).",
        "w = int(input())\nh = int(input())\nprint(w * h)",
        [
            {"input": "4\n7\n", "expected": "28"},
            {"input": "9\n3\n", "expected": "27"},
        ],
        _hint(
            "Area = width × height. What operator multiplies two numbers?",
            "w and h are already ints. One multiplication will do.",
            "print(w * h)",
        ),
    ),
    # ---------------------------------------------------------------- CS3
    _cc(
        "csc3-cc-maths",
        "CS3", "input_output", "easy",
        "Complete the calculator",
        "The program reads two integers and prints their sum and product. Fill the blanks.",
        "n1 = int(input())\nn2 = int(____())\n"
        'print(n1, "+", n2, "=", n1 + n2)\n'
        'print(n1, "x", n2, "=", n1 ____ n2)',
        [
            {"input": "6\n7\n", "expected": "6 + 7 = 13\n6 x 7 = 42"},
            {"input": "10\n5\n", "expected": "10 + 5 = 15\n10 x 5 = 50"},
        ],
        _hint(
            "One blank reads the second number; the other blank is the multiplication operator.",
            "The reading blank is input; the operator blank is *",
            "n2 = int(input())\nprint(n1, \"x\", n2, \"=\", n1 * n2)",
        ),
    ),
    _dbg(
        "csc3-dbg-score",
        "CS3", "input_output", "easy",
        "Fix 'scored'",
        "Read a name and then an integer score, then print a sentence. When you run it "
        "right now it crashes. Debug it.",
        'name = int(input("Name: "))\nnum = input("Score: ")\nprint(name + " scored " + num)',
        [
            {"input": "Ali\n34\n", "expected": "Ali scored 34"},            
        ],
        _hint(
            "Look at every call to input() and ask: is the value really a whole number?",
            "The name is being cast with int() but a name isn't a number; the score is kept as text "
            "even though we want to join them.",
            'name = input("Name: ")\nnum = int(input("Score: "))\nprint(name + " scored " + str(num))',
        ),
    ),
    # ---------------------------------------------------------------- CS4
    _out(
        "csc4-out-boolean",
        "CS4", "operators",
        "Predict the Boolean",
        "print(3 + 4 == 7 and not 2 > 5)",
        ["True", "False", "7", "3"],
        0,
        "3 + 4 == 7 is True; 2 > 5 is False so not False is True; True and True is True.",
    ),
    _chal(
        "csc4-chal-divisible",
        "CS4", "operators", "easy",
        "Is a divisible by b?",
        "Read two integers a and b (b is never 0). Print the word True if a is evenly "
        "divisible by b, otherwise print False.",
        "a = int(input())\nb = int(input())\nprint(a % b == 0)",
        [
            {"input": "10\n5\n", "expected": "True"},
            {"input": "10\n3\n", "expected": "False"},
            {"input": "0\n7\n", "expected": "True"},
        ],
        _hint(
            "There is an operator that gives the remainder of a division. A number is evenly "
            "divisible when that remainder is 0.",
            "Compare a % b against 0 — the result of that comparison is already True or False.",
            "print(a % b == 0)",
        ),
    ),
    _cc(
        "csc4-cc-quotient",
        "CS4", "operators", "medium",
        "Complete the division printer",
        "Print the whole-number quotient and the remainder of a divided by b.",
        "a = int(input())\nb = int(input())\nq = ____ // b\nr = a ____ b\nprint(q, r)",
        [
            {"input": "20\n6\n", "expected": "3 2"},
            {"input": "17\n5\n", "expected": "3 2"},
        ],
        _hint(
            "// gives the whole-number quotient; % gives the remainder.",
            "q should be a // b and r should be a % b.",
            "q = a // b\nr = a % b",
        ),
    ),
    # ---------------------------------------------------------------- CS5
    _cc(
        "csc5-cc-grade",
        "CS5", "conditionals", "medium",
        "Complete the grade ladder",
        "Fill the blanks so the program prints A for 90+, B for 80–89, otherwise C.",
        'score = int(input())\nif score ____ 90:\n    grade = "A"\nelif score >= 80:\n    grade = "B"\n____:\n    grade = "C"\nprint("Grade:", grade)',
        [
            {"input": "95\n", "expected": "Grade: A"},
            {"input": "84\n", "expected": "Grade: B"},
            {"input": "60\n", "expected": "Grade: C"},
        ],
        _hint(
            "The first condition decides the A band. What comparison marks '90 or more'?",
            ">= means 'greater than or equal to'. The fall-back branch keyword is else.",
            "if score >= 90: ... else: grade = \"C\"",
        ),
    ),
    _dbg(
        "csc5-dbg-sign",
        "CS5", "conditionals", "medium",
        "Fix the sign printer",
        "The program should print Positive for numbers above zero, Negative for numbers "
        "below zero, and Zero when it is exactly zero. The words are wrong. Debug it.",
        'n = int(input())\nif n > 0:\n    print("Negative")\nelse:\n    print("Positive or zero")',
        [
            {"input": "5\n", "expected": "Positive"},
            {"input": "-3\n", "expected": "Negative"},
            {"input": "0\n", "expected": "Zero"},
        ],
        _hint(
            "Check which branch each case actually lands in. There are three different "
            "outputs but only two branches.",
            "The n > 0 branch prints the wrong word, and a zero falls into the wrong branch entirely. "
            "Add an elif for negative numbers.",
            'if n > 0: print("Positive")\nelif n < 0: print("Negative")\nelse: print("Zero")',
        ),
    ),
    _out(
        "csc5-out-evenodd",
        "CS5", "conditionals",
        "Predict the printed word",
        'x = 7\nif x % 2 == 0:\n    print("even")\nelse:\n    print("odd")',
        ["odd", "even", "7", "odd even"],
        0,
        "7 % 2 is 1, not 0, so the condition is False and the else branch runs.",
    ),
    _chal(
        "csc5-chal-percent",
        "CS5", "conditionals", "medium",
        "Number text: positive / negative / zero",
        "Read one integer and print exactly Positive, Negative or Zero depending on it.",
        'n = int(input())\nif n > 0:\n    print("Positive")\nelif n < 0:\n    print("Negative")\nelse:\n    print("Zero")',
        [
            {"input": "12\n", "expected": "Positive"},
            {"input": "-4\n", "expected": "Negative"},
            {"input": "0\n", "expected": "Zero"},
        ],
        _hint(
            "Three cases need three branches. Start with the clearest rule (above zero is positive).",
            "Add an elif for below zero before the final else, which is left for exactly zero.",
            "See the starter code — it already lists the three correct words.",
        ),
    ),
    # ---------------------------------------------------------------- CS6
    _cc(
        "csc6-cc-factorial",
        "CS6", "loops", "medium",
        "Complete the factorial",
        "Complete the program so it computes n! = 1 × 2 × … × n.",
        "n = int(input())\nfact = 1\nfor i in range(1, ____ + 1):\n    fact ____= i\nprint(fact)",
        [
            {"input": "5\n", "expected": "120"},
            {"input": "3\n", "expected": "6"},
            {"input": "0\n", "expected": "1"},
        ],
        _hint(
            "range(1, k) visits 1…k−1. To visit up to n we need the stop argument to be one bigger.",
            "The loop bound must be n, and the update multiplies: fact *= i. For n = 0 the loop "
            "never runs, so fact stays 1 — which is correct (0! = 1).",
            "for i in range(1, n + 1):\n    fact *= i",
        ),
    ),
    _dbg(
        "csc6-dbg-offbyone",
        "CS6", "loops", "medium",
        "Fix the missing term",
        "This program should print the sum 1 + 2 + … + n, but it always comes up short. Debug it.",
        "n = int(input())\ntotal = 0\nfor i in range(1, n):\n    total += i\nprint(total)",
        [
            {"input": "5\n", "expected": "15"},
            {"input": "4\n", "expected": "10"},
            {"input": "1\n", "expected": "1"},
        ],
        _hint(
            "The loop stops too early. Write out which values i actually visits for n = 5.",
            "range(1, n) visits 1…n−1 and misses n itself. The stop value is exclusive.",
            "for i in range(1, n + 1):",
        ),
    ),
    _out(
        "csc6-out-range",
        "CS6", "loops",
        "Predict the stepped loop",
        "for i in range(0, 10, 3):\n    print(i)",
        ["0\n3\n6\n9", "0\n3\n6\n9\n10", "1\n4\n7\n10", "3\n6\n9"],
        0,
        "range(0, 10, 3) starts at 0, adds 3 each step, and stops before reaching 10.",
    ),
    _chal(
        "csc6-chal-sums",
        "CS6", "loops", "medium",
        "Sum 1 to n",
        "Read one integer n and print the sum 1 + 2 + … + n. For n = 100 the answer is 5050.",
        "n = int(input())\ntotal = 0\nfor i in range(1, n + 1):\n    total += i\nprint(total)",
        [
            {"input": "100\n", "expected": "5050"},
            {"input": "4\n", "expected": "10"},
        ],
        _hint(
            "Keep a running total: start at 0 and add each number as you see it.",
            "A for loop over range(1, n + 1) gives you exactly the numbers to add.",
            "See the starter code — it is already the complete solution pattern.",
        ),
    ),
    # ---------------------------------------------------------------- CS7
    _cc(
        "csc7-cc-whilesum",
        "CS7", "loops", "medium",
        "Complete the sentinel sum",
        "The program keeps reading numbers and adding them until the sentinel value -1 "
        "is entered, then prints the total. Fill the blanks.",
        'total = 0\nvalue = int(input())\nwhile value ____ -1:\n    total += value\n    value = int(____())\nprint(total)',
        [
            {"input": "5\n3\n-1\n", "expected": "8"},
            {"input": "10\n-1\n", "expected": "10"},
            {"input": "-1\n", "expected": "0"},
        ],
        _hint(
            "A sentinel loop runs while the value is NOT the stop signal.",
            "The condition should be value != -1, and inside the loop we read the next number with input().",
            "while value != -1: ... value = int(input())",
        ),
    ),
    _dbg(
        "csc7-dbg-infinite",
        "CS7", "loops", "medium",
        "Stop the runaway loop",
        "This program is supposed to print 0, 1, 2, …, n−1 — but it never stops. Debug it.",
        "n = int(input())\ni = 0\nwhile i < n:\n    print(i)",
        [{"input": "3\n", "expected": "0\n1\n2"}],
        _hint(
            "Every loop needs its control variable to move towards the stopping condition.",
            "i never changes inside the body. Add i += 1 after the print.",
            "while i < n:\n    print(i)\n    i += 1",
        ),
    ),
    _chal(
        "csc7-chal-triangle",
        "CS7", "loops", "hard",
        "Print a right triangle",
        "Read a size n and print n rows where row i has exactly i stars (*). For n = 3:",
        'n = int(input())\nfor row in range(1, n + 1):\n    print("*" * row)',
        [
            {"input": "3\n", "expected": "*\n**\n***"},
            {"input": "5\n", "expected": "*\n**\n***\n****\n*****"},
            {"input": "1\n", "expected": "*"},
        ],
        _hint(
            "A string can be multiplied: \"*\" * 3 gives \"***\". Row number i should print i stars.",
            "For row in range(1, n + 1) prints exactly one more star each line. No nested loop is needed.",
            "\"*\" * row reproduces the stars; see the starter for the full loop.",
        ),
    ),
    # ---------------------------------------------------------------- CS8
    _dbg(
        "csc8-dbg-palindrome",
        "CS8", "strings", "medium",
        "Fix the palindrome check",
        "This word should be reported 'palindrome' when it reads the same forwards and "
        "backwards. The program reports the opposite. Debug it.",
        'rev = word[::-1]\nword = input()\nif rev != word:\n    print("palindrome")\nelse:\n    print("no")',
        [
            {"input": "madam\n", "expected": "palindrome"},
            {"input": "hello\n", "expected": "no"},
            {"input": "arete\n", "expected": "no"},
        ],
        _hint(
            "Read the condition out loud and check which branch a real palindrome should hit.",
            "Also note word is read *after* rev is computed — the comparison uses rev before the "
            "input exists. Read the word first, then compare with ==.",
            'word = input()\nrev = word[::-1]\nif rev == word:\n    print("palindrome")\nelse:\n    print("no")',
        ),
    ),
    _out(
        "csc8-out-slice",
        "CS8", "strings",
        "Predict the slices",
        's = "Programming"\nprint(s[-3:])\nprint(s[:4])',
        ["ing\nProg", "Prog\ning", "ing\nProgra", "gar\nProg"],
        0,
        "s[-3:] takes the last three characters; s[:4] takes the first four.",
    ),
    _chal(
        "csc8-chal-vowels",
        "CS8", "strings", "medium",
        "Count the vowels",
        "Read one word and print how many of its letters are vowels (a, e, i, o, u — "
        "upper or lower case both count).",
        'word = input().lower()\ncount = 0\nfor ch in word:\n    if ch in "aeiou":\n        count += 1\nprint(count)',
        [
            {"input": "Arete\n", "expected": "3"},
            {"input": "bcdf\n", "expected": "0"},
            {"input": "ELEPHANT\n", "expected": "3"},
        ],
        _hint(
            "Compare each character to the set of vowels. Lower-casing first makes A and a behave the same.",
            'The test "ch in \\"aeiou\\"" is True for any vowel.',
            "See the starter code — it already implements the full strategy.",
        ),
    ),
    # ---------------------------------------------------------------- CS9
    _dbg(
        "csc9-dbg-index",
        "CS9", "lists", "medium",
        "Fix the runaway index",
        "This program should print the sum of the list, but it crashes. Debug it.",
        "items = [3, 1, 4, 1, 5]\ntotal = 0\ni = 0\nwhile i <= len(items):\n    total += items[i]\n    i += 1\nprint(total)",
        [{"input": "", "expected": "14"}],
        _hint(
            "A list of 5 elements is indexed 0 … 4. What does items[5] do?",
            "The condition should run only while i is strictly less than len(items).",
            "while i < len(items):",
        ),
    ),
    _chal(
        "csc9-chal-maxmin",
        "CS9", "lists", "hard",
        "Max and min of a list",
        "Read an integer n, then n more integers (one per line). Print the largest "
        "value as Max: and the smallest as Min:.",
        'n = int(input())\nvalues = [int(input()) for _ in range(n)]\nprint("Max:", max(values))\nprint("Min:", min(values))',
        [
            {"input": "5\n3\n9\n1\n7\n2\n", "expected": "Max: 9\nMin: 1"},
            {"input": "3\n8\n8\n8\n", "expected": "Max: 8\nMin: 8"},
        ],
        _hint(
            "max() and min() do the work once the values are in a list.",
            "Build the list with a loop or comprehension over range(n).",
            "See the starter — the comprehension values = [int(input()) for _ in range(n)] is the key.",
        ),
    ),
    # ---------------------------------------------------------------- CS10
    _cc(
        "csc10-cc-average",
        "CS10", "functions", "medium",
        "Complete the average function",
        "Fill the blanks so average(a, b, c) returns the mean of three numbers.",
        "def average(a, b, c):\n    return (a + b + c) / ____\n\n"
        "x = int(input())\ny = int(input())\nz = int(input())\nprint(average(____))",
        [
            {"input": "4\n5\n6\n", "expected": "5.0"},
            {"input": "10\n20\n30\n", "expected": "20.0"},
        ],
        _hint(
            "The mean divides the sum by how many values were added.",
            "Divide by 3, and pass all three variables in the call: x, y, z.",
            "return (a + b + c) / 3\nprint(average(x, y, z))",
        ),
    ),
    _dbg(
        "csc10-dbg-missingreturn",
        "CS10", "functions", "medium",
        "Bring back the return",
        "is_even(n) should give back True or False so the final print shows it. Right now it "
        "prints the wrong thing. Debug it.",
        "def is_even(n):\n    if n % 2 == 0:\n        print(\"even\")\n    else:\n        print(\"odd\")\n\nprint(is_even(4))",
        [
            {"input": "4\n", "expected": "True"},
            {"input": "7\n", "expected": "False"},
        ],
        _hint(
            "The function must hand a value back to the caller, not print it. What does is_even(4) "
            "print right now?",
            "Replace both print calls with return statements: return True for even, return False for odd.",
            'def is_even(n):\n    return n % 2 == 0\n\nprint(is_even(4))',
        ),
    ),
    _chal(
        "csc10-chal-maxofthree",
        "CS10", "functions", "medium",
        "Largest of three (function)",
        "Write a function max_of_three(a, b, c) and print what it returns for three "
        "integers read from input.",
        "def max_of_three(a, b, c):\n    if a >= b and a >= c:\n        return a\n    if b >= a and b >= c:\n        return b\n    return c\n\n"
        "a = int(input())\nb = int(input())\nc = int(input())\nprint(max_of_three(a, b, c))",
        [
            {"input": "3\n9\n5\n", "expected": "9"},
            {"input": "7\n7\n2\n", "expected": "7"},
            {"input": "1\n2\n3\n", "expected": "3"},
        ],
        _hint(
            "Compare a against both others; if a is not the greatest, is b greater than both?",
            "Chained comparisons with and check each candidate. Ties are fine because >= is used.",
            "See the starter code — it is a working implementation to learn from.",
        ),
    ),
    # ---------------------------------------------------------------- CS11
    _cc(
        "csc11-cc-recsum",
        "CS11", "recursion", "hard",
        "Complete the recursive sum",
        "sum_to(n) should return 1 + 2 + … + n using recursion (sum_to calls itself). "
        "Fill the blanks.",
        "def sum_to(n):\n    if n <= 1:\n        return ____\n    return n + ____(n - 1)\n\n"
        "print(sum_to(int(input())))",
        [
            {"input": "4\n", "expected": "10"},
            {"input": "1\n", "expected": "1"},
            {"input": "7\n", "expected": "28"},
        ],
        _hint(
            "Recursion needs a base case (the smallest input, answered directly) and a step that "
            "reduces the problem.",
            "sum_to(1) is 1; every other call is n plus the result for n−1.",
            "return 1\nreturn n + sum_to(n - 1)",
        ),
    ),
    _chal(
        "csc11-chal-recfact",
        "CS11", "recursion", "hard",
        "Recursive factorial",
        "Write a recursive function factorial(n) — factorial calls itself — and print "
        "its result for one integer read from input. 0! is 1.",
        "def factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n - 1)\n\n"
        "print(factorial(int(input())))",
        [
            {"input": "5\n", "expected": "120"},
            {"input": "6\n", "expected": "720"},
            {"input": "0\n", "expected": "1"},
        ],
        _hint(
            "Base case: 0! and 1! are both 1. Step: n! = n × (n−1)!.",
            "Return 1 when n <= 1; otherwise return n * factorial(n - 1).",
            "See the starter code — it is already the complete recursive implementation.",
        ),
    ),
    _out(
        "csc11-out-recursion",
        "CS11", "recursion",
        "Predict the recursion",
        'def mystery(n):\n    if n == 0:\n        return\n    print(n, end=" ")\n    mystery(n - 1)\n\nmystery(3)',
        ["3 2 1", "1 2 3", "3 2 1 0", "0 1 2 3"],
        0,
        "Each call prints n, then calls mystery(n − 1); the base case n == 0 returns "
        "without printing, so 0 never appears.",
    ),
]


def challenges_for_lesson(lesson_code: str) -> list[dict]:
    return [c for c in CHALLENGES if c["lesson_code"] == lesson_code]


def all_lessons() -> list[dict]:
    return [{"code": code, "title": title} for code, title in LESSONS]


def challenge_by_id(challenge_id: str) -> dict | None:
    for c in CHALLENGES:
        if c["id"] == challenge_id:
            return c
    return None


def lesson_title(lesson_code: str) -> str:
    for code, title in LESSONS:
        if code == lesson_code:
            return title
    return lesson_code