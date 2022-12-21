# rules_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def openness_question1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'openness_1', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.openness_question1: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def openness_question2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'openness_2', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.openness_question2: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'openness', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.openness_question2: got unexpected plan from when clause 2"
                tot = context.lookup_data('ans') + context.lookup_data('ans2')
                mark4 = context.mark(True)
                if rule.pattern(2).match_data(context, context,
                        int(tot)):
                  context.end_save_all_undo()
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
                else: context.end_save_all_undo()
                context.undo_to_mark(mark4)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def openness_question3(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'openness_3', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.openness_question3: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'openness2', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.openness_question3: got unexpected plan from when clause 2"
                tot = context.lookup_data('ans') + context.lookup_data('ans2')
                mark4 = context.mark(True)
                if rule.pattern(2).match_data(context, context,
                        int(tot)):
                  context.end_save_all_undo()
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
                else: context.end_save_all_undo()
                context.undo_to_mark(mark4)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def openness_question4(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'openness_3', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.openness_question4: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'openness3', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.openness_question4: got unexpected plan from when clause 2"
                tot = context.lookup_data('ans') + context.lookup_data('ans2')
                mark4 = context.mark(True)
                if rule.pattern(2).match_data(context, context,
                        int(tot)):
                  context.end_save_all_undo()
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
                else: context.end_save_all_undo()
                context.undo_to_mark(mark4)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def test(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'openness2', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.test: got unexpected plan from when clause 1"
            if context.lookup_data('tot') <= 10:
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('rules')
  
  bc_rule.bc_rule('openness_question1', This_rule_base, 'openness',
                  openness_question1, None,
                  (contexts.variable('ans'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('openness_question2', This_rule_base, 'openness2',
                  openness_question2, None,
                  (contexts.variable('tot'),),
                  (),
                  (contexts.variable('ans2'),
                   contexts.variable('ans'),
                   contexts.variable('tot'),))
  
  bc_rule.bc_rule('openness_question3', This_rule_base, 'openness3',
                  openness_question3, None,
                  (contexts.variable('tot'),),
                  (),
                  (contexts.variable('ans2'),
                   contexts.variable('ans'),
                   contexts.variable('tot'),))
  
  bc_rule.bc_rule('openness_question4', This_rule_base, 'openness_final',
                  openness_question4, None,
                  (contexts.variable('tot'),),
                  (),
                  (contexts.variable('ans2'),
                   contexts.variable('ans'),
                   contexts.variable('tot'),))
  
  bc_rule.bc_rule('test', This_rule_base, 'what_is_the_personality',
                  test, None,
                  (pattern.pattern_literal('openness'),),
                  (),
                  (contexts.variable('tot'),))


Krb_filename = '..\\rules.krb'
Krb_lineno_map = (
    ((14, 18), (2, 2)),
    ((20, 25), (4, 4)),
    ((38, 42), (7, 7)),
    ((44, 49), (9, 9)),
    ((50, 55), (10, 10)),
    ((56, 56), (11, 11)),
    ((59, 59), (13, 13)),
    ((75, 79), (16, 16)),
    ((81, 86), (18, 18)),
    ((87, 92), (19, 19)),
    ((93, 93), (20, 20)),
    ((96, 96), (22, 22)),
    ((112, 116), (25, 25)),
    ((118, 123), (27, 27)),
    ((124, 129), (28, 28)),
    ((130, 130), (29, 29)),
    ((133, 133), (31, 31)),
    ((149, 153), (34, 34)),
    ((155, 160), (36, 36)),
    ((161, 161), (37, 37)),
)
