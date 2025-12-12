"""Tests for tool manifest validation.

Verifies that tool_manifest.json5 is valid, complete, and conforms to schema.

Author: ALM Constitutional Engine Tests
Version: 0.1.0
"""

import json
import pytest
from pathlib import Path


# TODO: Import modules once implemented
# from alm.mod.tool_registry import ToolRegistry


class TestManifestSyntax:
    """Test manifest syntax and parsing."""

    def test_manifest_exists(self):
        """Verify tool_manifest.json5 exists."""
        manifest_path = Path("tools/tool_manifest.json5")
        assert manifest_path.exists(), "tool_manifest.json5 not found"

    def test_manifest_parseable(self):
        """Verify manifest can be parsed as JSON5."""
        manifest_path = Path("tools/tool_manifest.json5")

        # Try JSON5 first, fall back to JSON
        try:
            import json5
            with open(manifest_path) as f:
                data = json5.load(f)
        except ImportError:
            with open(manifest_path) as f:
                data = json.load(f)

        assert isinstance(data, dict)
        assert "tools" in data

    def test_manifest_has_version(self):
        """Verify manifest has version field."""
        # TODO: Load manifest and check version
        pass


class TestManifestSchema:
    """Test manifest conforms to schema."""

    def test_schema_exists(self):
        """Verify tool_manifest.schema.json5 exists."""
        schema_path = Path("mgfts/meta_schemas/tool_manifest.schema.json5")
        assert schema_path.exists(), "tool_manifest.schema.json5 not found"

    def test_manifest_validates_against_schema(self):
        """Verify manifest conforms to schema."""
        # TODO: Use jsonschema to validate
        # - Load manifest
        # - Load schema
        # - Validate
        pass


class TestToolDefinitions:
    """Test individual tool definitions."""

    def test_all_tools_have_unique_names(self):
        """Verify all tool names are unique."""
        # TODO: Load manifest and check uniqueness
        pass

    def test_all_tools_have_required_fields(self):
        """Verify all tools have required fields."""
        # TODO: Check each tool has:
        # - name, language, entry, version, category
        # - description, capabilities, targets_layers
        # - inputs, outputs, deterministic, config
        pass

    def test_all_tools_are_deterministic(self):
        """Verify all tools have deterministic: true."""
        # TODO: Check deterministic flag
        pass

    def test_layer_targets_valid(self):
        """Verify layer targets are 1-7."""
        # TODO: Check all layer_targets values are in range [1, 7]
        pass

    def test_categories_valid(self):
        """Verify categories are from approved list."""
        valid_categories = [
            "structural", "content", "semantic", "schema",
            "meta_schema", "ontological", "utility"
        ]
        # TODO: Check all categories are in valid_categories
        pass


class TestManifestIntegrity:
    """Test manifest integrity and consistency."""

    def test_entry_paths_exist(self):
        """Verify all tool entry paths exist."""
        # TODO: For each tool, check that entry path exists
        # (relative to /tools/)
        pass

    def test_no_circular_dependencies(self):
        """Verify no circular tool dependencies."""
        # TODO: Build dependency graph and detect cycles
        pass

    def test_dependencies_exist(self):
        """Verify all tool dependencies exist in manifest."""
        # TODO: Check that dependency names are valid tool names
        pass


# Pytest configuration
pytest_plugins = []


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
