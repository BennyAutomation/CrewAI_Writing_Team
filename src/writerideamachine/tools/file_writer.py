from crewai.tools import BaseTool
import os

class SaveToFileTool(BaseTool):
    name: str = "save_to_file"
    description: str = "Save text content to a file"

    def _run(self, content: str, filename: str = "output.txt") -> str:
        try:
            os.makedirs("outputs", exist_ok=True)
            path = os.path.join("outputs", filename)

            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

            return f"Saved to {path}"
        except Exception as e:
            return f"Error: {str(e)}"