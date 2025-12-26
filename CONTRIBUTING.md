# Contributing to Distributed Multi-Agent Communication Platform

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this project.

##  Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Respect different viewpoints and experiences

##  Getting Started

1. **Fork the repository**
2. **Clone your fork**:
   ```bash
   git clone https://github.com/your-username/distributed-multi-agent-platform.git
   cd distributed-multi-agent-platform
   ```

3. **Set up development environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Create a branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

##  Development Guidelines

### Code Style

- Follow PEP 8 Python style guide
- Use type hints where appropriate
- Write docstrings for all functions and classes
- Keep functions focused and single-purpose

### Testing

- Write tests for new features
- Ensure all tests pass before submitting:
  ```bash
  pytest tests/
  ```
- Aim for test coverage of new code

### Commit Messages

Use clear, descriptive commit messages:

```
feat: Add agent health monitoring endpoint
fix: Resolve WebSocket connection timeout issue
docs: Update API documentation
refactor: Simplify message routing logic
test: Add tests for load balancer
```

##  Pull Request Process

1. **Update documentation** if needed
2. **Add tests** for new functionality
3. **Ensure all tests pass**
4. **Update CHANGELOG.md** (if exists) with your changes
5. **Create Pull Request** with:
   - Clear description of changes
   - Reference to related issues
   - Screenshots (if UI changes)

### PR Checklist

- [ ] Code follows project style guidelines
- [ ] Tests added/updated and passing
- [ ] Documentation updated
- [ ] No breaking changes (or documented if necessary)
- [ ] Commit messages are clear

##  Reporting Bugs

When reporting bugs, please include:

- **Description**: Clear description of the bug
- **Steps to Reproduce**: Detailed steps to reproduce
- **Expected Behavior**: What should happen
- **Actual Behavior**: What actually happens
- **Environment**: Python version, OS, dependencies
- **Logs**: Relevant error messages or logs

##  Suggesting Features

Feature suggestions are welcome! Please:

- Check if the feature already exists
- Open an issue with the `enhancement` label
- Describe the use case and benefits
- Provide examples if possible

##  Documentation

- Keep README.md updated
- Add docstrings to new code
- Update ARCHITECTURE.md for architectural changes
- Include code examples in documentation

##  Architecture Guidelines

When adding new features:

- Follow existing patterns and structure
- Keep components loosely coupled
- Use dependency injection where appropriate
- Consider scalability and performance
- Maintain separation of concerns

##  Questions?

Feel free to open an issue for questions or discussions. We're happy to help!

Thank you for contributing! 

