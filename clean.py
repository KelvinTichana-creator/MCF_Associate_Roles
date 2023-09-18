import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import base64

# Define the Streamlit app
def main():
    st.title("MasterCard Foundation Associate Roles Applications Cleaner")

    # Allow the user to upload an Excel file
    uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

    if uploaded_file is not None:
        # Load the uploaded Excel file
        df = pd.read_excel(uploaded_file, header=1)

        # Data Cleaning
        st.header("Data Cleaning")

        # Filter rows where the specified column is "Yes"
        completion_col = "Have you completed school already or will you have completed school by 30th September 2023?"
        cleaned_df = df[df[completion_col] == 'Yes']

        # Remove rows with no value (empty) in column AP
        column_index_to_check = 41  # Index of column AP (0-based index)
        cleaned_df = cleaned_df.dropna(subset=[cleaned_df.columns[column_index_to_check]], how="any")

        # Specify the path to save the cleaned data
        cleaned_data_file = "cleaned_data.xlsx"
        current_directory = os.getcwd()  # Get the current working directory
        cleaned_data_path = os.path.join(current_directory, cleaned_data_file)

        # Create a link to download the cleaned data
        st.markdown(get_download_link(cleaned_data_path, 'cleaned_data.xlsx'), unsafe_allow_html=True)

        st.header("Statistics")

        # Display basic statistics about Age, Gender, and Country columns
        if 'What is your age?' in cleaned_df.columns:
            st.subheader("Age Statistics")
            st.write(cleaned_df['What is your age?'].describe())

            # Plot Age distribution
            st.pyplot(plot_distribution(cleaned_df['What is your age?'], 'Age Distribution'))

        if 'Gender' in cleaned_df.columns:
            st.subheader("Gender Statistics")
            st.write(cleaned_df['Gender'].value_counts())

        if 'Country of Origin:' in cleaned_df.columns:
            st.subheader("Country Statistics")
            st.write(cleaned_df['Country of Origin:'].value_counts())

        # Print the DataFrame
        st.subheader("Cleaned Data")
        st.write(cleaned_df)

# Plot a distribution using Matplotlib
def plot_distribution(data, title):
    plt.figure(figsize=(8, 6))
    sns.histplot(data, kde=True)
    plt.title(title)
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    return plt
def get_download_link(file_path, file_name):
    """Generate a download link for a file."""
    href = f'<a href="data:file/{file_path};base64,{base64.b64encode(open(file_path, "rb").read()).decode()}" download="{file_name}">Download {file_name}</a>'
    return href


if __name__ == "__main__":
    main()

