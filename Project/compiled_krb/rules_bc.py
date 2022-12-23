# rules_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def openness_questions(rule, arg_patterns, arg_context):
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
              "rules.openness_questions: got unexpected plan from when clause 1"
            with engine.prove('questions', 'openness_2', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.openness_questions: got unexpected plan from when clause 2"
                with engine.prove('questions', 'openness_3', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.openness_questions: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'openness_4', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.openness_questions: got unexpected plan from when clause 4"
                        mark5 = context.mark(True)
                        if rule.pattern(4).match_data(context, context,
                                context.lookup_data('ans1') + context.lookup_data('ans2') + context.lookup_data('ans3') + context.lookup_data('ans4')):
                          context.end_save_all_undo()
                          mark6 = context.mark(True)
                          if rule.pattern(5).match_data(context, context,
                                  context.lookup_data('tot') / 4):
                            context.end_save_all_undo()
                            rule.rule_base.num_bc_rule_successes += 1
                            yield
                          else: context.end_save_all_undo()
                          context.undo_to_mark(mark6)
                        else: context.end_save_all_undo()
                        context.undo_to_mark(mark5)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def neuroticism_questions(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'neuroticism_1', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.neuroticism_questions: got unexpected plan from when clause 1"
            with engine.prove('questions', 'neuroticism_2', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.neuroticism_questions: got unexpected plan from when clause 2"
                with engine.prove('questions', 'neuroticism_3', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.neuroticism_questions: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'neuroticism_4', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.neuroticism_questions: got unexpected plan from when clause 4"
                        mark5 = context.mark(True)
                        if rule.pattern(4).match_data(context, context,
                                context.lookup_data('ans1') + context.lookup_data('ans2') + context.lookup_data('ans3') + context.lookup_data('ans4')):
                          context.end_save_all_undo()
                          mark6 = context.mark(True)
                          if rule.pattern(5).match_data(context, context,
                                  context.lookup_data('tot') / 4):
                            context.end_save_all_undo()
                            rule.rule_base.num_bc_rule_successes += 1
                            yield
                          else: context.end_save_all_undo()
                          context.undo_to_mark(mark6)
                        else: context.end_save_all_undo()
                        context.undo_to_mark(mark5)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def conscientiousness_questions(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'conscientiousness_1', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.conscientiousness_questions: got unexpected plan from when clause 1"
            with engine.prove('questions', 'conscientiousness_2', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.conscientiousness_questions: got unexpected plan from when clause 2"
                with engine.prove('questions', 'conscientiousness_3', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.conscientiousness_questions: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'conscientiousness_4', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.conscientiousness_questions: got unexpected plan from when clause 4"
                        mark5 = context.mark(True)
                        if rule.pattern(4).match_data(context, context,
                                context.lookup_data('ans1') + context.lookup_data('ans2') + context.lookup_data('ans3') + context.lookup_data('ans4')):
                          context.end_save_all_undo()
                          mark6 = context.mark(True)
                          if rule.pattern(5).match_data(context, context,
                                  context.lookup_data('tot') / 4):
                            context.end_save_all_undo()
                            rule.rule_base.num_bc_rule_successes += 1
                            yield
                          else: context.end_save_all_undo()
                          context.undo_to_mark(mark6)
                        else: context.end_save_all_undo()
                        context.undo_to_mark(mark5)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def agreeableness_questions(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'agreeableness_1', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.agreeableness_questions: got unexpected plan from when clause 1"
            with engine.prove('questions', 'agreeableness_2', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.agreeableness_questions: got unexpected plan from when clause 2"
                with engine.prove('questions', 'agreeableness_3', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.agreeableness_questions: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'agreeableness_4', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.agreeableness_questions: got unexpected plan from when clause 4"
                        mark5 = context.mark(True)
                        if rule.pattern(4).match_data(context, context,
                                context.lookup_data('ans1') + context.lookup_data('ans2') + context.lookup_data('ans3') + context.lookup_data('ans4')):
                          context.end_save_all_undo()
                          mark6 = context.mark(True)
                          if rule.pattern(5).match_data(context, context,
                                  context.lookup_data('tot') / 4):
                            context.end_save_all_undo()
                            rule.rule_base.num_bc_rule_successes += 1
                            yield
                          else: context.end_save_all_undo()
                          context.undo_to_mark(mark6)
                        else: context.end_save_all_undo()
                        context.undo_to_mark(mark5)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def result(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'gender', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.result: got unexpected plan from when clause 1"
            with engine.prove('questions', 'age', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.result: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'openness', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.result: got unexpected plan from when clause 3"
                    with engine.prove(rule.rule_base.root_name, 'neuroticism', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.result: got unexpected plan from when clause 4"
                        with engine.prove(rule.rule_base.root_name, 'conscientiousness', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.result: got unexpected plan from when clause 5"
                            with engine.prove(rule.rule_base.root_name, 'agreeableness', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.result: got unexpected plan from when clause 6"
                                if context.lookup_data('avg_openness') >= 5.0:
                                  rule.rule_base.num_bc_rule_successes += 1
                                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('rules')
  
  bc_rule.bc_rule('openness_questions', This_rule_base, 'openness',
                  openness_questions, None,
                  (contexts.variable('avg'),),
                  (),
                  (contexts.variable('ans1'),
                   contexts.variable('ans2'),
                   contexts.variable('ans3'),
                   contexts.variable('ans4'),
                   contexts.variable('tot'),
                   contexts.variable('avg'),))
  
  bc_rule.bc_rule('neuroticism_questions', This_rule_base, 'neuroticism',
                  neuroticism_questions, None,
                  (contexts.variable('avg'),),
                  (),
                  (contexts.variable('ans1'),
                   contexts.variable('ans2'),
                   contexts.variable('ans3'),
                   contexts.variable('ans4'),
                   contexts.variable('tot'),
                   contexts.variable('avg'),))
  
  bc_rule.bc_rule('conscientiousness_questions', This_rule_base, 'conscientiousness',
                  conscientiousness_questions, None,
                  (contexts.variable('avg'),),
                  (),
                  (contexts.variable('ans1'),
                   contexts.variable('ans2'),
                   contexts.variable('ans3'),
                   contexts.variable('ans4'),
                   contexts.variable('tot'),
                   contexts.variable('avg'),))
  
  bc_rule.bc_rule('agreeableness_questions', This_rule_base, 'agreeableness',
                  agreeableness_questions, None,
                  (contexts.variable('avg'),),
                  (),
                  (contexts.variable('ans1'),
                   contexts.variable('ans2'),
                   contexts.variable('ans3'),
                   contexts.variable('ans4'),
                   contexts.variable('tot'),
                   contexts.variable('avg'),))
  
  bc_rule.bc_rule('result', This_rule_base, 'what_is_the_personality',
                  result, None,
                  (pattern.pattern_literal('lively'),),
                  (),
                  (contexts.variable('gender'),
                   contexts.variable('age'),
                   contexts.variable('avg_openness'),
                   contexts.variable('avg_neuroticism'),
                   contexts.variable('avg_conscientiousness'),
                   contexts.variable('avg_agreeableness'),))


Krb_filename = '..\\rules.krb'
Krb_lineno_map = (
    ((14, 18), (2, 2)),
    ((20, 25), (4, 4)),
    ((26, 31), (5, 5)),
    ((32, 37), (6, 6)),
    ((38, 43), (7, 7)),
    ((46, 46), (9, 9)),
    ((50, 50), (10, 10)),
    ((68, 72), (13, 13)),
    ((74, 79), (15, 15)),
    ((80, 85), (16, 16)),
    ((86, 91), (17, 17)),
    ((92, 97), (18, 18)),
    ((100, 100), (20, 20)),
    ((104, 104), (21, 21)),
    ((122, 126), (24, 24)),
    ((128, 133), (26, 26)),
    ((134, 139), (27, 27)),
    ((140, 145), (28, 28)),
    ((146, 151), (29, 29)),
    ((154, 154), (31, 31)),
    ((158, 158), (32, 32)),
    ((176, 180), (35, 35)),
    ((182, 187), (37, 37)),
    ((188, 193), (38, 38)),
    ((194, 199), (39, 39)),
    ((200, 205), (40, 40)),
    ((208, 208), (42, 42)),
    ((212, 212), (43, 43)),
    ((230, 234), (46, 46)),
    ((236, 241), (48, 48)),
    ((242, 247), (49, 49)),
    ((248, 253), (50, 50)),
    ((254, 259), (51, 51)),
    ((260, 265), (52, 52)),
    ((266, 271), (53, 53)),
    ((272, 272), (54, 54)),
)
