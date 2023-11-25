dictionary = {
    'API': 'Application Programming Interface - a set of rules that allows one software application to interact with another.',
    'Blockchain': 'A decentralized and distributed digital ledger that is used to record transactions across multiple computers.',
    'Machine Learning': 'A subset of artificial intelligence that involves the development of algorithms allowing computers to learn and make predictions or decisions without explicit programming.',
    'Responsive Design': 'Web design approach that makes web pages render well on a variety of devices and window or screen sizes.',
    'Cloud Computing': 'The delivery of computing services, including storage, processing, and software, over the internet.',
    'SEO': 'Search Engine Optimization - the practice of optimizing content to rank higher in search engine results.',
}

def find_information(query):
    query_lower = query.lower()  # Convert the query to lowercase for case-insensitive search
    for term, definition in dictionary.items():
        if query_lower == term.lower():
            return definition
    return 'Information for query "{}" not found.'.format(query)

def add_information(term, definition):
    dictionary[term] = definition

def display_all_terms():
    print("Available terms in the dictionary:")
    for term in dictionary:
        print("-", term)

# Example usage of the updated information system
while True:
    print("\n=== Information System ===")
    print("1. Search for information")
    print("2. Add new information")
    print("3. Display all terms")
    print("4. Exit")

    choice = input("Choose an action (1/2/3/4): ")

    if choice == '1':
        user_query = input('Enter a term to search for: ')
        result = find_information(user_query)
        print(result)

    elif choice == '2':
        new_term = input('Enter a new term: ')
        new_definition = input('Enter a definition for "{}": '.format(new_term))
        add_information(new_term, new_definition)
        print('Information added successfully.')

    elif choice == '3':
        display_all_terms()

    elif choice == '4':
        print("Exiting the program.")
        break

    else:
        print("Invalid input. Please choose an action from 1 to 4.")
1