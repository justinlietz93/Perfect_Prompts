#!/usr/bin/env bash
set -euo pipefail

cd docbuild
lake update ReviewReadyTemplate
lake update doc-gen4
lake build ReviewReadyTemplate:docs
