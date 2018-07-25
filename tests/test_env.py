import os
from subprocess import check_output

from tf_skein import Env


def test_env_create(tmpdir):
    env = Env(
        name="test",
        packages=["pycodestyle"])
    env_zip_path = env.create(str(tmpdir))
    assert os.path.exists(env_zip_path)

    env_path, _ext = os.path.splitext(env_zip_path)
    assert os.path.exists(env_path)
    assert os.path.isdir(env_path)

    env_python_bin = os.path.join(env_path, "bin", "python")
    check_output([env_python_bin, "-m", "pycodestyle", "--version"])
