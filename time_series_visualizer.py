import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    plt.subplots(figsize=(15, 5))

    sns.lineplot(data=df, x=df.index, y='value', color='red', linewidth=1)
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    sns.lineplot(data=df, legend=False)

    # Save image and return fig (don't change this part)
    plt.savefig('line_plot.png')
    return plt

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['year'] = df.index.year
    df['month'] = df.index.month
    df['month_name'] = df.index.strftime('%B')

    #Páginas por mês
    pag_mes = df.groupby(['year', 'month_name'])['value'].mean().reset_index()
    ordem_meses = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    # Draw bar plot

    plt.figure(figsize=(12, 8))
    sns.barplot(x='year', y='value', hue='month_name', data=pag_mes, hue_order=ordem_meses)

    # Customize the plot
    plt.title("Average Daily Page Views by Month and Year")
    plt.xlabel("Year")
    plt.ylabel("Average Page Views")
    
    # Save image and return fig (don't change this part)
    plt.savefig('bar_plot.png')
    return plt

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.month
    df_box['month_name'] = df_box.index.strftime('%b')

    # Draw box plots (using Seaborn)
    df_box['month_name'] = pd.Categorical(df_box['month_name'], categories=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ordered=True)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))

    #Box plot 1
    sns.boxplot(x='year', y='value', data=df_box, ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')


    #Box plot 1
    sns.boxplot(x='month_name', y='value', data=df_box, ax=ax2)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig