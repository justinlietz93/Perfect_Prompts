#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--claim-id", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    if args.output.exists():
        raise SystemExit(f"refusing to overwrite {args.output}")

    source_lines = [
        f"# {args.claim_id}: {args.title}",
        "# Replace placeholder computations. No file I/O is allowed here.",
        "import numpy as np",
        "import matplotlib.pyplot as plt",
        "",
        f"CLAIM_ID = {args.claim_id!r}",
        "THRESHOLD = 0.0  # REPLACE_ME",
        "",
        "def evaluate_claim():",
        "    raise NotImplementedError('REPLACE_ME')",
        "",
        "def evaluate_negative_control():",
        "    raise NotImplementedError('REPLACE_ME')",
        "",
        "observed = float(evaluate_claim())",
        "negative_control = float(evaluate_negative_control())",
        "passed = bool(observed > THRESHOLD and negative_control <= THRESHOLD)",
        "",
        "print({'claim_id': CLAIM_ID, 'observed': observed, 'negative_control': negative_control, 'threshold': THRESHOLD, 'decision': 'PASS' if passed else 'FAIL'})",
        "",
        "fig, ax = plt.subplots()",
        "ax.bar(['claim', 'negative control'], [observed, negative_control])",
        "ax.axhline(THRESHOLD, linestyle='--', label='threshold')",
        "ax.set_ylabel('REPLACE_ME metric')",
        "ax.set_title(f'{CLAIM_ID} decision figure')",
        "ax.legend()",
        "plt.show()",
        "",
        "assert passed, f'{CLAIM_ID} FAIL'",
    ]
    notebook = {
        "cells": [
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {
                    "claim_id": args.claim_id,
                    "contract": "one-cell-per-claim",
                },
                "outputs": [],
                "source": [line + "\n" for line in source_lines],
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3"},
            "orchestra_notebook_contract": "2.0.0",
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(notebook, indent=2) + "\n", encoding="utf-8")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
