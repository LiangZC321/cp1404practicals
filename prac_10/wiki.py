import wikipedia

while True:
    search_query = input("Enter a page title or search phrase (or press enter to quit): ")

    if search_query == '':
        print("Exiting the program.")
        break

    try:
        page_summary = wikipedia.summary(search_query)
        print("\nSummary of", search_query, ":\n", page_summary, "\n")
    except wikipedia.exceptions.DisambiguationError as e:
        print("The search phrase you entered is ambiguous. Please be more specific.")
        print("Some suggestions are:", e.options)
    except wikipedia.exceptions.PageError:
        print("Page not found. Please check the title and try again.")
    except wikipedia.exceptions.WikipediaException as e:
        print("An error occurred: ", e)