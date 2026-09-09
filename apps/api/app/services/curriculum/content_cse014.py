"""CSE014 — Structured Programming (introductory Java, AIU first year).

Curated from the CSE014 ARETE lectures (Fall 2024, Building Java Programs
textbook): lectures 1–6 and 8–12 (week 7 is the midterm, hence no lecture 7).
Each bundle is one module + one lesson, the same idempotent importer contract
as the PHY211 and MAT111 bundles.

Lesson map (code → source lecture):
  CS1  ← Lecture 1  Introduction to Java: programs, JDK/JRE/JVM, pipeline
  CS2  ← Lecture 2  Main memory, compilation, and first programs
  CS3  ← Lecture 3  Assignment operators, char/String, Scanner
  CS4  ← Lecture 4  Math library, type casting, Boolean operators
  CS5  ← Lecture 5  Selection statements (if / if-else / ?: / switch)
  CS6  ← Lecture 6  for loops, cumulative sum, factorial
  CS7  ← Lecture 8  while & do-while loops, nested loops, arrays
  CS8  ← Lecture 9  Strings, palindrome detection, array operations
  CS9  ← Lecture 10 Array problem set, 2D arrays, methods
  CS10 ← Lecture 11 Methods in depth: parameters, returns, arrays
  CS11 ← Lecture 12 Call-by-value vs reference, returning arrays, recursion

Fields are plain JSON-able Python, same conventions as the other bundles.
"""

from __future__ import annotations

COURSE_CODE = "CSE014"
COURSE_TITLE = "Structured Programming"
COURSE_CREDITS = 3
COURSE_DESCRIPTION = (
    "Structured Programming (CSE014) — first-year introductory Java course. "
    "Starts with how programs, the JVM and main memory work, then builds "
    "expressions, input/output, selection, loops, arrays, strings, static "
    "methods and recursion. Based on 'Building Java Programs: A Back to "
    "Basics Approach' (Reges & Stepp) and the ARETE content pipeline."
)

DEPARTMENT_CODE = "CS"
DEPARTMENT_NAME = "Computer Science"
FACULTY_CODE = "ENG"
FACULTY_NAME = "Faculty of Engineering"

MODULE_GETTING_STARTED = {
    "code": "M1",
    "title": "Module 1 — Getting Started with Java",
    "description": (
        "What a program is, the JDK/JRE/JVM stack, how main memory works and "
        "the compile→bytecode→run pipeline; your first complete programs."
    ),
    "sort_order": 1,
}

MODULE_TYPES_IO = {
    "code": "M2",
    "title": "Module 2 — Types, Operators and Input",
    "description": (
        "Assignment and increment operators, char, String immutability and the "
        "Scanner class, the Math library, casting and Boolean logic."
    ),
    "sort_order": 2,
}

MODULE_CONTROL = {
    "code": "M3",
    "title": "Module 3 — Control Flow",
    "description": (
        "Selection statements (if, if-else, ternary, switch) and counted "
        "repetition with the for loop, cumulative algorithms and factorial."
    ),
    "sort_order": 3,
}

MODULE_LOOPS_ARRAYS = {
    "code": "M4",
    "title": "Module 4 — while Loops, Nested Loops and Arrays",
    "description": (
        "Condition-driven while and do-while loops, nested loops and the "
        "declaration, traversal and input/output of one-dimensional arrays."
    ),
    "sort_order": 4,
}

MODULE_STRINGS_ARRAYS = {
    "code": "M5",
    "title": "Module 5 — Strings, Array Operations and 2D Arrays",
    "description": (
        "String basics and the palindrome algorithm, the array problem set "
        "(reverse, search, max, filtering) and two-dimensional arrays."
    ),
    "sort_order": 5,
}

MODULE_METHODS = {
    "code": "M6",
    "title": "Module 6 — Static Methods, Reference Semantics and Recursion",
    "description": (
        "Method anatomy, parameters and return values, arrays as parameters, "
        "call-by-value vs reference semantics, returning arrays and recursion."
    ),
    "sort_order": 6,
}

# --- CS1 ---------------------------------------------------------------

