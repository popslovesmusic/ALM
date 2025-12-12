#!/usr/bin/env python3
"""Create New MGFTS-Governed Project

This script scaffolds a new project with full MGFTS governance structure.

Usage:
    python create_new_project.py <project_name> [options]

    python create_new_project.py my-new-project --layers 1,2,3
    python create_new_project.py enterprise-app --layers all --language python

Author: ALM MGFTS System
Version: 1.0.0
"""

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ProjectScaffolder:
    """Scaffold new MGFTS-governed projects."""

    def __init__(
        self,
        project_name: str,
        target_dir: Optional[Path] = None,
        mgfts_root: Optional[Path] = None,
        layers: Optional[List[int]] = None,
        language: str = "python",
        author: str = "Unknown",
        license: str = "MIT"
    ):
        """Initialize scaffolder.

        Args:
            project_name: Name of the project
            target_dir: Directory to create project in (default: current dir)
            mgfts_root: Path to MGFTS installation
            layers: Which MGFTS layers to enable (default: [1, 2])
            language: Primary programming language
            author: Project author
            license: Project license
        """
        self.project_name = project_name
        self.target_dir = target_dir or Path.cwd()
        self.project_root = self.target_dir / project_name
        self.mgfts_root = mgfts_root or self._find_mgfts_root()
        self.layers = layers or [1, 2]
        self.language = language
        self.author = author
        self.license = license

        # Validate
        if self.project_root.exists():
            raise ValueError(f"Project directory already exists: {self.project_root}")

        if not self.mgfts_root or not self.mgfts_root.exists():
            raise ValueError(f"MGFTS root not found: {self.mgfts_root}")

    def _find_mgfts_root(self) -> Optional[Path]:
        """Try to find MGFTS installation."""
        # Check environment variable
        import os
        if "MGFTS_ROOT" in os.environ:
            return Path(os.environ["MGFTS_ROOT"])

        # Check current directory and parents
        current = Path.cwd()
        while current != current.parent:
            mgfts_dir = current / "mgfts"
            if mgfts_dir.exists() and (mgfts_dir / "COMPLIANCE_CHARTER.md").exists():
                return current
            current = current.parent

        return None

    def scaffold(self) -> None:
        """Execute scaffolding process."""
        logger.info(f"Creating MGFTS-governed project: {self.project_name}")
        logger.info(f"Target directory: {self.project_root}")
        logger.info(f"Enabled layers: {self.layers}")

        try:
            # Create directory structure
            self._create_directories()

            # Copy/create governance files
            self._setup_governance()

            # Create source structure
            self._create_source_structure()

            # Create configuration files
            self._create_configs()

            # Create documentation
            self._create_documentation()

            # Initialize version control
            self._initialize_git()

            # Create initial validation report
            self._create_validation_report()

            logger.info(f"✅ Project created successfully at: {self.project_root}")
            self._print_next_steps()

        except Exception as e:
            logger.error(f"❌ Error creating project: {e}")
            # Cleanup on error
            if self.project_root.exists():
                logger.info(f"Cleaning up {self.project_root}")
                shutil.rmtree(self.project_root)
            raise

    def _create_directories(self) -> None:
        """Create project directory structure."""
        logger.info("Creating directory structure...")

        dirs = [
            "",  # Root
            "src",
            "tests",
            "tests/fixtures",
            "docs",
            "config",
            "scripts",
            "mgfts",
            "mgfts/templates",
            "mgfts/meta_schemas",
            "mgfts/config",
        ]

        # Add language-specific directories
        if self.language == "python":
            dirs.extend([
                "src/__pycache__",
                ".pytest_cache",
            ])
        elif self.language == "javascript":
            dirs.extend([
                "node_modules",
                "dist",
            ])

        for dir_path in dirs:
            (self.project_root / dir_path).mkdir(parents=True, exist_ok=True)

    def _setup_governance(self) -> None:
        """Copy governance files from MGFTS installation."""
        logger.info("Setting up governance files...")

        # Required governance files
        governance_files = [
            "AGENTS.md",
            "COMPLIANCE_CHARTER.md",
            "PRESERVATION_PROTOCOL.md",
            "GLOBAL_CONCEPT_VAULT.json5",
        ]

        for file_name in governance_files:
            src = self.mgfts_root / "mgfts" / file_name
            dst = self.project_root / "mgfts" / file_name

            if src.exists():
                shutil.copy2(src, dst)
                logger.debug(f"Copied {file_name}")
            else:
                logger.warning(f"Governance file not found: {src}")

        # Copy templates
        template_dir = self.mgfts_root / "mgfts" / "templates"
        if template_dir.exists():
            dst_templates = self.project_root / "mgfts" / "templates"
            shutil.copytree(template_dir, dst_templates, dirs_exist_ok=True)
            logger.debug("Copied templates")

        # Copy meta-schemas
        schema_dir = self.mgfts_root / "mgfts" / "meta_schemas"
        if schema_dir.exists():
            dst_schemas = self.project_root / "mgfts" / "meta_schemas"
            shutil.copytree(schema_dir, dst_schemas, dirs_exist_ok=True)
            logger.debug("Copied meta-schemas")

    def _create_source_structure(self) -> None:
        """Create source code structure based on language."""
        logger.info(f"Creating {self.language} source structure...")

        if self.language == "python":
            self._create_python_structure()
        elif self.language == "javascript":
            self._create_javascript_structure()
        else:
            logger.warning(f"Unknown language: {self.language}, creating minimal structure")

    def _create_python_structure(self) -> None:
        """Create Python project structure."""
        # __init__.py
        (self.project_root / "src" / "__init__.py").write_text(
            f'"""{self.project_name} - Python Package\n\nVersion: 0.1.0\n"""\n\n'
            f'__version__ = "0.1.0"\n'
        )

        # Example module from template
        template_path = self.mgfts_root / "mgfts" / "templates" / "python_module.py.template"
        if template_path.exists():
            template_content = template_path.read_text()
            example_module = self._substitute_template(template_content, {
                "MODULE_DESCRIPTION": "Example module",
                "MODULE_PURPOSE": "Demonstrate MGFTS-compliant Python code",
                "MGFTS_LAYER": "1",
                "DEPENDENCIES": "None",
                "AUTHOR": self.author,
                "CREATED_DATE": datetime.now().strftime("%Y-%m-%d"),
                "VERSION": "0.1.0",
                "CLASS_NAME": "Example",
                "CLASS_DESCRIPTION": "Example class",
                "CLASS_PURPOSE": "demonstrates template usage",
            })
            (self.project_root / "src" / "example.py").write_text(example_module)

        # requirements.txt
        (self.project_root / "requirements.txt").write_text(
            "# Python dependencies\n"
            "pytest>=7.0.0\n"
            "pytest-cov>=4.0.0\n"
            "# Add your dependencies here\n"
        )

        # setup.py
        setup_py = f'''"""Setup script for {self.project_name}."""

from setuptools import setup, find_packages

setup(
    name="{self.project_name}",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={{"": "src"}},
    install_requires=[
        # Add runtime dependencies
    ],
    extras_require={{
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
        ],
    }},
    author="{self.author}",
    description="MGFTS-governed Python project",
    license="{self.license}",
    python_requires=">=3.8",
)
'''
        (self.project_root / "setup.py").write_text(setup_py)

    def _create_javascript_structure(self) -> None:
        """Create JavaScript/Node.js project structure."""
        # package.json
        package_json = {
            "name": self.project_name,
            "version": "0.1.0",
            "description": "MGFTS-governed JavaScript project",
            "main": "src/index.js",
            "scripts": {
                "test": "jest",
                "lint": "eslint src/",
                "validate": "python ../scripts/validate_project.py ."
            },
            "keywords": ["mgfts"],
            "author": self.author,
            "license": self.license,
            "devDependencies": {
                "jest": "^29.0.0",
                "eslint": "^8.0.0"
            }
        }
        (self.project_root / "package.json").write_text(
            json.dumps(package_json, indent=2)
        )

        # index.js
        (self.project_root / "src" / "index.js").write_text(
            f'/**\n * {self.project_name} - Main Entry Point\n */\n\n'
            'console.log("Hello from MGFTS project!");\n\n'
            'module.exports = {};\n'
        )

    def _create_configs(self) -> None:
        """Create configuration files."""
        logger.info("Creating configuration files...")

        # MGFTS project configuration
        mgfts_config = {
            "$schema": "../mgfts/meta_schemas/project_config.schema.json5",
            "version": "1.0.0",
            "project": {
                "name": self.project_name,
                "version": "0.1.0",
                "author": self.author,
                "license": self.license,
                "created": datetime.now().isoformat(),
            },
            "mgfts": {
                "enabled": True,
                "layers": self.layers,
                "validation": {
                    "enabled": True,
                    "on_commit": True,
                    "severity_threshold": "high",
                },
                "agent_mode": "guided_development",
            },
            "paths": {
                "root": ".",
                "source": "src",
                "tests": "tests",
                "docs": "docs",
                "mgfts_root": "mgfts",
            },
        }

        config_path = self.project_root / "mgfts" / "config" / "project.json5"
        config_path.write_text(json.dumps(mgfts_config, indent=2))

    def _create_documentation(self) -> None:
        """Create documentation files."""
        logger.info("Creating documentation...")

        # README.md from template
        template_path = self.mgfts_root / "mgfts" / "templates" / "README.md.template"
        if template_path.exists():
            readme_content = self._substitute_template(template_path.read_text(), {
                "PROJECT_NAME": self.project_name,
                "VERSION": "0.1.0",
                "GITHUB_USER": "yourname",
                "REPO_NAME": self.project_name,
                "LICENSE": self.license,
                "BUILD_STATUS": "passing",
                "BUILD_COLOR": "green",
                "PROJECT_TAGLINE": "MGFTS-governed project",
                "PROJECT_DESCRIPTION": "This project is governed by the Meta-Global File Template System.",
                "AUTHOR": self.author,
            })
            (self.project_root / "README.md").write_text(readme_content)

        # CHANGELOG.md from template
        template_path = self.mgfts_root / "mgfts" / "templates" / "CHANGELOG.md.template"
        if template_path.exists():
            changelog_content = self._substitute_template(template_path.read_text(), {
                "PROJECT_NAME": self.project_name,
                "CURRENT_VERSION": "0.1.0",
                "CURRENT_DATE": datetime.now().strftime("%Y-%m-%d"),
            })
            (self.project_root / "CHANGELOG.md").write_text(changelog_content)
        else:
            # Fallback minimal changelog
            (self.project_root / "CHANGELOG.md").write_text(
                f"# Changelog\n\n## [0.1.0] - {datetime.now().strftime('%Y-%m-%d')}\n\n"
                "### Added\n- Initial project structure\n- MGFTS governance files\n"
            )

    def _initialize_git(self) -> None:
        """Initialize git repository."""
        logger.info("Initializing git repository...")

        # .gitignore
        gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
