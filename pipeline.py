from pathlib import Path
import subprocess, sys, json, datetime, platform, hashlib, time, os
root = Path(__file__).resolve().parent
run_id = sys.argv[1]
dest = root / "evidence" / run_id
dest.mkdir(parents=True, exist_ok=False)
steps = [
    ("preparacao", [sys.executable, "-m", "pip", "install", "--no-index", "-r", "requirements.txt"]),
    ("testes", [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"]),
    ("build", [sys.executable, "ops.py", "build"]),
    ("deploy_simulado", [sys.executable, "ops.py", "deploy", run_id]),
    ("smoke", [sys.executable, "ops.py", "smoke", run_id])]
commit = os.environ.get("GITHUB_SHA") or subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
result = {"id": run_id, "commit": commit, "study_date": "2026-09-30", "executed_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "github_run_id": os.environ.get("GITHUB_RUN_ID"), "github_run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT"), "github_event": os.environ.get("GITHUB_EVENT_NAME"), "run_url": (os.environ.get("GITHUB_SERVER_URL", "https://github.com") + "/" + os.environ["GITHUB_REPOSITORY"] + "/actions/runs/" + os.environ["GITHUB_RUN_ID"]) if os.environ.get("GITHUB_RUN_ID") else None, "source_sha256": hashlib.sha256((root / "app.py").read_bytes()).hexdigest(), "environment": platform.platform(), "python": platform.python_version(), "steps": []}
blocked = False
for name, cmd in steps:
    if blocked:
        result["steps"].append({"name": name, "status": "skipped"})
        continue
    start = time.perf_counter()
    proc = subprocess.run(cmd, cwd=root, capture_output=True, text=True)
    log = proc.stdout + proc.stderr
    (dest / (name + ".log")).write_text(log, encoding="utf-8")
    result["steps"].append({"name": name, "status": "passed" if proc.returncode == 0 else "failed", "exit_code": proc.returncode, "seconds": round(time.perf_counter()-start, 4)})
    blocked = proc.returncode != 0
result["status"] = "failed" if blocked else "passed"
result["deployment_exists"] = (root / "staging" / run_id).exists()
if not blocked:
    result["artifact_sha256"] = hashlib.sha256((root / "dist/app.zip").read_bytes()).hexdigest()
(dest / "result.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps(result))
raise SystemExit(1 if blocked else 0)
