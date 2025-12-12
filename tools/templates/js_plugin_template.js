#!/usr/bin/env node

/**
 * MGFTS Tool Plugin Template (JavaScript/Node.js)
 *
 * This file serves as a template for MGFTS-compatible analysis tools written in JavaScript.
 *
 * Requirements:
 * - Deterministic behavior given the same inputs.
 * - Read configuration and parameters from JSON input via stdin.
 * - Write results to stdout in JSON format.
 *
 * Tool Output Contract:
 * - tool: string (name of this tool)
 * - version: string (semantic version)
 * - layer_targets: number[] (MGFTS layers analyzed: 1-7)
 * - violations: Array<{code, message, path, severity, layer}>
 * - warnings: Array<{code, message, path, severity, layer}>
 * - metrics: object with metric_name: value pairs
 * - score: number (0-1, optional)
 *
 * Usage:
 *   echo '{"project_path": "/path/to/project"}' | node tool_name.js
 *   node tool_name.js < config.json
 *
 * Author: MGFTS Constitutional Engine
 * Version: 1.0.0
 */

'use strict';

/**
 * Execute the tool's logic.
 *
 * This is the main entry point for tool implementation.
 * Override this function in derived tools with actual analysis logic.
 *
 * @param {Object} config - Configuration object
 * @param {string} config.project_path - Path to project root (required)
 * @returns {Object} Standard MGFTS tool output
 *
 * @example
 * const config = { project_path: '/path/to/project' };
 * const result = runTool(config);
 * console.assert('tool' in result);
 * console.assert('violations' in result);
 */
function runTool(config) {
  // TODO: Implement actual logic in derived tools.
  // This template provides a minimal valid response.

  const projectPath = config.project_path || '.';

  // Example structure - replace with real analysis
  const result = {
    tool: 'example_tool', // CHANGE THIS to actual tool name
    version: '1.0.0',
    layer_targets: [], // e.g., [1, 3] for layers 1 and 3
    violations: [
      // Example violation structure:
      // {
      //   code: 'MISSING_FILE',
      //   message: 'Required file not found: AGENTS.md',
      //   path: '/AGENTS.md',
      //   severity: 'critical',  // critical|high|medium|low
      //   layer: 2
      // }
    ],
    warnings: [
      // Example warning structure:
      // {
      //   code: 'NAMING_CONVENTION',
      //   message: 'File should use snake_case naming',
      //   path: '/ctl/MyModule.py',
      //   severity: 'medium',
      //   layer: 1
      // }
    ],
    metrics: {
      // Example metrics:
      // files_scanned: 42,
      // total_violations: 0,
      // total_warnings: 0
    },
    score: 1.0, // Optional: 0-1 compliance score
  };

  return result;
}

/**
 * Validate that config contains required fields.
 *
 * @param {Object} config - Configuration to validate
 * @returns {boolean} True if valid, false otherwise
 */
function validateConfig(config) {
  const requiredFields = ['project_path'];

  for (const field of requiredFields) {
    if (!(field in config)) {
      console.error(
        JSON.stringify(
          {
            error: `Missing required config field: ${field}`,
            tool: 'unknown',
            version: '1.0.0',
          },
          null,
          2
        )
      );
      return false;
    }
  }

  return true;
}

/**
 * Main entry point.
 *
 * Reads JSON config from stdin, runs tool, outputs JSON result to stdout.
 */
async function main() {
  try {
    // Read JSON config from stdin
    let configText = '';

    // Read from stdin
    process.stdin.setEncoding('utf8');

    for await (const chunk of process.stdin) {
      configText += chunk;
    }

    if (!configText.trim()) {
      console.error(
        JSON.stringify(
          {
            error: 'No input provided. Expected JSON config on stdin.',
            tool: 'unknown',
            version: '1.0.0',
          },
          null,
          2
        )
      );
      process.exit(1);
    }

    // Parse JSON
    const config = JSON.parse(configText);

    // Validate config
    if (!validateConfig(config)) {
      process.exit(1);
    }

    // Run tool
    const result = runTool(config);

    // Output result as JSON
    console.log(JSON.stringify(result, null, 2));

  } catch (error) {
    if (error instanceof SyntaxError) {
      console.error(
        JSON.stringify(
          {
            error: `Invalid JSON input: ${error.message}`,
            tool: 'unknown',
            version: '1.0.0',
          },
          null,
          2
        )
      );
    } else {
      console.error(
        JSON.stringify(
          {
            error: `Tool execution failed: ${error.message}`,
            tool: 'unknown',
            version: '1.0.0',
            stack: error.stack,
          },
          null,
          2
        )
      );
    }
    process.exit(1);
  }
}

// Run if executed directly
if (require.main === module) {
  main();
}

module.exports = { runTool, validateConfig };
