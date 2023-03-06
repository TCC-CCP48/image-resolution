import os
import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

python_dir = os.path.dirname(sys.executable)

include_files = [
    os.path.join(python_dir, "python3.dll"),
    os.path.join(python_dir, "python37.dll"),
    os.path.join(python_dir, "vcruntime140.dll")
]

options = {
    "build_exe": {
        'include_files': include_files,
        'include_msvcr': True,
    }
}

setup(
    name="IVision",
    version="1.0",
    description="Redimensionamento de imagens por IA",
    options=options,
    executables=[Executable("<caminho_arquivo>", base=base)]
)