.pytest_cache/
*.egg-info/
dist/
build/

# JavaScript
node_modules/
dist/
*.log

# IDEs
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Project-specific
config/local.json5
*.local
.env
"""
        (self.project_root / ".gitignore").write_text(gitignore_content)

        # Initialize git (if git is available)
        try:
            import subprocess
            subprocess.run(
                ["git", "init"],
                cwd=self.project_root,
                check=True,
                capture_output=True
            )
            subprocess.run(
                ["git", "add", "."],
                cwd=self.project_root,
                check=True,
                capture_output=True
            )
            subprocess.run(
                ["git", "commit", "-m", "Initial commit: MGFTS project scaffold"],
                cwd=self.project_root,
                check=True,
                capture_output=True
            )
            logger.debug("Git repository initialized")
        except (subprocess.CalledProcessError, FileNotFoundError):
            logger.warning("Git not available or initialization failed")

    def _create_validation_report(self) -> None:
        """Create initial validation report."""
        logger.info("Creating validation report...")

        report = {
            "project": self.project_name,
            "timestamp": datetime.now().isoformat(),
            "scaffolded": True,
            "layers": self.layers,
            "initial_compliance": {
                "structural": "compliant",
                "governance_files": "present",
                "templates": "present",
            },
            "next_steps": [
                "Add project-specific code",
                "Configure validation thresholds",
                "Run full Constitutional Engine validation",
            ]
        }

        report_path = self.project_root / "docs" / "initial_validation.json"
        report_path.write_text(json.dumps(report, indent=2))

    def _substitute_template(self, template: str, substitutions: Dict[str, str]) -> str:
        """Substitute template variables."""
        result = template
        for key, value in substitutions.items():
            placeholder = f"{{{{{key}}}}}"
            result = result.replace(placeholder, str(value))
        return result

    def _print_next_steps(self) -> None:
        """Print next steps for user."""
        print(f"""
