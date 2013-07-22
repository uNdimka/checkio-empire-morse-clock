import random

TESTS = None
RAND_TESTS = None
CURRENT_TEST = None
#options
RAND_TESTS_QUANTITY = None
FLOAT_PRECISION = None


def initial_checkio(data):
    global TESTS
    global RAND_TESTS
    global CURRENT_TEST
    global RAND_TESTS_QUANTITY
    global FLOAT_PRECISION
    TESTS = data.get("tests", [])
    RAND_TESTS = data.get("rand_tests", [])

    options = data.get("options", {})
    RAND_TESTS_QUANTITY = options.get("random-select", 0)
    FLOAT_PRECISION = options.get("float_precision", None)

    if TESTS:
        CURRENT_TEST = TESTS.pop(0)
    else:
        if RAND_TESTS_QUANTITY and RAND_TESTS:
            CURRENT_TEST = random.choice(RAND_TESTS)
            RAND_TESTS_QUANTITY -= 1
        else:
            raise DoneTest(1)

    return CURRENT_TEST["input"]


def checkio(data):
    global TESTS
    global RAND_TESTS
    global CURRENT_TEST
    global RAND_TESTS_QUANTITY
    global FLOAT_PRECISION
    CURRENT_TEST["user_answer"] = data
    answer = CURRENT_TEST["answer"]

    if (FLOAT_PRECISION and
                        answer - FLOAT_PRECISION <= data <= answer + FLOAT_PRECISION):
        CURRENT_TEST["result"] = True
    elif data == CURRENT_TEST["answer"]:
        CURRENT_TEST["result"] = True
    else:
        CURRENT_TEST["result"] = False
    ext_animation(CURRENT_TEST)
    if not CURRENT_TEST["result"]:
        raise FailTest('ERROR')

    if TESTS:
        CURRENT_TEST = TESTS.pop(0)
    else:
        if RAND_TESTS_QUANTITY and RAND_TESTS:
            CURRENT_TEST = random.choice(RAND_TESTS)
            RAND_TESTS_QUANTITY -= 1
        else:
            raise DoneTest(1)

    return CURRENT_TEST["input"]