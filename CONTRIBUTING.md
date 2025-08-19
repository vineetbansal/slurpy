# Contributing to Slurpy

Thank you for your interest in contributing to Slurpy! This guide will help you get started with development, testing, and contributing to the project.

## Table of Contents

- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Generating OpenAPI Clients](#generating-openapi-clients)
- [Testing](#testing)
- [Code Quality](#code-quality)
- [Docker Development Environment](#docker-development-environment)
- [Making Changes](#making-changes)
- [Submitting Contributions](#submitting-contributions)

## Development Setup

### Prerequisites

- Python 3.11+ (recommended)
- Poetry for dependency management
- Docker and Docker Compose (for integration tests)
- Git

### Initial Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/EBI-Metagenomics/slurpy.git
   cd slurpy
   ```

2. **Install Poetry** (if not already installed):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. **Install dependencies**:
   ```bash
   poetry install --with dev,test
   ```

4. **Activate the virtual environment**:
   ```bash
   poetry shell
   ```

5. **Install pre-commit hooks**:
   ```bash
   pre-commit install
   ```

## Project Structure

```
slurpy/
├── slurpy/                    # Main package
│   ├── __init__.py
│   ├── v0040/                 # Generated API client for v0.0.40
│   ├── v0041/                 # Generated API client for v0.0.41
│   └── v0042/                 # Generated API client for v0.0.42
├── tools/                     # Development tools
│   └── generate_versioned_clients.py  # Client generation script
├── tests/                     # Test suite
│   ├── conftest.py           # Shared test fixtures
│   └── integration/          # Integration tests
├── slurm/                    # Docker compose setup for testing
│   ├── docker-compose.yaml   # Slurm cluster for integration tests
│   └── ...                   # Slurm configuration files
├── pyproject.toml            # Project configuration and dependencies
├── README.md                 # User documentation
└── CONTRIBUTING.md           # This file
```

## Generating OpenAPI Clients

Slurpy uses auto-generated clients from OpenAPI specifications. The generation process is automated using our custom script.

### The Generation Script

The main generation tool is located at `tools/generate_versioned_clients.py`. This script:

- Downloads OpenAPI specifications for different Slurm versions
- Filters and processes the specs
- Generates Python clients using openapi-generator-cli
- Creates version-specific packages
- Sets up clean import structures

### Running the Generator

```bash
# Generate clients for all supported versions
python tools/generate_versioned_clients.py

# Generate with different api url
python tools/generate_versioned_clients.py --api-url http://example.com/openapi/v3

# Generate with specific output directory
python tools/generate_versioned_clients.py --output-dir ./my_output

# Enable debug logging
python tools/generate_versioned_clients.py --log-level DEBUG
```

### Generator Features

- **Automatic cleanup**: Removes temporary files and `.openapi-generator` directories
- **Logging**: Configurable log levels (DEBUG, INFO, WARNING, ERROR)
- **Filtering**: Processes OpenAPI specs to fix common issues
- **Version management**: Handles multiple API versions consistently
- **Bridge imports**: Creates clean `__init__.py` files for easy importing

### Adding New API Versions

To add support for a new Slurm API version:

1. **Update the generator script**:
   ```python
   # In tools/generate_versioned_clients.py
   VERSIONS = ["v0040", "v0041", "v0042", "v0043"]  # Add new version
   ```

2. **Ensure the OpenAPI spec is available**:
   - The script expects specs at URLs like: `http://example.com/openapi/v3`
   - Or provide local spec files

3. **Run the generator**:
   ```bash
   poetry run python tools/generate_versioned_clients.py
   ```

4. **Create integration tests**:
   - Copy an existing test file like `tests/integration/test_v0042.py`
   - Update the version imports and test class name
   - Test with a real Slurm cluster

## Testing

Slurpy has integration tests for now. Integration tests require a running Slurm cluster.

### Test Structure

- **Integration Tests**: `tests/integration/` (for end-to-end API testing)
- **Fixtures**: `tests/conftest.py` (shared test setup)

### Running Tests

```bash
# Run all tests
poetry run pytest

# Run only integration tests
poetry run pytest tests/integration/

# Run tests for specific version
poetry run pytest tests/integration/test_v0040.py

# Run with verbose output
poetry run pytest -v

# Run specific test
poetry run pytest tests/integration/test_v0040.py::TestSlurmV0040::test_ping_cluster
```

### Integration Test Requirements

Integration tests use **testcontainers** to spin up a real Slurm cluster:

1. **Docker must be running**
2. **Ports 3306 and 6820 must be available**
3. **Tests automatically**:
   - Start MariaDB and Slurm containers
   - Generate JWT tokens using `scontrol`
   - Run API tests against the live cluster
   - Clean up containers when done

### Writing New Tests

When adding new tests:

1. **Use existing patterns**:
   ```python
   @pytest.mark.asyncio
   class TestSlurmV0040:
       async def test_new_feature(self, api_client: slurpy.SlurmApi):
           response = await api_client.some_new_method()
           assert response is not None
   ```

2. **Follow test naming conventions**:
   - Test files: `test_*.py`
   - Test classes: `TestSlurm*`
   - Test methods: `test_*`

3. **Include cleanup in job-related tests**:
   ```python
   job_id = None
   try:
       # Create and test job
       job_id = submit_job()
       # ... test logic
   finally:
       if job_id:
           await api_client.delete_job(job_id)
   ```

## Code Quality

### Pre-commit Hooks

The project uses pre-commit hooks to maintain code quality:

```bash
# Install hooks (one-time setup)
pre-commit install

# Run hooks manually
pre-commit run --all-files

# Update hook versions
pre-commit autoupdate
```

### Linting and Formatting

We use **Ruff** for both linting and formatting:

```bash
# Check code style
poetry run ruff check

# Fix auto-fixable issues
poetry run ruff check --fix

# Format code
poetry run ruff format

# Check formatting without changing files
poetry run ruff format --check
```

### Pre-commit Configuration

The `.pre-commit-config.yaml` includes:
- **Ruff linting**: Catches common Python issues
- **Ruff formatting**: Ensures consistent code style

### Code Style Guidelines

- **Follow PEP 8**: Python style guidelines
- **Use type hints**: All public functions should have type annotations
- **Document public APIs**: Use docstrings for classes and public methods
- **Keep imports organized**: Use absolute imports, group by standard/third-party/local
- **Async/await patterns**: Use async/await consistently for async operations

## Docker Development Environment

### Slurm Test Cluster

The project includes a Docker Compose setup for running integration tests:

```bash
# Start the Slurm cluster (manual testing)
cd slurm/
docker-compose up -d

# Check logs
docker-compose logs -f slurm_node

# Stop the cluster
docker-compose down
```

### Cluster Components

- **slurm_db**: MariaDB database for Slurm accounting
- **slurm_node**: Single-node Slurm cluster (controller + compute + REST API)

### Manual API Testing

Once the cluster is running:

```bash
# Generate a JWT token
docker-compose exec slurm_node scontrol token username=slurm

# Test the REST API
curl -H "X-SLURM-USER-NAME: slurm" \\
     -H "X-SLURM-USER-TOKEN: <your-jwt-token>" \\
     http://localhost:6820/slurm/v0.0.40/ping
```

## Making Changes

### Development Workflow

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**:
   - Follow the code style guidelines
   - Add tests for new functionality
   - Update documentation if needed

3. **Test your changes**:
   ```bash
   # Run relevant tests
   poetry run pytest tests/integration/test_v0040.py
   
   # Run linting
   poetry run ruff check
   ```

4. **Commit your changes**:
   ```bash
   git add .
   git commit -m "feat: add new API endpoint support"
   ```
   
   > Use [Conventional Commits](https://www.conventionalcommits.org/) format

### Types of Changes

- **feat**: New features
- **fix**: Bug fixes  
- **docs**: Documentation changes
- **style**: Code style changes (formatting, etc.)
- **refactor**: Code refactoring
- **test**: Adding or updating tests
- **chore**: Maintenance tasks

### Regenerating Clients

If you modify the client generation process:

1. **Update the generator script**: `tools/generate_versioned_clients.py`
2. **Test the generator**:
   ```bash
   python tools/generate_versioned_clients.py --log-level DEBUG
   ```
3. **Verify the generated clients work**:
   ```bash
   poetry run pytest tests/integration/
   ```

## Submitting Contributions

### Pull Request Process

1. **Fork the repository** on GitHub

2. **Create a feature branch** from `main`:
   ```bash
   git checkout -b feature/your-feature
   ```

3. **Make your changes** following the guidelines above

4. **Push to your fork**:
   ```bash
   git push origin feature/your-feature
   ```

5. **Create a Pull Request**:
   - Use a clear, descriptive title
   - Include a detailed description of changes
   - Reference any related issues
   - Ensure all checks pass

### Pull Request Template

```markdown
## Description
Brief description of what this PR does.

## Type of Change
- [ ] Bug fix
- [ ] New feature  
- [ ] Documentation update
- [ ] Code refactoring

## Testing
- [ ] Added/updated tests
- [ ] All tests pass
- [ ] Integration tests pass

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated if needed
- [ ] No breaking changes (or marked as such)
```

### Review Process

- **Automated checks**: All PRs run through CI/CD
- **Code review**: At least one maintainer review required
- **Testing**: Integration tests must pass
- **Documentation**: Updates required for user-facing changes

## Getting Help

### Resources

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: Questions and community discussions
- **Code Review**: Ask for help in draft PRs
- **Documentation**: Check existing docs and docstrings

### Common Issues

1. **OpenAPI Generator Issues**:
   - Ensure you have Java 11+ installed
   - Check network connectivity for spec downloads
   - Try cleaning and regenerating

2. **Docker Issues**:
   - Ensure Docker is running
   - Check port availability (3306, 6820)
   - Try rebuilding containers

3. **Test Issues**:
   - Ensure Slurm cluster is healthy
   - Check JWT token generation
   - Verify network connectivity

### TODOs

- IDEA: use textual to add a CLI/TUI option for monitoring (and maybe submitting) jobs.
  - See [mjobs](https://github.com/mberacochea/mjobs) for inspiration.
  - This should be available as an add-on package, e.g. `pip install slurpy[cli]`.
  - Use [poetry extras](https://python-poetry.org/docs/pyproject/#extras) for this.

### Contact

- **Maintainers**: Listed in `pyproject.toml`
- **Issues**: GitHub Issues for bugs/features
- **Discussions**: GitHub Discussions for questions

Thank you for contributing to Slurpy! 🚀