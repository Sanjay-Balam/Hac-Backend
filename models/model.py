class SocraticAIAssistant:
    def __init__(self):
        # Sorting algorithms knowledge base
        self.algorithms_info = {
            'Bubble Sort': {
                'complexity': 'O(n²)',
                'description': 'Simple comparison-based algorithm where adjacent elements are compared and swapped.',
                'stability': 'Stable'
            },
            'Quick Sort': {
                'complexity': 'O(n log n) average, O(n²) worst-case',
                'description': 'Divide-and-conquer algorithm that selects a pivot and partitions the array.',
                'stability': 'Unstable'
            },
            'Merge Sort': {
                'complexity': 'O(n log n)',
                'description': 'Divide-and-conquer algorithm that divides the list into smaller sublists and merges them.',
                'stability': 'Stable'
            }
        }

    def get_initial_question(self, algorithm):
        if algorithm not in self.algorithms_info:
            return f"I don't have information about {algorithm}. Can you ask about one of the known algorithms like Bubble Sort or Quick Sort?"

        return f"What do you know about the time complexity of {algorithm}?"

    def get_follow_up_question(self, student_response, algorithm):
        if "O(n²)" in student_response or "slow" in student_response:
            return f"Yes, {algorithm} can degrade to O(n²). What conditions might cause {algorithm} to hit this worst-case performance?"

        if "pivot" in student_response and algorithm == 'Quick Sort':
            return f"Good observation! Can you explain how choosing a bad pivot in {algorithm} might affect its performance?"

        if "stability" in student_response:
            return f"Great! {algorithm} is {self.algorithms_info[algorithm]['stability']}. Why might stability be important in sorting?"

        return f"Interesting. Can you think of any scenarios where {algorithm} would be inefficient?"

    def summary(self, algorithm):
        info = self.algorithms_info.get(algorithm, {})
        return f"Summary for {algorithm}:\n- Complexity: {info.get('complexity')}\n- Stability: {info.get('stability')}\n- Description: {info.get('description')}"
