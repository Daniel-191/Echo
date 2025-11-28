# Contributing to Echo Bot

Thank you for your interest in contributing to Echo! This document provides guidelines and instructions for contributing to the project.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Coding Standards](#coding-standards)
- [Making Changes](#making-changes)
- [Submitting Changes](#submitting-changes)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)

---

## Code of Conduct

- **Be respectful** - Treat all contributors with respect
- **Be constructive** - Provide helpful feedback
- **Be collaborative** - Work together to improve the project
- **Be patient** - Remember that everyone is learning

---

## Getting Started

### Prerequisites

- **Python 3.12+** installed
- **Git** for version control
- **Discord Bot Token** (for testing)
- Basic knowledge of Python and discord.py

### First Time Contributors

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/Daniel-191/Echo.git
   cd Echo
   ```
3. **Add upstream remote**:
   ```bash
   git remote add upstream https://github.com/Daniel-191/Echo.git
   ```

---

## Development Setup

### 1. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
# Production dependencies
pip install -r requirements.txt

# Development dependencies (recommended)
pip install -r requirements-dev.txt  # If available
```

### 3. Configure the Bot

1. Copy `config.json` or create a `.env` file:
   ```bash
   cp config.json config.local.json
   ```

2. Add your bot token:
   ```json
   {
     "TOKEN": "your_bot_token_here",
     "ADMIN_ID": your_discord_id
   }
   ```

3. **Important**: Never commit your token to git!

### 4. Initialize Database

The bot will automatically create databases on first run, but you can also:
```bash
# Databases will be created in data/ directory
python main.py
```

---

## Project Structure

```
Echo/
├── main.py                 # Bot entry point
├── cogs/                   # Command modules
│   ├── economy/           # Economy system (split into modules)
│   ├── farming.py         # Farming commands
│   ├── crafting.py        # Crafting commands
│   └── ...
├── core/                   # Core infrastructure
│   └── database.py        # Database management
├── models/                 # Data models
│   └── user.py            # User-related models
├── utils/                  # Utilities
│   ├── constants.py       # Constants and config values
│   ├── utilities.py       # Helper functions
│   └── eco_support.py     # Economy support functions
├── assets/                 # Images and resources
│   ├── cards/             # Card images
│   └── images/            # Other images
└── data/                   # Runtime data (databases, logs)
```

For detailed architecture information, see [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

---

## Coding Standards

### Python Style

We follow **PEP 8** with some modifications:

- **Line length**: 120 characters (not 79)
- **Indentation**: 4 spaces (no tabs)
- **Imports**: Organized (standard library, third-party, local)
- **Naming**:
  - Functions/variables: `snake_case`
  - Classes: `PascalCase`
  - Constants: `UPPER_SNAKE_CASE`

### Code Quality

```python
# GOOD ✅
async def get_user_balance(user_id: int) -> int:
    """
    Get the user's current balance.

    Args:
        user_id: Discord user ID

    Returns:
        User's balance in credits
    """
    return db.get_user_balance(user_id)


# BAD ❌
async def getuserbal(uid):
    # no docstring, no type hints
    return db.get_user_balance(uid)
```

### Discord.py Best Practices

- ✅ Use `commands.Cog` for organizing commands
- ✅ Use `async`/`await` properly
- ✅ Handle errors gracefully
- ✅ Add cooldowns to prevent spam
- ✅ Use embeds for rich responses

### Documentation

Every function should have:
- **Docstring** explaining what it does
- **Type hints** for parameters and return values
- **Comments** for complex logic

```python
def calculate_rob_amount(target_balance: int) -> int:
    """
    Calculate how much can be robbed from target.

    Args:
        target_balance: Target's current balance

    Returns:
        Amount that can be robbed (20% of balance)
    """
    return int(target_balance * constants.ROB_PERCENTAGE)
```

---

## Making Changes

### Branching Strategy

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Branch naming conventions**:
   - `feature/add-new-command` - New features
   - `fix/bug-description` - Bug fixes
   - `docs/update-readme` - Documentation
   - `refactor/improve-code` - Code improvements

### Development Workflow

1. **Make your changes** in small, focused commits
2. **Test your changes** thoroughly
3. **Update documentation** if needed
4. **Add tests** for new features (if applicable)

### Commit Messages

Write clear, descriptive commit messages:

```bash
# GOOD ✅
git commit -m "Add daily reward claim command"
git commit -m "Fix inventory display bug for empty inventories"
git commit -m "Refactor database connection handling"

# BAD ❌
git commit -m "stuff"
git commit -m "fixed it"
git commit -m "changes"
```

### Commit Message Format

```
<type>: <subject>

<body (optional)>

<footer (optional)>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Example:**
```
feat: Add trade command for item exchange

- Implement .trade command to transfer items between users
- Add validation to prevent trading to self
- Add embed response with transaction details

Closes #42
```

---

## Submitting Changes

### Before Submitting

- [ ] Code follows style guidelines
- [ ] All tests pass (if tests exist)
- [ ] Documentation is updated
- [ ] No sensitive data (tokens, IDs) in commits
- [ ] Commit messages are clear

### Pull Request Process

1. **Push your branch**:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create Pull Request** on GitHub:
   - Use a clear, descriptive title
   - Explain what changes were made and why
   - Reference any related issues
   - Add screenshots if UI changes

3. **Pull Request Template**:
   ```markdown
   ## Description
   Brief description of changes

   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Breaking change
   - [ ] Documentation update

   ## Testing
   Describe how you tested your changes

   ## Checklist
   - [ ] Code follows style guidelines
   - [ ] Documentation updated
   - [ ] No sensitive data in commits
   ```

4. **Respond to feedback** - Address review comments promptly

5. **Merge** - Once approved, your PR will be merged!

---

## Reporting Bugs

### Before Reporting

- Check if the bug has already been reported
- Verify it's actually a bug (not expected behavior)
- Test on the latest version

### Bug Report Template

```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce:
1. Use command '.command'
2. With parameters '...'
3. See error

**Expected behavior**
What you expected to happen.

**Actual behavior**
What actually happened.

**Screenshots**
If applicable, add screenshots.

**Environment:**
- OS: [e.g. Windows 10]
- Python version: [e.g. 3.12]
- Discord.py version: [e.g. 2.3.2]

**Additional context**
Any other relevant information.
```

---

## Suggesting Features

### Feature Request Template

```markdown
**Is your feature request related to a problem?**
Describe the problem.

**Describe the solution you'd like**
Clear description of what you want.

**Describe alternatives you've considered**
Other solutions you've thought about.

**Additional context**
Any other relevant information.
```

---

## Development Tips

### Testing Your Changes

1. **Create a test server** on Discord
2. **Add your bot** to the test server
3. **Test all affected commands**
4. **Check error handling**
5. **Verify database changes**

### Debugging

```python
# Use logging instead of print
import logging

logger = logging.getLogger(__name__)
logger.debug("Debug info")
logger.error("Error occurred", exc_info=True)
```

### Common Issues

**Import errors?**
- Make sure you're in the virtual environment
- Check that all dependencies are installed

**Database errors?**
- Delete `data/*.db` files and restart
- Check file permissions

**Bot not responding?**
- Verify bot token is correct
- Check bot has proper permissions in Discord
- Look for errors in console

---

## Getting Help

- **Discord**: Join our development server (link)
- **Issues**: Open an issue on GitHub
- **Documentation**: Check [docs/](docs/) folder

---

## Recognition

Contributors will be added to the README and receive credit for their work!

---

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to Echo!** 🎉
