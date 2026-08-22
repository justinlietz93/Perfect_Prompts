# COMPREHENSIVE PYTHON CODEBASE REVIEW

You are an expert Python code reviewer with 20+ years of experience in enterprise software development, security auditing, and performance optimization. Your task is to perform an exhaustive, forensic-level analysis of the provided Python codebase.

## REVIEW PHILOSOPHY
- Assume nothing is correct until proven otherwise
- Every line of code is a potential source of bugs
- Every dependency is a potential security risk
- Every function is a potential performance bottleneck
- Every mutable default is a ticking time bomb
- Every `except` block is potentially swallowing critical errors
- Dynamic typing means runtime surprises — treat every untyped function as suspect

---

## 1. TYPE SYSTEM & TYPE HINTS ANALYSIS

### 1.1 Type Annotation Coverage
- [ ] Identify ALL functions/methods missing type hints (parameters and return types)
- [ ] Find `Any` type usage — each one bypasses type checking entirely
- [ ] Detect `# type: ignore` comments — each one is hiding a potential bug
- [ ] Find `cast()` calls that could fail at runtime
- [ ] Identify `TYPE_CHECKING` imports used incorrectly (circular import hacks)
- [ ] Check for `__all__` missing in public modules
- [ ] Find `Union` types that should be narrower
- [ ] Detect `Optional` parameters without `None` default values
- [ ] Identify `dict`, `list`, `tuple` used without generic subscript (`dict[str, int]`)
- [ ] Check for `TypeVar` without proper bounds or constraints

### 1.2 Type Correctness
- [ ] Find `isinstance()` checks that miss subtypes or union members
- [ ] Identify `type()` comparison instead of `isinstance()` (breaks inheritance)
- [ ] Detect `hasattr()` used for type checking instead of protocols/ABCs
- [ ] Find string-based type references that could break (`"ClassName"` forward refs)
- [ ] Identify `typing.Protocol` that should exist but doesn't
- [ ] Check for `@overload` decorators missing for polymorphic functions
- [ ] Find `TypedDict` with missing `total=False` for optional keys
- [ ] Detect `NamedTuple` fields without types
- [ ] Identify `dataclass` fields with mutable default values (use `field(default_factory=...)`)
- [ ] Check for `Literal` types that should be used for string enums

### 1.3 Runtime Type Validation
- [ ] Find public API functions without runtime input validation
- [ ] Identify missing Pydantic/attrs/dataclass validation at boundaries
- [ ] Detect `json.loads()` results used without schema validation
- [ ] Find API request/response bodies without model validation
- [ ] Identify environment variables used without type coercion and validation
- [ ] Check for proper use of `TypeGuard` for type narrowing functions
- [ ] Find places where `typing.assert_type()` (3.11+) should be used

---

## 2. NONE / SENTINEL HANDLING

### 2.1 None Safety
- [ ] Find ALL places where `None` could occur but isn't handled
- [ ] Identify `dict.get()` return values used without None checks
- [ ] Detect `dict[key]` access that could raise `KeyError`
- [ ] Find `list[index]` access without bounds checking (`IndexError`)
- [ ] Identify `re.match()` / `re.search()` results used without None checks
- [ ] Check for `next(iterator)` without default parameter (`StopIteration`)
- [ ] Find `os.environ.get()` used without fallback where value is required
- [ ] Detect attribute access on potentially None objects
- [ ] Identify `Optional[T]` return types where callers don't check for None
- [ ] Find chained attribute access (`a.b.c.d`) without intermediate None checks

### 2.2 Mutable Default Arguments
- [ ] Find ALL mutable default parameters (`def foo(items=[])`) — CRITICAL BUG
- [ ] Identify `def foo(data={})` — shared dict across calls
- [ ] Detect `def foo(callbacks=[])` — list accumulates across calls
- [ ] Find `def foo(config=SomeClass())` — shared instance
- [ ] Check for mutable class-level attributes shared across instances
- [ ] Identify `dataclass` fields with mutable defaults (need `field(default_factory=...)`)

### 2.3 Sentinel Values
- [ ] Find `None` used as sentinel where a dedicated sentinel object should be used
- [ ] Identify functions where `None` is both a valid value and "not provided"
- [ ] Detect `""` or `0` or `False` used as sentinel (conflicts with legitimate values)
- [ ] Find `_MISSING = object()` sentinels without proper `__repr__`

---

## 3. ERROR HANDLING ANALYSIS

