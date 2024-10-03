import os

# Weight min, max and step values
WEIGHT_MIN = 0
WEIGHT_MAX = 1.95
WEIGHT_STEP = 0.1

# Weight display format (number or slider)
WEIGHT_DISPLAY = "number"

WEIGHT_LABEL_SUFFIX = " (weight)"

def apply_weight(text: str, weight: float) -> str:
    """
    Apply a weight to the given text.

    Args:
        text (str): The text to which the weight will be applied.
        weight (float): The weight to be applied to the text.

    Returns:
        str: The text with the applied weight in the format "(text:weight)".
    
    Note that if the weight is equal to 1, the function returns the text as is.
    """    
    if weight == 1:
        return text
    else:
        return f"({text}:{round(weight,2)})"

def generate_prompt(self, text_in_opt="", **kwargs) -> str:
    """
    Generate a prompt string based on the provided input text and keyword arguments.

    Args:
        self: The instance of the class calling this method.
        text_in_opt (str, optional): An optional input text to be included in the prompt. Defaults to an empty string.
        **kwargs: Additional keyword arguments representing text and their corresponding weights.

    Returns:
        str: A generated prompt string based on the input text and keyword arguments.
    
    The function constructs a prompt string by appending the `text_in_opt` and other text values
    from `kwargs` if they are active and have a positive weight. The text values are weighted
    using the `apply_weight` function. The resulting prompt is a comma-separated, lowercase string.
    """    
    prompt = []

    if text_in_opt != "":
        prompt.append(text_in_opt)

    if kwargs["active"] == True:
        for key in kwargs.keys():
            if WEIGHT_LABEL_SUFFIX not in str(key) and "active" not in str(key):
                if kwargs[key] != "-" and kwargs[key + WEIGHT_LABEL_SUFFIX] > 0:
                    prompt.append(apply_weight(kwargs[key], kwargs[key + WEIGHT_LABEL_SUFFIX]))

    if len(prompt) > 0:
        prompt = ", ".join(prompt)
        prompt = prompt.lower()

        return(prompt,)
    else:
        return("",)    
    
def read_words_from_file(file_path: str) -> list:
    """
    Read words from a text file.

    Args:
        file_path (str): The path to the text file.

    Returns:
        list: A list of words read from the file, with each word being a line from the file.
    
    The function reads the content of the specified text file line by line, strips any leading
    and trailing whitespace from each line, and returns a list of these cleaned lines.
    """    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        values = [line.strip() for line in lines]

        return values

def custom_lists(folder: str) -> dict:
    """
    Generate custom lists from text files in a folder.

    Args:
        folder (str): The path to the folder containing text files.

    Returns:
        dict: A dictionary with custom lists and their configurations.
    
    The dictionary keys are the filenames (without extensions) of the text files in the folder.
    Each key maps to a tuple containing:
        - A list of values read from the corresponding text file, prefixed with a '-'.
        - A dictionary with a "default" key, whose value is the first item in the list.
    """    
    custom_lists = {}

    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)

        if os.path.isfile(filepath) and filename.lower().endswith('.txt'):
            values = read_words_from_file(folder + "/" + filename)
            values = ['-'] + values
            filename = os.path.splitext(filename)[0]

            custom_lists[filename] = (values, { "default" : values[0]})
            custom_lists[filename + WEIGHT_LABEL_SUFFIX] = ("FLOAT", {
                "default": 1,
                "min": WEIGHT_MIN,
                "max": WEIGHT_MAX,
                "step": WEIGHT_STEP,
                "display": WEIGHT_DISPLAY
            })

    custom_lists["active"] = ("BOOLEAN", {"default": True})

    return custom_lists

def sub_custom_lists(folder: str) -> dict:
    """
    Generate custom lists from text files in a folder and its subfolders.

    Args:
        folder (str): The path to the folder containing text files.

    Returns:
        dict: A dictionary with custom lists and their configurations.
    
    The dictionary keys are the filenames (without extensions) of the text files in the folder.
    Each key maps to a tuple containing:
        - A list of values read from the corresponding text file, prefixed with a '-'.
        - A dictionary with a "default" key, whose value is the first item in the list.
    """   
    sub_custom_lists = {}

    for filename in os.listdir(folder):
        folder_name = os.path.join(folder, filename)

        if os.path.isdir(folder_name):
            sub_custom_lists[filename] = custom_lists(folder_name)

    return sub_custom_lists