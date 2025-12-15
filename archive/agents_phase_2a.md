ALM v0.2 Phase 2 — Time & Execution Model: Agent Instructions
Overview
In this phase, you will implement the free-running time stencil and execution model for the ALM v0.2 cognitive core. The goal is to create independent ingest and compute loops while ensuring the system can handle timing drift (jitter) and maintain stable performance.

Key Objectives
Free-Running Model: Implement a model that allows independent ingest and compute threads, with timing drift allowed but measured.

Rotation Mechanism: Establish a four-slice time stencil to handle history and prediction within the cognitive model.

Jitter Management: Design and test the system's response to timing drift and drift recovery mechanisms.

Phase 2 Constraints:
These constraints must be adhered to when designing the Time & Execution model.

Real-Time Core Constraints
No Blocking: Ensure there are no blocking syscalls or mutex locks within the compute loop. Disk I/O must not happen during compute cycles.

No Heap Allocation: All memory required by the model should be preallocated during initialization. No dynamic allocation should occur during computation.

Deterministic Control Flow: Ensure that the control flow in the compute loop is deterministic and free from lane-dependent branching.

Time Model Constraints
Time Stencil: The model must implement a fixed 4-slice stencil with explicit time progression through index rotation. This stencil will consist of:

Stable History

Recent Past

Now

Future (Staged)

Time Advancement: Time should advance via pointer swapping, not using memcpy. This ensures that slices are updated directly without extra memory copying, maintaining both efficiency and precision.

Memory and Cache Constraints
Working Set Size: The working set must fit within private L2 cache:

Target size: < 200 KB for primary state.

Max size: < 256 KB for the complete working state.

Alignment: Ensure memory structures used in the SIMD kernel are at least 128 bytes aligned for efficient prefetching.

Jitter Constraints
Free-Running Model: The ingest and compute loops should be asynchronous with drift allowed. Jitter should be measurable and should not destabilize the core system.

Bulldozer Bound: If necessary, the read/write heads should be advanced, but the advancement must be bounded and not exceed the required future window for staged computations.

Key Metrics to Collect
Jitter Metrics:

Measure timing drift between the ingest and compute loops.

Capture how jitter affects the stability of the computation over time.

Performance Metrics:

Time Stencil Efficiency: Measure the effectiveness of the 4-slice stencil and verify that time progresses smoothly.

Throughput: Capture the number of writes ingested and processed per cycle.

Resource Utilization:

Track L2 cache usage and ensure the active state stays within memory constraints.

Monitor the number of simultaneous active threads to evaluate computational efficiency.

Error Metrics:

Overflow Detection: Track when the future slice write index exceeds the allocated space (overflow conditions).

Rotational Integrity: Ensure the rotation mechanism operates correctly and efficiently, with no loss of data integrity.

Buffer Overwrite: Monitor and record when the buffer experiences an overwrite (when the write head overwrites previous data).

System Stability:

Record any instances where drift becomes catastrophic or the system goes into an unstable state.

Track recovery or corrective actions the system takes in case of a failure.

Phase 2 Implementation Tasks
Time Stencil Creation:

Implement a TimeStencil class to handle the 4-slice time stencil, including:

Method for writing to the future slice.

Method for rotating the slices after each cycle.

Mechanism to capture pressure metrics and handle drift.

Asynchronous Ingest and Compute Loops:

Create independent loops for ingesting new data and processing it in parallel, ensuring there is no blocking and that they can run asynchronously.

Implement a mechanism to handle the jitter drift, such as measuring drift and adjusting the system accordingly.

Metrics Collection:

Implement logging and reporting for the key metrics listed above, storing the results in a system log or a memory-mapped file for later analysis.

Testing:

Ensure that no lane-dependent branching occurs during the compute loop.

Test that the time stencil correctly rotates and maintains consistency during execution.

Confirm that jitter and drift are both measurable and managed, and that system behavior is consistent even when jitter is introduced.

End of Phase 2: Completion Criteria
Time Stencil: The 4-slice stencil is functional, with rotation implemented and pressure metrics captured.

Asynchronous Execution: Both ingest and compute loops are fully asynchronous, with drift management in place.

Metrics: Key metrics, including jitter, performance, and error rates, are tracked and logged.

Error Handling: Any errors (e.g., overflow, buffer overwrite) are captured, with recovery mechanisms tested.

System Stability: The system runs without instability, even under heavy jitter or data overflow conditions.

Post-Phase 2 Actions:
Archive the current agents.md after completing this task, to maintain version control and proper documentation.

Begin preparations for Phase 3.

