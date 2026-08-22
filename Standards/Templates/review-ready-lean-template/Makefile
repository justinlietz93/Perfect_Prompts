build:
	lake build

test:
	lake test

lint:
	lake lint

audit:
	bash scripts/audit_axioms.sh

checker:
	lake exe lean4checker --fresh ReviewReadyTemplate

docs:
	bash scripts/build_docs.sh

manifest:
	python scripts/recompute_sha256.py
