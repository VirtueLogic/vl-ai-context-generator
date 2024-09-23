# Project Context Generator for AI Tools

This open-source tool allows developers to quickly generate project summaries and key file archives that can be used to provide context for AI systems (e.g., Claude, ChatGPT). The tool generates structured summaries of project directories and files, along with a concise prompt to help AI tools understand the project context efficiently.

## Features

- **Project Structure Generation**: Scans your project and generates a full and abbreviated directory structure.
- **Configurable Exclusions**: Customize which files and directories are excluded from the AI context using an `exclusions-config.json` file.
- **AI-Ready Summaries**: Creates a concise project summary (`project-structure-abbreviated.md`) that highlights the most relevant files for AI to analyze.
- **Project Key Files Archive**: Automatically zips key project files for easy upload to AI tools that require project context.
- **Predefined AI Prompt**: Provides a ready-to-use prompt (`core-prompt.txt`) that developers can give to AI tools to guide their analysis and feedback.

## Folder Structure

```
root/
├── project/
│   ├── core-prompt.txt              # The AI prompt developers can use
│   ├── exclusions-config.json       # Customize excluded files and directories
│   ├── create-pm-md-js.py           # Generates the project structure and summary files
│   ├── pack-zip.py                  # Zips the relevant project files
│   └── README.md                    # This file
└── ai-support/
    ├── project-structure-generated.md    # Full project structure
    ├── project-pack.json                 # JSON map of included files
    └── for-ai/
        ├── project-structure-abbreviated.md  # Abbreviated project structure
        └── project-key-files.zip             # Key files archive
```

## Example Folder Structure

To better illustrate how the Project Context Generator integrates with your existing project, here's an example folder structure:

```markdown
your-project-root/
├── src/
│   ├── main.py
│   ├── utils.py
│   └── config.py
├── tests/
│   ├── test_main.py
│   └── test_utils.py
├── docs/
│   └── api.md
├── project/                         # Project Context Generator folder
│   ├── core-prompt.txt
│   ├── exclusions-config.json
│   ├── create-pm-md-js.py
│   ├── pack-zip.py
│   └── README.md
├── ai-support/                      # Generated AI support files
│   ├── project-structure-generated.md
│   ├── project-pack.json
│   └── for-ai/
│       ├── project-structure-abbreviated.md
│       └── project-key-files.zip
├── .gitignore
├── requirements.txt
└── README.md
```

In this example, the Project Context Generator files are located in the `project/` folder within your project's root directory. The generated AI support files are placed in the `ai-support/` folder, also in the root directory.

## How to Use

### 1. Set Up Your Project

Clone this repository into your project directory:

```bash
git clone https://github.com/VirtueLogic/vl-ai-context-generator.git project
```

### 2. Customize Exclusions

Edit the `exclusions-config.json` file in the `project/` folder to define which directories or files should be excluded from the AI context:

```json
{
  "excluded_directories": ["node_modules", ".git", "build", "dist", "venv"],
  "excluded_files": [".env", ".env.local", ".DS_Store", "package-lock.json", "yarn.lock", "*.pyc", "*.class"]
}
```

### 3. Generate Project Structure and Summary

Run the `create-pm-md-js.py` script to generate the full project structure and abbreviated structure files:

```bash
python project/create-pm-md-js.py
```

This will generate:
- A full project structure (`project-structure-generated.md`)
- An abbreviated project structure (`project-structure-abbreviated.md`) in the `ai-support/for-ai` folder


### 4. Optionally create a Project Summary
You can create a project-summary.md file in the root directory of your project to provide additional context for AI tools. This summary should include:

An overview of the project
Key features
Technical details
Use cases
Any other relevant information

Example structure for project-summary.md can be seen in the project-summary.md included for this project.

### 5. Zip the Key Files

Run the `pack-zip.py` script to create a zip file of key project files based on the JSON map:

```bash
python project/pack-zip.py
```

This will create `project-key-files.zip` in the `ai-support/for-ai` folder.

### 6. Provide Context to AI

Use the provided `core-prompt.txt` file to guide the AI in understanding your project. Upload the key files from the ./ai-supp folder. The prompt, key files, and project structure summaries can be uploaded to AI tools like Claude or ChatGPT for code analysis, updates, or general advice.

## Example AI Prompt (from core-prompt.txt)

```
You are tasked with analyzing and providing updates or advice on the code based on the project's key resources. 

First, review the `project-structure-abbreviated.md` to understand the key directories and files. If available, review the `project-summary.md` for a high-level overview of the project. Additionally, examine the `project-key-files.zip` for the essential files.

Focus on source code (e.g., `.py`, `.js`, `.ts`) and configuration files (`Dockerfile`, `.env`, `package.json`). Provide specific suggestions for code improvements, updates, or general coding advice, referencing the relevant files or functions.
```

## Contributions

Contributions are welcome! Feel free to submit issues, fork the project, and submit pull requests to enhance the tool.

## License

This project is licensed under the GNU General Public License v3.0.