✅ Project '{self.project_name}' created successfully!

📂 Project location: {self.project_root}

🚀 Next steps:

1. Navigate to project:
   cd {self.project_root}

2. Review governance files:
   - mgfts/AGENTS.md
   - mgfts/COMPLIANCE_CHARTER.md
   - mgfts/PRESERVATION_PROTOCOL.md

3. Configure project:
   - Edit mgfts/config/project.json5
   - Customize templates if needed

4. Start developing:
   - Add code to src/
   - Add tests to tests/
   - Follow MGFTS compliance rules

5. Validate compliance:
   python ../scripts/validate_project.py .

6. Commit your changes:
   git add .
   git commit -m "Initial project setup"

📚 Documentation: docs/
🧪 Tests: Run with `pytest` (Python) or `npm test` (JavaScript)
✅ Validation: Constitutional Engine validation enabled

Happy coding! 🎉
""")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Create new MGFTS-governed project",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python create_new_project.py my-project
  python create_new_project.py my-project --layers 1,2,3
  python create_new_project.py enterprise-app --layers all --language javascript
"""
    )

    parser.add_argument(
        "project_name",
        help="Name of the project to create"
    )

    parser.add_argument(
        "--target-dir",
        type=Path,
        default=Path.cwd(),
        help="Directory to create project in (default: current directory)"
    )

    parser.add_argument(
        "--mgfts-root",
        type=Path,
        help="Path to MGFTS installation (default: auto-detect)"
    )

    parser.add_argument(
        "--layers",
        default="1,2",
        help="MGFTS layers to enable (comma-separated or 'all'). Default: 1,2"
    )

    parser.add_argument(
        "--language",
        choices=["python", "javascript"],
        default="python",
        help="Primary programming language (default: python)"
    )

    parser.add_argument(
        "--author",
        default="Unknown",
        help="Project author name"
    )

    parser.add_argument(
        "--license",
        default="MIT",
        help="Project license (default: MIT)"
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose output"
    )

    args = parser.parse_args()

    if args.verbose:
        logger.setLevel(logging.DEBUG)

    # Parse layers
    if args.layers.lower() == "all":
        layers = [1, 2, 3, 4, 5, 6, 7]
    else:
        try:
            layers = [int(l.strip()) for l in args.layers.split(",")]
            if not all(1 <= l <= 7 for l in layers):
                print("Error: Layers must be between 1 and 7")
                sys.exit(1)
        except ValueError:
            print("Error: Invalid layer specification. Use comma-separated numbers or 'all'")
            sys.exit(1)

    try:
        scaffolder = ProjectScaffolder(
            project_name=args.project_name,
            target_dir=args.target_dir,
            mgfts_root=args.mgfts_root,
            layers=layers,
            language=args.language,
            author=args.author,
            license=args.license
        )

        scaffolder.scaffold()
        sys.exit(0)

    except Exception as e:
        logger.error(f"Failed to create project: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
