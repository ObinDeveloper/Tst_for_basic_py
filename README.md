# VSCode Workspace Overview

Visual Studio Code (VSCode) is a versatile code editor that supports various programming languages, development tools, and extensions.  This README will help you navigate and utilize various features within your VSCode workspace effectively. For more detailed information, consider exploring the official [Visual Studio Code documentation](https://code.visualstudio.com/docs).


## Icons on the Left Bar
There are five primary icons present in the left bar. More icons will append as you install extensions. Here is an overview of the default five icons. 

- **File Explorer**: Navigate through your project's files and folders in a hierarchical view with the Explorer section. The icon is a file icon on the sidebar, which you can click to toggle the view. 
    - You can right-click on files or folders for options like rename, delete, move, download, etc.
    - You can drag and drop files to reorganize them, create new files and folders, and delete or rename existing files directly from the explorer.
- **Search**: Use the Search feature to find specific pieces of text within your project files. This is represented by a magnifying glass icon on the sidebar.
- **Source Control**: Manage your version control systems such as Git, allowing you to track changes, commit, push, and pull code. The icon is a branch icon on the sidebar.
- **Run and Debug**: Launch your code with or without debugging, which is ideal for testing and troubleshooting applications. Look for the play and bug icon on the sidebar.
- **Extensions**: Enhance VSCode functionality by installing extensions for additional languages, themes, debuggers, and more. The associated icon is a square icon on the sidebar.
    - To install an extension, for example, **Live Preview**, search for the extension name and click `Install`.



<br/> <br/>

## Key Sections in the VSCode

- **File Explorer**: Provides an easy way to browse and manage the files and folders within your project.

- **Editor Pane**: The main area where you can write and edit your code. It supports syntax highlighting, intelligent code completion (IntelliSense), and numerous shortcuts for efficient coding.
    - **Access**: Double-click a file in the File Explorer to open it in the Editor Pane.
    - **Features**: Multiple tabs can be opened simultaneously for different files, and you can split the editor to have multiple files visible at once.

- **Terminal**: Integrated terminal where you can run shell commands, interact with version control systems, or execute scripts and compile code directly within the environment.
    - **Access**: Navigate to the top menu and select **Terminal -> New Terminal** to open a new terminal pane. You can open multiple terminal instances.
    - **Features**: Supports multiple terminal instances, customization of the shell used, and direct integration with the workspace's current directory.


<br/> <br/>

## Running Code Files in VSCode 

### Running a JavaScript File
1. Open your `.js` file in VSCode.
2. Open a terminal, and run the following command to check if NodeJS is installed. If not, you can do so by using the [official commands](https://nodejs.org/en/download/package-manager).
    ```bash
    node -v
    ```

3. To run a file, execute the following command in the terminal. Replace `<your-file-name>.js` with the actual file name.
    ```bash
    node <your-file-name>.py
    ```

### Running a Python File
1. Open your `.py` file in VSCode.
2. Open a terminal, and run the following command to check if Python is installed. 
    ```bash
    python --version
    ```

3. To run a file, execute the following command in the terminal. Replace `<your-file-name>.py` with the actual file name.
    ```bash
    python <your-file-name>.py
    ```
