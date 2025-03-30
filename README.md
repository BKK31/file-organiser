# File Organiser

## About the project

A simple file organiser made using python that moves files to specific folders based on the file names and the file types. A standalone executable has also been made using pyinstaller library.

This has been created based on the file structure as per youtuber Jeff Su's [video](https://youtu.be/MM-MPS57qKA?si=S3JOl3832kKwZ22v) 

## Technologies Used

*   Python
*   Libraries Used:
    *   os
    *   shutil
    *   pyinstaller

## Getting started:

### Prerequisites

Ensure you have Python installed. Install required packages using:

```bash
pip install pyinstaller
```

### Installation

1.  Clone the repository:

    ```bash
    git clone github.com/bkk31/file-organiser
    cd file-organiser
    ```

### Usage

1.  Run the script:

    ```bash
    python main.py
    ```
    Or run the executable if you've built it:
     ```bash
     cd dist
    ./main
    ```
2.  The script will automatically organise the files in the directory it is run from, moving them to appropriate folders based on their types and names.
3. **Note:** Make sure the script is placed in the directory that needs to be organised, or the path should be defined in the script accordingly.

## License

This project is licensed under the GNU Public License.

## Contributing

Contributions are welcome! Please feel free to submit pull requests.

## Contact

If you have any questions or suggestions, feel free to contact me at [bhargavakk13@gmail.com](mailto:bhargavakk13@gmail.com)

## Acknowledgement

*   Thanks to the Python community for providing excellent libraries and resources.
*   Thanks to Jeff Su for making the file organization video which helped me automate the task of moving the files manually
