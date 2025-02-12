
import pandas as pd

def cleanStats(df):
  for col in ['FG', '3PT', 'FT']:
    if col in df.columns:
      print(f"Processing column: {col}") # Debugging output


      df[col] = df[col].astype(str) # Convert to string in case of NaN
      new_cols = df[col].str.split('-', expand=True)

    
      if new_cols.shape[1] == 2: # Check if splitting worked correctly
        df[col + 'M'] = pd.to_numeric(new_cols[0], errors='coerce')
        df[col + 'A'] = pd.to_numeric(new_cols[1], errors='coerce')
      else:
        print(f"Skipping {col} due to incorrect format: {df[col].unique()}") # Debug info


      df.drop(columns=[col], inplace=True)


  return df


data = {'FG': ['5-10', '3-7', None], '3PT': ['2-5', '1-4', '0-2'], 'FT': ['4-6', '5-8', '2-3']}

df = pd.DataFrame(data)

df = cleanStats(df)

print(df)
