from . import utils

# Prompt Composer Single Text Node
class PromptComposerTextSingle:
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "promptComposerTextSingle"
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
                "text": ("STRING", {
                    "multiline": True
                }),
                "weight": ("FLOAT", {
                    "default": 1,
                    "min": utils.WEIGHT_MIN,
                    "max": utils.WEIGHT_MAX,
                    "step": utils.WEIGHT_STEP,
                    "display": utils.WEIGHT_DISPLAY
                }),
                "active": ("BOOLEAN", {"default": False}),
            }
        }

    def promptComposerTextSingle(self, text_in_opt="", text="", weight=0, active=True):
        prompt = []
        if text_in_opt != "":
            prompt.append(text_in_opt)
        if text != "" and weight > 0 and active:
            prompt.append(utils.applyWeight(text, weight))
        if len(prompt) > 0:
            prompt = ", ".join(prompt)
            prompt = prompt.lower()
            return(prompt,)
        else:
            return("",)