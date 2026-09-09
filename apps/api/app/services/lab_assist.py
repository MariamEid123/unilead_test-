"""In-lab programming coach (deterministic, teaching-first).

The Coach's answers are assembled from the student's own artifacts — their
question, the code currently in the editor, and any error the sandbox
reported — not from a hidden reference script. Depth is progressive
(hint → explain → deeper → solution) and the student chooses how far to go.

No internal state leaks: only the curated teaching text is ever returned.
"""

from __future__ import annotations

import re

from . import lab_content

_ERROR_TUTOR = {
    "syntaxerror": {
        "name": "syntax error",
        "explain": (
            "Python stopped before executing — the code doesn't parse as a valid program. "
            "This is the compiler's way of saying 'I cannot understand this yet'. Look at "
            "the line number in the message and check for an unclosed bracket, a missing "
            "colon at the end of an if/for/def line, a missing closing quote, or "
            "inconsistent indentation between blocks."
        ),
        "hint": "The error message points at the first place Python got confused — that is usually one or two characters away from the actual mistake.",
        "deeper": (
            "A syntax error is reported once for the whole file, and the fix is usually small: "
            "make sure every opening bracket has a partner, every string has matching quotes, "
            "every block header (if/for/while/def) ends with :, and blocks are indented with "
            "the same amount of spaces each time."
        ),
    },
    "indentationerror": {
        "name": "indentation error",
        "explain": (
            "Python uses indentation to mark blocks. An IndentationError means a line is "
            "indented inconsistently — too much, too little, or mixed tabs and spaces. "
            "Everything inside an if/for/while/def body must be indented identically."
        ),
        "hint": "Re-indent the lines: each block level adds exactly the same number of spaces (4 is the convention).",
        "deeper": (
            "Unlike C or Java, Python has no braces — the indentation IS the block structure. "
            "If a +1-space line drifts in or out, Python reads it as a new block, which "
            "breaks the flow. Highlight the whole block and re-indent uniformly."
        ),
    },
    "nameerror": {
        "name": "undefined name",
        "explain": (
            "Python looked for a variable or function by that name and couldn't find it. "
            "Two classic causes: the name is spelled differently from where it was assigned "
            "(Python names are case-sensitive), or you used the value before assigning it — "
            "for example reading a variable before input() ever set it."
        ),
        "hint": "Find every place that name is mentioned and compare the spelling exactly, character by character, to the assignment.",
        "deeper": (
            "Names come into existence at the point of assignment. Reading a name earlier "
            "raises NameError. Also watch order: in a function, parameters only exist inside "
            "it; outside the function they are not visible."
        ),
    },
    "typeerror": {
        "name": "type error",
        "explain": (
            "An operation doesn't make sense for the types involved — the classic one is "
            "adding a string and a number: \"2 + 3 is \" + 5. Convert one side first with "
            "str(...), int(...) or float(...), or use an f-string."
        ),
        "hint": "Check what type each operand really is — input() always gives you a string, even when it looks like a number.",
        "deeper": (
            "Types are chosen when values are created, not when you want them to change. "
            "input() returns a string; int(...) builds an int; + is addition for numbers but "
            "concatenation for strings. Mixing them is a TypeError while they stay mixed."
        ),
    },
    "indexerror": {
        "name": "index out of range",
        "explain": (
            "You asked for an element that isn't there. A list of len n is indexed 0…n−1, so "
            "asking for items[n] or items[len(items)] is out of range. The loop condition "
            "i <= len(items) is the usual culprit — it lets the index run one past the end."
        ),
        "hint": "Your loop must stop BELOW the length: use i < len(items), never i <= len(items).",
        "deeper": (
            "Indexing is 0-based in Python: the first element is items[0]. The valid range is "
            "0 up to len(items)-1. Double check any while loop that advances an index — the "
            "off-by-one makes it overshoot exactly when the last element is processed."
        ),
    },
    "valueerror": {
        "name": "conversion error",
        "explain": (
            "A conversion like int(...) or float(...) was handed text it can't convert. "
            "int(\"Ahmed\") raises ValueError, while int(\"19\") is fine. The fix is usually "
            "converting the right piece of input — the number, not the name — or validating "
            "the input first."
        ),
        "hint": "Which input are you casting, and could it contain letters? Often the name and the number got swapped.",
        "deeper": (
            "int() refuses anything that isn't a valid integer literal, including whitespace, "
            "letters and decimals. When a program reads several values from input(), map each "
            "one to the type you need at the point where it is read."
        ),
    },
    "attributeerror": {
        "name": "missing method or attribute",
        "explain": (
            "You called .method() on a value that doesn't have it — for example calling a "
            "string method on an int. Each type has its own toolbox: len() works on any "
            "sequence, but .upper(), .split() and .find() belong to strings."
        ),
        "hint": "Which type is your value? Print(type(value)) if unsure — the fix is matching the method to that type.",
        "deeper": (
            "The error text names both the method and the type that lacks it — that is your "
            "diagnosis on a plate. A number that came from int() has no .upper(); a string "
            "you forgot to convert has no .append() (lists have that).",
        ),
    },
    "zerodivisionerror": {
        "name": "division by zero",
        "explain": (
            "You divided by zero, which has no answer. In a program this usually means the "
            "denominator can legitimately become 0 for some input — guard it with an if and "
            "decide what should happen in that case."
        ),
        "hint": "On which input does the denominator become 0? Guard the division with an if so it never runs with 0.",
        "deeper": (
            "Zero is not a legal divisor. For robust programs ask: for every possible input, "
            "could b be 0 when I compute a / b? If yes, branch around the division and print "
            "a sensible message (or skip it)."
        ),
    },
}

