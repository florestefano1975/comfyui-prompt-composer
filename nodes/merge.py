# Merge Node
class PromptComposerMerge:
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "promptComposerMerge"
    CATEGORY = "AI WizArt/Prompt Composer Tools"

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text_a": ("STRING", {"forceInput": True}),
                "text_b": ("STRING", {"forceInput": True}),
            }
        }

    def promptComposerMerge(self, text_a="", text_b=""):
        return(text_a + ", " + text_b,)