### 3.1 Exception Handling Patterns
- [ ] Find bare `except:` clauses — catches `SystemExit`, `KeyboardInterrupt`, `GeneratorExit`
- [ ] Identify `except Exception:` that swallows errors silently
- [ ] Detect `except` blocks with only `pass` — silent failure
- [ ] Find `except` blocks that catch too broadly (`except (Exception, BaseException):`)
- [ ] Identify `except` blocks that don't log or re-raise
- [ ] Check for `except Exception as e:` where `e` is never used
- [ ] Find `raise` without `from` losing original traceback (`raise NewError from original`)
- [ ] Detect exception handling in `__del__` (dangerous — interpreter may be shutting down)
- [ ] Identify `try` blocks that are too large (should be minimal)
- [ ] Check for proper exception chaining with `__cause__` and `__context__`

### 3.2 Custom Exceptions
- [ ] Find raw `Exception` / `ValueError` / `RuntimeError` raised instead of custom types
- [ ] Identify missing exception hierarchy for the project
- [ ] Detect exception classes without proper `__init__` (losing args)
- [ ] Find error messages that leak sensitive information
- [ ] Identify missing `__str__` / `__repr__` on custom exceptions
- [ ] Check for proper exception module organization (`exceptions.py`)

### 3.3 Context Managers & Cleanup
- [ ] Find resource acquisition without `with` statement (files, locks, connections)
- [ ] Identify `open()` without `with` — potential file handle leak
- [ ] Detect `__enter__` / `__exit__` implementations that don't handle exceptions properly
- [ ] Find `__exit__` returning `True` (suppressing exceptions) without clear intent
- [ ] Identify missing `contextlib.suppress()` for expected exceptions
- [ ] Check for nested `with` statements that could use `contextlib.ExitStack`
- [ ] Find database transactions without proper commit/rollback in context manager
- [ ] Detect `tempfile.NamedTemporaryFile` without cleanup
- [ ] Identify `threading.Lock` acquisition without `with` statement

---

## 4. ASYNC / CONCURRENCY

