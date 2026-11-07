"""Run with Python 3 on a computer with Flutter and Android SDK installed."""
import pathlib, re, shutil, subprocess, tempfile
root = pathlib.Path(__file__).resolve().parent
flutter = shutil.which('flutter')
if not flutter:
    raise SystemExit('Install Flutter and add it to PATH first.')
# Generate in a temporary directory so the existing Dart source is preserved.
with tempfile.TemporaryDirectory() as temp:
    generated = pathlib.Path(temp) / 'mychat'
    subprocess.run([flutter, 'create', '--platforms=android', '--org=com.chandravir', '--project-name=mychat', str(generated)], check=True)
    config = (root / 'android/app/google-services.json').read_bytes()
    shutil.copytree(generated / 'android', root / 'android', dirs_exist_ok=True)
    (root / 'android/app/google-services.json').write_bytes(config)
    shutil.copytree(generated / '.metadata', root / '.metadata') if (generated / '.metadata').is_dir() else shutil.copy2(generated / '.metadata', root / '.metadata')
app = root / 'android/app'
gradle = app / 'build.gradle.kts'
if not gradle.exists():
    gradle = app / 'build.gradle'
s = gradle.read_text()
s, count = re.subn(r'(applicationId\s*(?:=\s*)?)[\"\'][^\"\']+[\"\']', r'\1"com.chandravir.HelloApp"', s)
if count != 1:
    raise SystemExit('Could not set Android applicationId. Inspect app build.gradle.')
gradle.write_text(s)
manifest = app / 'src/main/AndroidManifest.xml'
s = manifest.read_text().replace('android:label="mychat"', 'android:label="MyChat"')
if 'android.permission.INTERNET' not in s:
    s = s.replace('<application', '<uses-permission android:name="android.permission.INTERNET"/>\n    <application', 1)
manifest.write_text(s)
subprocess.run([flutter, 'pub', 'get'], cwd=root, check=True)
print('Android setup complete: com.chandravir.HelloApp. Next: flutter run')
