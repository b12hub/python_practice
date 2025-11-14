#!/usr/bin/env python3
import json, os, subprocess, sys, datetime, shutil

def run_cmd(cmd):
    try:
        print("Running:", cmd)
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
        print(res.stdout)
        if res.returncode != 0:
            print("ERROR:", res.stderr)
        return res.returncode == 0, res.stdout + "\\n" + res.stderr
    except Exception as e:
        return False, str(e)

modules = [
  {"name":"A-auth","schema_cmd":"tools/validate_schema.sh services/a-auth","contract_cmd":"pact-broker publish --consumer-version 1.0","tests_cmd":"pytest services/a-auth/tests -q"},
  {"name":"A-gateway","schema_cmd":"tools/validate_schema.sh services/a-gateway","tests_cmd":"pytest services/a-gateway/tests -q"},
  {"name":"B-processor","schema_cmd":"tools/validate_schema.sh services/b-processor","contract_cmd":"pact-broker publish --consumer-version 1.0","tests_cmd":"pytest services/b-processor/tests -q"},
  {"name":"B-queue","schema_cmd":"tools/validate_schema.sh services/b-queue","tests_cmd":"pytest services/b-queue/tests -q"},
  {"name":"C-analytics","schema_cmd":"tools/validate_schema.sh services/c-analytics","tests_cmd":"pytest services/c-analytics/tests -q"},
  {"name":"D-security","schema_cmd":"tools/validate_schema.sh services/d-security","tests_cmd":"pytest services/d-security/tests -q"},
  {"name":"D-gateway","schema_cmd":"tools/validate_schema.sh services/d-gateway","tests_cmd":"pytest services/d-gateway/tests -q"}
]

results = []
passed = 0
for m in modules:
    name = m['name']
    print("\n--- Checking module:\n", name)
    module_ok = True
    notes = []

    # Schema validation
    schema_cmd = m.get('schema_cmd')
    if schema_cmd:
        ok, out = run_cmd(schema_cmd)
        notes.append({'schema': ok, 'out': out[:1000]})
        module_ok = module_ok and ok

    # Contract (Pact) publishing/testing (optional)
    contract_cmd = m.get('contract_cmd')
    if contract_cmd:
        ok, out = run_cmd(contract_cmd)
        notes.append({'contract': ok, 'out': out[:1000]})
        module_ok = module_ok and ok

    # Unit/Integration tests
    tests_cmd = m.get('tests_cmd')
    if tests_cmd:
        ok, out = run_cmd(tests_cmd)
        notes.append({'tests': ok, 'out': out[:1000]})
        module_ok = module_ok and ok

    results.append({'name': name, 'status': 'PASS' if module_ok else 'FAIL', 'notes': notes})
    if module_ok:
        passed += 1

integrity_percent = round(passed / len(modules) * 100, 2)
report = {
  'version': os.environ.get('BUILD_TAG','local') + '-validation',
  'timestamp': datetime.datetime.utcnow().isoformat() + 'Z',
  'integrity_percent': integrity_percent,
  'modules': results
}

out = 'integrity_report.json'
with open(out,'w') as f:
    json.dump(report, f, indent=2)
print('Wrote', out)