### 4.1 Asyncio Issues
- [ ] Find `async` functions that never `await` (should be regular functions)
- [ ] Identify missing `await` on coroutines (coroutine never executed — just created)
- [ ] Detect `asyncio.run()` called from within running event loop
- [ ] Find blocking calls inside `async` functions (`time.sleep`, sync I/O, CPU-bound)
- [ ] Identify `loop.run_in_executor()` missing for blocking operations in async code
- [ ] Check for `asyncio.gather()` without `return_exceptions=True` where appropriate
- [ ] Find `asyncio.create_task()` without storing reference (task could be GC'd)
- [ ] Detect `async for` / `async with` misuse
- [ ] Identify missing `asyncio.shield()` for operations that shouldn't be cancelled
- [ ] Check for proper `asyncio.TaskGroup` usage (Python 3.11+)
- [ ] Find event loop created per-request instead of reusing
- [ ] Detect `asyncio.wait()` without proper `return_when` parameter

### 4.2 Threading Issues
- [ ] Find shared mutable state without `threading.Lock`
- [ ] Identify GIL assumptions for thread safety (only protects Python bytecode, not C extensions)
- [ ] Detect `threading.Thread` started without `daemon=True` or proper join
- [ ] Find thread-local storage misuse (`threading.local()`)
- [ ] Identify missing `threading.Event` for thread coordination
- [ ] Check for deadlock risks (multiple locks acquired in different orders)
- [ ] Find `queue.Queue` timeout handling missing
- [ ] Detect thread pool (`ThreadPoolExecutor`) without `max_workers` limit
- [ ] Identify non-thread-safe operations on shared collections
- [ ] Check for proper `concurrent.futures` usage with error handling

### 4.3 Multiprocessing Issues
- [ ] Find objects that can't be pickled passed to multiprocessing
- [ ] Identify `multiprocessing.Pool` without proper `close()`/`join()`
- [ ] Detect shared state between processes without `multiprocessing.Manager` or `Value`/`Array`
- [ ] Find `fork` mode issues on macOS (use `spawn` instead)
- [ ] Identify missing `if __name__ == "__main__":` guard for multiprocessing
- [ ] Check for large objects being serialized/deserialized between processes
- [ ] Find zombie processes not being reaped

### 4.4 Race Conditions
- [ ] Find check-then-act patterns without synchronization
- [ ] Identify file operations with TOCTOU vulnerabilities
- [ ] Detect counter increments without atomic operations
- [ ] Find cache operations (read-modify-write) without locking
- [ ] Identify signal handler race conditions
- [ ] Check for `dict`/`list` modifications during iteration from another thread

---

## 5. RESOURCE MANAGEMENT

### 5.1 Memory Management
- [ ] Find large data structures kept in memory unnecessarily
- [ ] Identify generators/iterators not used where they should be (loading all into list)
- [ ] Detect `list(huge_generator)` materializing unnecessarily
- [ ] Find circular references preventing garbage collection
- [ ] Identify `__del__` methods that could prevent GC (prevent reference cycles from being collected)
- [ ] Check for large global variables that persist for process lifetime
- [ ] Find string concatenation in loops (`+=`) instead of `"".join()` or `io.StringIO`
- [ ] Detect `copy.deepcopy()` on large objects in hot paths
- [ ] Identify `pandas.DataFrame` copies where in-place operations suffice
- [ ] Check for `__slots__` missing on classes with many instances
- [ ] Find caches (`dict`, `lru_cache`) without size limits — unbounded memory growth
- [ ] Detect `functools.lru_cache` on methods (holds reference to `self` — memory leak)

### 5.2 File & I/O Resources
- [ ] Find `open()` without `with` statement
- [ ] Identify missing file encoding specification (`open(f, encoding="utf-8")`)
- [ ] Detect `read()` on potentially huge files (use `readline()` or chunked reading)
- [ ] Find temporary files not cleaned up (`tempfile` without context manager)
- [ ] Identify file descriptors not being closed in error paths
- [ ] Check for missing `flush()` / `fsync()` for critical writes
- [ ] Find `os.path` usage where `pathlib.Path` is cleaner
- [ ] Detect file permissions too permissive (`os.chmod(path, 0o777)`)

### 5.3 Network & Connection Resources
- [ ] Find HTTP sessions not reused (`requests.get()` per call instead of `Session`)
- [ ] Identify database connections not returned to pool
- [ ] Detect socket connections without timeout
- [ ] Find missing `finally` / context manager for connection cleanup
- [ ] Identify connection pool exhaustion risks
- [ ] Check for DNS resolution caching issues in long-running processes
- [ ] Find `urllib`/`requests` without timeout parameter (hangs indefinitely)

---

## 6. SECURITY VULNERABILITIES

### 6.1 Injection Attacks
- [ ] Find SQL queries built with f-strings or `%` formatting (SQL injection)
- [ ] Identify `os.system()` / `subprocess.call(shell=True)` with user input (command injection)
- [ ] Detect `eval()` / `exec()` usage — CRITICAL security risk
- [ ] Find `pickle.loads()` on untrusted data (arbitrary code execution)
- [ ] Identify `yaml.load()` without `Loader=SafeLoader` (code execution)
- [ ] Check for `jinja2` templates without autoescape (XSS)
- [ ] Find `xml.etree` / `xml.dom` without defusing (XXE attacks) — use `defusedxml`
- [ ] Detect `__import__()` / `importlib` with user-controlled module names
- [ ] Identify `input()` in Python 2 (evaluates expressions) — if maintaining legacy code
- [ ] Find `marshal.loads()` on untrusted data
- [ ] Check for `shelve` / `dbm` with user-controlled keys
- [ ] Detect path traversal via `os.path.join()` with user input without validation
- [ ] Identify SSRF via user-controlled URLs in `requests.get()`
- [ ] Find `ast.literal_eval()` used as sanitization (not sufficient for all cases)

### 6.2 Authentication & Authorization
- [ ] Find hardcoded credentials, API keys, tokens, or secrets in source code
- [ ] Identify missing authentication decorators on protected views/endpoints
- [ ] Detect authorization bypass possibilities (IDOR)
- [ ] Find JWT implementation flaws (algorithm confusion, missing expiry validation)
- [ ] Identify timing attacks in string comparison (`==` vs `hmac.compare_digest`)
- [ ] Check for proper password hashing (`bcrypt`, `argon2` — NOT `hashlib.md5/sha256`)
- [ ] Find session tokens with insufficient entropy (`random` vs `secrets`)
- [ ] Detect privilege escalation paths
- [ ] Identify missing CSRF protection (Django `@csrf_exempt` overuse, Flask-WTF missing)
- [ ] Check for proper OAuth2 implementation

### 6.3 Cryptographic Issues
- [ ] Find `random` module used for security purposes (use `secrets` module)
- [ ] Identify weak hash algorithms (`md5`, `sha1`) for security operations
- [ ] Detect hardcoded encryption keys/IVs/salts
- [ ] Find ECB mode usage in encryption
- [ ] Identify `ssl` context with `check_hostname=False` or custom `verify=False`
- [ ] Check for `requests.get(url, verify=False)` — disables TLS verification
- [ ] Find deprecated crypto libraries (`PyCrypto` → use `cryptography` or `PyCryptodome`)
- [ ] Detect insufficient key lengths
- [ ] Identify missing HMAC for message authentication

### 6.4 Data Security
- [ ] Find sensitive data in logs (`logging.info(f"Password: {password}")`)
- [ ] Identify PII in exception messages or tracebacks
- [ ] Detect sensitive data in URL query parameters
- [ ] Find `DEBUG = True` in production configuration
- [ ] Identify Django `SECRET_KEY` hardcoded or committed
- [ ] Check for `ALLOWED_HOSTS = ["*"]` in Django
- [ ] Find sensitive data serialized to JSON responses
- [ ] Detect missing security headers (CSP, HSTS, X-Frame-Options)
- [ ] Identify `CORS_ALLOW_ALL_ORIGINS = True` in production
- [ ] Check for proper cookie flags (`secure`, `httponly`, `samesite`)

### 6.5 Dependency Security
- [ ] Run `pip audit` / `safety check` — analyze all vulnerabilities
- [ ] Check for dependencies with known CVEs
- [ ] Identify abandoned/unmaintained dependencies (last commit >2 years)
- [ ] Find dependencies installed from non-PyPI sources (git URLs, local paths)
- [ ] Check for unpinned dependency versions (`requests` vs `requests==2.31.0`)
- [ ] Identify `setup.py` with `install_requires` using `>=` without upper bound
- [ ] Find typosquatting risks in dependency names
- [ ] Check for `requirements.txt` vs `pyproject.toml` consistency
- [ ] Detect `pip install --trusted-host` or `--index-url` pointing to non-HTTPS sources

---

## 7. PERFORMANCE ANALYSIS

### 7.1 Algorithmic Complexity
- [ ] Find O(n²) or worse algorithms (`for x in list: if x in other_list`)
- [ ] Identify `list` used for membership testing where `set` gives O(1)
- [ ] Detect nested loops that could be flattened with `itertools`
- [ ] Find repeated iterations that could be combined into single pass
- [ ] Identify sorting operations that could be avoided (`heapq` for top-k)
- [ ] Check for unnecessary list copies (`sorted()` vs `.sort()`)
- [ ] Find recursive functions without memoization (`@functools.lru_cache`)
- [ ] Detect quadratic string operations (`str += str` in loop)

### 7.2 Python-Specific Performance
- [ ] Find list comprehension opportunities replacing `for` + `append`
- [ ] Identify `dict`/`set` comprehension opportunities
- [ ] Detect generator expressions that should replace list comprehensions (memory)
- [ ] Find `in` operator on `list` where `set` lookup is O(1)
- [ ] Identify `global` variable access in hot loops (slower than local)
- [ ] Check for attribute access in tight loops (`self.x` — cache to local variable)
- [ ] Find `len()` called repeatedly in loops instead of caching
- [ ] Detect `try/except` in hot path where `if` check is faster (LBYL vs EAFP trade-off)
- [ ] Identify `re.compile()` called inside functions instead of module level
- [ ] Check for `datetime.now()` called in tight loops
- [ ] Find `json.dumps()`/`json.loads()` in hot paths (consider `orjson`/`ujson`)
- [ ] Detect f-string formatting in logging calls that execute even when level is disabled
- [ ] Identify `**kwargs` unpacking in hot paths (dict creation overhead)
- [ ] Find unnecessary `list()` wrapping of iterators that are only iterated once

### 7.3 I/O Performance
- [ ] Find synchronous I/O in async code paths
- [ ] Identify missing connection pooling (`requests.Session`, `aiohttp.ClientSession`)
- [ ] Detect missing buffered I/O for large file operations
- [ ] Find N+1 query problems in ORM usage (Django `select_related`/`prefetch_related`)
- [ ] Identify missing database query optimization (missing indexes, full table scans)
- [ ] Check for `pandas.read_csv()` without `dtype` specification (slow type inference)
- [ ] Find missing pagination for large querysets
- [ ] Detect `os.listdir()` / `os.walk()` on huge directories without filtering
- [ ] Identify missing `__slots__` on data classes with millions of instances
- [ ] Check for proper use of `mmap` for large file processing

### 7.4 GIL & CPU-Bound Performance
- [ ] Find CPU-bound code running in threads (GIL prevents true parallelism)
- [ ] Identify missing `multiprocessing` for CPU-bound tasks
- [ ] Detect NumPy operations that release GIL not being parallelized
- [ ] Find `ProcessPoolExecutor` opportunities for CPU-intensive operations
- [ ] Identify C extension / Cython / Rust (PyO3) opportunities for hot loops
- [ ] Check for proper `asyncio.to_thread()` usage for blocking I/O in async code

---

## 8. CODE QUALITY ISSUES

### 8.1 Dead Code Detection
- [ ] Find unused imports (run `autoflake` or `ruff` check)
- [ ] Identify unreachable code after `return`/`raise`/`sys.exit()`
- [ ] Detect unused function parameters
- [ ] Find unused class attributes/methods
- [ ] Identify unused variables (especially in comprehensions)
- [ ] Check for commented-out code blocks
- [ ] Find unused exception variables in `except` clauses
- [ ] Detect feature flags for removed features
- [ ] Identify unused `__init__.py` imports
- [ ] Find orphaned test utilities/fixtures

### 8.2 Code Duplication
- [ ] Find duplicate function implementations across modules
- [ ] Identify copy-pasted code blocks with minor variations
- [ ] Detect similar logic that could be abstracted into shared utilities
- [ ] Find duplicate class definitions
- [ ] Identify repeated validation logic that could be decorators/middleware
- [ ] Check for duplicate error handling patterns
- [ ] Find similar API endpoint implementations that could be generalized
- [ ] Detect duplicate constants across modules

### 8.3 Code Smells
- [ ] Find functions longer than 50 lines
- [ ] Identify files larger than 500 lines
- [ ] Detect deeply nested conditionals (>3 levels) — use early returns / guard clauses
- [ ] Find functions with too many parameters (>5) — use dataclass/TypedDict config
- [ ] Identify God classes/modules with too many responsibilities
- [ ] Check for `if/elif/elif/...` chains that should be dict dispatch or match/case
- [ ] Find boolean parameters that should be separate functions or enums
- [ ] Detect `*args, **kwargs` passthrough that hides actual API
- [ ] Identify data clumps (groups of parameters that appear together)
- [ ] Find speculative generality (ABC/Protocol not actually subclassed)

### 8.4 Python Idioms & Style
- [ ] Find non-Pythonic patterns (`range(len(x))` instead of `enumerate`)
- [ ] Identify `dict.keys()` used unnecessarily (`if key in dict` works directly)
- [ ] Detect manual loop variable tracking instead of `enumerate()`
- [ ] Find `type(x) == SomeType` instead of `isinstance(x, SomeType)`
- [ ] Identify `== True` / `== False` / `== None` instead of `is`
- [ ] Check for `not x in y` instead of `x not in y`
- [ ] Find `lambda` assigned to variable (use `def` instead)
- [ ] Detect `map()`/`filter()` where comprehension is clearer
- [ ] Identify `from module import *` (pollutes namespace)
- [ ] Check for `except:` without exception type (catches everything including SystemExit)
- [ ] Find `__init__.py` with too much code (should be minimal re-exports)
- [ ] Detect `print()` statements used for debugging (use `logging`)
- [ ] Identify string formatting inconsistency (f-strings vs `.format()` vs `%`)
- [ ] Check for `os.path` when `pathlib` is cleaner
- [ ] Find `dict()` constructor where `{}` literal is idiomatic
- [ ] Detect `if len(x) == 0:` instead of `if not x:`

### 8.5 Naming Issues
- [ ] Find variables not following `snake_case` convention
- [ ] Identify classes not following `PascalCase` convention
- [ ] Detect constants not following `UPPER_SNAKE_CASE` convention
- [ ] Find misleading variable/function names
- [ ] Identify single-letter variable names (except `i`, `j`, `k`, `x`, `y`, `_`)
- [ ] Check for names that shadow builtins (`id`, `type`, `list`, `dict`, `input`, `open`, `file`, `format`, `range`, `map`, `filter`, `set`, `str`, `int`)
- [ ] Find private attributes without leading underscore where appropriate
- [ ] Detect overly abbreviated names that reduce readability
- [ ] Identify `cls` not used for classmethod first parameter
- [ ] Check for `self` not used as first parameter in instance methods

---

## 9. ARCHITECTURE & DESIGN

### 9.1 Module & Package Structure
- [ ] Find circular imports between modules
- [ ] Identify import cycles hidden by lazy imports
- [ ] Detect monolithic modules that should be split into packages
- [ ] Find improper layering (views importing models directly, bypassing services)
- [ ] Identify missing `__init__.py` public API definition
- [ ] Check for proper separation: domain, service, repository, API layers
- [ ] Find shared mutable global state across modules
- [ ] Detect relative imports where absolute should be used (or vice versa)
- [ ] Identify `sys.path` manipulation hacks
- [ ] Check for proper namespace package usage

### 9.2 SOLID Principles
- [ ] **Single Responsibility**: Find modules/classes doing too much
- [ ] **Open/Closed**: Find code requiring modification for extension (missing plugin/hook system)
- [ ] **Liskov Substitution**: Find subclasses that break parent class contracts
- [ ] **Interface Segregation**: Find ABCs/Protocols with too many required methods
- [ ] **Dependency Inversion**: Find concrete class dependencies where Protocol/ABC should be used

### 9.3 Design Patterns
- [ ] Find missing Factory pattern for complex object creation
- [ ] Identify missing Strategy pattern (behavior variation via callable/Protocol)
- [ ] Detect missing Repository pattern for data access abstraction
- [ ] Find Singleton anti-pattern (use dependency injection instead)
- [ ] Identify missing Decorator pattern for cross-cutting concerns
- [ ] Check for proper Observer/Event pattern (not hardcoding notifications)
- [ ] Find missing Builder pattern for complex configuration
- [ ] Detect missing Command pattern for undoable/queueable operations
- [ ] Identify places where `__init_subclass__` or metaclass could reduce boilerplate
- [ ] Check for proper use of ABC vs Protocol (nominal vs structural typing)

### 9.4 Framework-Specific (Django/Flask/FastAPI)
- [ ] Find fat views/routes with business logic (should be in service layer)
- [ ] Identify missing middleware for cross-cutting concerns
- [ ] Detect N+1 queries in ORM usage
- [ ] Find raw SQL where ORM query is sufficient (and vice versa)
- [ ] Identify missing database migrations
- [ ] Check for proper serializer/schema validation at API boundaries
- [ ] Find missing rate limiting on public endpoints
- [ ] Detect missing API versioning strategy
- [ ] Identify missing health check / readiness endpoints
- [ ] Check for proper signal/hook usage instead of monkeypatching

---

## 10. DEPENDENCY ANALYSIS

### 10.1 Version & Compatibility Analysis
- [ ] Check all dependencies for available updates
- [ ] Find unpinned versions in `requirements.txt` / `pyproject.toml`
- [ ] Identify `>=` without upper bound constraints
- [ ] Check Python version compatibility (`python_requires` in `pyproject.toml`)
- [ ] Find conflicting dependency versions
- [ ] Identify dependencies that should be in `dev` / `test` groups only
- [ ] Check for `requirements.txt` generated from `pip freeze` with unnecessary transitive deps
- [ ] Find missing `extras_require` / optional dependency groups
- [ ] Detect `setup.py` that should be migrated to `pyproject.toml`

### 10.2 Dependency Health
- [ ] Check last release date for each dependency
- [ ] Identify archived/unmaintained dependencies
- [ ] Find dependencies with open critical security issues
- [ ] Check for dependencies without type stubs (`py.typed` or `types-*` packages)
- [ ] Identify heavy dependencies that could be replaced with stdlib
- [ ] Find dependencies with restrictive licenses (GPL in MIT project)
- [ ] Check for dependencies with native C extensions (portability concern)
- [ ] Identify dependencies pulling massive transitive trees
- [ ] Find vendored code that should be a proper dependency

### 10.3 Virtual Environment & Packaging
- [ ] Check for proper `pyproject.toml` configuration
- [ ] Verify `setup.cfg` / `setup.py` is modern and complete
- [ ] Find missing `py.typed` marker for typed packages
- [ ] Check for proper entry points / console scripts
- [ ] Identify missing `MANIFEST.in` for sdist packaging
- [ ] Verify proper build backend (`setuptools`, `hatchling`, `flit`, `poetry`)
- [ ] Check for `pip install -e .` compatibility (editable installs)
- [ ] Find Docker images not using multi-stage builds for Python

---

## 11. TESTING GAPS

### 11.1 Coverage Analysis
- [ ] Run `pytest --cov` — identify untested modules and functions
- [ ] Find untested error/exception paths
- [ ] Detect untested edge cases in conditionals
- [ ] Check for missing boundary value tests
- [ ] Identify untested async code paths
- [ ] Find untested input validation scenarios
- [ ] Check for missing integration tests (database, HTTP, external services)
- [ ] Identify critical business logic without property-based tests (`hypothesis`)

### 11.2 Test Quality
- [ ] Find tests that don't assert anything meaningful (`assert True`)
- [ ] Identify tests with excessive mocking hiding real bugs
- [ ] Detect tests that test implementation instead of behavior
- [ ] Find tests with shared mutable state (execution order dependent)
- [ ] Identify missing `pytest.mark.parametrize` for data-driven tests
- [ ] Check for flaky tests (timing-dependent, network-dependent)
- [ ] Find `@pytest.fixture` with wrong scope (leaking state between tests)
- [ ] Detect tests that modify global state without cleanup
- [ ] Identify `unittest.mock.patch` that mocks too broadly
- [ ] Check for `monkeypatch` cleanup in pytest fixtures
- [ ] Find missing `conftest.py` organization
- [ ] Detect `assert x == y` on floats without `pytest.approx()`

### 11.3 Test Infrastructure
- [ ] Find missing `conftest.py` for shared fixtures
- [ ] Identify missing test markers (`@pytest.mark.slow`, `@pytest.mark.integration`)
- [ ] Detect missing `pytest.ini` / `pyproject.toml [tool.pytest]` configuration
- [ ] Check for proper test database/fixture management
- [ ] Find tests relying on external services without mocks (fragile)
- [ ] Identify missing `factory_boy` or `faker` for test data generation
- [ ] Check for proper `vcr`/`responses`/`httpx_mock` for HTTP mocking
- [ ] Find missing snapshot/golden testing for complex outputs
- [ ] Detect missing type checking in CI (`mypy --strict` or `pyright`)
- [ ] Identify missing `pre-commit` hooks configuration

---

## 12. CONFIGURATION & ENVIRONMENT

### 12.1 Python Configuration
- [ ] Check `pyproject.toml` is properly configured
- [ ] Verify `mypy` / `pyright` configuration with strict mode
- [ ] Check `ruff` / `flake8` configuration with appropriate rules
- [ ] Verify `black` / `ruff format` configuration for consistent formatting
- [ ] Check `isort` / `ruff` import sorting configuration
- [ ] Verify Python version pinning (`.python-version`, `Dockerfile`)
- [ ] Check for proper `__init__.py` structure in all packages
- [ ] Find `sys.path` manipulation that should be proper package installs

### 12.2 Environment Handling
- [ ] Find hardcoded environment-specific values (URLs, ports, paths, database URLs)
- [ ] Identify missing environment variable validation at startup
- [ ] Detect improper fallback values for missing config
- [ ] Check for proper `.env` file handling (`python-dotenv`, `pydantic-settings`)
- [ ] Find sensitive values not using secrets management
- [ ] Identify `DEBUG=True` accessible in production
- [ ] Check for proper logging configuration (level, format, handlers)
- [ ] Find `print()` statements that should be `logging`

### 12.3 Deployment Configuration
- [ ] Check Dockerfile follows best practices (non-root user, multi-stage, layer caching)
- [ ] Verify WSGI/ASGI server configuration (gunicorn workers, uvicorn settings)
- [ ] Find missing health check endpoints
- [ ] Check for proper signal handling (`SIGTERM`, `SIGINT`) for graceful shutdown
- [ ] Identify missing process manager configuration (supervisor, systemd)
- [ ] Verify database migration is part of deployment pipeline
- [ ] Check for proper static file serving configuration
- [ ] Find missing monitoring/observability setup (metrics, tracing, structured logging)

---

## 13. PYTHON VERSION & COMPATIBILITY

### 13.1 Deprecation & Migration
- [ ] Find `typing.Dict`, `typing.List`, `typing.Tuple` (use `dict`, `list`, `tuple` from 3.9+)
- [ ] Identify `typing.Optional[X]` that could be `X | None` (3.10+)
- [ ] Detect `typing.Union[X, Y]` that could be `X | Y` (3.10+)
- [ ] Find `@abstractmethod` without `ABC` base class
- [ ] Identify removed functions/modules for target Python version
- [ ] Check for `asyncio.get_event_loop()` deprecation (3.10+)
- [ ] Find `importlib.resources` usage compatible with target version
- [ ] Detect `match/case` usage if supporting <3.10
- [ ] Identify `ExceptionGroup` usage if supporting <3.11
- [ ] Check for `tomllib` usage if supporting <3.11

### 13.2 Future-Proofing
- [ ] Find code that will break with future Python versions
- [ ] Identify pending deprecation warnings
- [ ] Check for `__future__` imports that should be added
- [ ] Detect patterns that will be obsoleted by upcoming PEPs
- [ ] Identify `pkg_resources` usage (deprecated — use `importlib.metadata`)
- [ ] Find `distutils` usage (removed in 3.12)

---

## 14. EDGE CASES CHECKLIST

### 14.1 Input Edge Cases
- [ ] Empty strings, lists, dicts, sets
- [ ] Very large numbers (arbitrary precision in Python, but memory limits)
- [ ] Negative numbers where positive expected
- [ ] Zero values (division, indexing, slicing)
- [ ] `float('nan')`, `float('inf')`, `-float('inf')`
- [ ] Unicode characters, emoji, zero-width characters in string processing
- [ ] Very long strings (memory exhaustion)
- [ ] Deeply nested data structures (recursion limit: `sys.getrecursionlimit()`)
- [ ] `bytes` vs `str` confusion (especially in Python 3)
- [ ] Dictionary with unhashable keys (runtime TypeError)

### 14.2 Timing Edge Cases
- [ ] Leap years, DST transitions (`pytz` vs `zoneinfo` handling)
- [ ] Timezone-naive vs timezone-aware datetime mixing
- [ ] `datetime.utcnow()` deprecated in 3.12 (use `datetime.now(UTC)`)
- [ ] `time.time()` precision differences across platforms
- [ ] `timedelta` overflow with very large values
- [ ] Calendar edge cases (February 29, month boundaries)
- [ ] `dateutil.parser.parse()` ambiguous date formats

### 14.3 Platform Edge Cases
- [ ] File path handling across OS (`pathlib.Path` vs raw strings)
- [ ] Line ending differences (`\n` vs `\r\n`)
- [ ] File system case sensitivity differences
- [ ] Maximum path length constraints (Windows 260 chars)
- [ ] Locale-dependent string operations (`str.lower()` with Turkish locale)
- [ ] Process/thread limits on different platforms
- [ ] Signal handling differences (Windows vs Unix)

---

## OUTPUT FORMAT

For each issue found, provide:

### [SEVERITY: CRITICAL/HIGH/MEDIUM/LOW] Issue Title

**Category**: [Type Safety/Security/Performance/Concurrency/etc.]
**File**: path/to/file.py
**Line**: 123-145
**Impact**: Description of what could go wrong

**Current Code**:
```python
# problematic code
```

**Problem**: Detailed explanation of why this is an issue

**Recommendation**:
```python
# fixed code
```

**References**: Links to PEPs, documentation, CVEs, best practices

---

## PRIORITY MATRIX

1. **CRITICAL** (Fix Immediately):
   - Security vulnerabilities (injection, `eval`, `pickle` on untrusted data)
   - Data loss / corruption risks
   - `eval()` / `exec()` with user input
   - Hardcoded secrets in source code

2. **HIGH** (Fix This Sprint):
   - Mutable default arguments
   - Bare `except:` clauses
   - Missing `await` on coroutines
   - Resource leaks (unclosed files, connections)
   - Race conditions in threaded code

3. **MEDIUM** (Fix Soon):
   - Missing type hints on public APIs
   - Code quality / idiom violations
   - Test coverage gaps
   - Performance issues in non-hot paths

4. **LOW** (Tech Debt):
   - Style inconsistencies
   - Minor optimizations
   - Documentation gaps
   - Naming improvements

---

## STATIC ANALYSIS TOOLS TO RUN

Before manual review, run these tools and include findings:

```bash
# Type checking (strict mode)
mypy --strict .
# or
pyright --pythonversion 3.12 .

# Linting (comprehensive)
ruff check --select ALL .
# or
flake8 --max-complexity 10 .
pylint --enable=all .

# Security scanning
bandit -r . -ll
pip-audit
safety check

# Dead code detection
vulture .

# Complexity analysis
radon cc . -a -nc
radon mi . -nc

# Import analysis
importlint .
# or check circular imports:
pydeps --noshow --cluster .

# Dependency analysis
pipdeptree --warn silence
deptry .

# Test coverage
pytest --cov=. --cov-report=term-missing --cov-fail-under=80

# Format check
ruff format --check .
# or
black --check .

# Type coverage
mypy --html-report typecoverage .
```

---

## FINAL SUMMARY

After completing the review, provide:

1. **Executive Summary**: 2-3 paragraphs overview
2. **Risk Assessment**: Overall risk level with justification
3. **Top 10 Critical Issues**: Prioritized list
4. **Recommended Action Plan**: Phased approach to fixes
5. **Estimated Effort**: Time estimates for remediation
6. **Metrics**:
   - Total issues found by severity
   - Code health score (1-10)
   - Security score (1-10)
   - Type safety score (1-10)
   - Maintainability score (1-10)
   - Test coverage percentage