_CONCEPT_TUTOR = {
    "loop": {
        "label": "loops",
        "explain": (
            "A loop runs a block repeatedly. The for loop is driven by a sequence "
            "(for i in range(n) counts n times); the while loop runs while a condition is "
            "true and MUST eventually make that condition false. The most common bug — the "
            "off-by-one — comes from range(1, n) visiting 1…n−1 instead of 1…n."
        ),
        "hint": "Ask yourself: how many times should this body run? Then choose range or while so it runs exactly that many.",
        "deeper": (
            "Every loop needs three ingredients: an initial state, a body that makes progress, "
            "and a stopping test. In a counted loop the test is the range bounds; in a "
            "sentinel loop the body must re-read the value that the test examines, or the "
            "condition never changes."
        ),
    },
    "condition": {
        "label": "selection / if",
        "explain": (
            "if / elif / else runs different branches for different cases. Conditions are "
            "Booleans (True or False). Comparisons use == for equality (not =, which "
            "assigns), and you can chain with and / or and flip with not."
        ),
        "hint": "List the distinct cases your input can have — each distinct output needs its own branch.",
        "deeper": (
            "Branches are checked top to bottom and the FIRST true one wins — an elif lower "
            "down never runs if an earlier condition already matched. Order overlapping "
            "conditions deliberately, widest first."
        ),
    },
    "list": {
        "label": "lists",
        "explain": (
            "A list holds many values in one name. Indexing is zero-based: numbers[0] is the "
            "first element, numbers[-1] the last. len(numbers) is the count. To visit every "
            "element use for x in numbers (value) or for i in range(len(numbers)) (position)."
        ),
        "hint": "Do you need each value itself, or its position? The first is for x in list; the second is range(len(list)).",
        "deeper": (
            "range(len(items)) produces indexes 0…len-1 — always stop below the length. "
            "Appending grows a list; items[i] = v overwrites; slicing items[a:b] builds a "
            "new list. The IndexError (running one past the end) is its signature bug."
        ),
    },
    "function": {
        "label": "functions",
        "explain": (
            "A function bundles a reusable task under a name. Its parameters are the inputs "
            "it receives; return hands the answer back to the caller. A very common mistake "
            "is printing inside the function instead of returning — printing gives you "
            "None as the result."
        ),
        "hint": "What does the caller need back? Everything the caller prints or uses must come back through return.",
        "deeper": (
            "return ends the function immediately and ships one value back; print only writes "
            "to the screen. If is_even(n) prints \"even\", then is_even(n) itself evaluates "
            "to None wherever it's used. Return values flow — parameters flow in, return "
            "flows out."
        ),
    },
    "string": {
        "label": "strings",
        "explain": (
            "A string is a sequence of characters you can index and slice like a list. "
            "s[::-1] reverses it; len(s) counts characters. Strings are immutable — methods "
            "like .upper() return NEW strings, they never alter the original."
        ),
        "hint": "If you need to compare text, normalize it first (e.g. .lower()) so case differences don't fool the comparison.",
        "deeper": (
            "Character types: strings vs chars. A single character is just a one-character "
            "string in Python, so indexing s[i] returns a string of length 1. Slices "
            "s[a:b] end at b-1. Reversing s[::-1] is a handy idiom for palindrome checks."
        ),
    },
    "recursion": {
        "label": "recursion",
        "explain": (
            "Recursion is a function calling itself. It works when two pieces exist: a base "
            "case (the smallest input, answered directly, no call) and a step that rewrites "
            "the problem as one smaller version of itself. For factorial: factorial(n) = "
            "n × factorial(n−1), with factorial(1) = 1 as the base."
        ),
        "hint": "Write the base case first: what input can you answer without any further calls?",
        "deeper": (
            "Each call keeps its own copy of the parameters on a stack, so later calls "
            "unwind back to earlier ones. If the base case never triggers, the calls nest "
            "forever → RecursionError. Make the argument strictly smaller on every step."
        ),
    },
}

_INTRO = "Let's look at that together — the goal is for it to click, not for me to just hand you code."


