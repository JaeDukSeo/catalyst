from importlib.util import module_from_spec, spec_from_file_location
import os
import pathlib
import shutil
import sys

from .misc import get_utcnow_time


def import_module(expdir: pathlib.Path):
    """
    @TODO: Docs. Contribution is welcome
    """
    # @TODO: better PYTHONPATH handling
    if not isinstance(expdir, pathlib.Path):
        expdir = pathlib.Path(expdir)
    sys.path.insert(0, str(expdir.absolute()))
    sys.path.insert(0, os.path.dirname(str(expdir.absolute())))
    s = spec_from_file_location(
        expdir.name,
        str(expdir.absolute() / "__init__.py"),
        submodule_search_locations=[expdir.absolute()],
    )
    m = module_from_spec(s)
    s.loader.exec_module(m)
    sys.modules[expdir.name] = m
    return m


def _tricky_dir_copy(dir_from, dir_to):
    os.makedirs(dir_to, exist_ok=True)
    shutil.rmtree(dir_to)
    shutil.copytree(dir_from, dir_to)


def dump_code(expdir, logdir):
    """
    @TODO: Docs. Contribution is welcome
    """
    expdir = expdir[:-1] if expdir.endswith("/") else expdir
    new_src_dir = f"code"

    # @TODO: hardcoded
    old_pro_dir = os.path.dirname(os.path.abspath(__file__)) + "/../"
    new_pro_dir = os.path.join(logdir, new_src_dir, "catalyst")
    _tricky_dir_copy(old_pro_dir, new_pro_dir)

    old_expdir = os.path.abspath(expdir)
    expdir_ = os.path.basename(old_expdir)
    new_expdir = os.path.join(logdir, new_src_dir, expdir_)
    _tricky_dir_copy(old_expdir, new_expdir)


def dump_python_files(src, dst):
    """
    @TODO: Docs. Contribution is welcome
    """
    py_files = list(src.glob("*.py"))
    ipynb_files = list(src.glob("*.ipynb"))

    py_files += ipynb_files
    py_files = list(set(py_files))
    for py_file in py_files:
        shutil.copy2(f"{str(py_file.absolute())}", f"{dst}/{py_file.name}")


def import_experiment_and_runner(expdir: pathlib.Path):
    """
    @TODO: Docs. Contribution is welcome
    """
    if not isinstance(expdir, pathlib.Path):
        expdir = pathlib.Path(expdir)
    m = import_module(expdir)
    Experiment, Runner = m.Experiment, m.Runner
    return Experiment, Runner


def dump_base_experiment_code(src: pathlib.Path, dst: pathlib.Path):
    """
    @TODO: Docs. Contribution is welcome
    """
    utcnow = get_utcnow_time()
    dst_ = dst.joinpath("code")
    dst = dst.joinpath(f"code-{utcnow}") if dst_.exists() else dst_
    os.makedirs(dst, exist_ok=True)
    dump_python_files(src, dst)


__all__ = [
    "import_module",
    "dump_code",
    "dump_python_files",
    "import_experiment_and_runner",
    "dump_base_experiment_code",
]
