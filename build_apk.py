"""Build an installable debug APK on a machine with Flutter + Android SDK."""
from pathlib import Path
import shutil
import subprocess
import sys
root = Path(__file__).resolve().parent
flutter = shutil.which('flutter')
if not flutter:
    raise SystemExit('Flutter is required. Install Flutter + Android SDK, or use the included GitHub Actions workflow.')
subprocess.run([sys.executable, str(root / 'setup_android.py')], cwd=root, check=True)
subprocess.run([flutter, 'analyze'], cwd=root, check=True)
subprocess.run([flutter, 'build', 'apk', '--debug'], cwd=root, check=True)
output = root / 'build/app/outputs/flutter-apk/app-debug.apk'
if not output.is_file():
    raise SystemExit('Build did not produce an APK.')
shutil.copy2(output, root / 'MyChat.apk')
print('Created:', root / 'MyChat.apk')
