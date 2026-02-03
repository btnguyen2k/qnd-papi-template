# qnd-papi-template

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A quick-and-dirty template repository to rapidly spin up a Python API server with containerization support.

## 📋 Table of Contents

- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Getting Started](#-getting-started)
- [Docker Support](#-docker-support)
- [Usage](#-usage)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

- **🐍 Python-based API Server**: Built with Python for rapid development and deployment
- **🐳 Docker Ready**: Includes Dockerfile for easy containerization and deployment
- **⚡ Quick Setup**: Minimal configuration required to get started
- **🔧 Modular Architecture**: Clean project structure for easy customization
- **📦 Dependency Management**: Pre-configured dependency management with requirements.txt
- **🚀 Production Ready**: Configured for both development and production environments
- **🔒 Security Best Practices**: Follows Python security guidelines
- **📝 Well Documented**: Comprehensive documentation and code comments
- **🧪 Test Ready**: Structure supports unit and integration testing
- **🔄 CI/CD Friendly**: Easy integration with continuous integration and deployment pipelines

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
- **pip**: Python package installer (usually comes with Python)
- **Docker** (optional): [Install Docker](https://docs.docker.com/get-docker/)
- **Git**: [Install Git](https://git-scm.com/downloads)

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/btnguyen2k/qnd-papi-template.git
cd qnd-papi-template
```

### 2. Create a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the API Server

```bash
python app.py
```

The API server should now be running on `http://localhost:8000` (or your configured port).

## 🐳 Docker Support

This project includes a Dockerfile for containerization, making it easy to deploy in any environment.

### Build Docker Image

```bash
docker build -t qnd-papi-template .
```

### Run Docker Container

```bash
docker run -p 8000:8000 qnd-papi-template
```

### Using Docker Compose (if available)

```bash
docker-compose up
```

## 📖 Usage

### Basic API Endpoint

Example of making a request to the API:

```bash
curl http://localhost:8000/api/v1/health
```

### API Documentation

Once the server is running, you can access the API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Reporting Issues

If you find a bug or have a suggestion:

1. **Search existing issues** to avoid duplicates
2. **Create a new issue** on GitHub:
   - Go to: https://github.com/btnguyen2k/qnd-papi-template/issues/new
   - Provide a clear title and description
   - Include steps to reproduce (for bugs)
   - Add relevant labels (bug, enhancement, question, etc.)

### Submitting Pull Requests

1. **Fork the repository** to your GitHub account

2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/qnd-papi-template.git
   cd qnd-papi-template
   ```

3. **Create a new branch** for your feature or fix:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

4. **Make your changes** following the project's coding standards

5. **Test your changes** thoroughly:
   ```bash
   # Run tests
   pytest
   
   # Run linters
   flake8 .
   black --check .
   ```

6. **Commit your changes** with clear, descriptive messages:
   ```bash
   git add .
   git commit -m "Add: brief description of your changes"
   ```

7. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Create a Pull Request**:
   - Go to the original repository
   - Click "New Pull Request"
   - Select your fork and branch
   - Provide a clear title and description
   - Reference any related issues (e.g., "Fixes #123")

### Code Contribution Guidelines

- Follow [PEP 8](https://peps.python.org/pep-0008/) style guide for Python code
- Write clear, self-documenting code with appropriate comments
- Add unit tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR
- Keep pull requests focused on a single feature or fix

### Development Setup

For contributors who want to set up the development environment:

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Check code style
flake8 .
black --check .

# Format code
black .
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to all contributors who help improve this project
- Built with ❤️ by the community

## 📞 Contact & Support

- **Issues**: [GitHub Issues](https://github.com/btnguyen2k/qnd-papi-template/issues)
- **Discussions**: [GitHub Discussions](https://github.com/btnguyen2k/qnd-papi-template/discussions)

---

**Happy Coding! 🚀**
