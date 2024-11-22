import os

def create_file(filepath, content=""):
    """Creates a file with optional content."""
    with open(filepath, 'w') as f:
        f.write(content)

def create_frontend_structure(base_path):
    """Creates the frontend structure."""
    frontend_path = os.path.join(base_path, "client")
    src_path = os.path.join(frontend_path, "src")

    directories = [
        os.path.join(frontend_path, "public"),
        os.path.join(frontend_path, "node_modules"),
        os.path.join(src_path, "components/common"),
        os.path.join(src_path, "components/layout"),
        os.path.join(src_path, "features/article/components"),
        os.path.join(src_path, "features/article/pages"),
        os.path.join(src_path, "features/auth"),
        os.path.join(src_path, "context"),
        os.path.join(src_path, "hooks"),
        os.path.join(src_path, "pages"),
        os.path.join(src_path, "services"),
        os.path.join(src_path, "styles"),
        os.path.join(src_path, "utils"),
    ]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    # Create common frontend files
    create_file(os.path.join(frontend_path, ".gitignore"), "# Node.js dependencies\nnode_modules\n")
    create_file(os.path.join(frontend_path, "package.json"), "// Defines frontend dependencies and scripts")
    create_file(os.path.join(frontend_path, "README.md"), "# Frontend Documentation\n// Add details about the frontend setup here.")
    create_file(os.path.join(frontend_path, ".env"), "# Environment variables for the frontend")
    create_file(os.path.join(src_path, "App.jsx"), "// Root component of the frontend\nimport React from 'react';\nexport default function App() { return <div>App</div>; }")
    create_file(os.path.join(src_path, "index.jsx"), "// Entry point for React\nimport ReactDOM from 'react-dom';\nimport App from './App';\nReactDOM.render(<App />, document.getElementById('root'));")

    # Add specific files in folders
    create_file(os.path.join(src_path, "components/common/Button.jsx"), "// A reusable button component")
    create_file(os.path.join(src_path, "components/layout/Header.jsx"), "// The header layout component")
    create_file(os.path.join(src_path, "features/article/components/ArticleCard.jsx"), "// Displays a single article card")
    create_file(os.path.join(src_path, "features/article/pages/ArticlePage.jsx"), "// The page displaying a single article")
    create_file(os.path.join(src_path, "features/auth/LoginForm.jsx"), "// A login form component for authentication")
    create_file(os.path.join(src_path, "context/AuthContext.js"), "// Context for managing authentication state")
    create_file(os.path.join(src_path, "hooks/useAuth.js"), "// A custom hook for authentication logic")
    create_file(os.path.join(src_path, "services/apiClient.js"), "// Handles API requests to the backend")
    create_file(os.path.join(src_path, "styles/theme.css"), "/* Global theme styles */")
    create_file(os.path.join(src_path, "utils/formatDate.js"), "// Utility function to format dates")


def create_backend_structure(base_path):
    """Creates the backend structure."""
    backend_path = os.path.join(base_path, "backend")

    directories = [
        os.path.join(backend_path, "config"),
        os.path.join(backend_path, "controllers"),
        os.path.join(backend_path, "middleware"),
        os.path.join(backend_path, "models"),
        os.path.join(backend_path, "routes"),
        os.path.join(backend_path, "services"),
        os.path.join(backend_path, "utils"),
        os.path.join(backend_path, "tests"),
    ]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    # Create common backend files
    create_file(os.path.join(backend_path, ".gitignore"), "# Node.js dependencies\nnode_modules\n.env")
    create_file(os.path.join(backend_path, "package.json"), "// Defines backend dependencies and scripts")
    create_file(os.path.join(backend_path, "README.md"), "# Backend Documentation\n// Add details about the backend setup here.")
    create_file(os.path.join(backend_path, ".env"), "# Environment variables for the backend")
    create_file(os.path.join(backend_path, "app.js"), "// Main application logic\nconst express = require('express');\nconst app = express();\nmodule.exports = app;")
    create_file(os.path.join(backend_path, "server.js"), "// Entry point for the backend server\nconst app = require('./app');\nconst PORT = process.env.PORT || 3000;\napp.listen(PORT, () => console.log(`Server running on port ${PORT}`));")

    # Add specific files in folders
    create_file(os.path.join(backend_path, "config/dbConfig.js"), "// Configuration for the database connection")
    create_file(os.path.join(backend_path, "config/env.js"), "// Environment configuration file")
    create_file(os.path.join(backend_path, "controllers/articleController.js"), "// Logic for handling article-related requests")
    create_file(os.path.join(backend_path, "controllers/userController.js"), "// Logic for handling user-related requests")
    create_file(os.path.join(backend_path, "middleware/authMiddleware.js"), "// Middleware for handling authentication")
    create_file(os.path.join(backend_path, "middleware/errorHandler.js"), "// Middleware for handling errors globally")
    create_file(os.path.join(backend_path, "models/Article.js"), "// Schema for article data")
    create_file(os.path.join(backend_path, "models/User.js"), "// Schema for user data")
    create_file(os.path.join(backend_path, "routes/articleRoutes.js"), "// Routes for article-related API endpoints")
    create_file(os.path.join(backend_path, "routes/userRoutes.js"), "// Routes for user-related API endpoints")
    create_file(os.path.join(backend_path, "services/articleService.js"), "// Business logic for article management")
    create_file(os.path.join(backend_path, "services/userService.js"), "// Business logic for user management")
    create_file(os.path.join(backend_path, "utils/logger.js"), "// Logger utility for logging application events")
    create_file(os.path.join(backend_path, "tests/app.test.js"), "// Unit tests for the app.js file")


def main():
    project_name = input("Enter the name of your project: ").strip()
    base_path = os.path.join(os.getcwd(), project_name)

    if not os.path.exists(base_path):
        os.makedirs(base_path)

    print(f"Creating frontend structure for '{project_name}'...")
    create_frontend_structure(base_path)

    print(f"Creating backend structure for '{project_name}'...")
    create_backend_structure(base_path)

    print(f"Project '{project_name}' structure has been successfully created!")

if __name__ == "__main__":
    main()