CS1_OBJECTIVES = [
    "Define a program in your own words.",
    "Distinguish JVM, JRE and JDK and describe the compile/run pipeline.",
    "Identify the parts of a Java program: class, main method, statement, comment.",
    "Compile and run a 'Hello World' style program.",
    "Use System.out.println and the four escape sequences.",
    "Classify syntax, logic and runtime errors.",
]
CS1_PREREQUISITES = [
    "No prior programming experience required — this is the entry lesson.",
]
CS1_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "A program is a set of instructions to be carried out by a computer. "
            "Java is unusual: source code is first compiled into bytecode, then "
            "executed by a virtual machine. That is why the same .class file "
            "runs unchanged on Windows, macOS and Linux."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "The runtime and development stack",
        "body": (
            "JRE = JVM + Library Classes\n"
            "JDK = JRE + Java Compiler (javac)\n"
            "Compile:  javac Hello.java  →  Hello.class\n"
            "Run:      java Hello        →  JVM runs the main method"
        ),
        "metadata": {
            "meaning": "The JRE can run programs; the JDK can also write and compile them.",
            "when_used": "Choosing what to install and turning source into running programs.",
        },
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example — a complete program",
        "body": (
            "public class Demo {\n"
            "    public static void main(String[] args) {\n"
            "        System.out.println(\"Hello, World!\");\n"
            "    }\n"
            "}\n"
            "Save as Demo.java, compile with javac Demo.java, run with java Demo. "
            "The class name must match the file name exactly, including capitalisation."
        ),
    },
    {
        "section_type": "TABLE",
        "title": "Escape sequences (Lecture 1)",
        "body": (
            "\\t  →  tab\n"
            "\\n  →  newline\n"
            "\\\"  →  a literal double quote\n"
            "\\\\  →  a literal backslash"
        ),
        "metadata": {"note": "The backslash is the escape character; a literal backslash is always written as \\\\."},
    },
    {
        "section_type": "KEY_POINT",
        "title": "main is the front door",
        "body": (
            "The JVM looks for exactly public static void main(String[] args). "
            "Java classes can contain many methods, so the entry point must be "
            "unambiguous — that signature says 'start here'."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example — predicting output (Q2.2)",
        "body": (
            "System.out.println(\"a\\\\b\\nc\\\"d\"); prints two lines:\n"
            "a\\b\n"
            "c\"d\n"
            "Because \\\\ → one backslash, \\n → newline, \\\" → one quote."
        ),
    },
    {
        "section_type": "WARNING",
        "title": "Compiling is not executing",
        "body": (
            "javac checks syntax only. A program that compiles can still have "
            "logic errors (runs but prints the wrong output) or runtime errors "
            "(crashes while running). Success at compile time proves nothing "
            "about intent."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Summary",
        "body": (
            "JDK compiles, JRE runs, JVM executes. Source → bytecode → output. "
            "class name = file name, main is the entry point, println and the "
            "four escape sequences control the output."
        ),
    },
]
CS1_PRACTICE = [
    {
        "prompt": "Which tool chain correctly describes the Java compile/run pipeline?",
        "options": [
            "javac compiles .java to .class bytecode; java runs the bytecode on the JVM",
            "java compiles source directly to machine language; javac runs it",
            "The JRE compiles source; the JVM is only used for debugging",
            "Both commands are interchangeable for compiling and running",
        ],
        "correct_index": 0,
        "explanation": "javac produces bytecode; java launches the JVM to execute it.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "java-program-anatomy",
    },
    {
        "prompt": "A friend sends you a compiled .class file. You have only the JRE installed. Can you run it?",
        "options": [
            "Yes, with the command: java Mystery",
            "No — you need the JDK installed first",
            "Yes, with the command: javac Mystery",
            "No — .class files need to be recompiled to your OS",
        ],
        "correct_index": 0,
        "explanation": "Bytecode is already compiled; the JRE (which includes the JVM) is all that is needed. The command takes the class name, no extension.",
        "level": "TRANSFER",
        "difficulty": 3,
        "skill": "java-program-anatomy",
    },
    {
        "prompt": "Which statement prints: She said, \"Java is fun!\"",
        "options": [
            "System.out.println(\"She said, \\\"Java is fun!\\\"\");",
            "System.out.println(\"She said, \"Java is fun!\"\");",
            "System.out.println('She said, \"Java is fun!\"');",
            "System.out.println(\"She said, Java is fun!\");",
        ],
        "correct_index": 0,
        "explanation": "Quotes inside a string literal must be escaped as \\\".",
        "level": "APPLY",
        "difficulty": 2,
        "skill": "escape-sequences",
    },
    {
        "prompt": "A program compiles successfully but prints \"Hellow\" instead of \"Hello\". What kind of error is this?",
        "options": [
            "Logic error",
            "Syntax error",
            "Runtime error",
            "Compiler error",
        ],
        "correct_index": 0,
        "explanation": "It compiles fine but the output is wrong — the classic logic error.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "error-classification",
    },
]
CS1_LINKS = [
    {"code": "java-program-anatomy", "role": "teaches"},
    {"code": "escape-sequences", "role": "teaches"},
    {"code": "compilation-pipeline", "role": "teaches"},
]

# --- CS2 ---------------------------------------------------------------

CS2_OBJECTIVES = [
    "Explain how main memory stores data and why it is volatile.",
    "Trace source code → bytecode → executed bytecode.",
    "Identify the structural parts of a Java program.",
    "Use arithmetic operators with correct precedence and associativity.",
    "Distinguish integer division from real division and use modulus.",
    "Declare, initialise and assign primitive variables.",
]
CS2_PREREQUISITES = [
    "CS1: what a program is and how to compile and run one.",
]
CS2_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "Main memory (RAM) is a large array of numbered cells. Variables "
            "are really names for groups of those cells, and every value has "
            "a type because the type fixes how many cells it occupies and how "
            "those bits are interpreted. Memory is volatile — it forgets "
            "everything when the power goes off."
        ),
    },
    {
        "section_type": "TABLE",
        "title": "Primitive types and sizes",
        "body": (
            "int   4 bytes  — whole numbers\n"
            "double 8 bytes — real numbers (fractional)\n"
            "char   2 bytes — a single character\n"
            "boolean 1 byte — true or false"
        ),
        "metadata": {"note": "First-semester programs use int, double, char and boolean."},
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example — variable assignment",
        "body": (
            "int x = 5;\n"
            "double y = 2.5;\n"
            "x = x + 3;   // now x is 8\n"
            "y = y * 2;   // now y is 5.0\n"
            "Assignment evaluates the right side first, then stores the result "
            "into the variable on the left."
        ),
    },
    {
        "section_type": "TABLE",
        "title": "Arithmetic operators and precedence",
        "body": (
            "*  /  %   — higher precedence, left-associative\n"
            "+  -      — lower precedence, left-associative\n"
            "int / int always yields int (3/2 → 1).\n"
            "int % int yields the remainder (14 % 3 → 2).\n"
            "If either operand is double, division is real (3.0/2 → 1.5)."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example — modulus extracts digits",
        "body": (
            "int n = 482;\n"
            "n % 10          → 2   (rightmost digit)\n"
            "n / 10          → 48  (drop the last digit)\n"
            "n % 2 == 0 tests whether n is even: 482 % 2 → 0."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "Type is the tie-breaker",
        "body": (
            "The same symbols behave differently by operand type. 7/2 is 3, "
            "but 7/2.0 is 3.5. Predict the type of an expression before you "
            "predict its value."
        ),
    },
    {
        "section_type": "WARNING",
        "title": "Volatile memory",
        "body": (
            "RAM needs power to hold data. Powerful and fast, but forgetful — "
            "the reason saved work must go to disk or flash storage."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Summary",
        "body": (
            "Variables name typed cells in main memory. Integer division "
            "truncates and % extracts remainders; operator precedence follows "
            "Mathematics but types decide the outcome."
        ),
    },
]
CS2_PRACTICE = [
    {
        "prompt": "What is the value of 14 % 3?",
        "options": ["2", "4.6", "4", "5"],
        "correct_index": 0,
        "explanation": "14 = 4×3 + 2, so the remainder is 2.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "arithmetic-operators",
    },
    {
        "prompt": "What is the value of 2 + 3 * 4, evaluated with Java precedence?",
        "options": ["14", "20", "24", "32"],
        "correct_index": 0,
        "explanation": "* binds tighter than +: 3*4 = 12, then 2+12 = 14.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "arithmetic-operators",
    },
    {
        "prompt": "The expression 7 / 2.0 evaluates to:",
        "options": ["3.5", "3", "3.0", "3 remainder 1"],
        "correct_index": 0,
        "explanation": "A double operand makes division real: 7 / 2.0 → 3.5.",
        "level": "APPLY",
        "difficulty": 2,
        "skill": "arithmetic-operators",
    },
    {
        "prompt": "Write an expression that extracts the digit '8' from the int 482 (hundreds place).",
        "options": ["(482 / 10) % 10", "482 % 10", "482 / 100", "(482 % 10) / 1"],
        "correct_index": 0,
        "explanation": "482/10 → 48, then 48%10 → 8.",
        "level": "TRANSFER",
        "difficulty": 3,
        "skill": "arithmetic-operators",
    },
]
CS2_LINKS = [
    {"code": "arithmetic-operators", "role": "teaches"},
    {"code": "java-program-anatomy", "role": "requires"},
]

# --- CS3 ---------------------------------------------------------------

CS3_OBJECTIVES = [
    "Decompose a word problem into inputs, outputs and calculations.",
    "Use compound assignment operators and explain prefix vs postfix increments.",
    "Use char and the String methods length, charAt, indexOf, substring, toLowerCase, toUpperCase.",
    "Explain String immutability and why String is a reference type.",
    "Build a Scanner bound to System.in and pick the correct next* method.",
    "Identify a token and when InputMismatchException is thrown.",
]
CS3_PREREQUISITES = [
    "CS2: variables and arithmetic operators.",
]
CS3_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "Real programs rarely compute from constants: they read input, "
            "crunch numbers, then print output. Planning a solution as "
            "Inputs → Outputs → Calculations keeps Java programs small and "
            "testable. Interactive input comes from the Scanner class; text "
            "handling from the String class and its methods."
        ),
    },
    {
        "section_type": "TABLE",
        "title": "Compound assignment and increments",
        "body": (
            "x += 5   ⟺  x = x + 5\n"
            "x -= 3   ⟺  x = x - 3\n"
            "x *= 2   ⟺  x = x * 2\n"
            "x /= 4   ⟺  x = x / 4\n"
            "x++ / ++x  ⟺  x = x + 1\n"
            "x-- / --x  ⟺  x = x - 1"
        ),
        "metadata": {"note": "In x = y++ the old y is used; in x = ++y the new value is used first."},
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example — prefix vs postfix",
        "body": (
            "int a = 5;\n"
            "int b = a++;   // b = 5, then a = 6  (post: use old, then increment)\n"
            "int c = ++a;   // a = 7, then c = 7  (pre: increment, then use)"
        ),
    },
    {
        "section_type": "TABLE",
        "title": "Essential String methods",
        "body": (
            "s.length()            → number of characters\n"
            "s.charAt(i)           → character at index i (0-based)\n"
            "s.indexOf(s2)         → first index of s2, or -1 if absent\n"
            "s.substring(a, b)     → characters from index a up to (not including) b\n"
            "s.substring(a)        → characters from a to the end\n"
            "s.toLowerCase()       → new all-lowercase String\n"
            "s.toUpperCase()       → new all-uppercase String"
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example — interactive program",
        "body": (
            "Scanner input = new Scanner(System.in);\n"
            "System.out.print(\"How many hours? \");\n"
            "int hours = input.nextInt();\n"
            "input.nextLine();   // consume the leftover newline\n"
            "System.out.println(hours + \" hours = \" + (hours * 60) + \" minutes\");"
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "String is immutable",
        "body": (
            "s.toLowerCase() does not change s — it returns a new String. "
            "Every method that 'changes' a String actually yields a fresh "
            "object; the original stays intact. That is why s.toUpperCase(); "
            "alone does nothing useful."
        ),
    },
    {
        "section_type": "WARNING",
        "title": "nextInt pitfalls",
        "body": (
            "nextInt reads a token but leaves the newline behind; the next "
            "nextLine then returns an empty string. Call input.nextLine() "
            "after numeric reads. If the token is not an int, "
            "InputMismatchException is thrown."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Summary",
        "body": (
            "Decompose problems into input → calculation → output, use "
            "compound and increment operators for brevity, and treat String "
            "as immutable text with a fixed set of query methods."
        ),
    },
]
CS3_PRACTICE = [
    {
        "prompt": "int x = 5; int y = x++; What are x and y?",
        "options": ["x = 6, y = 5", "x = 5, y = 5", "x = 6, y = 6", "x = 5, y = 6"],
        "correct_index": 0,
        "explanation": "Postfix uses the old value (5) then increments x to 6.",
        "level": "APPLY",
        "difficulty": 2,
        "skill": "compound-operators",
    },
    {
        "prompt": "String s = \"hello\"; s.toUpperCase(); What is s afterwards?",
        "options": ["\"hello\"", "\"HELLO\"", "\"Hello\"", "the result is undefined"],
        "correct_index": 0,
        "explanation": "toUpperCase returns a new String; the result was discarded, so s is unchanged (immutability).",
        "level": "APPLY",
        "difficulty": 2,
        "skill": "string-methods",
    },
    {
        "prompt": "\"university\".substring(2, 5) returns:",
        "options": ["\"ive\"", "\"niv\"", "\"ive\"", "\"univers\""],
        "correct_index": 0,
        "explanation": "Characters at indices 2,3,4 → 'i','v','e'. End index is exclusive.",
        "level": "APPLY",
        "difficulty": 2,
        "skill": "string-methods",
    },
    {
        "prompt": "Scanner.nextInt() throws InputMismatchException when:",
        "options": [
            "the next token is not an int",
            "the user presses Enter with no input",
            "the scanner is bound to a file",
            "the int is larger than an int",
        ],
        "correct_index": 0,
        "explanation": "The Scanner scans tokens; a non-int token where an int is expected throws InputMismatchException.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "scanner-input",
    },
]
CS3_LINKS = [
    {"code": "compound-operators", "role": "teaches"},
    {"code": "string-methods", "role": "teaches"},
    {"code": "scanner-input", "role": "teaches"},
    {"code": "arithmetic-operators", "role": "requires"},
]

# --- CS4 ---------------------------------------------------------------

CS4_OBJECTIVES = [
    "Use the Math library methods and the constants PI and E.",
    "Distinguish parameters from return values.",
    "Cast between numeric types and explain (int) truncation.",
    "Evaluate relational and Boolean operators and combine them.",
    "Rewrite 2 ≤ x ≤ 10 correctly in Java.",
    "Generate a random integer in a desired range.",
]
CS4_PREREQUISITES = [
    "CS3: variables, operators and Scanner.",
]
CS4_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "The Math class is a library of ready-made functions: pass values "
            "in (parameters), get a computed value back (return value). "
            "Casting lets you force a conversion between numeric types — its "
            "superpower is controlling division. Boolean logic drives every "
            "selection statement that follows in Lecture 5."
        ),
    },
    {
        "section_type": "TABLE",
        "title": "Math library essentials",
        "body": (
            "Math.sqrt(x), Math.pow(x, y), Math.abs(x)\n"
            "Math.min(a, b), Math.max(a, b)\n"
            "Math.round(x) — nearest long\n"
            "Math.ceil(x), Math.floor(x)\n"
            "Math.random() — a double in [0, 1)\n"
            "Math.PI, Math.E — the two constants\n"
            "Math.sin, Math.cos, Math.tan — in radians"
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example — range from random()",
        "body": (
            "Random doubles in [min, max):\n"
            "double r = Math.random() * (max - min) + min;\n"
            "A random integer 1..6 (dice):\n"
            "int die = (int) (Math.random() * 6) + 1;"
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Casting syntax and truncation",
        "body": (
            "(int) 2.9    → 2     (fraction is truncated, not rounded)\n"
            "(double) 3   → 3.0\n"
            "(int) (Math.random() * 100)  → integer 0..99\n"
            "To force real division:  (double) a / b"
        ),
        "metadata": {
            "meaning": "A cast creates a new value of the target type from the old value.",
            "when_used": "Controlling division, truncating, generating random integers.",
        },
    },
    {
        "section_type": "TABLE",
        "title": "Relational and Boolean operators",
        "body": (
            "Relational: <  >  <=  >=  ==  !=\n"
            "Boolean:    ! (not), && (and), || (or)\n"
            "De Morgan:  !(a && b) == (!a || !b)\n"
            "Java cannot chain: 2 <= x <= 10 must be written\n"
            "2 <= x && x <= 10"
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example — combined condition",
        "body": (
            "int grade = 86;\n"
            "boolean honours = grade >= 85 && grade <= 95;\n"
            "// true — both relational results are true, and joins them.\n"
            "boolean fail = !(grade >= 50);  // equivalent to grade < 50."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "The no-chaining rule",
        "body": (
            "2 <= x <= 10 is a syntax error in Java because <= produces a "
            "boolean, and a boolean cannot be compared with <=. Always split "
            "a mathematical range into two relational tests joined by &&."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Summary",
        "body": (
            "Math provides functions and constants; casting forces type "
            "conversions and controls division; Boolean operators combine "
            "conditions, but ranges need two tests joined by &&."
        ),
    },
]
CS4_PRACTICE = [
    {
        "prompt": "(int) 7.99 evaluates to:",
        "options": ["7", "8", "8.0", "7.9"],
        "correct_index": 0,
        "explanation": "Casting a double to int truncates the fraction — 7.99 becomes 7.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "casting",
    },
    {
        "prompt": "Which expression produces a random integer in the range 0..99 inclusive?",
        "options": [
            "(int) (Math.random() * 100)",
            "(int) Math.random() * 100",
            "Math.random() * 100",
            "(int) (Math.random() * 99)",
        ],
        "correct_index": 0,
        "explanation": "Math.random() is in [0,1); times 100 gives [0,100); casting truncates to 0..99. Casting the whole product (parentheses) is essential.",
        "level": "APPLY",
        "difficulty": 2,
        "skill": "math-library",
    },
    {
        "prompt": "The condition for 2 ≤ x ≤ 10 is written in Java as:",
        "options": [
            "2 <= x && x <= 10",
            "2 <= x <= 10",
            "x >= 2 || x <= 10",
            "(2 <= x) || (x <= 10)",
        ],
        "correct_index": 0,
        "explanation": "Ranges must use two relational tests joined by &&; chaining is illegal.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "boolean-expressions",
    },
    {
        "prompt": "What does the following produce?\nint a = 3, b = 2;\n(double) a / b",
        "options": ["1.5", "1", "1.0", "2"],
        "correct_index": 0,
        "explanation": "Casting only a to double makes the division real: 3.0 / 2 = 1.5.",
        "level": "APPLY",
        "difficulty": 2,
        "skill": "casting",
    },
]
CS4_LINKS = [
    {"code": "math-library", "role": "teaches"},
    {"code": "casting", "role": "teaches"},
    {"code": "boolean-expressions", "role": "teaches"},
    {"code": "arithmetic-operators", "role": "requires"},
]

# --- CS5 ---------------------------------------------------------------

CS5_OBJECTIVES = [
    "Identify when to use if, if-else and switch.",
    "Write if and if-else statements and decide when braces are required.",
    "Write cascading else-if ladders such as letter grades.",
    "Use the ternary operator ?:.",
    "Write a switch with case labels, default and break.",
    "Predict the output when break is omitted (fall-through).",
]
CS5_PREREQUISITES = [
    "CS4: relational and Boolean operators.",
]
CS5_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "Selection lets a program choose a path based on a boolean test. "
            "Java offers three tools for the job: if (a single guard), "
            "if-else with cascading else-if (mutually exclusive branches) and "
            "switch (a table lookup on one expression). Choose by how many "
            "branches you need and what you are testing."
        ),
    },
    {
        "section_type": "TABLE",
        "title": "Selection forms",
        "body": (
            "if (test) { ... }                — run if test is true\n"
            "if (test) { ... } else { ... }   — choose between two blocks\n"
            "if (..) {} else if (..) {} else {}  — cascading ladder\n"
            "(test) ? valueTrue : valueFalse  — ternary, an expression\n"
            "switch (x) { case 1: ...; break; default: ...; }"
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example — letter grade with a ladder",
        "body": (
            "int score = ...;\n"
            "char grade;\n"
            "if (score >= 90)      grade = 'A';\n"
            "else if (score >= 80) grade = 'B';\n"
            "else if (score >= 70) grade = 'C';\n"
            "else if (score >= 60) grade = 'D';\n"
            "else                  grade = 'F';"
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example — switch and fall-through",
        "body": (
            "switch (day) {\n"
            "  case 1: System.out.println(\"Monday\"); break;\n"
            "  case 2: System.out.println(\"Tuesday\"); break;\n"
            "  default: System.out.println(\"Weekend\");\n"
            "}\n"
            "Without break, execution keeps falling into the next case — "
            "deliberate in some algorithms, a bug in most."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "Braces are about single statements",
        "body": (
            "If a branch body is a single statement, braces are optional — but "
            "only one statement belongs to that branch. Add a second line "
            "without braces and it always runs. Always brace to be safe."
        ),
    },
    {
        "section_type": "WARNING",
        "title": "elif does not exist in Java",
        "body": (
            "The ladder is else if — two words, no apostrophe, else then if. "
            "A common newcomer typo is 'elseif' or 'else if()' with wrong "
            "spacing, which the compiler rejects."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Summary",
        "body": (
            "Guard with if, choose between two with if-else, cascade with "
            "else-if for ranges, table-lookup with switch. Ternary is an "
            "expression; break controls switch fall-through; always brace."
        ),
    },
]
CS5_PRACTICE = [
    {
        "prompt": "Which construct is best for mapping a score to a letter grade across many ranges?",
        "options": [
            "A cascading if-else-if ladder",
            "A single if statement",
            "A switch statement",
            "The ternary operator",
        ],
        "correct_index": 0,
        "explanation": "Ranges of one variable are naturally expressed as an else-if ladder; switch works on exact equality.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "selection-statements",
    },
    {
        "prompt": "The ternary (x % 2 == 0) ? \"even\" : \"odd\" is equivalent to:",
        "options": [
            "An if-else that sets the result to \"even\" or \"odd\"",
            "A switch with two cases",
            "A while loop testing evenness",
            "A cascading else-if ladder with three branches",
        ],
        "correct_index": 0,
        "explanation": "The ternary is a compact two-way expression: one value when true, another when false.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "ternary-operator",
    },
    {
        "prompt": "switch (n) { case 1: print(\"A\"); case 2: print(\"B\"); break; } with n = 1 outputs:",
        "options": ["AB", "A", "B", "nothing"],
        "correct_index": 0,
        "explanation": "No break after case 1, so execution falls through into case 2 and prints B too.",
        "level": "APPLY",
        "difficulty": 2,
        "skill": "switch-statements",
    },
    {
        "prompt": "int x = 10, y = 20; int max = x > y ? x : y; What is max?",
        "options": ["20", "10", "true", "the ternary is a syntax error here"],
        "correct_index": 0,
        "explanation": "x > y is false, so the ternary yields the false branch, y = 20.",
        "level": "APPLY",
        "difficulty": 2,
        "skill": "ternary-operator",
    },
]
CS5_LINKS = [
    {"code": "selection-statements", "role": "teaches"},
    {"code": "ternary-operator", "role": "teaches"},
    {"code": "switch-statements", "role": "teaches"},
    {"code": "boolean-expressions", "role": "requires"},
]

# --- CS6 ---------------------------------------------------------------

CS6_OBJECTIVES = [
    "Explain why loops eliminate copy-pasted statements.",
    "Choose for, while or do-while for a given problem.",
    "Write for (init; cond; update) and trace its four-step flow.",
    "Count up, count down and step by custom amounts.",
    "Recognise infinite loops and the empty for (;;) form.",
    "Implement cumulative sum and product, and a factorial program.",
]
CS6_PREREQUISITES = [
    "CS5: conditions and selection.",
]
CS6_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "Repetition is the point of a computer: the for loop runs a block "
            "a fixed number of times using a counter variable. The classic "
            "companion is the cumulative algorithm — keep one variable that "
            "grows inside the loop — which powers sums, products and factorial."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "The for loop",
        "body": (
            "for (init; condition; update) { body }\n"
            "Execution order: 1) init  2) condition (loop while true)\n"
            "                  3) body  4) update → back to 2.\n"
            "for (int i = 1; i <= 10; i++) { ... }  // count up\n"
            "for (int i = 10; i >= 1; i--) { ... }  // count down\n"
            "for (int i = 0; i <= 100; i += 10) { ... } // step 10"
        ),
        "metadata": {
            "meaning": "A compact counted loop: initialise, test, run, update.",
            "when_used": "Known iteration counts: ranges, arrays, tables.",
        },
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example — cumulative sum 1..N",
        "body": (
            "int sum = 0;            // accumulator starts at 0\n"
            "for (int i = 1; i <= N; i++) {\n"
            "    sum = sum + i;      // or sum += i\n"
            "}\n"
            "The variable i only exists inside the loop; sum must be declared "
            "outside so it survives."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example — factorial N!",
        "body": (
            "int product = 1;        // accumulator starts at 1\n"
            "for (int i = 1; i <= N; i++) {\n"
            "    product = product * i;\n"
            "}\n"
            "For N = 5: 1×1×2×3×4×5 = 120. Start at 1, never 0 — multiplying "
            "by 0 would zero the product."
        ),
    },
    {
        "section_type": "WARNING",
        "title": "Infinite loops",
        "body": (
            "for (int i = 0; i <= 10; i--) ...  never ends: i drops away from "
            "10. If the condition can never turn false the loop runs forever "
            "(or until you interrupt it). for (;;) is the deliberate infinite "
            "form."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "i++ inside the body is a different animal",
        "body": (
            "Incrementing the counter in the loop body as well as the header "
            "changes the iteration count (usually doubling it). Keep the "
            "update in the header only, unless the problem demands a "
            "middle-modified loop."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Summary",
        "body": (
            "for centralises init/condition/update. Accumulators live outside "
            "the loop (0 for sums, 1 for products), and the counter is local "
            "to the loop."
        ),
    },
]
CS6_PRACTICE = [
    {
        "prompt": "How many times does this loop run its body?\nfor (int i = 10; i >= 1; i--)",
        "options": ["10", "9", "11", "infinite"],
        "correct_index": 0,
        "explanation": "i takes 10 down to 1 inclusive — exactly ten iterations.",
        "level": "APPLY",
        "difficulty": 1,
        "skill": "for-loops",
    },
    {
        "prompt": "To compute the sum 1+2+...+50, the accumulator must be:",
        "options": [
            "Declared outside the loop and initialised to 0",
            "Declared inside the loop body each iteration",
            "Initialised to 1",
            "A for-loop counter itself",
        ],
        "correct_index": 0,
        "explanation": "sum += i must persist across iterations; inside the loop it would reset to 0 every pass.",
        "level": "APPLY",
        "difficulty": 2,
        "skill": "cumulative-algorithms",
    },
    {
        "prompt": "5! (factorial) evaluates to:",
        "options": ["120", "15", "20", "125"],
        "correct_index": 0,
        "explanation": "5! = 1×2×3×4×5 = 120.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "cumulative-algorithms",
    },
    {
        "prompt": "The loop for (int i = 0; i <= 10; i--) will:",
        "options": [
            "Run forever (infinite loop)",
            "Run 10 times",
            "Run 11 times",
            "Fail to compile",
        ],
        "correct_index": 0,
        "explanation": "Counting down keeps i further from 10 each pass, so the condition never fails.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "for-loops",
    },
]
CS6_LINKS = [
    {"code": "for-loops", "role": "teaches"},
    {"code": "cumulative-algorithms", "role": "teaches"},
    {"code": "selection-statements", "role": "requires"},
]

# --- CS7 ---------------------------------------------------------------

CS7_OBJECTIVES = [
    "Describe the while and do-while loops and contrast pre-test vs post-test.",
    "Trace nested loops and the outer/inner counter relationship.",
    "Produce and escape from infinite loops.",
    "Declare, instantiate and initialise an array with common syntaxes.",
    "Traverse an array with a for loop and a.length.",
    "Read array values from the user and print them back.",
]
CS7_PREREQUISITES = [
    "CS6: for loops and cumulative algorithms.",
]
CS7_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "for counts known iterations; while keeps going while a condition "
            "holds (unknown count); do-while guarantees at least one run. "
            "Nested loops iterate a grid: the outer counter controls the rows, "
            "the inner the columns. Arrays give a single named collection of "
            "values accessible by index."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Loop forms and array creation",
        "body": (
            "while (condition) { body }          // pre-test\n"
            "do { body } while (condition);      // post-test, runs ≥ 1 time\n"
            "int[] a = new int[5];               // all zeros\n"
            "int[] b = {3, 7, 1};                // literal initialisation\n"
            "int[] c = new int[]{2, 4};          // anonymous form\n"
            "a.length → 5 (property, not a method!)"
        ),
        "metadata": {
            "meaning": "while = unknown repetition; do-while = at least once; arrays hold many values under one name.",
            "when_used": "Input validation, processing collections, tables and grids.",
        },
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example — array sum and input",
        "body": (
            "int[] a = new int[5];\n"
            "Scanner scan = new Scanner(System.in);\n"
            "for (int i = 0; i < a.length; i++) {\n"
            "    System.out.print(\"a[\" + i + \"]? \");\n"
            "    a[i] = scan.nextInt();\n"
            "}\n"
            "int sum = 0;\n"
            "for (int i = 0; i < a.length; i++) sum += a[i];\n"
            "System.out.println(\"sum = \" + sum);"
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example — nested loop grid",
        "body": (
            "for (int row = 1; row <= 3; row++) {\n"
            "    for (int col = 1; col <= row; col++) {\n"
            "        System.out.print(\"*\");\n"
            "    }\n"
            "    System.out.println();\n"
            "}\n"
            "Prints a right triangle: row controls col's upper bound."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "while vs do-while decision",
        "body": (
            "Pre-test (for/while): condition checked before the body — runs "
            "zero or more times. Post-test (do-while): body runs once before "
            "the condition — at least one iteration. Use do-while when the "
            "body must always execute at least once, e.g. validating a menu "
            "choice."
        ),
    },
    {
        "section_type": "WARNING",
        "title": "length is a property, not a method",
        "body": (
            "a.length has no parentheses — that is the array's field. "
            "s.length() has parentheses because String.length is a method. "
            "Writing a.length() is a compile error."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Summary",
        "body": (
            "while and do-while cover unknown repetition, nested loops draw "
            "grids, and arrays pair a fixed size (a.length) with index-based "
            "access from 0."
        ),
    },
]
CS7_PRACTICE = [
    {
        "prompt": "The main difference between while and do-while is:",
        "options": [
            "do-while runs its body at least once; while may run zero times",
            "while runs at least once; do-while may run zero times",
            "do-while needs a counter variable",
            "there is no difference",
        ],
        "correct_index": 0,
        "explanation": "do-while is post-test: the body executes before the condition is first checked.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "while-loops",
    },
    {
        "prompt": "int[] a = {5, 9, 2}; a.length equals:",
        "options": ["3", "4", "2", "error — length is a method"],
        "correct_index": 0,
        "explanation": "The literal has three elements, so length is 3.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "array-basics",
    },
    {
        "prompt": "Which loop form runs at least once by construction?",
        "options": ["do { } while (...)", "for (...)", "while (...)", "a nested for"],
        "correct_index": 0,
        "explanation": "do-while checks the condition after the body, guaranteeing one execution.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "while-loops",
    },
    {
        "prompt": "After int[] a = new int[4]; each element of a holds:",
        "options": ["0", "null", "undefined", "an empty array"],
        "correct_index": 0,
        "explanation": "Numeric arrays are zero-initialised (0 for int, 0.0 for double).",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "array-basics",
    },
]
CS7_LINKS = [
    {"code": "while-loops", "role": "teaches"},
    {"code": "array-basics", "role": "teaches"},
    {"code": "for-loops", "role": "requires"},
]

# --- CS8 ---------------------------------------------------------------

CS8_OBJECTIVES = [
    "Declare, read and inspect Strings with the core methods.",
    "Define a palindrome and check one by inspection.",
    "Implement the two-pointer palindrome algorithm and trace it.",
    "Traverse arrays, find a minimum, copy arrays and sum them.",
]
CS8_PREREQUISITES = [
    "CS7: arrays and loops.",
    "CS3: String methods.",
]
CS8_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "Strings are sequences of characters indexed from 0; the classic "
            "first algorithm is palindrome detection — reading a word with "
            "two pointers, one from each end. Arrays begin to earn their "
            "keep when you search, copy and reduce them."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Two-pointer palindrome",
        "body": (
            "int LP = 0, RP = s.length() - 1;\n"
            "while (LP < RP) {\n"
            "    if (s.charAt(LP) != s.charAt(RP)) return false;\n"
            "    LP++; RP--;\n"
            "}\n"
            "return true;\n"
            "For the 5-letter word m a d a m: LP 0↔RP 4, 1↔3, then 2↔2."
        ),
        "metadata": {
            "meaning": "Move one pointer from the left and one from the right; if they ever disagree, it is not a palindrome.",
            "when_used": "Any symmetric-sequence test, also arrays.",
        },
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example — array min and copy",
        "body": (
            "int min = arr[0];                 // candidate starts at first element\n"
            "for (int i = 1; i < arr.length; i++)\n"
            "    if (arr[i] < min) min = arr[i];\n"
            "\n"
            "int[] copy = new int[arr.length];\n"
            "for (int i = 0; i < arr.length; i++)\n"
            "    copy[i] = arr[i];             // element-by-element copy"
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "Indices run 0..length()-1",
        "body": (
            "charAt(0) is the first character, charAt(s.length()-1) the last. "
            "charAt(i) for i = s.length() throws "
            "StringIndexOutOfBoundsException — off-by-one is the most common "
            "palindrome bug."
        ),
    },
    {
        "section_type": "WARNING",
        "title": "Assignment copies references, not arrays",
        "body": (
            "int[] b = a; does NOT copy the array — both names point at the "
            "same cells. To copy, traverse element by element. Aliasing means "
            "changing b[0] changes a[0] too."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Summary",
        "body": (
            "Strings and arrays are indexed from 0. Palindrome is a two-pointer "
            "symmetric scan; min/max reduce arrays with an accumulator; copying "
            "arrays requires element-by-element traversal."
        ),
    },
]
CS8_PRACTICE = [
    {
        "prompt": "In the two-pointer palindrome test, when do the pointers first cross?",
        "options": [
            "When they meet or pass in the middle of the word",
            "When the word has an even length only",
            "At index 0",
            "Only if the word is a palindrome",
        ],
        "correct_index": 0,
        "explanation": "LP climbs while RP descends; the scan stops when LP >= RP, i.e. they meet or cross in the middle.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "palindrome",
    },
    {
        "prompt": "int[] a = {{4, 1, 8}}; what does the loop if (a[i] < min) min = a[i]; compute when min starts at a[0]?",
        "options": ["The minimum 1", "The maximum 8", "The sum 13", "The length 3"],
        "correct_index": 0,
        "explanation": "The accumulator pattern updates min whenever a smaller value is found: 4→1 is the only improvement.",
        "level": "APPLY",
        "difficulty": 2,
        "skill": "array-operations",
    },
    {
        "prompt": "Which statement truly duplicates an array a into array b?",
        "options": [
            "for (int i=0; i<a.length; i++) b[i] = a[i];",
            "int[] b = a;",
            "b = a.clone(a);",
            "a.copyTo(b);",
        ],
        "correct_index": 0,
        "explanation": "Each element must be copied individually; b = a only aliases the same array.",
        "level": "APPLY",
        "difficulty": 2,
        "skill": "array-operations",
    },
]
CS8_LINKS = [
    {"code": "palindrome", "role": "teaches"},
    {"code": "array-operations", "role": "teaches"},
    {"code": "string-methods", "role": "requires"},
    {"code": "array-basics", "role": "requires"},
]

# --- CS9 ---------------------------------------------------------------

CS9_OBJECTIVES = [
    "Reverse an array in place with the two-pointer swap.",
    "Implement linear search returning an index or a not-found indicator.",
    "Find the maximum and its position, and build a filtered array.",
    "Declare and traverse 2D arrays; distinguish arr.length from arr[i].length.",
    "Explain jagged arrays and avoid the two classic exceptions.",
    "Declare and call static methods with zero, one or more parameters.",
]
CS9_PREREQUISITES = [
    "CS8: array traversal, min and copy.",
]
CS9_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "The array problem set collects the six reusable techniques: "
            "reverse, linear search, find max (+ position), build a new array "
            "of squares, sum, and filter by a predicate. Two-dimensional "
            "arrays are arrays of arrays — arr.length is the rows, "
            "arr[i].length the columns of row i."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "In-place reverse with two pointers",
        "body": (
            "int i = 0, j = a.length - 1;\n"
            "while (i < j) {\n"
            "    int t = a[i]; a[i] = a[j]; a[j] = t;  // swap\n"
            "    i++; j--;\n"
            "}\n"
            "Linear search:\n"
            "for (int i = 0; i < a.length; i++)\n"
            "    if (a[i] == target) return i;\n"
            "return -1;   // not found"
        ),
        "metadata": {
            "meaning": "Swap outer pairs inward for reverse; scan-and-return for search.",
            "when_used": "Any order-reversal or membership test.",
        },
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example — squares array and filter",
        "body": (
            "int[] squares = new int[a.length];\n"
            "for (int i = 0; i < a.length; i++)\n"
            "    squares[i] = a[i] * a[i];\n"
            "\n"
            "int count = 0;\n"
            "for (int v : a) if (v % 2 == 0) count++;\n"
            "int[] evens = new int[count];\n"
            "int k = 0;\n"
            "for (int i = 0; i < a.length; i++)\n"
            "    if (a[i] % 2 == 0) evens[k++] = a[i];"
        ),
    },
    {
        "section_type": "TABLE",
        "title": "2D arrays: rows and columns",
        "body": (
            "int[][] g = new int[3][4];       // 3 rows, 4 columns, all 0\n"
            "g.length     → 3 (rows)\n"
            "g[i].length  → 4 (columns of row i)\n"
            "int[][] h = {{1,2},{3,4,5}};     // ragged rows are allowed\n"
            "new int[6][] then allocate each row separately (jagged)."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "The two exceptions to fear",
        "body": (
            "ArrayIndexOutOfBoundsException: an index outside 0..length-1. "
            "NullPointerException: touching arr[i] on a row that was never "
            "allocated (new int[6][] then arr[0] is null). Count rows first, "
            "then allocate."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example — static method basics",
        "body": (
            "public static int maxOf(int a, int b) {   // value-returning\n"
            "    return (a > b) ? a : b;\n"
            "}\n"
            "public static void printBanner() {        // void, no parameters\n"
            "    System.out.println(\"=====\");\n"
            "}\n"
            "Call: int m = maxOf(3, 7) + 1;  // m = 8 — calls nest in expressions."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Summary",
        "body": (
            "Reverse/search/max/filter cover most one-dimensional problems; "
            "2D arrays need explicit row and column counts; static methods "
            "package reusable behaviour with parameters in and return values out."
        ),
    },
]
CS9_PRACTICE = [
    {
        "prompt": "For int[][] g = new int[3][4]; g[0].length is:",
        "options": ["4", "3", "12", "error"],
        "correct_index": 0,
        "explanation": "g[0] is a row array of width 4 — columns of the first row.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "2d-arrays",
    },
    {
        "prompt": "Linear search returns -1 when:",
        "options": [
            "the target is not in the array",
            "the target is in the array",
            "the array is empty but target exists",
            "the array is initialised",
        ],
        "correct_index": 0,
        "explanation": "-1 is the conventional 'not found' indicator, since indices are 0-based.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "array-operations",
    },
    {
        "prompt": "Which code reverses array a in place?",
        "options": [
            "Two-pointer swap: while (i < j) { swap a[i], a[j]; i++; j--; }",
            "int[] b = a;",
            "for (int i = 0; i < a.length; i++) a[i] = a[i];",
            "Collections.reverse(a);",
        ],
        "correct_index": 0,
        "explanation": "Swapping the i and j pairs inward rewrites the same array; the other options do nothing or fail.",
        "level": "APPLY",
        "difficulty": 2,
        "skill": "array-operations",
    },
    {
        "prompt": "What exactly causes a NullPointerException in new int[6][]?",
        "options": [
            "Accessing a row before it has been allocated its own array",
            "Reading an index past length - 1",
            "Declaring a 2D array with two sizes",
            "Printing the array with a for loop",
        ],
        "correct_index": 0,
        "explanation": "Only the outer array is created; each row is null until you allocate it.",
        "level": "UNDERSTAND",
        "difficulty": 2,
        "skill": "2d-arrays",
    },
]
CS9_LINKS = [
    {"code": "array-operations", "role": "teaches"},
    {"code": "2d-arrays", "role": "teaches"},
    {"code": "methods-intro", "role": "teaches"},
    {"code": "array-basics", "role": "requires"},
]

# --- CS10 --------------------------------------------------------------

CS10_OBJECTIVES = [
    "Identify the four parts of a method declaration.",
    "Distinguish void from value-returning methods.",
    "Explain positional argument binding and predict the Parameter Mystery.",
    "Declare array parameters and call methods without [] at the call site.",
    "Use a method call inside a larger expression.",
    "Return an array from a method.",
]
CS10_PREREQUISITES = [
    "CS9: methods-intro and 2D arrays.",
]
CS10_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "A static method is a named, reusable block with a contract: "
            "parameters are the information in, the return value the "
            "information out. Arguments bind to parameters positionally — the "
            "first argument lands in the first parameter regardless of the "
            "names. Arrays are perfectly good parameters and return values."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Method anatomy",
        "body": (
            "public static <returnType> name(<params>) { body }\n"
            "void method:  performs work, returns nothing.\n"
            "value method: returns one value with return expr;\n"
            "Example:\n"
            "public static int max(int a, int b) {\n"
            "    return a > b ? a : b;\n"
            "}\n"
            "Call: int k = max(i, j) + 1;"
        ),
        "metadata": {
            "meaning": "Return type, name, parameter list, and body are the four parts.",
            "when_used": "Every reusable computation or side-effect.",
        },
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example — arrays as parameters",
        "body": (
            "public static void printAll(int[] a) {\n"
            "    for (int i = 0; i < a.length; i++)\n"
            "        System.out.print(a[i] + \" \");\n"
            "}\n"
            "public static int average(int[] a) {\n"
            "    int sum = 0;\n"
            "    for (int i = 0; i < a.length; i++) sum += a[i];\n"
            "    return sum / a.length;\n"
            "}\n"
            "Call site: printAll(values);   // no [] on the argument"
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example — returning an array (stutter)",
        "body": (
            "public static int[] stutter(int[] a) {\n"
            "    int[] out = new int[a.length * 2];\n"
            "    for (int i = 0; i < a.length; i++) {\n"
            "        out[2*i]     = a[i];\n"
            "        out[2*i + 1] = a[i];\n"
            "    }\n"
            "    return out;\n"
            "}"
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "Parameters in, return out — the one-way street",
        "body": (
            "Parameters move data into a method; return moves one value out. "
            "There is no other channel: if a method must affect several "
            "caller variables, it either returns an array/object or the "
            "caller re-assigns the result. (Arrays are the big exception, "
            "because Java passes object references — Lecture 12.)"
        ),
    },
    {
        "section_type": "WARNING",
        "title": "Parameter binding ignores names",
        "body": (
            "public static void f(int x, int y) called as f(p, q) sends p "
            "into x and q into y — order, not name, decides. The "
            "Parameter Mystery problem exists precisely to catch students "
            "who name-match instead of position-match."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Summary",
        "body": (
            "Methods = returnType + name + parameters + body. Arguments bind "
            "by position. Arrays are legal parameters (no [] at call site) "
            "and legal return values (allocate, fill, return)."
        ),
    },
]
CS10_PRACTICE = [
    {
        "prompt": "public static void f(int a, int b) ... called as f(x, y). Which pairing is correct?",
        "options": [
            "a receives x, b receives y (positional)",
            "a receives y, b receives x (by name)",
            "a and b receive copies of both x and y",
            "the call is illegal",
        ],
        "correct_index": 0,
        "explanation": "Arguments bind to parameters positionally: first argument → first parameter.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "method-parameters",
    },
    {
        "prompt": "A void method is one that:",
        "options": [
            "returns no value",
            "returns an int",
            "cannot take parameters",
            "must be static",
        ],
        "correct_index": 0,
        "explanation": "void means 'no return value' — the method performs work only.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "method-anatomy",
    },
    {
        "prompt": "Which call site matches public static int[] squares(int[] a)?",
        "options": [
            "int[] r = squares(values);",
            "int[] r = squares(values[]);",
            "squares(values[])",
            "int[] r = squares();",
        ],
        "correct_index": 0,
        "explanation": "The array argument is passed by name only; no [] at the call site.",
        "level": "APPLY",
        "difficulty": 2,
        "skill": "array-parameters",
    },
    {
        "prompt": "In the Parameter Mystery pattern, the trap is that students:",
        "options": [
            "match arguments to parameters by name rather than position",
            "forget to add the return keyword",
            "declare parameters inside the body",
            "call the method twice",
        ],
        "correct_index": 0,
        "explanation": "Names are irrelevant to binding — only the order matters, and name-matching misleads.",
        "level": "UNDERSTAND",
        "difficulty": 2,
        "skill": "method-parameters",
    },
]
CS10_LINKS = [
    {"code": "method-anatomy", "role": "teaches"},
    {"code": "method-parameters", "role": "teaches"},
    {"code": "array-parameters", "role": "teaches"},
    {"code": "methods-intro", "role": "requires"},
]

# --- CS11 --------------------------------------------------------------

CS11_OBJECTIVES = [
    "Explain pass-by-value and why swap(int a, int b) cannot swap primitives.",
    "Explain why method changes to an array parameter are visible to the caller.",
    "Recognise and avoid unintended array aliasing.",
    "Use Arrays.toString to print arrays.",
    "Implement matrix addition, diagonal extraction and array merge.",
]
CS11_PREREQUISITES = [
    "CS10: method anatomy and array parameters.",
]
CS11_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "Java is always pass-by-value: a method receives a copy of each "
            "argument. For primitives that copy means the original can never "
            "change. For arrays the 'value' copied is the reference — a "
            "pointer to the same array — so modifying elements inside a "
            "method is visible to the caller. The reference is copied, the "
            "object is shared."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "The reference rule",
        "body": (
            "Primitive argument:  copy of the value  → original never changes\n"
            "Array argument:       copy of the reference → same cells, changes "
            "visible\n"
            "b = a;  aliases: both names point at the one array.\n"
            "Arrays.toString(a)  prints [1, 2, 3] instead of a memory address."
        ),
        "metadata": {
            "meaning": "Copies of values for primitives, copies of references for objects.",
            "when_used": "Predicting whether a method call mutates the caller's data.",
        },
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example — why swap fails",
        "body": (
            "public static void swap(int a, int b) {\n"
            "    int tmp = a; a = b; b = tmp;   // swaps the copies only\n"
            "}\n"
            "int x = 3, y = 7; swap(x, y);      // x still 3, y still 7\n"
            "Because a and b are local copies, the caller's x and y are never touched."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example — matrix addition",
        "body": (
            "public static int[][] add(int[][] a, int[][] b) {\n"
            "    int rows = a.length, cols = a[0].length;\n"
            "    int[][] c = new int[rows][cols];\n"
            "    for (int r = 0; r < rows; r++)\n"
            "        for (int col = 0; col < cols; col++)\n"
            "            c[r][col] = a[r][col] + b[r][col];\n"
            "    return c;\n"
            "}"
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example — array merge",
        "body": (
            "public static int[] merge(int[] a, int[] b) {\n"
            "    int[] out = new int[a.length + b.length];\n"
            "    for (int i = 0; i < a.length; i++) out[i] = a[i];\n"
            "    for (int i = 0; i < b.length; i++) out[a.length + i] = b[i];\n"
            "    return out;\n"
            "}"
        ),
    },
    {
        "section_type": "WARNING",
        "title": "Aliasing is silent",
        "body": (
            "int[] b = a; is not a copy — it is a second name for the same "
            "array. Mutating through either name mutates the single shared "
            "object. If you need a true copy, allocate and fill."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Summary",
        "body": (
            "Java passes values; for arrays the value is a shared reference. "
            "Primitives can never be swapped by a method; array element "
            "changes persist. Guard against aliasing and print with "
            "Arrays.toString."
        ),
    },
]
CS11_PRACTICE = [
    {
        "prompt": "public static void swap(int a, int b) called with swap(x, y) leaves x and y:",
        "options": [
            "Unchanged — the method swaps local copies",
            "Swapped — Java passes by reference",
            "Unchanged only for even values",
            "Undefined",
        ],
        "correct_index": 0,
        "explanation": "Primitives are passed by value; x and y never enter the method.",
        "level": "APPLY",
        "difficulty": 2,
        "skill": "pass-by-value",
    },
    {
        "prompt": "A method sets arr[0] = 99 inside; the caller's array afterwards:",
        "options": [
            "shows 99 — the method shares the same array via the copied reference",
            "stays unchanged — arr was a copy",
            "crashes with a null pointer",
            "becomes length 0",
        ],
        "correct_index": 0,
        "explanation": "The reference is copied but the array is shared, so element writes persist.",
        "level": "APPLY",
        "difficulty": 2,
        "skill": "reference-semantics",
    },
    {
        "prompt": "int[] b = a; — what does this actually do?",
        "options": [
            "Makes b a second name for the same array (aliasing)",
            "Copies every element from a into a new array b",
            "Collapses a into a single element",
            "It is a compile error",
        ],
        "correct_index": 0,
        "explanation": "A lone array assignment copies the reference, not the contents.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "reference-semantics",
    },
    {
        "prompt": "Which call nicely turns array a into readable text?",
        "options": [
            "Arrays.toString(a)",
            "add(a)",
            "a.toStringValues()",
            "printf(\"%d\", a)",
        ],
        "correct_index": 0,
        "explanation": "Arrays.toString prints the formatted contents; plain a.toString would print a memory address.",
        "level": "APPLY",
        "difficulty": 1,
        "skill": "reference-semantics",
    },
]
CS11_LINKS = [
    {"code": "pass-by-value", "role": "teaches"},
    {"code": "reference-semantics", "role": "teaches"},
    {"code": "array-parameters", "role": "requires"},
]

# --- CS12 --------------------------------------------------------------

CS12_OBJECTIVES = [
    "Define recursion and identify its two essential parts.",
    "Explain why a base case is mandatory.",
    "Trace factorial(4) through the call stack.",
    "Return arrays from methods and apply matrix/diagonal/merge patterns.",
]
CS12_PREREQUISITES = [
    "CS11: reference semantics and methods returning arrays.",
]
CS12_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "Recursion is a method that calls itself. Every recursive method "
            "needs two things: a base case that stops the calls, and a "
            "recursive call that moves toward that base. The runtime tracks "
            "pending calls on the call stack; trace a small case on paper "
            "before trusting it."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Recursive factorial",
        "body": (
            "public static int factorial(int n) {\n"
            "    if (n == 0) return 1;           // base case\n"
            "    return n * factorial(n - 1);    // recursive case\n"
            "}\n"
            "Trace factorial(4): 4→3→2→1→0 hits the base case,\n"
            "then unwinds 1·2·3·4 = 24."
        ),
        "metadata": {
            "meaning": "n! = n · (n-1)! with 0! = 1 as the anchor.",
            "when_used": "Problems whose solution contains a smaller instance of itself.",
        },
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example — call-stack trace of factorial(4)",
        "body": (
            "factorial(4) = 4 × factorial(3)\n"
            "                     factorial(3) = 3 × factorial(2)\n"
            "                                          factorial(2) = 2 × factorial(1)\n"
            "                                                               factorial(1) = 1 × factorial(0)\n"
            "                                                                                    factorial(0) = 1\n"
            "Unwind: 1 → 1 → 2 → 6 → 24."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example — diagonal of a matrix",
        "body": (
            "public static int[] diagonal(int[][] m) {\n"
            "    int n = Math.min(m.length, m[0].length);\n"
            "    int[] d = new int[n];\n"
            "    for (int i = 0; i < n; i++) d[i] = m[i][i];\n"
            "    return d;\n"
            "}"
        ),
    },
    {
        "section_type": "WARNING",
        "title": "No base case = stack overflow",
        "body": (
            "A recursive call that never reaches the anchor keeps pushing "
            "frames until the stack overflows (StackOverflowError). Every "
            "recursive call must make progress: n-1, a smaller slice, "
            "half the array — something strictly smaller."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "Match recursion to the shape",
        "body": (
            "Use recursion when the problem is naturally self-similar "
            "(factorial, Fibonacci, tree/nested structures). For linear tasks "
            "with explicit counters (summing an array forwards) an iterative "
            "loop is usually clearer. Recognise both and choose per problem."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Summary",
        "body": (
            "Recursion = base case + a recursive call that shrinks the "
            "problem. The stack unwinds in reverse order. Arrays can be "
            "returned from methods, and matrix diagonal/merge patterns "
            "combine indexing with accumulation."
        ),
    },
]
CS12_PRACTICE = [
    {
        "prompt": "The two essential parts of every recursive method are:",
        "options": [
            "A base case and a recursive call that moves toward it",
            "A for loop and a while loop",
            "A static keyword and a void return",
            "A parameter and a local variable",
        ],
        "correct_index": 0,
        "explanation": "Without a base case there is no stopping rule; without progress toward it the base is never reached.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "recursion",
    },
    {
        "prompt": "factorial(0) equals:",
        "options": ["1", "0", "undefined", "−1"],
        "correct_index": 0,
        "explanation": "0! = 1 by definition — it is the base case of the recursive factorial.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "recursion",
    },
    {
        "prompt": "factorial(5) evaluates to:",
        "options": ["120", "125", "25", "15"],
        "correct_index": 0,
        "explanation": "5! = 5 × 4! = 5 × 24 = 120.",
        "level": "APPLY",
        "difficulty": 1,
        "skill": "recursion",
    },
    {
        "prompt": "A method that calls itself with the same argument every time will:",
        "options": [
            "never reach a base case and overflow the stack",
            "work correctly but slowly",
            "return immediately",
            "compile-fail",
        ],
        "correct_index": 0,
        "explanation": "No progress means the base case is never hit and the stack overflows.",
        "level": "APPLY",
        "difficulty": 2,
        "skill": "recursion",
    },
]
CS12_LINKS = [
    {"code": "recursion", "role": "teaches"},
    {"code": "pass-by-value", "role": "requires"},
    {"code": "reference-semantics", "role": "requires"},
]


def _bundle(
    *,
    module: dict,
    lesson: dict,
    contents: list,
    practice: list,
    links: list,
    competency_codes: list,
) -> dict:
    """Build one importer bundle (course + module + lesson) with a shared course shell."""
    return {
        "course": {
            "code": COURSE_CODE,
            "title": COURSE_TITLE,
            "credits": COURSE_CREDITS,
            "description": COURSE_DESCRIPTION,
            "department_code": DEPARTMENT_CODE,
            "department_name": DEPARTMENT_NAME,
            "faculty_code": FACULTY_CODE,
            "faculty_name": FACULTY_NAME,
            "module": module,
            "lesson": lesson,
            "lesson_contents": contents,
            "summary_contents": [
                {
                    "section_type": "SUMMARY",
                    "title": "Lesson review",
                    "body": next(
                        (s["body"] for s in contents if s["section_type"] == "SUMMARY"),
                        "",
                    ),
                }
            ],
            "resources": [],
            "competencies": [
                {
                    "code": code,
                    "title": _COMPETENCY_TITLES[code],
                    "description": _COMPETENCY_DESCRIPTIONS[code],
                    "taxonomy_level": _COMPETENCY_LEVELS[code],
                }
                for code in competency_codes
            ],
            "competency_prerequisites": [
                (pre, post)
                for pre, post in [
                    ("java-program-anatomy", "arithmetic-operators"),
                    ("arithmetic-operators", "compound-operators"),
                    ("compound-operators", "string-methods"),
                    ("string-methods", "scanner-input"),
                    ("arithmetic-operators", "math-library"),
                    ("math-library", "casting"),
                    ("boolean-expressions", "selection-statements"),
                    ("selection-statements", "for-loops"),
                    ("for-loops", "while-loops"),
                    ("while-loops", "array-basics"),
                    ("array-basics", "array-operations"),
                    ("array-operations", "2d-arrays"),
                    ("array-basics", "methods-intro"),
                    ("methods-intro", "method-anatomy"),
                    ("method-anatomy", "method-parameters"),
                    ("array-parameters", "reference-semantics"),
                    ("method-parameters", "recursion"),
                ]
                if pre in competency_codes and post in competency_codes
            ],
            "lesson_competencies": links,
            "practice_items": [
                {
                    **item,
                    "competency_code": item.get("competency_code")
                    or (item.get("skill") if item.get("skill") in competency_codes else None),
                }
                for item in practice
            ],
        }
    }


_COMPETENCY_TITLES = {
    "java-program-anatomy": "Anatomy of a Java program and the JDK/JRE/JVM stack",
    "escape-sequences": "Output with System.out and escape sequences",
    "compilation-pipeline": "Compile/run pipeline from source to bytecode",
    "arithmetic-operators": "Arithmetic operators, precedence and types",
    "compound-operators": "Compound assignment and increment operators",
    "string-methods": "String immutability and core methods",
    "scanner-input": "Console input with the Scanner class",
    "math-library": "The Math library and random integers",
    "casting": "Numeric type casting and truncation",
    "boolean-expressions": "Relational and Boolean expressions",
    "selection-statements": "Selection with if, if-else and ladders",
    "ternary-operator": "The ternary conditional operator",
    "switch-statements": "Switch statements and fall-through",
    "for-loops": "Counted repetition with the for loop",
    "cumulative-algorithms": "Cumulative sum, product and factorial",
    "while-loops": "while and do-while loops and nesting",
    "array-basics": "Array declaration, initialisation and traversal",
    "palindrome": "Two-pointer palindrome detection",
    "array-operations": "Array reverse, search, max, sum and filtering",
    "2d-arrays": "Two-dimensional and ragged arrays",
    "methods-intro": "Declaring and calling static methods",
    "method-anatomy": "Method declaration anatomy and return types",
    "method-parameters": "Positional parameter binding",
    "array-parameters": "Arrays as method parameters and return values",
    "pass-by-value": "Pass-by-value for primitives",
    "reference-semantics": "Reference semantics, aliasing and Arrays.toString",
    "recursion": "Recursion with base cases and the call stack",
}

_COMPETENCY_DESCRIPTIONS = {
    "java-program-anatomy": "Identify class/main structure and the JVM/JRE/JDK relationship.",
    "escape-sequences": "Predict and produce output using println and the four escapes.",
    "compilation-pipeline": "Compile, run and reason about Java's two-stage execution.",
    "arithmetic-operators": "Evaluate arithmetic expressions with correct precedence and type rules.",
    "compound-operators": "Use +=, -=, *=, /= and prefix/postfix increments correctly.",
    "string-methods": "Apply length, charAt, indexOf, substring and case conversions to immutable Strings.",
    "scanner-input": "Read typed console input and handle token pitfalls.",
    "math-library": "Apply Math methods, constants and range-shifted randomness.",
    "casting": "Cast between numeric types and control division and rounding.",
    "boolean-expressions": "Combine relational tests with !, && and ||; split ranges.",
    "selection-statements": "Write guarded, two-way and cascading selection.",
    "ternary-operator": "Choose between two values inside an expression.",
    "switch-statements": "Route on exact equality with break and fall-through awareness.",
    "for-loops": "Write and trace counted loops with correct header semantics.",
    "cumulative-algorithms": "Implement accumulators for sums, products and factorial.",
    "while-loops": "Choose and trace pre-test vs post-test loops and nesting.",
    "array-basics": "Declare, initialise and traverse one-dimensional arrays.",
    "palindrome": "Detect palindromes with the two-pointer algorithm.",
    "array-operations": "Apply reverse, search, min/max and filter patterns.",
    "2d-arrays": "Declare and traverse rectangular and jagged 2D arrays.",
    "methods-intro": "Declare and call static void and value-returning methods.",
    "method-anatomy": "Read and write the four parts of a method declaration.",
    "method-parameters": "Bind arguments positionally and use calls in expressions.",
    "array-parameters": "Pass and return arrays through method boundaries.",
    "pass-by-value": "Predict primitive behaviour under mutation attempts.",
    "reference-semantics": "Predict shared-mutation effects and avoid aliasing.",
    "recursion": "Write recursive methods with guaranteed base-case progress.",
}

_COMPETENCY_LEVELS = {
    "java-program-anatomy": "understand",
    "escape-sequences": "apply",
    "compilation-pipeline": "understand",
    "arithmetic-operators": "apply",
    "compound-operators": "apply",
    "string-methods": "apply",
    "scanner-input": "apply",
    "math-library": "apply",
    "casting": "apply",
    "boolean-expressions": "apply",
    "selection-statements": "apply",
    "ternary-operator": "apply",
    "switch-statements": "apply",
    "for-loops": "apply",
    "cumulative-algorithms": "apply",
    "while-loops": "apply",
    "array-basics": "apply",
    "palindrome": "apply",
    "array-operations": "apply",
    "2d-arrays": "apply",
    "methods-intro": "understand",
    "method-anatomy": "understand",
    "method-parameters": "apply",
    "array-parameters": "apply",
    "pass-by-value": "understand",
    "reference-semantics": "apply",
    "recursion": "apply",
}


def _lesson(
    *,
    code: str,
    title: str,
    description: str,
    minutes: int,
    difficulty: str,
    objectives: list,
    prerequisites: list,
    sort_order: int,
) -> dict:
    return {
        "code": code,
        "title": title,
        "description": description,
        "estimated_minutes": minutes,
        "difficulty": difficulty,
        "objectives": objectives,
        "prerequisites": prerequisites,
        "sort_order": sort_order,
    }


BUNDLES = [
    _bundle(
        module=MODULE_GETTING_STARTED,
        lesson=_lesson(
            code="CS1",
            title="Introduction to Java: Programs, JDK/JRE/JVM and the Pipeline",
            description=(
                "Lecture 1 — what a program is, the compile/run pipeline, "
                "program anatomy and output with escape sequences."
            ),
            minutes=75,
            difficulty="beginner",
            objectives=CS1_OBJECTIVES,
            prerequisites=CS1_PREREQUISITES,
            sort_order=1,
        ),
        contents=CS1_CONTENTS,
        practice=CS1_PRACTICE,
        links=CS1_LINKS,
        competency_codes=["java-program-anatomy", "escape-sequences", "compilation-pipeline"],
    ),
    _bundle(
        module=MODULE_GETTING_STARTED,
        lesson=_lesson(
            code="CS2",
            title="Main Memory, Compilation and First Programs",
            description=(
                "Lecture 2 — volatile main memory, primitive types, arithmetic "
                "operators and the first complete variable-driven programs."
            ),
            minutes=80,
            difficulty="beginner",
            objectives=CS2_OBJECTIVES,
            prerequisites=CS2_PREREQUISITES,
            sort_order=2,
        ),
        contents=CS2_CONTENTS,
        practice=CS2_PRACTICE,
        links=CS2_LINKS,
        competency_codes=["arithmetic-operators", "java-program-anatomy"],
    ),
    _bundle(
        module=MODULE_TYPES_IO,
        lesson=_lesson(
            code="CS3",
            title="Assignment Operators, char/String and the Scanner Class",
            description=(
                "Lecture 3 — compound assignment, prefix/postfix increment, "
                "String methods and immutability, and interactive Scanner input."
            ),
            minutes=85,
            difficulty="medium",
            objectives=CS3_OBJECTIVES,
            prerequisites=CS3_PREREQUISITES,
            sort_order=1,
        ),
        contents=CS3_CONTENTS,
        practice=CS3_PRACTICE,
        links=CS3_LINKS,
        competency_codes=["compound-operators", "string-methods", "scanner-input"],
    ),
    _bundle(
        module=MODULE_TYPES_IO,
        lesson=_lesson(
            code="CS4",
            title="The Math Library, Type Casting and Boolean Operators",
            description=(
                "Lecture 4 — Math methods and constants, numeric casting and "
                "truncation, relational/Boolean logic and range conditions."
            ),
            minutes=80,
            difficulty="medium",
            objectives=CS4_OBJECTIVES,
            prerequisites=CS4_PREREQUISITES,
            sort_order=2,
        ),
        contents=CS4_CONTENTS,
        practice=CS4_PRACTICE,
        links=CS4_LINKS,
        competency_codes=["math-library", "casting", "boolean-expressions"],
    ),
    _bundle(
        module=MODULE_CONTROL,
        lesson=_lesson(
            code="CS5",
            title="Selection Statements: if, if-else, ?: and switch",
            description=(
                "Lecture 5 — guarded and two-way selection, cascading ladders, "
                "the ternary operator and switch with fall-through."
            ),
            minutes=75,
            difficulty="medium",
            objectives=CS5_OBJECTIVES,
            prerequisites=CS5_PREREQUISITES,
            sort_order=1,
        ),
        contents=CS5_CONTENTS,
        practice=CS5_PRACTICE,
        links=CS5_LINKS,
        competency_codes=["selection-statements", "ternary-operator", "switch-statements"],
    ),
    _bundle(
        module=MODULE_CONTROL,
        lesson=_lesson(
            code="CS6",
            title="The for Loop, Cumulative Sum and Factorial",
            description=(
                "Lecture 6 — counted repetition, loop traces, infinite loops "
                "and the cumulative sum/product patterns behind factorial."
            ),
            minutes=80,
            difficulty="medium",
            objectives=CS6_OBJECTIVES,
            prerequisites=CS6_PREREQUISITES,
            sort_order=2,
        ),
        contents=CS6_CONTENTS,
        practice=CS6_PRACTICE,
        links=CS6_LINKS,
        competency_codes=["for-loops", "cumulative-algorithms"],
    ),
    _bundle(
        module=MODULE_LOOPS_ARRAYS,
        lesson=_lesson(
            code="CS7",
            title="while & do-while Loops, Nested Loops and Arrays",
            description=(
                "Lecture 8 — condition-driven repetition, pre-test vs post-test, "
                "nested loops and the declaration, traversal and input of arrays."
            ),
            minutes=85,
            difficulty="medium",
            objectives=CS7_OBJECTIVES,
            prerequisites=CS7_PREREQUISITES,
            sort_order=1,
        ),
        contents=CS7_CONTENTS,
        practice=CS7_PRACTICE,
        links=CS7_LINKS,
        competency_codes=["while-loops", "array-basics"],
    ),
    _bundle(
        module=MODULE_STRINGS_ARRAYS,
        lesson=_lesson(
            code="CS8",
            title="Strings, Palindrome Detection and Array Operations",
            description=(
                "Lecture 9 — String basics, the two-pointer palindrome "
                "algorithm, and min/copy/sum patterns over arrays."
            ),
            minutes=80,
            difficulty="medium",
            objectives=CS8_OBJECTIVES,
            prerequisites=CS8_PREREQUISITES,
            sort_order=1,
        ),
        contents=CS8_CONTENTS,
        practice=CS8_PRACTICE,
        links=CS8_LINKS,
        competency_codes=["palindrome", "array-operations"],
    ),
    _bundle(
        module=MODULE_STRINGS_ARRAYS,
        lesson=_lesson(
            code="CS9",
            title="Array Operations, 2D Arrays and Static Methods",
            description=(
                "Lecture 10 — the array problem set (reverse, search, max, "
                "squares, filter), two-dimensional arrays and the first "
                "static methods."
            ),
            minutes=90,
            difficulty="hard",
            objectives=CS9_OBJECTIVES,
            prerequisites=CS9_PREREQUISITES,
            sort_order=2,
        ),
        contents=CS9_CONTENTS,
        practice=CS9_PRACTICE,
        links=CS9_LINKS,
        competency_codes=["array-operations", "2d-arrays", "methods-intro"],
    ),
    _bundle(
        module=MODULE_METHODS,
        lesson=_lesson(
            code="CS10",
            title="Methods in Depth: Parameters, Returns and Array Parameters",
            description=(
                "Lecture 11 — method anatomy, positional binding, the "
                "Parameter Mystery, arrays as parameters and returned arrays."
            ),
            minutes=85,
            difficulty="hard",
            objectives=CS10_OBJECTIVES,
            prerequisites=CS10_PREREQUISITES,
            sort_order=1,
        ),
        contents=CS10_CONTENTS,
        practice=CS10_PRACTICE,
        links=CS10_LINKS,
        competency_codes=["method-anatomy", "method-parameters", "array-parameters"],
    ),
    _bundle(
        module=MODULE_METHODS,
        lesson=_lesson(
            code="CS11",
            title="Call by Value vs Reference, Returning Arrays and Aliasing",
            description=(
                "Lecture 12 (a) — pass-by-value for primitives, shared "
                "references for arrays, aliasing traps, matrix addition and "
                "array merge."
            ),
            minutes=80,
            difficulty="hard",
            objectives=CS11_OBJECTIVES,
            prerequisites=CS11_PREREQUISITES,
            sort_order=2,
        ),
        contents=CS11_CONTENTS,
        practice=CS11_PRACTICE,
        links=CS11_LINKS,
        competency_codes=["pass-by-value", "reference-semantics"],
    ),
    _bundle(
        module=MODULE_METHODS,
        lesson=_lesson(
            code="CS12",
            title="Recursion: Base Cases, the Call Stack and Factorial",
            description=(
                "Lecture 12 (b) — recursion anatomy, mandatory base cases, a "
                "full factorial call-stack trace, and matrix diagonal patterns."
            ),
            minutes=80,
            difficulty="hard",
            objectives=CS12_OBJECTIVES,
            prerequisites=CS12_PREREQUISITES,
            sort_order=3,
        ),
        contents=CS12_CONTENTS,
        practice=CS12_PRACTICE,
        links=CS12_LINKS,
        competency_codes=["recursion"],
    ),
]