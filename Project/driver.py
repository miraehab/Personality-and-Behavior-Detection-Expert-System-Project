import contextlib
import sys

from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)

def test_questions():

    engine.reset()      # Allows us to run tests multiple times.

    engine.activate('rules')

    print("doing proof")
    
    try:
        with engine.prove_goal('rules.what_is_the_personality($personality)') as gen: #STUDENTS: you will need to edit this line
            for vars, plan in gen:
                print("You Personality is: %s" % (vars['personality'])) #STUDENTS: you will need to edit this line

    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    print()
    print("done")