Act as a web developer tasked with creating a modern Administrator Portal for an Auto File Renaming Tool. Your task is to develop a secure, responsive web-based interface using Google Apps Script, HTML, CSS, and JavaScript.

Your responsibilities include:
- Implementing secure administrator login with session management and automatic timeout.
- Creating a dashboard to display metrics such as total CSV records uploaded, total files uploaded, successfully renamed files, unmatched files, duplicate matches, processing status, download history, and recent activity.
- Designing a file renaming system that matches employee information from CSV files using any two fields (Employee ID, First Name, Middle Name, or Surname).
- Allowing administrators to define a renaming template.
- Generating a ZIP archive of successfully renamed files with a naming convention: `SalarySlips_Renamed_${month}_${year}.zip`.
- Producing a processing report with detailed statistics and errors, exportable in Excel and CSV formats.

Rules and Constraints:
- Ensure all uploaded files (PDF and JPG) are renamed according to the template.
- Handle errors by logging and including failed/skipped files in the report.
- Maintain a clean and professional user interface.
- Provide options to download ZIP and processing reports after completion.

You will use variables such as `${month}` and `${year}` in file naming for flexibility.
