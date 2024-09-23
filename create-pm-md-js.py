import os
import json

def load_exclusions(json_file_path):
    """
    Loads the exclusion rules from a JSON file.
    
    :param json_file_path: Path to the exclusions configuration JSON file.
    :return: A tuple of two lists: excluded_directories and excluded_files.
    """
    with open(json_file_path, 'r') as json_file:
        exclusions = json.load(json_file)
    
    excluded_directories = exclusions.get('excluded_directories', [])
    excluded_files = exclusions.get('excluded_files', [])
    
    return excluded_directories, excluded_files

def should_include(item_name, is_dir, parent_excluded, excluded_directories, excluded_files):
    """
    Determines whether a file or directory should be included based on the loaded exclusion rules.
    
    :param item_name: Name of the file or directory.
    :param is_dir: Boolean indicating if the item is a directory.
    :param parent_excluded: Boolean indicating if the parent directory is excluded.
    :param excluded_directories: List of directories to exclude.
    :param excluded_files: List of files to exclude.
    :return: Boolean value indicating whether the item should be included.
    """
    # If the parent is excluded, we exclude everything under it
    if parent_excluded:
        return False
    
    if is_dir and item_name in excluded_directories:
        return False
    if not is_dir:
        # Exclude based on file patterns
        if item_name in excluded_files or any(item_name.endswith(ext) for ext in ['.pyc', '.class']):
            return False
    return True

def is_relevant_for_abbreviation(item_name, is_dir):
    """
    Determines whether a file or directory is relevant for the abbreviated project structure.
    Only source code files and important configuration files are included.
    
    :param item_name: Name of the file or directory.
    :param is_dir: Boolean indicating if the item is a directory.
    :return: Boolean value indicating whether the item is relevant for AI context.
    """
    if is_dir:
        # Always include directories, but don't dive into irrelevant ones
        return True
    else:
        # Include source code and key configuration files
        relevant_extensions = ['.py', '.js', '.ts', '.html', '.css']
        important_files = ['Dockerfile', '.gitignore', '.env', 'package.json', 'README.md']

        if item_name in important_files or any(item_name.endswith(ext) for ext in relevant_extensions):
            return True
        return False

def generate_markdown_and_json(base_path, markdown_file, abbreviated_markdown_file, json_file, excluded_directories, excluded_files):
    """
    Generates a full markdown file, an abbreviated markdown file, and a JSON file listing 
    all files with an 'include' flag indicating whether they should be included in the zip.
    
    :param base_path: The root directory to scan.
    :param markdown_file: The path to the full markdown file to be generated.
    :param abbreviated_markdown_file: The path to the abbreviated markdown file to be generated.
    :param json_file: The path to the json file to be generated.
    :param excluded_directories: List of directories to exclude.
    :param excluded_files: List of files to exclude.
    """
    project_structure = {}
    markdown_lines = []
    abbreviated_markdown_lines = []

    def scan_directory(path, indent_level=0, parent_excluded=False):
        """
        Recursively scans the directory to build the markdown file and the JSON structure.
        
        :param path: The directory path to scan.
        :param indent_level: The indentation level for markdown formatting.
        :param parent_excluded: Boolean indicating if the parent directory is excluded.
        """
        items = sorted(os.listdir(path))
        relative_path = os.path.relpath(path, base_path)

        for item in items:
            item_path = os.path.join(path, item)
            relative_item_path = os.path.relpath(item_path, base_path)
            is_directory = os.path.isdir(item_path)

            # Determine whether to include the item or not based on exclusion rules
            include_item = should_include(item, is_directory, parent_excluded, excluded_directories, excluded_files)

            # Add to full markdown (everything is included in markdown)
            if is_directory:
                markdown_lines.append(f"{'  ' * indent_level}- {item}/")
                project_structure[relative_item_path] = {"type": "directory", "include": include_item}
                
                # Check if it's relevant for abbreviated markdown
                if is_relevant_for_abbreviation(item, is_directory):
                    abbreviated_markdown_lines.append(f"{'  ' * indent_level}- {item}/")

                # If the directory itself is excluded, don't scan its contents
                scan_directory(item_path, indent_level + 1, parent_excluded=not include_item)
            else:
                markdown_lines.append(f"{'  ' * indent_level}- {item}")
                project_structure[relative_item_path] = {"type": "file", "include": include_item}
                
                # Add to abbreviated markdown if it's relevant
                if is_relevant_for_abbreviation(item, is_directory):
                    abbreviated_markdown_lines.append(f"{'  ' * indent_level}- {item}")

    # Start scanning from the base path
    scan_directory(base_path)

    # Write the full markdown file (everything is included in markdown)
    with open(markdown_file, 'w') as md_file:
        md_file.write("# Full Project Structure\n\n")
        md_file.write("\n".join(markdown_lines))
        print(f"Full markdown structure saved to {markdown_file}")

    # Write the abbreviated markdown file (only relevant files are included)
    with open(abbreviated_markdown_file, 'w') as abbr_md_file:
        abbr_md_file.write("# Abbreviated Project Structure (For AI Context)\n\n")
        abbr_md_file.write("\n".join(abbreviated_markdown_lines))
        print(f"Abbreviated markdown structure saved to {abbreviated_markdown_file}")

    # Write the json file (with inclusion/exclusion logic)
    with open(json_file, 'w') as json_out:
        json.dump(project_structure, json_out, indent=4)
        print(f"Project pack JSON saved to {json_file}")

if __name__ == "__main__":
    # The script is inside the /projects folder, so we want to scan its parent folder
    projects_folder = os.path.dirname(os.path.abspath(__file__))  # Where the script is located
    root_folder = os.path.dirname(projects_folder)  # This is the root folder containing /projects

    # Define the ai-supp folder (create it if it doesn't exist)
    ai_supp_folder = os.path.join(root_folder, 'ai-supp')
    os.makedirs(ai_supp_folder, exist_ok=True)

    # Define the 'for-ai' subfolder within 'ai-supp' (create it if it doesn't exist)
    for_ai_folder = os.path.join(ai_supp_folder, 'for-ai')
    os.makedirs(for_ai_folder, exist_ok=True)

    # Path to the exclusion configuration JSON file (now in the /projects folder)
    exclusions_config_path = os.path.join(projects_folder, 'exclusions-config.json')
    
    # Load exclusions from JSON
    excluded_directories, excluded_files = load_exclusions(exclusions_config_path)

    # Paths for the markdown, abbreviated markdown, and json outputs (saved in the appropriate folders)
    markdown_output = os.path.join(ai_supp_folder, 'project-structure-generated.md')
    abbreviated_markdown_output = os.path.join(for_ai_folder, 'project-structure-abbreviated.md')
    json_output = os.path.join(ai_supp_folder, 'project-pack.json')

    # Generate the full markdown, abbreviated markdown, and json for the root folder
    generate_markdown_and_json(root_folder, markdown_output, abbreviated_markdown_output, json_output, excluded_directories, excluded_files)
