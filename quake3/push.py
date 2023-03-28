from pathlib import Path
import shutil

dst = Path(R'C:\Program Files (x86)\GOG Galaxy\Games\Quake III\baseq3\q3config.cfg')
this_dir = Path(__file__).parent
src = this_dir / dst.name

shutil.copyfile(src, dst)
