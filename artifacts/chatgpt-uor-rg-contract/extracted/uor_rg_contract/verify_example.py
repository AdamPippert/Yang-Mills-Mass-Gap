import json,hashlib,sys
from pathlib import Path
from fractions import Fraction
from jsonschema import Draft202012Validator
root=Path(__file__).parent
schema=json.loads((root/'contract.schema.json').read_text())
doc=json.loads((root/'example.jsonld').read_text())
def digest(o): return 'sha256:'+hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def f(s): return Fraction(s)
entries={x['digest']:x['payload'] for x in doc['objects']}
for x in doc['objects']:
    Draft202012Validator(schema).validate(x['payload'])
    assert digest(x['payload'])==x['digest']
    assert x['id']=='urn:sha256:'+x['digest'][7:]
t=next(x for x in entries.values() if x['kind']=='RGTransition')
s=entries[t['source']]; d=entries[t['target']]
assert d['k']==s['k']+1
assert f(d['a'])==t['blockFactor']*f(s['a'])
assert s['boxLength']==t['blockFactor']*d['boxLength']
assert s['volumeSites']==s['boxLength']**4 and d['volumeSites']==d['boxLength']**4
assert entries[t['sourceAction']]['scaleState']==t['source']
assert entries[t['targetAction']]['scaleState']==t['target']
assert entries[t['observable']]['algebraId']=='su2-wilson-loop-algebra/v1'
assert t['leanProof'] in entries
for c in t['constantEnvelope']:
    assert c['scope']=='uniform_all_a_L'
    assert not set(c['freeVariables']) & {'a','L','a_k','volume','box_length'}
    assert f(c['value']['lo'])<=f(c['value']['hi'])
assert {c['name'] for c in t['constantEnvelope']}=={'C','m','g_bound'}
print('PASS structural checks; NOT certified: unresolved certificate hashes, absent Lean build and analytic uniformity proofs')
