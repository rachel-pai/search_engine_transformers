import os
import glob
import pandas as pd
import re
import numpy as np
# the features for all inputs
subdirectories = [x[0] for x in os.walk('../obesity')]
subdirectories.remove('../obesity')
ill_df  = pd.DataFrame(columns = ['desp'])

for subdire in subdirectories:
    subfiles = glob.glob(subdire+ "/*.txt") # [x[0] for x in os.walk(subdire)]

    for files in subfiles:
        f = open(files, 'r')
        # split into sublist if there are two "\n"
        text_list = f.readlines()
        start = 0
        end = None
        for idx, item in enumerate(text_list):
            if item == "\n" and text_list[idx-1] == "\n" and idx!= len(text_list)-2:
                end = idx
                # remove citation [\d] and \n
                content = " ".join([re.sub(r"\[\d+\]", "", ele.replace("\n","") ) for ele in text_list[start:end]]).strip()
                if len(content.split(" ")) > 20:
                    ill_df.loc[len(ill_df)] = [content.strip()]
                start = idx
                end = None

# shuffle datset
ill_df = ill_df.sample(frac=1).reset_index(drop=True)
ill_df.to_csv('../data.csv',index = False)
