#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------

import random

# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
        ("What gas do plants absorb from the atmosphere?", "Carbon dioxide"),
        ("What planet is known as the Red Planet?", "Mars"),
        ("What part of the cell contains genetic material?", "Nucleus"),
        ("Which force keeps us anchored to the Earth?", "Gravity"),
        ("What is the process by which plants make their food?", "Photosynthesis"),
        ("What gas do humans need to breathe to survive?", "Oxygen"),
        ("What is the boiling point of water in Celsius?", "100"),
        ("What part of the human body is responsible for pumping blood?", "Heart"),
        ("What natural satellite orbits the Earth?", "Moon"),
        # Add more questions as tuples (question, answer)
    ],
}

hints = {
    "Science": [
        "It's made of hydrogen and oxygen.",
        "It's a gas humans exhale.",
        "It’s named after the Roman god of war.",
        "It's often called the 'brain' of the cell.",
        "It’s the reason things fall when dropped.",
        "Involves sunlight, water, and carbon dioxide.",
        "We inhale it every few seconds.",
        "It's a round number and the same in metric units.",
        "It beats nonstop and is vital to life.",
        "It appears at night and affects tides.",
    ],
    # Repeat for other categories as needed.
}

#---------------------------------------

def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    #------------------------
    # Add your code here
    if category not in questions :
        return None
    index = random.randint(0, len(questions[category]) - 1)
    return questions[category][index]
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    #------------------------
    # Add your code here
    return player_answer == correct_answer
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    if category in questions:
        
        question_list = questions[category]
        hint_list = hints[category]

        for pair in question_list:
            q, a = pair
            if q == question:
                index = question_list.index(pair)
                del question_list[index]
                del hint_list[index]
                break

    
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    #------------------------
    # Add your code here
    print(f"\nQuestion: {question}")
    return input("Your answer: ")
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    #------------------------
    # Add your code here
    if category not in questions or category not in hints:
        return "No hint available."

        question_list = questions[category]
        hint_list = hints[category]

        for pair in question_list:
            q, _ = pair
            if q == question:
                index = question_list.index(pair)
                return hint_list[index]

        return "No hint found."

    
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    print(f"The correct answer was: {correct_answer}")
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------



