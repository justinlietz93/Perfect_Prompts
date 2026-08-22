#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--claim-id', required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()

    claim = args.claim_id.upper()
    source = f'''# {claim}: replace this entire cell with one honest claim attack.\nimport numpy as np\nimport matplotlib.pyplot as plt\n\nCLAIM_ID = "{claim}"\nthreshold = REPLACE_ME\nnegative_control = REPLACE_ME\n\n# Compute exact numeric metrics here. No file I/O.\nmetric = REPLACE_ME\ncontrol_metric = REPLACE_ME\npassed = bool(REPLACE_ME)\n\nfig, ax = plt.subplots()\n# Draw one decision figure with readable labels and direct interpretation.\nREPLACE_ME\nax.set_title(f"{{CLAIM_ID}} decision figure")\nplt.show()\n\nprint({{"claim_id": CLAIM_ID, "metric": metric, "threshold": threshold,\n       "negative_control": control_metric}})\nprint("PASS" if passed else "FAIL")\n'''
    notebook = {
        'cells': [{
            'cell_type': 'code',
            'execution_count': None,
            'metadata': {'claim_id': claim},
            'outputs': [],
            'source': source.splitlines(keepends=True),
        }],
        'metadata': {
            'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'},
            'language_info': {'name': 'python', 'version': '3'},
        },
        'nbformat': 4,
        'nbformat_minor': 5,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if args.output.exists():
        raise SystemExit(f'refusing to overwrite: {args.output}')
    args.output.write_text(json.dumps(notebook, indent=2) + '\n', encoding='utf-8')
    print(args.output)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
