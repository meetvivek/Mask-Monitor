import pandas as pd
import time

class ExcelHandler:
    def __init__(self, excel_file='mask_records.xlsx'):
        self.excel_file = excel_file

    def record_to_excel(self, status):
        current_date = time.strftime('%Y-%m-%d')
        current_time = time.strftime('%H:%M:%S')

        try:
            # Read the existing Excel file
            excel_data = pd.ExcelFile(self.excel_file, engine='openpyxl')

            # Check if the sheet with the current date exists
            if current_date in excel_data.sheet_names:
                # Append data to the existing sheet
                df = pd.read_excel(self.excel_file, sheet_name=current_date)
                df = pd.concat([df, pd.DataFrame({'S.No.': [len(df) + 1], 'Time': [current_time], 'Status': [status]})],
                               ignore_index=True)
                # Write the updated sheet back to the Excel file
                with pd.ExcelWriter(self.excel_file, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name=current_date, index=False)
            else:
                # Create a new sheet with the current date
                df = pd.DataFrame({'S.No.': [1], 'Time': [current_time], 'Status': [status]})
                with pd.ExcelWriter(self.excel_file, engine='openpyxl', mode='a') as writer:
                    df.to_excel(writer, sheet_name=current_date, index=False)

        except FileNotFoundError:
            # Create a new Excel file with the current date as the sheet name
            df = pd.DataFrame({'S.No.': [1], 'Time': [current_time], 'Status': [status]})
            df.to_excel(self.excel_file, sheet_name=current_date, index=False, engine='openpyxl')

        except Exception as e:
            print(f"An error occurred: {e}")

# Example usage:
excel_handler = ExcelHandler()
excel_handler.record_to_excel('With Mask')
