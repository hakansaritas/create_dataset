import pandas as pd
import numpy as np


def create_dataset():
    """
    creating a dataset includes AGE,SEX,INSTRUMENT,CITY,PRICE variables with 5000 samples.

    Parameters
    ----------
    None.

    Returns
    -------
    df: dataframe of the created dataset

    Notes
    ------
    This function export the dataframe to csv format into your main work directory

    """

    # AGE variable is between 15-65 age years old, 5000 samples

    AGE = np.random.randint(15, 71, 5000)

    # * SEX variable is composed of  Male and Female. 5000 observations.
    # * To create object variables as np.Series use random.choise().
    # * p  is probability associated with each entry in the variable list

    sex_list = ["Male", "Female"]
    SEX = np.random.choice(sex_list, 5000, p=[0.6, 0.4])

    # * INSTRUMENT variable: "Guitar","Violin","Harmonica","Drum" , 5000 samples

    inst_list = ["Guitar", "Violin", "Harmonica", "Drum"]
    INSTRUMENT = np.random.choice(inst_list, 5000, p=[0.3, 0.4, 0.2, 0.1])

    # * CITY variable includes "Izmir","Vancouver","Paris","Tokyo", 5000 samples

    city_list = ["Izmir", "Vancouver", "Paris", "Tokyo"]
    CITY = np.random.choice(city_list, 5000, p=[0.3, 0.2, 0.1, 0.4])

    ############### create DataFrame ################
    list_of_tuples = list(zip(AGE, SEX, INSTRUMENT, CITY))

    df_0 = pd.DataFrame(list_of_tuples,
                        columns=["AGE", "SEX", "INSTRUMENT", "CITY"])

    ###### Create a new DataFrame for PRICE variable #######

    # * PRICE variable is float number, it is described in different price ranges for each instrument in "price_dict" as dict type
    # * the price_dict shows average low price as price1 values and average high as price2 values depending on the instrument order in inst_list. You can put different numbers.
    # * random.uniform produces float numbers in given ranges.
    # * len(df_0[df_0["INSTRUMENT"] == "Guitar"] is used to get exact number of the sample to create PRICE

    ###### Price List : You can change the values #######
    price_dict = {"price1": [100, 150, 50, 300],
                  "price2": [1800, 2000, 800, 2500]}

    ####### Function for gettin a dataframe includes PRICE and INSTRUMENT variables ##########

    def price_fill(instrument_list, price_dictionary):
        dict_inst = {}
        inst_price_df = pd.DataFrame()

        for count, inst in enumerate(instrument_list):
            dict_inst[inst] = [round(num, 2) for num in
                               np.random.uniform(price_dict["price1"][count], price_dict["price2"][count],
                                                 len(df_0[df_0["INSTRUMENT"] == inst]))]

            frame = pd.DataFrame({"INSTRUMENT": inst, "PRICE": dict_inst[inst]})

            inst_price_df = inst_price_df.append(frame, True)

        return inst_price_df

    df_1 = price_fill(inst_list, price_dict)

    #### MERGE the df_0 and df_1 as named df ####
    df = pd.merge(df_0, df_1, suffixes=("_del", ""), left_index=True, right_index=True)

    #### shuffle the df rows to get more realistic dataset ####
    df = df.sample(frac=1, ignore_index=True)

    ### Drop INSTRUMENT_del variable ####
    df = df.drop("INSTRUMENT_del", axis=1)

    ### SAVE to CSV FORMAT ###
    df.to_csv('export_dataframe.csv', index=False)

    #### RETURN exact dataframe ####
    return df
