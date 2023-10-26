class Output:
    def __init__(self, results, keywords):
        self.results = results
        self.keywords = keywords

    def prepare_results(self):
        combined_results = []  # Create an empty list to store combined results

        for keyword in self.keywords:
            for item in self.results[keyword]:
                combined_results.append(item)

        # Remove duplicates by converting the list to a set and back to a list
        combined_results = list(set(combined_results))

        # Sort the list to maintain order
        combined_results.sort()

        return combined_results
