import os
import subprocess
import json

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
    create_file(os.path.join(frontend_path, "README.md"), "# Frontend Documentation\n")
    create_file(os.path.join(src_path, "App.jsx"), """// Root component of the frontend
import React from 'react';
import Header from './components/layout/Header';
import ArticlePage from './features/article/pages/ArticlePage';

export default function App() {
    return (
        <div>
            <Header />
            <ArticlePage />
        </div>
    );
}
""")
    create_file(os.path.join(src_path, "index.jsx"), """// Entry point for React
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />, document.getElementById('root'));
""")

    # Generate package.json with required fields
    package_json_content = {
        "name": "client",
        "version": "0.1.0",
        "private": True,
        "dependencies": {
            "react": "^18.2.0",
            "react-dom": "^18.2.0",
            "react-scripts": "^5.0.1"
        },
        "scripts": {
            "start": "react-scripts start",
            "build": "react-scripts build",
            "test": "react-scripts test",
            "eject": "react-scripts eject"
        },
        "eslintConfig": {
            "extends": ["react-app", "react-app/jest"]
        },
        "browserslist": {
            "production": [
                ">0.2%",
                "not dead",
                "not op_mini all"
            ],
            "development": [
                "last 1 chrome version",
                "last 1 firefox version",
                "last 1 safari version"
            ]
        }
    }

    create_file(
        os.path.join(frontend_path, "package.json"),
        content=json.dumps(package_json_content, indent=4)
    )

    # Install dependencies
    subprocess.run(["npm", "install"], cwd=frontend_path)

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
    create_file(os.path.join(backend_path, "README.md"), "# Backend Documentation\n")
    create_file(os.path.join(backend_path, "app.js"), """// Main application logic
const express = require('express');
const app = express();
module.exports = app;
""")
    create_file(os.path.join(backend_path, "server.js"), """// Entry point for the backend server
const app = require('./app');
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
""")
    create_file(os.path.join(backend_path, "config/dbConfig.js"), """// Database configuration file
module.exports = {
    url: process.env.DB_URL || 'mongodb://localhost:27017/project_db',
};
""")

    # Generate package.json and package-lock.json
    subprocess.run(["npm", "init", "-y"], cwd=backend_path)
    subprocess.run(["npm", "install", "express", "dotenv"], cwd=backend_path)

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
