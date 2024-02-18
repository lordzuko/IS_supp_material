import pandas as pd

# Read the CSV file
df = pd.read_csv("ui_data.csv")

ref_mapping = {
    "CB-EM-04-130.wav": "utt1",
    "CB-EM-09-264.wav": "utt2",
    "CB-EM-26-343.wav": "utt3",
    "CB-FFM-31-47.wav": "utt4",
    "CB-LCL-12-167.wav": "utt5"
}
ref_mapping = {v:k for k,v in ref_mapping.items()}
ref_text_map = {
    "utt1": "and walking a few yards forward, while they talked together, soon made her quick eye sufficiently acquainted with Mr. Robert Martin.",
    "utt2": "It is such a pretty charade, my dear, that I can easily guess what fairy brought it.",
    "utt3": "I have heard him express himself so warmly on those points!",
    "utt4": "God’s sake, yes–I am come to that low, lowest stage–to ask a woman for pity!",
    "utt5": "Then where are you supposed to be getting the child?"
}

text_mapping = {
    "text1": "The time passed very slowly",
    "text2": "She immediately liked him",
    "text3": "Gabriel, will you stay?",
    "text4": "Such a sad loss!"
}


# Group the dataframe by reference utterance
grouped = df.groupby("utt")


out = ""
# Generate tables for each group
for ref_utt, group_df in grouped:

    # Create table header
    main_table_header = f"""
        <h4>Reference Text: {ref_text_map[ref_utt]}</h3>
        <table class="custom-table">
            <tr>
                
                <th>Reference Utterance</th>
            </tr>
            <tr>
                
                <td><audio controls><source src="samples/ref_style/{ref_mapping[ref_utt]}" type="audio/mpeg"></audio></td>
            </tr>

        </table>
    """

    # Initialize main table content
    main_table_content = ""

    # Group the subgroup by target text
    subgrouped = group_df.groupby("text")

    # Generate sub-tables for each text group
    for text, subgroup_df in subgrouped:

        # Create sub-table header
        sub_table_header = f"""
        <table class="custom-table">
            
            <tr>
                <th>Target Text</th>
                <th>Synthesized Unedited</th>
                <th>Synthesized Edited</th>
            </tr>
        """

        # Create sub-table rows
        sub_table_rows = []
        for i, row in subgroup_df.iterrows():
            wav_name = row["save_wav_name"]
            sub_table_rows.append(f"""
                <tr>
                    <td>{text}</td>
                    <td><audio controls><source src="samples/unedited/{wav_name}" type="audio/mpeg"></audio></td>
                    <td><audio controls><source src="samples/edited/{wav_name}" type="audio/mpeg"></audio></td>
                </tr>
            """)
        # sub_table_rows.append("<tr></tr>")

        # Combine sub-table header and rows
        sub_table_content = "".join(sub_table_rows)
        sub_table = sub_table_header + sub_table_content + "</table>"

        # Append sub-table to main table content
        main_table_content += sub_table

    # Combine main table header and content
    main_table = main_table_header + main_table_content + "</table>"
    out += main_table + " <br> " + f"<!-- {ref_utt} -->" + "<br>"

# Write the main table to a file
with open(f"table.html", "w") as f:
    f.write(out)


# <h4>Target Text: {text_mapping[text]}</h4>