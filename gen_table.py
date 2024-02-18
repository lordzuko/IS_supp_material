import pandas as pd

df = pd.read_csv("ui_data.csv")

mapping = {
    "CB-EM-04-130.wav": "utt1",
    "CB-EM-09-264.wav": "utt2",
    "CB-EM-26-343.wav": "utt3",
    "CB-FFM-31-47.wav": "utt4",
    "CB-LCL-12-167.wav": "utt5"
}
mapping = {v:k for k,v in mapping.items()}
print(mapping)
out = []
for i, r in df.iterrows():

    wav_name = r["save_wav_name"]
    ref_text = r["utt"]
    ref_style = mapping[r["utt"]]
    tgt_text = r["text"]

    out.append(f""" 
        <tr>
        <td><i>{ref_text}</i></td>
        <td><i>{tgt_text}</i></td>
        <td><audio controls><source src="samples/ref_style/{ref_style}" type="audio/mpeg"></audio></td>
        <td><audio controls><source src="samples/unedited/{wav_name}" type="audio/mpeg"></audio></td>
        <td><audio controls><source src="samples/edited/{wav_name}" type="audio/mpeg"></audio></td>
        </tr>
    """)

with open("out.txt", "w") as f:
    f.writelines(out)