def tutor_response(*, question: str, code: str = "", error: str = "", depth: str = "explain", challenge_id: str = "") -> dict:
    """Assemble a teaching response from the student's actual artifacts."""
    battle = question.strip().lower()
    depth = depth if depth in ("hint", "explain", "deeper", "solution") else "explain"

    # 1) A visible sandbox error beats guesses — tutor that first.
    error_key = _match_error(error or "")
    if error_key:
        return _error_response(error_key, error, depth)

    # 2) A known challenge + solution-level request hands over the curated solution.
    if depth == "solution" and challenge_id:
        challenge = lab_content.challenge_by_id(challenge_id)
        if challenge and challenge.get("hints", {}).get("solution"):
            return {
                "depth": depth,
                "suggestions": ["Now reset the editor and try it yourself without peeking."],
                "text": (
                    f"For “{challenge['title']}” the solution is:\n\n"
                    f"{challenge['hints']['solution']}\n\n"
                    "Only read this if you're stuck for a while — recreating it on your own "
                    "is where the learning happens."
                ),
            }

    # 3) Concept tutoring by keyword.
    concept_key = _match_concept(battle)
    if concept_key:
        tutor = _CONCEPT_TUTOR[concept_key]
        return {
            "depth": depth,
            "suggestions": _concept_suggestions(concept_key),
            "text": _with_intro(tutor[depth] if depth in tutor else tutor["explain"]),
        }

    # 4) General encouragement + a concrete next step.
    if not code.strip():
        return {
            "depth": "hint",
            "suggestions": ["How do I read input?", "How do I print output?", "What's the difference between a for and a while loop?"],
            "text": (
                _with_intro(
                    "Tell me what you're working on — paste your code, describe the challenge, "
                    "or ask about a concept (loops, if/else, lists, functions, recursion, input/"
                    "output). I can also look at any error the lab reports."
                )
            ),
        }
    return {
        "depth": "hint",
        "suggestions": ["Explain the concept I'm using", "Give me a hint", "Show me the solution"],
        "text": _with_intro(
            "I can see the code you're editing. Describe what it should do and what's "
            "happening instead, or ask a direct question — e.g. “why does my loop stop "
            "one early?” — and I'll help you reason about it."
        ),
    }


def _error_response(error_key: str, raw_error: str, depth: str) -> dict:
    tutor = _ERROR_TUTOR[error_key]
    where = ""
    match = re.search(r"line (\d+)[,\s]", raw_error or "")
    if not match:
        match = re.search(r"line (\d+)", raw_error or "")
    if match:
        where = f" (around line {match.group(1)})"
    text = tutor["explain"]
    if depth == "hint":
        text = tutor.get("hint", tutor["explain"])
    elif depth == "deeper":
        text = tutor.get("deeper", tutor["explain"])
    return {
        "depth": depth,
        "suggestions": ["Help me fix this step by step", "Why did this happen?", f"Teach me about {tutor['name']}s deeper"],
        "text": (
            _with_intro(
                f"This is a {tutor['name']}{where}.\n\n{text}\n\n"
                "If you'd like, send me the code as it is now and tell me what behavior you "
                "expected — that usually pinpoints the fix in one exchange."
            )
        ),
    }


def _with_intro(text: str) -> str:
    return f"{_INTRO}\n\n{text}"


def _match_error(error: str) -> str | None:
    lowered = (error or "").lower()
    for key, tutor in _ERROR_TUTOR.items():
        if key in lowered.replace(" ", ""):
            return key
    # Signature-only fallbacks.
    if "traceback" in lowered and "cannot concatenate" in lowered:
        return "typeerror"
    if "out of range" in lowered:
        return "indexerror"
    if "division by zero" in lowered:
        return "zerodivisionerror"
    return None


def _match_concept(question_lower: str) -> str | None:
    mapping = [
        ("recursion", ("recurs", "base case", "stack overflow")),
        ("function", ("function", "def ", "return", "parameter", "method", "call")),
        ("list", ("list", "array", "index", "element", "append", "items[")),
        ("string", ("string", "palindrome", "character", ".upper", "slice", "text")),
        ("loop", ("loop", "for ", " while ", "range", "iteration", "repeat", "iterate", "nested")),
        ("condition", ("if ", "elif", "else", "condition", "boolean", "comparison", "branch")),
    ]
    for key, needles in mapping:
        for needle in needles:
            if needle.replace(" ", "") in question_lower.replace(" ", ""):
                return key
    return None


def _concept_suggestions(concept_key: str) -> list[str]:
    if concept_key == "loop":
        return ["Why is my loop off by one?", "Difference between for and while", "How do nested loops work?"]
    if concept_key == "function":
        return ["Why does my function print None?", "What is return for?", "How do parameters work?"]
    if concept_key == "list":
        return ["Why am I getting IndexError?", "How do I loop through a list?", "What does len() give me?"]
    if concept_key == "string":
        return ["How do I reverse a string?", "What is a slice?", "How do I count characters?"]
    if concept_key == "condition":
        return ["How do I check several cases?", "What's the difference between = and ==?", "How do I combine conditions?"]
    if concept_key == "recursion":
        return ["What is a base case?", "Why does recursion fail with RecursionError?", "How do I trace recursion?"]
    return ["Give me a hint", "Show me the solution"]