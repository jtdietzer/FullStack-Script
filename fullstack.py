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
}""")
    create_file(os.path.join(src_path, "index.jsx"), """// Entry point for React
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />, document.getElementById('root'));
""")

    # Add specific files in folders
    create_file(os.path.join(src_path, "components/common/Button.jsx"), """// A reusable button component
import React from 'react';

export default function Button({ label, onClick }) {
    return <button onClick={onClick}>{label}</button>;
}
""")
    create_file(os.path.join(src_path, "components/layout/Header.jsx"), """// The header layout component
import React from 'react';

export default function Header() {
    return (
        <header>
            <h1>Application Header</h1>
        </header>
    );
}
""")
    create_file(os.path.join(src_path, "features/article/components/ArticleCard.jsx"), """// Displays a single article card
import React from 'react';

export default function ArticleCard({ title, summary }) {
    return (
        <div>
            <h2>{title}</h2>
            <p>{summary}</p>
        </div>
    );
}
""")
    create_file(os.path.join(src_path, "features/article/pages/ArticlePage.jsx"), """// The page displaying a single article
import React from 'react';
import ArticleCard from '../components/ArticleCard';

export default function ArticlePage() {
    const sampleArticle = { title: 'Sample Article', summary: 'This is a summary of the article.' };

    return (
        <div>
            <h1>Article Page</h1>
            <ArticleCard title={sampleArticle.title} summary={sampleArticle.summary} />
        </div>
    );
}
""")
    create_file(os.path.join(src_path, "features/auth/LoginForm.jsx"), """// A login form component for authentication
import React, { useState } from 'react';

export default function LoginForm() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log('Login attempted:', { username, password });
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
            <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
            <button type="submit">Login</button>
        </form>
    );
}
""")
    create_file(os.path.join(src_path, "context/AuthContext.js"), """// Context for managing authentication state
import React, { createContext, useState } from 'react';

export const AuthContext = createContext();

export default function AuthProvider({ children }) {
    const [authState, setAuthState] = useState(null);

    return (
        <AuthContext.Provider value={{ authState, setAuthState }}>
            {children}
        </AuthContext.Provider>
    );
}
""")
    create_file(os.path.join(src_path, "hooks/useAuth.js"), """// A custom hook for authentication logic
import { useContext } from 'react';
import { AuthContext } from '../context/AuthContext';

export default function useAuth() {
    return useContext(AuthContext);
}
""")
    create_file(os.path.join(src_path, "services/apiClient.js"), """// Handles API requests to the backend
import axios from 'axios';

const apiClient = axios.create({
    baseURL: process.env.REACT_APP_API_URL || 'http://localhost:3000',
});

export default apiClient;
""")
    create_file(os.path.join(src_path, "styles/theme.css"), "/* Global theme styles */\nbody { font-family: Arial, sans-serif; }\n")
    create_file(os.path.join(src_path, "utils/formatDate.js"), """// Utility function to format dates
export default function formatDate(date) {
    return new Date(date).toLocaleDateString();
}
""")


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
    create_file(os.path.join(backend_path, "config/dbConfig.js"), "// Configuration for the
