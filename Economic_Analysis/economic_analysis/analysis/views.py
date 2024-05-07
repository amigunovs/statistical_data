from django.shortcuts import render
import beapy
import os
import pandas as pd
from matplotlib import pyplot as plt
from stats_can import StatsCan
from pathlib import Path
sc = StatsCan()

# BASE_DIR = Path(__file__).resolve().parent.parent

def Statistics_data(request):

    sc = StatsCan(data_folder=os.path.join('../economic_analysis/content/'))

    # df_GDP_at_basic_prices_growth_rates = sc.table_to_df("36-10-0434-01")

    df = sc.vectors_to_df("v65201210")

    # df_Laboure = sc.table_to_df("14-10-0022-01")


    df_Laboure_vector = sc.vectors_to_df("v2710104")


    marged_df_canada = pd.merge(df,df_Laboure_vector, on = "REF_DATE")


    marged_df_canada['Predictivity'] = marged_df_canada['v65201210'] / marged_df_canada['v2710104']

    marged_df_canada['Predictivity'].plot(kind='line', figsize=(8, 4), title='Predictivity')
    plt.gca().spines[['top', 'right']].set_visible(False)


    plot_path = os.path.join('../economic_analysis/analysis/static/analysis/plot_canada.png')  # Save to a static directory
    plt.savefig(plot_path)
    plt.clf()


    # Replace 'YOUR_API_KEY' with your actual key
    bea = beapy.BEA(key='4E1A17C0-437B-4BE1-AE32-6C0B4B33ECB5')

    res = bea.data('nipa', tablename='t10106', frequency='A', year="X")
    res_labour = bea.data('nipa', tablename='t60400D', frequency='A', year="X")

    # Access data and metadata
    data_gdp = res.data  # pandas DataFrame containing GDP data

    data_res_labour = res_labour.data  # pandas DataFrame containing GDP data

    df_2 = pd.DataFrame(data_res_labour.A4201C)
    df1 = pd.DataFrame(data_gdp.A191RX)

    marged_df_usa = pd.merge(df1, df_2, left_index=True, right_index=True)

    marged_df_usa['Predictivity'] = marged_df_usa['A191RX'] / marged_df_usa['A4201C']

    # @title Predictivity

    marged_df_usa['Predictivity'].plot(kind='line', figsize=(8, 4), title='Predictivity')
    plt.gca().spines[['top', 'right']].set_visible(False)

    plot_path = os.path.join('../economic_analysis/analysis/static/analysis/plot_usa.png')  # Save to a static directory
    plt.savefig(plot_path)
    plt.clf()

    return render(request,"analysis/home.html")
