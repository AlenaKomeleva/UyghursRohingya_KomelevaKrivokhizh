# List of suitable article texts
suitable_articles = []

# Loop through all saved article texts
for article in articles:
    # Counters for keywords in the text
    uyghur_keyword_count = 0
    rohingya_keyword_count = 0

    # Loop through all words in a single article text
    for word in article:
        # Increase the counter if the current word matches the required keyword
        if word == 'أويغور':
            uyghur_keyword_count += 1
        if word == 'روهينغيا':
            rohingya_keyword_count += 1

    # Article selection criteria - at least 3 keywords from one of the topics
    if uyghur_keyword_count >= 3 or rohingya_keyword_count >= 3:
        # If the criteria are met, add the article to the list
        suitable_articles.append(article)

# Open a text file
with open('articles.txt', 'w') as file:
    # Loop through each suitable article
    for article in suitable_articles:
        # Write to the text file
        file.write(str(article) + '\n')
