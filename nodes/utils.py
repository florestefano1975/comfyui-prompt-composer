import os

# Weight min, max and step values
WEIGHT_MIN = 0
WEIGHT_MAX = 1.95
WEIGHT_STEP = 0.1

# Weight display format (number or slider)
WEIGHT_DISPLAY = "number"

WEIGHT_LABEL_SUFFIX = " (weight)"

# Apply weight    
def applyWeight(text, weight):
    if weight == 1:
        return text
    else:
        return f"({text}:{round(weight,2)})"
    

# Generate prompt (used by the custom list nodes)
def generatePrompt(self, text_in_opt="", **kwargs):
    prompt = []

    if text_in_opt != "":
        prompt.append(text_in_opt)

    if kwargs["active"] == True:
        for key in kwargs.keys():
            if WEIGHT_LABEL_SUFFIX not in str(key) and "active" not in str(key):
                if kwargs[key] != "-" and kwargs[key + WEIGHT_LABEL_SUFFIX] > 0:
                    prompt.append(applyWeight(kwargs[key], kwargs[key + WEIGHT_LABEL_SUFFIX]))

    if len(prompt) > 0:
        prompt = ", ".join(prompt)
        prompt = prompt.lower()

        return(prompt,)
    else:
        return("",)    
    
# Read txt file
def pmReadTxt(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        values = [line.strip() for line in lines]

        return values

# Custom lists
def customLists(folder):
    custom_lists = {}

    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)

        if os.path.isfile(filepath) and filename.lower().endswith('.txt'):
            values = pmReadTxt(folder + "/" + filename)
            values = ['-'] + values

            filename = os.path.splitext(filename)[0]

            custom_lists[str(filename)] = (values, { "default" : values[0]})
            custom_lists[str(filename) + WEIGHT_LABEL_SUFFIX] = ("FLOAT", {
                "default": 1,
                "min": WEIGHT_MIN,
                "max": WEIGHT_MAX,
                "step": WEIGHT_STEP,
                "display": WEIGHT_DISPLAY
            })

    custom_lists["active"] = ("BOOLEAN", {"default": True})

    return custom_lists



# Custom sublists
def subCustomLists(folder):
    sub_custom_lists = {}

    for filename in os.listdir(folder):
        folder_name = os.path.join(folder, filename)

        if os.path.isdir(folder_name):
            sub_custom_lists[filename] = customLists(folder_name)

    return sub_custom_lists