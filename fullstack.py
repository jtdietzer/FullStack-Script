import os
import subprocess

def create_file(filepath, content=""):
    """Creates a file with optional content."""
    with open(filepath, 'w') as f:
        f.write(content)

def run_npm_install(path):
    """Runs npm install in the specified directory."""
    try:
        subprocess.run(["npm", "install"], cwd=path, check=True)
        print(f"npm install completed successfully in {path}")
    except subprocess.CalledProcessError as e:
        print(f"Error running npm install in {path}: {e}")

def update_browserslist_config(path):
    """Adds a browserslist configuration to the package.json file if required."""
    package_json_path = os.path.join(path, "package.json")
    if os.path.exists(package_json_path):
        with open(package_json_path, "r") as f:
            package_data = f.read()
        if "browserslist" not in package_data:
            package_data = package_data.strip().rstrip("}") + ",\n  \"browserslist\": [\"defaults\"]\n}\n"
            with open(package_json_path, "w") as f:
                f.write(package_data)
            print(f"Added browserslist configuration to {package_json_path}")

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

    # Create required files for the React frontend
    create_file(os.path.join(frontend_path, ".gitignore"), "# Node.js dependencies\nnode_modules\n")
    create_file(os.path.join(frontend_path, "README.md"), "# Frontend Documentation\n")
    create_file(os.path.join(frontend_path, "public", "index.html"), """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>React App</title>
</head>
<body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id=\"root\"></div>
</body>
</html>
""")

    create_file(os.path.join(src_path, "index.jsx"), """// Entry point for React
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />, document.getElementById('root'));
""")

    create_file(os.path.join(src_path, "App.jsx"), """// Root component of the frontend
import React from 'react';

export default function App() {
    return (
        <div>
            <h1>Welcome to the React App</h1>
        </div>
    );
}
""")

    # Create package.json for the frontend
    create_file(os.path.join(frontend_path, "package.json"), """{
  "name": "react-app",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "react-scripts": "^5.0.1"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }
}
""")

    # Run npm install in the frontend directory
    run_npm_install(frontend_path)

    # Add browserslist configuration if missing
    update_browserslist_config(frontend_path)

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

    # Create package.json for the backend
    create_file(os.path.join(backend_path, "package.json"), """{
  "name": "backend-server",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "express": "^4.0.0"
  },
  "scripts": {
    "start": "node server.js"
  }
}
""")

    # Run npm install in the backend directory
    run_npm_install(backend_path)

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
