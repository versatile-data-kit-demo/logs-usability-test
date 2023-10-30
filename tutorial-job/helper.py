def classify_score(score):
    if 0 <= score <= 6:
        return 'Detractors'
    else:
        return 'Promoters' 
    

import matplotlib.pyplot as plt
    
    
def visualize_data(df):
    type_counts = df['Type'].value_counts(normalize=True) * 100

    # Create a bar chart
    type_counts.plot(kind='bar', color=['blue', 'red'])

    # Add labels and title
    plt.ylabel('Percentage')
    plt.xlabel('Type')
    plt.title('Percentage of Promoters vs Detractors')
    plt.xticks(rotation=0) # to keep the x-axis labels readable

    # Add percentage on the top of the bars
    for i, percentage in enumerate(type_counts):
        plt.text(i, percentage + 1, f"{percentage:.2f}%", ha='center')

    # Display the plot
    plt.show()