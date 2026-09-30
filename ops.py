from pathlib import Path
import sys, zipfile, hashlib, json, subprocess, os
root = Path(__file__).resolve().parent
def commit():
    return os.environ.get("GITHUB_SHA") or subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
cmd = sys.argv[1]
if cmd == "build":
    compile((root / "app.py").read_text(), "app.py", "exec")
    (root / "dist").mkdir(exist_ok=True)
    with zipfile.ZipFile(root / "dist/app.zip", "w", compression=zipfile.ZIP_STORED) as z:
        z.writestr(zipfile.ZipInfo("app.py", (2026, 1, 1, 0, 0, 0)), (root / "app.py").read_bytes())
    digest = hashlib.sha256((root / "dist/app.zip").read_bytes()).hexdigest()
    (root / "dist/manifest.json").write_text(json.dumps({"commit": commit(), "artifact_sha256": digest}, indent=2))
    print("BUILD_OK", digest)
elif cmd == "deploy":
    dest = root / "staging" / sys.argv[2]
    dest.mkdir(parents=True, exist_ok=False)
    with zipfile.ZipFile(root / "dist/app.zip") as z: z.extractall(dest)
    (dest / "manifest.json").write_bytes((root / "dist/manifest.json").read_bytes())
    print("DEPLOY_SIMULADO_OK", dest.name)
elif cmd == "smoke":
    dest = root / "staging" / sys.argv[2]
    code = "from app import total; from decimal import Decimal; assert total('10.00',3)==Decimal('30.00'); print('SMOKE_OK')"
    subprocess.run([sys.executable, "-c", code], cwd=dest, check=True)
else: raise SystemExit("comando desconhecido")
