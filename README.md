```markdown
# Git Contributions Report Generator  

Generate a comprehensive and visually appealing report of Git contributions in any repository.  
This tool creates an HTML report with detailed insights into the contributions of each author, including commits, modified files, and more, displayed through static and interactive graphs.  

## Features  

### Current Features  
- **Branch Analysis**: Analyzes the active branch of a Git repository.  
- **Commits by Author**: Displays the number of commits made by each contributor.  
- **Files Modified by Author**: Counts the number of files modified by each contributor.  
- **Static Graphs**: Generates bar charts using Matplotlib for commits and file modifications.  
- **Interactive Graphs**: Creates dynamic visualizations with Plotly for in-depth exploration.  
- **HTML Report**: Exports a Bootstrap-styled report with embedded charts and detailed tables.  

### Planned Features (Short-Term)  
- **Support for Multiple Branches**: Analyze contributions across all branches in a repository.  
- **Line Changes**: Display lines added and deleted by each contributor.  
- **Export Options**: Generate PDF and Excel reports from the analysis.  
- **Custom Date Ranges**: Filter contributions by specific time periods.  
- **Enhanced Graphs**: Add pie charts and stacked bar charts for richer visualizations.  
- **CLI Arguments**: Add command-line options for better flexibility and automation.  

## Installation  

1. Clone the repository:  
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```  

2. Install the dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

## Usage  

1. Run the script in any Git repository:  
   ```bash
   python generate_report.py
   ```  

2. Open the generated HTML report in your browser:  
   ```bash
   xdg-open rapport_contributions.html  # Linux  
   start rapport_contributions.html     # Windows  
   open rapport_contributions.html      # macOS  
   ```  

## Requirements  

- Python 3.8+  
- Git installed and accessible via the command line  

## Contributing  

Contributions are welcome! If you’d like to add new features or fix any issues, feel free to submit a pull request.  

## License  

This project is licensed under the MIT License.  

---

Feel free to suggest new features or improvements in the **Issues** section.  
