from . import utils

# Prompt Composer Text Node
class promptComposerTextMultiple:
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "promptComposerTextMultiple"
    CATEGORY = "AI WizArt/Prompt Composer Tools"    
    
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "text_in_opt": ("STRING", {"forceInput": True}),
            },
            "required": {
                "text_1": ("STRING", {
                    "multiline": True
                }),
                "weight_1": ("FLOAT", {
                    "default": 1,
                    "min": utils.WEIGHT_MIN,
                    "max": utils.WEIGHT_MAX,
                    "step": utils.WEIGHT_STEP,
                    "display": utils.WEIGHT_DISPLAY
                }),
                "text_2": ("STRING", {
                    "multiline": True
                }),
                "weight_2": ("FLOAT", {
                    "default": 1,
                    "min": utils.WEIGHT_MIN,
                    "max": utils.WEIGHT_MAX,
                    "step": utils.WEIGHT_STEP,
                    "display": utils.WEIGHT_DISPLAY
                }),
                "text_3": ("STRING", {
                    "multiline": True
                }),
                "weight_3": ("FLOAT", {
                    "default": 1,
                    "min": utils.WEIGHT_MIN,
                    "max": utils.WEIGHT_MAX,
                    "step": utils.WEIGHT_STEP,
                    "display": utils.WEIGHT_DISPLAY
                }),
                "text_4": ("STRING", {
                    "multiline": True
                }),
                "weight_4": ("FLOAT", {
                    "default": 1,
                    "min": utils.WEIGHT_MIN,
                    "max": utils.WEIGHT_MAX,
                    "step": utils.WEIGHT_STEP,
                    "display": utils.WEIGHT_DISPLAY
                }),
                "text_5": ("STRING", {
                    "multiline": True
                }),
                "weight_5": ("FLOAT", {
                    "default": 1,
                    "min": utils.WEIGHT_MIN,
                    "max": utils.WEIGHT_MAX,
                    "step": utils.WEIGHT_STEP,
                    "display": utils.WEIGHT_DISPLAY
                }),
                "text_6": ("STRING", {
                    "multiline": True
                }),
                "weight_6": ("FLOAT", {
                    "default": 1,
                    "min": utils.WEIGHT_MIN,
                    "max": utils.WEIGHT_MAX,
                    "step": utils.WEIGHT_STEP,
                    "display": utils.WEIGHT_DISPLAY
                }),
                "text_7": ("STRING", {
                    "multiline": True
                }),
                "weight_7": ("FLOAT", {
                    "default": 1,
                    "min": utils.WEIGHT_MIN,
                    "max": utils.WEIGHT_MAX,
                    "step": utils.WEIGHT_STEP,
                    "display": utils.WEIGHT_DISPLAY
                }),
                "text_8": ("STRING", {
                    "multiline": True
                }),
                "weight_8": ("FLOAT", {
                    "default": 1,
                    "min": utils.WEIGHT_MIN,
                    "max": utils.WEIGHT_MAX,
                    "step": utils.WEIGHT_STEP,
                    "display": utils.WEIGHT_DISPLAY
                }),
                "text_9": ("STRING", {
                    "multiline": True
                }),
                "weight_9": ("FLOAT", {
                    "default": 1,
                    "min": utils.WEIGHT_MIN,
                    "max": utils.WEIGHT_MAX,
                    "step": utils.WEIGHT_STEP,
                    "display": utils.WEIGHT_DISPLAY
                }),
                "text_10": ("STRING", {
                    "multiline": True
                }),
                "weight_10": ("FLOAT", {
                    "default": 1,
                    "min": utils.WEIGHT_MIN,
                    "max": utils.WEIGHT_MAX,
                    "step": utils.WEIGHT_STEP,
                    "display": utils.WEIGHT_DISPLAY
                }),
                "active": ("BOOLEAN", {"default": False}),
            }
        }

    def promptComposerTextMultiple(self, text_in_opt="", text_1="", weight_1=0, text_2="", weight_2=0, text_3="", weight_3=0, text_4="", weight_4=0, text_5="", weight_5=0, text_6="", weight_6=0, text_7="", weight_7=0, text_8="", weight_8=0, text_9="", weight_9=0, text_10="", weight_10=0, active=True):
        prompt = []
        if text_in_opt != "":
            prompt.append(text_in_opt)
        if text_1 != "" and weight_1 > 0 and active:
            prompt.append(utils.applyWeight(text_1, weight_1))
        if text_2 != "" and weight_2 > 0 and active:
            prompt.append(utils.applyWeight(text_2, weight_2))
        if text_3 != "" and weight_3 > 0 and active:
            prompt.append(utils.applyWeight(text_3, weight_3))
        if text_4 != "" and weight_4 > 0 and active:
            prompt.append(utils.applyWeight(text_4, weight_4))
        if text_5 != "" and weight_5 > 0 and active:
            prompt.append(utils.applyWeight(text_5, weight_5))
        if text_6 != "" and weight_6 > 0 and active:
            prompt.append(utils.applyWeight(text_6, weight_6))
        if text_7 != "" and weight_7 > 0 and active:
            prompt.append(utils.applyWeight(text_7, weight_7))
        if text_8 != "" and weight_8 > 0 and active:
            prompt.append(utils.applyWeight(text_8, weight_8))
        if text_9 != "" and weight_9 > 0 and active:
            prompt.append(utils.applyWeight(text_9, weight_9))
        if text_10 != "" and weight_10 > 0 and active:
            prompt.append(utils.applyWeight(text_10, weight_10))
        if len(prompt) > 0:
            prompt = ", ".join(prompt)
            prompt = prompt.lower()
            return(prompt,)
        else:
            return("",)