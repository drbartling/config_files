from pathlib import Path
import shutil

src = Path(R'C:\Program Files (x86)\GOG Galaxy\Games\Unreal Tournament GOTY\System\user.ini')
this_dir = Path(__file__).parent
dst = this_dir / src.name

shutil.copyfile(src, dst)
