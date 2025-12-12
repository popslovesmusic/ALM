"""ALM Constitutional Engine - Tool Registry

This module implements tool discovery and registry management.

The Tool Registry:
- Loads tool_manifest.json5
- Validates against tool_manifest.schema.json5
- Builds internal data structures for efficient lookup
- Provides tool selection logic
- Manages tool execution

Author: ALM Constitutional Engine
Version: 0.1.0
"""

from typing import Any, Dict, List, Optional, Set
from pathlib import Path
import json
import subprocess


class Tool:
    """Represents a single analysis tool."""

    def __init__(self, definition: Dict[str, Any]):
        """Initialize tool from manifest definition.

        Parameters
        ----------
        definition : dict
            Tool definition from manifest
        """
        self.name = definition["name"]
        self.language = definition["language"]
        self.entry = definition["entry"]
        self.version = definition["version"]
        self.category = definition["category"]
        self.description = definition["description"]
        self.capabilities = definition["capabilities"]
        self.targets_layers = definition["targets_layers"]
        self.inputs = definition["inputs"]
        self.outputs = definition["outputs"]
        self.deterministic = definition["deterministic"]
        self.config = definition.get("config", {})
        self.dependencies = definition.get("dependencies", [])
        self.optional = definition.get("optional", False)
        self.timeout_ms = definition.get("timeout_ms", 60000)

    def __repr__(self) -> str:
        return f"Tool({self.name} v{self.version}, layers={self.targets_layers})"


