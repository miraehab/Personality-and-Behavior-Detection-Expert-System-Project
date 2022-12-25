import sys

from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)


def bc_test():

    engine.reset()      # Allows us to run tests multiple times.

    engine.activate('bc_rules') #STUDENTS: you will need to edit the name of your rule file here

    res = []
    try:
        with engine.prove_goal('bc_rules.what_is_the_personality($personality)') as gen: #STUDENTS: you will need to edit this line
            for vars, plan in gen:
                res.append(vars['personality'])
    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)
    return res