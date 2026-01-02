# Research: Console-Based Todo Application

## Decision: Architecture Pattern
**Rationale**: Chose a layered architecture with clear separation of concerns to satisfy the "Testability" and "Extensibility" principles from the constitution. This allows domain logic to be tested independently of console I/O.

**Alternatives considered**: 
- Monolithic approach: rejected due to poor testability
- MVC pattern: considered but overkill for this simple application

## Decision: Data Storage
**Rationale**: Using Python built-in list/dict for in-memory storage satisfies the "In-Memory by Design" principle from the constitution and meets the requirement of no persistence after program exit.

**Alternatives considered**:
- SQLite in-memory: rejected as it's unnecessary complexity for this phase
- Custom data structures: rejected as built-ins are sufficient

## Decision: Console Interaction
**Rationale**: Using Python's built-in `input()` and `print()` functions for console I/O keeps dependencies minimal, satisfying the "Simplicity First" principle.

**Alternatives considered**:
- Rich library for enhanced UI: rejected as it adds unnecessary dependencies
- Click library for CLI: rejected as the interface is simple enough for built-ins

## Decision: Error Handling
**Rationale**: Using Python's exception handling mechanism with custom exceptions provides clear error reporting while maintaining simplicity.

**Alternatives considered**:
- Return codes: rejected as exceptions are more Pythonic
- Logging errors to file: rejected as it violates the in-memory-only requirement

## Decision: Testing Framework
**Rationale**: Using pytest for testing provides a robust testing framework that supports the "Testability" principle by allowing easy unit and integration tests.

**Alternatives considered**:
- unittest: rejected as pytest is more concise and feature-rich
- No testing: rejected as it violates the constitution's testability principle