import os
import json
import zipfile

def zip_included_files(json_file_path, root_folder, zip_output_path):
    """
    Reads the JSON file and zips all files marked as 'include': true.
    
    :param json_file_path: Path to the project-pack.json file.
    :param root_folder: The root folder where the files are located.
    :param zip_output_path: The path for the output zip file.
    """
    # Load the JSON file that maps the files to include or exclude
    with open(json_file_path, 'r') as json_file:
        project_structure = json.load(json_file)
    
    # Create the zip file
    with zipfile.ZipFile(zip_output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for relative_path, file_info in project_structure.items():
            # Only include files marked as 'include': true
            if file_info.get('include', False):
                absolute_path = os.path.join(root_folder, relative_path)
                
                # Ensure the file exists before adding (in case of race conditions or file removal)
                if os.path.exists(absolute_path):
                    print(f"Including: {relative_path}")
                    zipf.write(absolute_path, arcname=relative_path)
                else:
                    print(f"Warning: {absolute_path} does not exist and will not be included.")

    print(f"Files successfully zipped into {zip_output_path}")

if __name__ == "__main__":
    # Define where the script is located (inside the /projects folder)
    projects_folder = os.path.dirname(os.path.abspath(__file__))
    
    # The root folder is the parent directory of /projects
    root_folder = os.path.dirname(projects_folder)
    
    # Define the ai-supp and for-ai folders
    ai_supp_folder = os.path.join(root_folder, 'ai-supp')
    for_ai_folder = os.path.join(ai_supp_folder, 'for-ai')
    os.makedirs(for_ai_folder, exist_ok=True)

    # Path to the project-pack.json file in the ai-supp folder
    json_file_path = os.path.join(ai_supp_folder, 'project-pack.json')

    # Output zip file will be created in the for-ai folder
    zip_output_path = os.path.join(for_ai_folder, 'project-key-files.zip')

    # Run the function to zip the files based on the JSON mapping
    zip_included_files(json_file_path, root_folder, zip_output_path)
