from . import utils

# Grouping Node
class PromptComposerGrouping:
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "promptComposerGrouping"
    CATEGORY = "AI WizArt/Prompt Composer Tools"

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text_in": ("STRING", {"forceInput": True}),
                "weight": ("FLOAT", {
                    "default": 1,
                    "step": utils.WEIGHT_STEP,
                    "min": utils.WEIGHT_MIN,
                    "max": utils.WEIGHT_MAX,
                    "display": utils.WEIGHT_DISPLAY,
                }),
                "active": ("BOOLEAN", {"default": False}),
            }
        }

    def promptComposerGrouping(self, text_in="", weight=0, active=True):
        prompt = text_in
        if text_in != "" and weight > 0 and active:
            prompt = utils.applyWeight(text_in, weight)
        return(prompt,)