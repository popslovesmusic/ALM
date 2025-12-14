"""Shared utilities for CTL test suite."""
import json
import os
from typing import Any, Dict, List

from ctl.tensor_r_update import init_tensor_r_cell, update_tensor_r_sequence

Config = Dict[str, Any]
ChromaticCell = Dict[str, Any]


def load_tensor_r_config() -> Config:
    path = os.path.join(os.path.dirname(__file__), "../ctl/tensor_R.json5")
    with open(path, "r") as f:
        return json.load(f)


def load_coupling_config() -> Config:
    path = os.path.join(os.path.dirname(__file__), "../ctl/coupling_config.json5")
    with open(path, "r") as f:
        return json.load(f)


def build_r_sequence(l_sequence: List[ChromaticCell], config: Config = None) -> List[ChromaticCell]:
    cfg = config or load_tensor_r_config()
    if not l_sequence:
        return []
    return update_tensor_r_sequence(l_sequence, cfg)


def initialize_r_cell(l_cell: ChromaticCell, config: Config = None) -> ChromaticCell:
    cfg = config or load_tensor_r_config()
    return init_tensor_r_cell(l_cell, cfg)