class ToolRegistry:
    """Registry for managing analysis tools.

    Provides:
    - Tool discovery from manifest
    - Tool lookup by name, layer, category
    - Tool selection logic
    - Tool execution management
    """

    def __init__(self, tools_root: Path, mgfts_root: Optional[Path] = None):
        """Initialize tool registry.

        Parameters
        ----------
        tools_root : Path
            Root directory containing /tools/
        mgfts_root : Path, optional
            Root directory containing MGFTS installation
        """
        self.tools_root = tools_root
        self.mgfts_root = mgfts_root
        self.manifest_path = tools_root / "tool_manifest.json5"

        # Registry data structures
        self.tools_by_name: Dict[str, Tool] = {}
        self.tools_by_layer: Dict[int, List[Tool]] = {i: [] for i in range(1, 8)}
        self.tools_by_category: Dict[str, List[Tool]] = {}

        # Load manifest
        self._load_manifest()

    def _load_manifest(self) -> None:
        """Load and parse tool manifest."""
        if not self.manifest_path.exists():
            raise FileNotFoundError(f"Tool manifest not found: {self.manifest_path}")

        try:
            # Load JSON5 (fallback to JSON if json5 not available)
            with open(self.manifest_path) as f:
                try:
                    import json5
                    manifest = json5.load(f)
                except ImportError:
                    # Fallback to JSON (comments will cause errors)
                    manifest = json.load(f)

            # Parse tools
            for tool_def in manifest.get("tools", []):
                tool = Tool(tool_def)

                # Validate determinism requirement
                if not tool.deterministic:
                    print(f"Warning: Tool {tool.name} is not deterministic, skipping")
                    continue

                # Register tool
                self.tools_by_name[tool.name] = tool

                # Index by layer
                for layer in tool.targets_layers:
                    if 1 <= layer <= 7:
                        self.tools_by_layer[layer].append(tool)

                # Index by category
                if tool.category not in self.tools_by_category:
                    self.tools_by_category[tool.category] = []
                self.tools_by_category[tool.category].append(tool)

        except Exception as e:
            raise RuntimeError(f"Failed to load tool manifest: {e}")

    def get_tool(self, name: str) -> Optional[Tool]:
        """Get tool by name.

        Parameters
        ----------
        name : str
            Tool name

        Returns
        -------
        Tool or None
            Tool instance if found
        """
        return self.tools_by_name.get(name)

    def get_tools_for_layer(self, layer: int) -> List[Tool]:
        """Get all tools that analyze a specific layer.

        Parameters
        ----------
        layer : int
            MGFTS layer (1-7)

        Returns
        -------
        list of Tool
            Tools targeting this layer
        """
        return self.tools_by_layer.get(layer, [])

    def get_tools_by_category(self, category: str) -> List[Tool]:
        """Get all tools in a category.

        Parameters
        ----------
        category : str
            Tool category

        Returns
        -------
        list of Tool
            Tools in this category
        """
        return self.tools_by_category.get(category, [])

    def select_tools(
        self,
        project_state: Dict[str, Any],
        requested_layers: Optional[List[int]] = None
    ) -> List[Tool]:
        """Select appropriate tools based on project state.

        Parameters
        ----------
        project_state : dict
            Current project state information
        requested_layers : list of int, optional
            Specific layers to analyze (default: all)

        Returns
        -------
        list of Tool
            Selected tools in execution order
        """
        selected: List[Tool] = []
        selected_names: Set[str] = set()

        # Determine layers to analyze
        if requested_layers is None:
            requested_layers = list(range(1, 8))

        # Always run structural tools first
        if 1 in requested_layers:
            for tool in self.get_tools_for_layer(1):
                if tool.name not in selected_names:
                    selected.append(tool)
                    selected_names.add(tool.name)

        # Run governance tools if Layer 2 requested
        if 2 in requested_layers:
            for tool in self.get_tools_for_layer(2):
                if tool.name not in selected_names:
                    selected.append(tool)
                    selected_names.add(tool.name)

        # Run schema tools if Layer 3 requested and schemas present
        if 3 in requested_layers:
            has_schemas = project_state.get("has_schemas", False)
            if has_schemas:
                for tool in self.get_tools_for_layer(3):
                    if tool.name not in selected_names:
                        selected.append(tool)
                        selected_names.add(tool.name)

        # Run semantic tools if Layer 4 requested and concept vault present
        if 4 in requested_layers:
            has_concept_vault = project_state.get("has_concept_vault", False)
            if has_concept_vault:
                for tool in self.get_tools_for_layer(4):
                    if tool.name not in selected_names:
                        selected.append(tool)
                        selected_names.add(tool.name)

        # Run remaining layers tools
        for layer in [5, 6, 7]:
            if layer in requested_layers:
                for tool in self.get_tools_for_layer(layer):
                    if tool.name not in selected_names and not tool.optional:
                        selected.append(tool)
                        selected_names.add(tool.name)

        # Always run coherence and concealment calculators last
        for name in ["coherence_calculator", "concealment_calculator"]:
            tool = self.get_tool(name)
            if tool and name not in selected_names:
                selected.append(tool)
                selected_names.add(name)

        return selected

    def execute_tool(
        self,
        tool: Tool,
        config: Dict[str, Any]
    ) -> Optional[Dict[str, Any]]:
        """Execute a tool with given configuration.

        Parameters
        ----------
        tool : Tool
            Tool to execute
        config : dict
            Configuration including project_path, mgfts_root, etc.

        Returns
        -------
        dict or None
            Tool output (JSON), or None if execution failed
        """
        # Build full path to tool
        tool_path = self.tools_root / tool.entry

        if not tool_path.exists():
            print(f"Error: Tool not found: {tool_path}")
            return None

        # Prepare input JSON
        input_data = json.dumps(config)

        try:
            # Execute tool
            if tool.language == "python":
                result = subprocess.run(
                    ["python", str(tool_path)],
                    input=input_data,
                    capture_output=True,
                    text=True,
                    timeout=tool.timeout_ms / 1000
                )
            elif tool.language in ["javascript", "js"]:
                result = subprocess.run(
                    ["node", str(tool_path)],
                    input=input_data,
                    capture_output=True,
                    text=True,
                    timeout=tool.timeout_ms / 1000
                )
            else:
                print(f"Error: Unsupported language: {tool.language}")
                return None

            # Check for errors
            if result.returncode != 0:
                print(f"Tool {tool.name} failed:")
                print(f"  stdout: {result.stdout}")
                print(f"  stderr: {result.stderr}")
                return None

            # Parse JSON output
            output = json.loads(result.stdout)
            return output

        except subprocess.TimeoutExpired:
            print(f"Tool {tool.name} timed out after {tool.timeout_ms}ms")
            return None
        except json.JSONDecodeError as e:
            print(f"Tool {tool.name} produced invalid JSON: {e}")
            print(f"  output: {result.stdout}")
            return None
        except Exception as e:
            print(f"Tool {tool.name} execution failed: {e}")
            return None

    def list_tools(self) -> List[str]:
        """List all registered tool names.

        Returns
        -------
        list of str
            Tool names
        """
        return list(self.tools_by_name.keys())

    def get_statistics(self) -> Dict[str, Any]:
        """Get registry statistics.

        Returns
        -------
        dict
            Statistics about registered tools
        """
        return {
            "total_tools": len(self.tools_by_name),
            "tools_by_layer": {
                layer: len(tools) for layer, tools in self.tools_by_layer.items()
            },
            "tools_by_category": {
                cat: len(tools) for cat, tools in self.tools_by_category.items()
            },
            "languages": list(set(t.language for t in self.tools_by_name.values()))
        }
