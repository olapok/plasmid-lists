import pandas as pd

df = pd.read_table('human_plasmids.tsv')
pd.set_option('display.max_columns', None)
print(df)

df_filtered = df.dropna(subset=['IsolationSource_BIOSAMPLE'])
print(df_filtered)


healthy = df_filtered[df_filtered["IsolationSource_BIOSAMPLE"].str.contains("healthy")]
print(healthy)
healthy.to_csv("healthy.csv", index=False, header="Healthy")


sick = df_filtered[df_filtered["IsolationSource_BIOSAMPLE"].str.contains('infection|diarrhea|pus|Wound|disease|drainage|UTI|Diarrheal')]
print(sick)
sick.to_csv("sick.csv", index=False, header="Sick")


everything_minus_healthy = df[df["IsolationSource_BIOSAMPLE"].str.contains("healthy") == False]
print(everything_minus_healthy)
everything_minus_healthy.to_csv("everything_except_healthy.csv", index=False, header="Everything_except_healthy")


everything_minus_sick = df[df["IsolationSource_BIOSAMPLE"].str.contains('infection|diarrhea|pus|Wound|disease|drainage|UTI|Diarrheal') == False ]
print(everything_minus_sick)
everything_minus_sick.to_csv("everything_minus_sick.csv", index=False, header="Everything_except_sick")