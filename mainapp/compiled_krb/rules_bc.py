# rules_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def test_rule(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'age', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.test_rule: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

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
        with engine.prove('facts', 'openness_1', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.openness_questions: got unexpected plan from when clause 1"
            with engine.prove('facts', 'openness_2', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.openness_questions: got unexpected plan from when clause 2"
                with engine.prove('facts', 'openness_3', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.openness_questions: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'openness_4', context,
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
        with engine.prove('facts', 'neuroticism_1', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.neuroticism_questions: got unexpected plan from when clause 1"
            with engine.prove('facts', 'neuroticism_2', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.neuroticism_questions: got unexpected plan from when clause 2"
                with engine.prove('facts', 'neuroticism_3', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.neuroticism_questions: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'neuroticism_4', context,
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
        with engine.prove('facts', 'conscientiousness_1', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.conscientiousness_questions: got unexpected plan from when clause 1"
            with engine.prove('facts', 'conscientiousness_2', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.conscientiousness_questions: got unexpected plan from when clause 2"
                with engine.prove('facts', 'conscientiousness_3', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.conscientiousness_questions: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'conscientiousness_4', context,
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
        with engine.prove('facts', 'agreeableness_1', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.agreeableness_questions: got unexpected plan from when clause 1"
            with engine.prove('facts', 'agreeableness_2', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.agreeableness_questions: got unexpected plan from when clause 2"
                with engine.prove('facts', 'agreeableness_3', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.agreeableness_questions: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'agreeableness_4', context,
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

def extraversion_questions(rule, arg_patterns, arg_context):
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
        with engine.prove('facts', 'extraversion_1', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.extraversion_questions: got unexpected plan from when clause 1"
            with engine.prove('facts', 'extraversion_2', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.extraversion_questions: got unexpected plan from when clause 2"
                with engine.prove('facts', 'extraversion_3', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.extraversion_questions: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'extraversion_4', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.extraversion_questions: got unexpected plan from when clause 4"
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

def gender_question(rule, arg_patterns, arg_context):
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
        with engine.prove('facts', 'gender', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.gender_question: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def age_question(rule, arg_patterns, arg_context):
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
        with engine.prove('facts', 'age', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.age_question: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def check_serious_1(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'gender', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.check_serious_1: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'age', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.check_serious_1: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'openness', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.check_serious_1: got unexpected plan from when clause 3"
                    with engine.prove(rule.rule_base.root_name, 'neuroticism', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.check_serious_1: got unexpected plan from when clause 4"
                        with engine.prove(rule.rule_base.root_name, 'conscientiousness', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.check_serious_1: got unexpected plan from when clause 5"
                            with engine.prove(rule.rule_base.root_name, 'agreeableness', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.check_serious_1: got unexpected plan from when clause 6"
                                with engine.prove(rule.rule_base.root_name, 'extraversion', context,
                                                  (rule.pattern(6),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "rules.check_serious_1: got unexpected plan from when clause 7"
                                    if context.lookup_data('avg_agreeableness') > 6.5:
                                      if context.lookup_data('avg_neuroticism') > 2.5:
                                        if context.lookup_data('avg_conscientiousness') > 1.5:
                                          if context.lookup_data('avg_neuroticism') > 5.5:
                                            rule.rule_base.num_bc_rule_successes += 1
                                            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def check_serious_2(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'age', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.check_serious_2: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'openness', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.check_serious_2: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'neuroticism', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.check_serious_2: got unexpected plan from when clause 3"
                    with engine.prove(rule.rule_base.root_name, 'conscientiousness', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.check_serious_2: got unexpected plan from when clause 4"
                        with engine.prove(rule.rule_base.root_name, 'agreeableness', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.check_serious_2: got unexpected plan from when clause 5"
                            with engine.prove(rule.rule_base.root_name, 'extraversion', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.check_serious_2: got unexpected plan from when clause 6"
                                if context.lookup_data('avg_agreeableness') > 6.5:
                                  if context.lookup_data('avg_neuroticism') <= 2.5:
                                    if context.lookup_data('avg_conscientiousness') > 1.5:
                                      if context.lookup_data('age') > 18.5:
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def check_serious_3(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'age', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.check_serious_3: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'openness', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.check_serious_3: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'neuroticism', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.check_serious_3: got unexpected plan from when clause 3"
                    with engine.prove(rule.rule_base.root_name, 'conscientiousness', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.check_serious_3: got unexpected plan from when clause 4"
                        with engine.prove(rule.rule_base.root_name, 'agreeableness', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.check_serious_3: got unexpected plan from when clause 5"
                            with engine.prove(rule.rule_base.root_name, 'extraversion', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.check_serious_3: got unexpected plan from when clause 6"
                                if context.lookup_data('avg_agreeableness') <= 6.5:
                                  if context.lookup_data('avg_agreeableness') > 5.5:
                                    if context.lookup_data('avg_conscientiousness') > 3.5  :
                                      if context.lookup_data('avg_extraversion') <= 3.5  :
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def check_serious_4(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'age', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.check_serious_4: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'openness', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.check_serious_4: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'neuroticism', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.check_serious_4: got unexpected plan from when clause 3"
                    with engine.prove(rule.rule_base.root_name, 'conscientiousness', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.check_serious_4: got unexpected plan from when clause 4"
                        with engine.prove(rule.rule_base.root_name, 'agreeableness', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.check_serious_4: got unexpected plan from when clause 5"
                            with engine.prove(rule.rule_base.root_name, 'extraversion', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.check_serious_4: got unexpected plan from when clause 6"
                                if context.lookup_data('avg_agreeableness') <= 6.5:
                                  if context.lookup_data('avg_agreeableness') <= 5.5:
                                    if context.lookup_data('age') <= 18.5:
                                      if context.lookup_data('avg_openness') > 3.5:
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def check_serious_5(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'age', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.check_serious_5: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'openness', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.check_serious_5: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'neuroticism', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.check_serious_5: got unexpected plan from when clause 3"
                    with engine.prove(rule.rule_base.root_name, 'conscientiousness', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.check_serious_5: got unexpected plan from when clause 4"
                        with engine.prove(rule.rule_base.root_name, 'agreeableness', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.check_serious_5: got unexpected plan from when clause 5"
                            with engine.prove(rule.rule_base.root_name, 'extraversion', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.check_serious_5: got unexpected plan from when clause 6"
                                if context.lookup_data('avg_agreeableness') > 6.5:
                                  if context.lookup_data('avg_neuroticism') > 2.5:
                                    if context.lookup_data('avg_conscientiousness') <= 1.5:
                                      if context.lookup_data('avg_neuroticism') > 6.5:
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def check_responsible_1(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'age', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.check_responsible_1: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'openness', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.check_responsible_1: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'neuroticism', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.check_responsible_1: got unexpected plan from when clause 3"
                    with engine.prove(rule.rule_base.root_name, 'conscientiousness', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.check_responsible_1: got unexpected plan from when clause 4"
                        with engine.prove(rule.rule_base.root_name, 'agreeableness', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.check_responsible_1: got unexpected plan from when clause 5"
                            with engine.prove(rule.rule_base.root_name, 'extraversion', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.check_responsible_1: got unexpected plan from when clause 6"
                                if context.lookup_data('avg_agreeableness') > 6.5:
                                  if context.lookup_data('avg_neuroticism') <= 2.5:
                                    if context.lookup_data('avg_conscientiousness') <= 1.5:
                                      rule.rule_base.num_bc_rule_successes += 1
                                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def check_responsible_2(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'age', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.check_responsible_2: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'openness', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.check_responsible_2: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'neuroticism', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.check_responsible_2: got unexpected plan from when clause 3"
                    with engine.prove(rule.rule_base.root_name, 'conscientiousness', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.check_responsible_2: got unexpected plan from when clause 4"
                        with engine.prove(rule.rule_base.root_name, 'agreeableness', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.check_responsible_2: got unexpected plan from when clause 5"
                            with engine.prove(rule.rule_base.root_name, 'extraversion', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.check_responsible_2: got unexpected plan from when clause 6"
                                if context.lookup_data('avg_agreeableness') <= 6.5:
                                  if context.lookup_data('avg_agreeableness') > 5.5:
                                    if context.lookup_data('avg_conscientiousness') <= 3.5:
                                      if context.lookup_data('age') > 18.5:
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def check_responsible_3(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'age', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.check_responsible_3: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'openness', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.check_responsible_3: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'neuroticism', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.check_responsible_3: got unexpected plan from when clause 3"
                    with engine.prove(rule.rule_base.root_name, 'conscientiousness', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.check_responsible_3: got unexpected plan from when clause 4"
                        with engine.prove(rule.rule_base.root_name, 'agreeableness', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.check_responsible_3: got unexpected plan from when clause 5"
                            with engine.prove(rule.rule_base.root_name, 'extraversion', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.check_responsible_3: got unexpected plan from when clause 6"
                                if context.lookup_data('avg_agreeableness') <= 5.5:
                                  if context.lookup_data('age') > 18.5:
                                    if context.lookup_data('avg_extraversion') > 2.5:
                                      rule.rule_base.num_bc_rule_successes += 1
                                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def check_extraverted(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'age', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.check_extraverted: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'openness', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.check_extraverted: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'neuroticism', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.check_extraverted: got unexpected plan from when clause 3"
                    with engine.prove(rule.rule_base.root_name, 'conscientiousness', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.check_extraverted: got unexpected plan from when clause 4"
                        with engine.prove(rule.rule_base.root_name, 'agreeableness', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.check_extraverted: got unexpected plan from when clause 5"
                            with engine.prove(rule.rule_base.root_name, 'extraversion', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.check_extraverted: got unexpected plan from when clause 6"
                                if context.lookup_data('avg_agreeableness') > 6.5:
                                  if context.lookup_data('avg_neuroticism') > 2.5:
                                    if context.lookup_data('avg_conscientiousness') > 1.5:
                                      if context.lookup_data('avg_neuroticism') >= 5.5:
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def check_lively_1(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'age', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.check_lively_1: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'openness', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.check_lively_1: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'neuroticism', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.check_lively_1: got unexpected plan from when clause 3"
                    with engine.prove(rule.rule_base.root_name, 'conscientiousness', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.check_lively_1: got unexpected plan from when clause 4"
                        with engine.prove(rule.rule_base.root_name, 'agreeableness', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.check_lively_1: got unexpected plan from when clause 5"
                            with engine.prove(rule.rule_base.root_name, 'extraversion', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.check_lively_1: got unexpected plan from when clause 6"
                                if context.lookup_data('avg_agreeableness') <= 5.5:
                                  if context.lookup_data('age') <= 18.5:
                                    if context.lookup_data('avg_openness') <= 3.5:
                                      rule.rule_base.num_bc_rule_successes += 1
                                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def check_lively_2(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'age', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.check_lively_2: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'openness', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.check_lively_2: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'neuroticism', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.check_lively_2: got unexpected plan from when clause 3"
                    with engine.prove(rule.rule_base.root_name, 'conscientiousness', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.check_lively_2: got unexpected plan from when clause 4"
                        with engine.prove(rule.rule_base.root_name, 'agreeableness', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.check_lively_2: got unexpected plan from when clause 5"
                            with engine.prove(rule.rule_base.root_name, 'extraversion', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.check_lively_2: got unexpected plan from when clause 6"
                                if context.lookup_data('avg_agreeableness') <= 5.5:
                                  if context.lookup_data('age') > 18.5:
                                    if context.lookup_data('avg_extraversion') <= 2.5:
                                      rule.rule_base.num_bc_rule_successes += 1
                                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def check_lively_3(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'age', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.check_lively_3: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'openness', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.check_lively_3: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'neuroticism', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.check_lively_3: got unexpected plan from when clause 3"
                    with engine.prove(rule.rule_base.root_name, 'conscientiousness', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.check_lively_3: got unexpected plan from when clause 4"
                        with engine.prove(rule.rule_base.root_name, 'agreeableness', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.check_lively_3: got unexpected plan from when clause 5"
                            with engine.prove(rule.rule_base.root_name, 'extraversion', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.check_lively_3: got unexpected plan from when clause 6"
                                if context.lookup_data('avg_agreeableness') > 6.5:
                                  if context.lookup_data('avg_neuroticism') <= 2.5:
                                    if context.lookup_data('avg_conscientiousness') > 1.5:
                                      if context.lookup_data('age') <= 18.5:
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def check_dependable_1(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'age', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.check_dependable_1: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'openness', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.check_dependable_1: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'neuroticism', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.check_dependable_1: got unexpected plan from when clause 3"
                    with engine.prove(rule.rule_base.root_name, 'conscientiousness', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.check_dependable_1: got unexpected plan from when clause 4"
                        with engine.prove(rule.rule_base.root_name, 'agreeableness', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.check_dependable_1: got unexpected plan from when clause 5"
                            with engine.prove(rule.rule_base.root_name, 'extraversion', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.check_dependable_1: got unexpected plan from when clause 6"
                                if context.lookup_data('avg_agreeableness') <= 6.5:
                                  if context.lookup_data('avg_agreeableness') > 5.5:
                                    if context.lookup_data('avg_conscientiousness') <= 3.5:
                                      if context.lookup_data('age') <= 18.5:
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def check_dependable_2(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'age', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.check_dependable_2: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'openness', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.check_dependable_2: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'neuroticism', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.check_dependable_2: got unexpected plan from when clause 3"
                    with engine.prove(rule.rule_base.root_name, 'conscientiousness', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.check_dependable_2: got unexpected plan from when clause 4"
                        with engine.prove(rule.rule_base.root_name, 'agreeableness', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.check_dependable_2: got unexpected plan from when clause 5"
                            with engine.prove(rule.rule_base.root_name, 'extraversion', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.check_dependable_2: got unexpected plan from when clause 6"
                                if context.lookup_data('avg_agreeableness') <= 6.5:
                                  if context.lookup_data('avg_agreeableness') > 5.5:
                                    if context.lookup_data('avg_conscientiousness') > 3.5:
                                      if context.lookup_data('avg_extraversion') > 3.5:
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def check_dependable_3(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'age', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.check_dependable_3: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'openness', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.check_dependable_3: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'neuroticism', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.check_dependable_3: got unexpected plan from when clause 3"
                    with engine.prove(rule.rule_base.root_name, 'conscientiousness', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.check_dependable_3: got unexpected plan from when clause 4"
                        with engine.prove(rule.rule_base.root_name, 'agreeableness', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.check_dependable_3: got unexpected plan from when clause 5"
                            with engine.prove(rule.rule_base.root_name, 'extraversion', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.check_dependable_3: got unexpected plan from when clause 6"
                                if context.lookup_data('avg_agreeableness') > 6.5:
                                  if context.lookup_data('avg_neuroticism') > 2.5:
                                    if context.lookup_data('avg_conscientiousness') <= 1.5:
                                      if context.lookup_data('avg_neuroticism') <= 6.5:
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('rules')
  
  bc_rule.bc_rule('test_rule', This_rule_base, 'what_is_the_personality',
                  test_rule, None,
                  (pattern.pattern_literal('test'),),
                  (),
                  (pattern.pattern_literal(41),))
  
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
  
  bc_rule.bc_rule('extraversion_questions', This_rule_base, 'extraversion',
                  extraversion_questions, None,
                  (contexts.variable('avg'),),
                  (),
                  (contexts.variable('ans1'),
                   contexts.variable('ans2'),
                   contexts.variable('ans3'),
                   contexts.variable('ans4'),
                   contexts.variable('tot'),
                   contexts.variable('avg'),))
  
  bc_rule.bc_rule('gender_question', This_rule_base, 'gender',
                  gender_question, None,
                  (contexts.variable('gender'),),
                  (),
                  (contexts.variable('gender'),))
  
  bc_rule.bc_rule('age_question', This_rule_base, 'age',
                  age_question, None,
                  (contexts.variable('age'),),
                  (),
                  (contexts.variable('age'),))
  
  bc_rule.bc_rule('check_serious_1', This_rule_base, 'what_is_the_personality',
                  check_serious_1, None,
                  (pattern.pattern_literal('serious'),),
                  (),
                  (contexts.variable('gender'),
                   contexts.variable('age'),
                   contexts.variable('avg_openness'),
                   contexts.variable('avg_neuroticism'),
                   contexts.variable('avg_conscientiousness'),
                   contexts.variable('avg_agreeableness'),
                   contexts.variable('avg_extraversion'),))
  
  bc_rule.bc_rule('check_serious_2', This_rule_base, 'what_is_the_personality',
                  check_serious_2, None,
                  (pattern.pattern_literal('serious'),),
                  (),
                  (contexts.variable('age'),
                   contexts.variable('avg_openness'),
                   contexts.variable('avg_neuroticism'),
                   contexts.variable('avg_conscientiousness'),
                   contexts.variable('avg_agreeableness'),
                   contexts.variable('avg_extraversion'),))
  
  bc_rule.bc_rule('check_serious_3', This_rule_base, 'what_is_the_personality',
                  check_serious_3, None,
                  (pattern.pattern_literal('serious'),),
                  (),
                  (contexts.variable('age'),
                   contexts.variable('avg_openness'),
                   contexts.variable('avg_neuroticism'),
                   contexts.variable('avg_conscientiousness'),
                   contexts.variable('avg_agreeableness'),
                   contexts.variable('avg_extraversion'),))
  
  bc_rule.bc_rule('check_serious_4', This_rule_base, 'what_is_the_personality',
                  check_serious_4, None,
                  (pattern.pattern_literal('serious'),),
                  (),
                  (contexts.variable('age'),
                   contexts.variable('avg_openness'),
                   contexts.variable('avg_neuroticism'),
                   contexts.variable('avg_conscientiousness'),
                   contexts.variable('avg_agreeableness'),
                   contexts.variable('avg_extraversion'),))
  
  bc_rule.bc_rule('check_serious_5', This_rule_base, 'what_is_the_personality',
                  check_serious_5, None,
                  (pattern.pattern_literal('serious'),),
                  (),
                  (contexts.variable('age'),
                   contexts.variable('avg_openness'),
                   contexts.variable('avg_neuroticism'),
                   contexts.variable('avg_conscientiousness'),
                   contexts.variable('avg_agreeableness'),
                   contexts.variable('avg_extraversion'),))
  
  bc_rule.bc_rule('check_responsible_1', This_rule_base, 'what_is_the_personality',
                  check_responsible_1, None,
                  (pattern.pattern_literal('responsible'),),
                  (),
                  (contexts.variable('age'),
                   contexts.variable('avg_openness'),
                   contexts.variable('avg_neuroticism'),
                   contexts.variable('avg_conscientiousness'),
                   contexts.variable('avg_agreeableness'),
                   contexts.variable('avg_extraversion'),))
  
  bc_rule.bc_rule('check_responsible_2', This_rule_base, 'what_is_the_personality',
                  check_responsible_2, None,
                  (pattern.pattern_literal('responsible'),),
                  (),
                  (contexts.variable('age'),
                   contexts.variable('avg_openness'),
                   contexts.variable('avg_neuroticism'),
                   contexts.variable('avg_conscientiousness'),
                   contexts.variable('avg_agreeableness'),
                   contexts.variable('avg_extraversion'),))
  
  bc_rule.bc_rule('check_responsible_3', This_rule_base, 'what_is_the_personality',
                  check_responsible_3, None,
                  (pattern.pattern_literal('responsible'),),
                  (),
                  (contexts.variable('age'),
                   contexts.variable('avg_openness'),
                   contexts.variable('avg_neuroticism'),
                   contexts.variable('avg_conscientiousness'),
                   contexts.variable('avg_agreeableness'),
                   contexts.variable('avg_extraversion'),))
  
  bc_rule.bc_rule('check_extraverted', This_rule_base, 'what_is_the_personality',
                  check_extraverted, None,
                  (pattern.pattern_literal('extraverted'),),
                  (),
                  (contexts.variable('age'),
                   contexts.variable('avg_openness'),
                   contexts.variable('avg_neuroticism'),
                   contexts.variable('avg_conscientiousness'),
                   contexts.variable('avg_agreeableness'),
                   contexts.variable('avg_extraversion'),))
  
  bc_rule.bc_rule('check_lively_1', This_rule_base, 'what_is_the_personality',
                  check_lively_1, None,
                  (pattern.pattern_literal('lively'),),
                  (),
                  (contexts.variable('age'),
                   contexts.variable('avg_openness'),
                   contexts.variable('avg_neuroticism'),
                   contexts.variable('avg_conscientiousness'),
                   contexts.variable('avg_agreeableness'),
                   contexts.variable('avg_extraversion'),))
  
  bc_rule.bc_rule('check_lively_2', This_rule_base, 'what_is_the_personality',
                  check_lively_2, None,
                  (pattern.pattern_literal('lively'),),
                  (),
                  (contexts.variable('age'),
                   contexts.variable('avg_openness'),
                   contexts.variable('avg_neuroticism'),
                   contexts.variable('avg_conscientiousness'),
                   contexts.variable('avg_agreeableness'),
                   contexts.variable('avg_extraversion'),))
  
  bc_rule.bc_rule('check_lively_3', This_rule_base, 'what_is_the_personality',
                  check_lively_3, None,
                  (pattern.pattern_literal('lively'),),
                  (),
                  (contexts.variable('age'),
                   contexts.variable('avg_openness'),
                   contexts.variable('avg_neuroticism'),
                   contexts.variable('avg_conscientiousness'),
                   contexts.variable('avg_agreeableness'),
                   contexts.variable('avg_extraversion'),))
  
  bc_rule.bc_rule('check_dependable_1', This_rule_base, 'what_is_the_personality',
                  check_dependable_1, None,
                  (pattern.pattern_literal('dependable'),),
                  (),
                  (contexts.variable('age'),
                   contexts.variable('avg_openness'),
                   contexts.variable('avg_neuroticism'),
                   contexts.variable('avg_conscientiousness'),
                   contexts.variable('avg_agreeableness'),
                   contexts.variable('avg_extraversion'),))
  
  bc_rule.bc_rule('check_dependable_2', This_rule_base, 'what_is_the_personality',
                  check_dependable_2, None,
                  (pattern.pattern_literal('dependable'),),
                  (),
                  (contexts.variable('age'),
                   contexts.variable('avg_openness'),
                   contexts.variable('avg_neuroticism'),
                   contexts.variable('avg_conscientiousness'),
                   contexts.variable('avg_agreeableness'),
                   contexts.variable('avg_extraversion'),))
  
  bc_rule.bc_rule('check_dependable_3', This_rule_base, 'what_is_the_personality',
                  check_dependable_3, None,
                  (pattern.pattern_literal('dependable'),),
                  (),
                  (contexts.variable('age'),
                   contexts.variable('avg_openness'),
                   contexts.variable('avg_neuroticism'),
                   contexts.variable('avg_conscientiousness'),
                   contexts.variable('avg_agreeableness'),
                   contexts.variable('avg_extraversion'),))


Krb_filename = '..\\rules.krb'
Krb_lineno_map = (
    ((14, 18), (2, 2)),
    ((20, 25), (4, 4)),
    ((38, 42), (8, 8)),
    ((44, 49), (10, 10)),
    ((50, 55), (11, 11)),
    ((56, 61), (12, 12)),
    ((62, 67), (13, 13)),
    ((70, 70), (15, 15)),
    ((74, 74), (16, 16)),
    ((92, 96), (19, 19)),
    ((98, 103), (21, 21)),
    ((104, 109), (22, 22)),
    ((110, 115), (23, 23)),
    ((116, 121), (24, 24)),
    ((124, 124), (26, 26)),
    ((128, 128), (27, 27)),
    ((146, 150), (30, 30)),
    ((152, 157), (32, 32)),
    ((158, 163), (33, 33)),
    ((164, 169), (34, 34)),
    ((170, 175), (35, 35)),
    ((178, 178), (37, 37)),
    ((182, 182), (38, 38)),
    ((200, 204), (41, 41)),
    ((206, 211), (43, 43)),
    ((212, 217), (44, 44)),
    ((218, 223), (45, 45)),
    ((224, 229), (46, 46)),
    ((232, 232), (48, 48)),
    ((236, 236), (49, 49)),
    ((254, 258), (52, 52)),
    ((260, 265), (54, 54)),
    ((266, 271), (55, 55)),
    ((272, 277), (56, 56)),
    ((278, 283), (57, 57)),
    ((286, 286), (59, 59)),
    ((290, 290), (60, 60)),
    ((308, 312), (63, 63)),
    ((314, 319), (65, 65)),
    ((332, 336), (68, 68)),
    ((338, 343), (70, 70)),
    ((356, 360), (73, 73)),
    ((362, 367), (75, 75)),
    ((368, 373), (76, 76)),
    ((374, 379), (77, 77)),
    ((380, 385), (78, 78)),
    ((386, 391), (79, 79)),
    ((392, 397), (80, 80)),
    ((398, 403), (81, 81)),
    ((404, 404), (82, 82)),
    ((405, 405), (83, 83)),
    ((406, 406), (84, 84)),
    ((407, 407), (85, 85)),
    ((420, 424), (88, 88)),
    ((426, 431), (90, 90)),
    ((432, 437), (91, 91)),
    ((438, 443), (92, 92)),
    ((444, 449), (93, 93)),
    ((450, 455), (94, 94)),
    ((456, 461), (95, 95)),
    ((462, 462), (96, 96)),
    ((463, 463), (97, 97)),
    ((464, 464), (98, 98)),
    ((465, 465), (99, 99)),
    ((478, 482), (102, 102)),
    ((484, 489), (104, 104)),
    ((490, 495), (105, 105)),
    ((496, 501), (106, 106)),
    ((502, 507), (107, 107)),
    ((508, 513), (108, 108)),
    ((514, 519), (109, 109)),
    ((520, 520), (110, 110)),
    ((521, 521), (111, 111)),
    ((522, 522), (112, 112)),
    ((523, 523), (113, 113)),
    ((536, 540), (116, 116)),
    ((542, 547), (118, 118)),
    ((548, 553), (119, 119)),
    ((554, 559), (120, 120)),
    ((560, 565), (121, 121)),
    ((566, 571), (122, 122)),
    ((572, 577), (123, 123)),
    ((578, 578), (124, 124)),
    ((579, 579), (125, 125)),
    ((580, 580), (126, 126)),
    ((581, 581), (127, 127)),
    ((594, 598), (130, 130)),
    ((600, 605), (132, 132)),
    ((606, 611), (133, 133)),
    ((612, 617), (134, 134)),
    ((618, 623), (135, 135)),
    ((624, 629), (136, 136)),
    ((630, 635), (137, 137)),
    ((636, 636), (138, 138)),
    ((637, 637), (139, 139)),
    ((638, 638), (140, 140)),
    ((639, 639), (141, 141)),
    ((652, 656), (144, 144)),
    ((658, 663), (146, 146)),
    ((664, 669), (147, 147)),
    ((670, 675), (148, 148)),
    ((676, 681), (149, 149)),
    ((682, 687), (150, 150)),
    ((688, 693), (151, 151)),
    ((694, 694), (152, 152)),
    ((695, 695), (153, 153)),
    ((696, 696), (154, 154)),
    ((709, 713), (157, 157)),
    ((715, 720), (159, 159)),
    ((721, 726), (160, 160)),
    ((727, 732), (161, 161)),
    ((733, 738), (162, 162)),
    ((739, 744), (163, 163)),
    ((745, 750), (164, 164)),
    ((751, 751), (165, 165)),
    ((752, 752), (166, 166)),
    ((753, 753), (167, 167)),
    ((754, 754), (168, 168)),
    ((767, 771), (171, 171)),
    ((773, 778), (173, 173)),
    ((779, 784), (174, 174)),
    ((785, 790), (175, 175)),
    ((791, 796), (176, 176)),
    ((797, 802), (177, 177)),
    ((803, 808), (178, 178)),
    ((809, 809), (179, 179)),
    ((810, 810), (180, 180)),
    ((811, 811), (181, 181)),
    ((824, 828), (184, 184)),
    ((830, 835), (186, 186)),
    ((836, 841), (187, 187)),
    ((842, 847), (188, 188)),
    ((848, 853), (189, 189)),
    ((854, 859), (190, 190)),
    ((860, 865), (191, 191)),
    ((866, 866), (192, 192)),
    ((867, 867), (193, 193)),
    ((868, 868), (194, 194)),
    ((869, 869), (195, 195)),
    ((882, 886), (198, 198)),
    ((888, 893), (200, 200)),
    ((894, 899), (201, 201)),
    ((900, 905), (202, 202)),
    ((906, 911), (203, 203)),
    ((912, 917), (204, 204)),
    ((918, 923), (205, 205)),
    ((924, 924), (206, 206)),
    ((925, 925), (207, 207)),
    ((926, 926), (208, 208)),
    ((939, 943), (211, 211)),
    ((945, 950), (213, 213)),
    ((951, 956), (214, 214)),
    ((957, 962), (215, 215)),
    ((963, 968), (216, 216)),
    ((969, 974), (217, 217)),
    ((975, 980), (218, 218)),
    ((981, 981), (219, 219)),
    ((982, 982), (220, 220)),
    ((983, 983), (221, 221)),
    ((996, 1000), (224, 224)),
    ((1002, 1007), (226, 226)),
    ((1008, 1013), (227, 227)),
    ((1014, 1019), (228, 228)),
    ((1020, 1025), (229, 229)),
    ((1026, 1031), (230, 230)),
    ((1032, 1037), (231, 231)),
    ((1038, 1038), (232, 232)),
    ((1039, 1039), (233, 233)),
    ((1040, 1040), (234, 234)),
    ((1041, 1041), (235, 235)),
    ((1054, 1058), (238, 238)),
    ((1060, 1065), (240, 240)),
    ((1066, 1071), (241, 241)),
    ((1072, 1077), (242, 242)),
    ((1078, 1083), (243, 243)),
    ((1084, 1089), (244, 244)),
    ((1090, 1095), (245, 245)),
    ((1096, 1096), (246, 246)),
    ((1097, 1097), (247, 247)),
    ((1098, 1098), (248, 248)),
    ((1099, 1099), (249, 249)),
    ((1112, 1116), (252, 252)),
    ((1118, 1123), (254, 254)),
    ((1124, 1129), (255, 255)),
    ((1130, 1135), (256, 256)),
    ((1136, 1141), (257, 257)),
    ((1142, 1147), (258, 258)),
    ((1148, 1153), (259, 259)),
    ((1154, 1154), (260, 260)),
    ((1155, 1155), (261, 261)),
    ((1156, 1156), (262, 262)),
    ((1157, 1157), (263, 263)),
    ((1170, 1174), (266, 266)),
    ((1176, 1181), (268, 268)),
    ((1182, 1187), (269, 269)),
    ((1188, 1193), (270, 270)),
    ((1194, 1199), (271, 271)),
    ((1200, 1205), (272, 272)),
    ((1206, 1211), (273, 273)),
    ((1212, 1212), (274, 274)),
    ((1213, 1213), (275, 275)),
    ((1214, 1214), (276, 276)),
    ((1215, 1215), (277, 277)),
)
