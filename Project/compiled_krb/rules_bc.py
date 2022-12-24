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
        with engine.prove('questions', 'extraversion_1', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.extraversion_questions: got unexpected plan from when clause 1"
            with engine.prove('questions', 'extraversion_2', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.extraversion_questions: got unexpected plan from when clause 2"
                with engine.prove('questions', 'extraversion_3', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.extraversion_questions: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'extraversion_4', context,
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
        with engine.prove('questions', 'gender', context,
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
        with engine.prove('questions', 'age', context,
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
    ((262, 262), (53, 53)),
    ((266, 266), (54, 54)),
    ((284, 288), (57, 57)),
    ((290, 295), (59, 59)),
    ((308, 312), (62, 62)),
    ((314, 319), (64, 64)),
    ((332, 336), (67, 67)),
    ((338, 343), (69, 69)),
    ((344, 349), (70, 70)),
    ((350, 355), (71, 71)),
    ((356, 361), (72, 72)),
    ((362, 367), (73, 73)),
    ((368, 373), (74, 74)),
    ((374, 379), (75, 75)),
    ((380, 380), (76, 76)),
    ((381, 381), (77, 77)),
    ((382, 382), (78, 78)),
    ((383, 383), (79, 79)),
    ((396, 400), (82, 82)),
    ((402, 407), (84, 84)),
    ((408, 413), (85, 85)),
    ((414, 419), (86, 86)),
    ((420, 425), (87, 87)),
    ((426, 431), (88, 88)),
    ((432, 437), (89, 89)),
    ((438, 438), (90, 90)),
    ((439, 439), (91, 91)),
    ((440, 440), (92, 92)),
    ((441, 441), (93, 93)),
    ((454, 458), (96, 96)),
    ((460, 465), (98, 98)),
    ((466, 471), (99, 99)),
    ((472, 477), (100, 100)),
    ((478, 483), (101, 101)),
    ((484, 489), (102, 102)),
    ((490, 495), (103, 103)),
    ((496, 496), (104, 104)),
    ((497, 497), (105, 105)),
    ((498, 498), (106, 106)),
    ((499, 499), (107, 107)),
    ((512, 516), (110, 110)),
    ((518, 523), (112, 112)),
    ((524, 529), (113, 113)),
    ((530, 535), (114, 114)),
    ((536, 541), (115, 115)),
    ((542, 547), (116, 116)),
    ((548, 553), (117, 117)),
    ((554, 554), (118, 118)),
    ((555, 555), (119, 119)),
    ((556, 556), (120, 120)),
    ((557, 557), (121, 121)),
    ((570, 574), (124, 124)),
    ((576, 581), (126, 126)),
    ((582, 587), (127, 127)),
    ((588, 593), (128, 128)),
    ((594, 599), (129, 129)),
    ((600, 605), (130, 130)),
    ((606, 611), (131, 131)),
    ((612, 612), (132, 132)),
    ((613, 613), (133, 133)),
    ((614, 614), (134, 134)),
    ((615, 615), (135, 135)),
    ((628, 632), (138, 138)),
    ((634, 639), (140, 140)),
    ((640, 645), (141, 141)),
    ((646, 651), (142, 142)),
    ((652, 657), (143, 143)),
    ((658, 663), (144, 144)),
    ((664, 669), (145, 145)),
    ((670, 670), (146, 146)),
    ((671, 671), (147, 147)),
    ((672, 672), (148, 148)),
    ((685, 689), (151, 151)),
    ((691, 696), (153, 153)),
    ((697, 702), (154, 154)),
    ((703, 708), (155, 155)),
    ((709, 714), (156, 156)),
    ((715, 720), (157, 157)),
    ((721, 726), (158, 158)),
    ((727, 727), (159, 159)),
    ((728, 728), (160, 160)),
    ((729, 729), (161, 161)),
    ((730, 730), (162, 162)),
    ((743, 747), (165, 165)),
    ((749, 754), (167, 167)),
    ((755, 760), (168, 168)),
    ((761, 766), (169, 169)),
    ((767, 772), (170, 170)),
    ((773, 778), (171, 171)),
    ((779, 784), (172, 172)),
    ((785, 785), (173, 173)),
    ((786, 786), (174, 174)),
    ((787, 787), (175, 175)),
    ((800, 804), (178, 178)),
    ((806, 811), (180, 180)),
    ((812, 817), (181, 181)),
    ((818, 823), (182, 182)),
    ((824, 829), (183, 183)),
    ((830, 835), (184, 184)),
    ((836, 841), (185, 185)),
    ((842, 842), (186, 186)),
    ((843, 843), (187, 187)),
    ((844, 844), (188, 188)),
    ((845, 845), (189, 189)),
    ((858, 862), (192, 192)),
    ((864, 869), (194, 194)),
    ((870, 875), (195, 195)),
    ((876, 881), (196, 196)),
    ((882, 887), (197, 197)),
    ((888, 893), (198, 198)),
    ((894, 899), (199, 199)),
    ((900, 900), (200, 200)),
    ((901, 901), (201, 201)),
    ((902, 902), (202, 202)),
    ((915, 919), (205, 205)),
    ((921, 926), (207, 207)),
    ((927, 932), (208, 208)),
    ((933, 938), (209, 209)),
    ((939, 944), (210, 210)),
    ((945, 950), (211, 211)),
    ((951, 956), (212, 212)),
    ((957, 957), (213, 213)),
    ((958, 958), (214, 214)),
    ((959, 959), (215, 215)),
    ((972, 976), (218, 218)),
    ((978, 983), (220, 220)),
    ((984, 989), (221, 221)),
    ((990, 995), (222, 222)),
    ((996, 1001), (223, 223)),
    ((1002, 1007), (224, 224)),
    ((1008, 1013), (225, 225)),
    ((1014, 1014), (226, 226)),
    ((1015, 1015), (227, 227)),
    ((1016, 1016), (228, 228)),
    ((1017, 1017), (229, 229)),
    ((1030, 1034), (232, 232)),
    ((1036, 1041), (234, 234)),
    ((1042, 1047), (235, 235)),
    ((1048, 1053), (236, 236)),
    ((1054, 1059), (237, 237)),
    ((1060, 1065), (238, 238)),
    ((1066, 1071), (239, 239)),
    ((1072, 1072), (240, 240)),
    ((1073, 1073), (241, 241)),
    ((1074, 1074), (242, 242)),
    ((1075, 1075), (243, 243)),
    ((1088, 1092), (246, 246)),
    ((1094, 1099), (248, 248)),
    ((1100, 1105), (249, 249)),
    ((1106, 1111), (250, 250)),
    ((1112, 1117), (251, 251)),
    ((1118, 1123), (252, 252)),
    ((1124, 1129), (253, 253)),
    ((1130, 1130), (254, 254)),
    ((1131, 1131), (255, 255)),
    ((1132, 1132), (256, 256)),
    ((1133, 1133), (257, 257)),
    ((1146, 1150), (260, 260)),
    ((1152, 1157), (262, 262)),
    ((1158, 1163), (263, 263)),
    ((1164, 1169), (264, 264)),
    ((1170, 1175), (265, 265)),
    ((1176, 1181), (266, 266)),
    ((1182, 1187), (267, 267)),
    ((1188, 1188), (268, 268)),
    ((1189, 1189), (269, 269)),
    ((1190, 1190), (270, 270)),
    ((1191, 1191), (271, 271)),
)
