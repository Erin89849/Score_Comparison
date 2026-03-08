# Google Sheets Score Comparison
## Purpose:
This project connects to multiple Google Sheets to calculate and compare final scores between them.
- Each Google Sheet represents a category.
  - There can be multiple, each for a different score keeper, i.e. Director and VP.
- Each individual Sheet represents a team.

## Technologies Used:
`gspread` Utilized to interface with the Google Sheets API for reading and extracting data from cells.

`google.auth` Utilized for authenticating Google Drive in order to be able to retrieve information from the Drive.

## How to Use:
- Download this code as a `.ipynb` file and import it into **Google Colab** in your Google Drive where the Google Sheets are present.
- The URL's of the Google Sheets need to be used in order to connect to them for this project.
  - `auth.authenticate_user()` will securely connect to Google Drive.
  - You need to allow the program to have access to your Google Drive in order to work.

## Features:
- **Data Extraction:** Automatically retrieves final scores from multiple Sheets.
- **Score Validation:** Compares the final scores to that of another Google Sheet in the same category.
- **Discrepancies:** Identifies inconsistent scores between Google Sheets within the same category and displays them.
- **Winner Identification:** Determines winning team based on highest score and generates a summary for the category.

## Future Improvements:
- Update the `winning_team` function to handle ties.
- Implement a ranking feature to display the first, second and third place results.
- Add a visualization of the results i.e. a bar chart.

## Example Output:
```
=======================================================================

Category: Innovation

Comparing Director and VP Final Scores...

| All final scores, for all teams, is the same for Director and VP |

The winning team is...

Team 1!

=======================================================================
