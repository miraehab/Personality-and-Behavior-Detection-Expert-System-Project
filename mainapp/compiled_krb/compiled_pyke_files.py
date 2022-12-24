# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('mainapp', '', 'facts.kfb'):
           [1671890396.7258887, 'facts.fbc'],
         ('mainapp', '', 'questions.kqb'):
           [1671890396.7338634, 'questions.qbc'],
         ('mainapp', '', 'rules.krb'):
           [1671890396.7818959, 'rules_bc.py'],
        },
        compiler_version)

