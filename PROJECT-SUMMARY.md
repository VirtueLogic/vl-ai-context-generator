# Project Summary: Project Context Generator for AI Tools

## Overview
The Project Context Generator is an open-source tool designed to bridge the gap between developers and AI assistants especially when developers aren't using extensions or expensive and less customisable AI Copilots. It automates the process of creating comprehensive project summaries and key file archives, enabling AI tools to quickly understand and provide more accurate assistance on software projects.

## Key Features
1. **Automated Project Scanning**: Efficiently scans project directories to generate both full and abbreviated structure summaries.
2. **Customizable Exclusions**: Allows developers to specify which files or directories should be excluded from AI analysis, ensuring sensitive or irrelevant information is not shared.
3. **AI-Optimized Output**: Produces concise, AI-readable summaries that highlight the most pertinent aspects of a project.
4. **Key File Archiving**: Automatically compiles essential project files into a zip archive for easy sharing with AI tools.
5. **Guided AI Interaction**: Includes a predefined prompt to direct AI tools in analyzing the project effectively.

## Technical Details
- **Language**: Primarily written in Python
- **Key Components**:
  - `create-pm-md-js.py`: Generates project structure and summary files
  - `pack-zip.py`: Creates an archive of key project files
  - `exclusions-config.json`: Configures file and directory exclusions
  - `core-prompt.txt`: Contains the AI guidance prompt
  - `PROJECT-SUMMARY.md`: Contains an example project summary that you can optionally create and include.

## Use Cases
1. **Code Review and Improvement**: Quickly provide AI tools with context for suggesting code optimizations or identifying potential issues.
2. **Documentation Assistance**: Help AI generate or update project documentation based on the current project structure and key files.
3. **Onboarding**: Facilitate faster onboarding for new team members by providing a comprehensive project overview.
4. **Architectural Analysis**: Enable AI to analyze and provide feedback on the overall architecture and structure of the project.

## Benefits
- **Time-Saving**: Automates the tedious process of manually explaining project structure to AI tools.
- **Consistency**: Ensures that AI tools always have access to up-to-date project information.
- **Privacy-Conscious**: Allows control over what information is shared with AI assistants.
- **Enhanced AI Assistance**: Improves the quality and relevance of AI-generated suggestions and analyses.

## Future Enhancements
- Integration with version control systems for automatic updates
- Support for additional programming languages and project types
- GUI for easier configuration and use
- Plugins for popular IDEs and text editors

This Project Context Generator aims to streamline developer-AI interaction, making it easier to leverage AI tools for various software development tasks while maintaining control over shared project information.